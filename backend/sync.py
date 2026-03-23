import requests
import mysql.connector
import time
from datetime import datetime, UTC

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="cp_grind"
)
cursor = db.cursor(buffered=True)

# ---- helper
def fetch_with_retry(url):
    for _ in range(5):
        res = requests.get(url)

        if res.status_code == 200:
            try:
                return res.json()
            except:
                print("Invalid JSON")
                return None

        if res.status_code == 429:
            print("Rate limited... waiting")
            time.sleep(5)
        else:
            print("API error:", res.status_code)
            time.sleep(2)

    print("Failed to fetch API")
    return None


# ---- submissions!! ----
data = fetch_with_retry(
    "https://alfa-leetcode-api.onrender.com/Harshith-2007/submission?limit=50"    // use your account
)
if not data:
    print("Using old data, skipping sync")
    exit()
subs = data.get("submission", [])
inserted = 0
for sub in subs:
    title   = sub["title"]
    slug    = sub["titleSlug"]
    verdict = "AC" if sub["statusDisplay"] == "Accepted" else "WA"
    link    = f"https://leetcode.com/problems/{slug}/"
    solved_at = datetime.fromtimestamp(int(sub["timestamp"]), UTC)

    cursor.execute(
        "INSERT IGNORE INTO problems (platform_id, name, difficulty, topic, link) VALUES (1, %s, 'Medium', 'Unknown', %s)",
        (title, link)
    )
    cursor.execute("SELECT id FROM problems WHERE name = %s", (title,))
    row = cursor.fetchone()
    if not row:
        continue
    problem_id = row[0]
    cursor.execute(
        "INSERT IGNORE INTO submissions (problem_id, verdict, solved_at) VALUES (%s, %s, %s)",
        (problem_id, verdict, solved_at)
    )

    inserted += 1
time.sleep(10)
profile = fetch_with_retry(
    "https://alfa-leetcode-api.onrender.com/Harshith-2007"
)

if not profile or "totalSolved" not in profile:
    print("Profile API failed, not updating total")
else:
    total_solved = profile["totalSolved"]

    cursor.execute("""
    INSERT INTO daily_log (log_date, solved_count, streak_alive)
    VALUES (CURDATE(), %s, 1)
    ON DUPLICATE KEY UPDATE solved_count = %s
    """, (total_solved, total_solved))

db.commit()
cursor.close()
db.close()
print(f"synced {inserted} submissions into cp_grind 🖤")
