import requests
import mysql.connector
from datetime import datetime

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="harshith",
    database="cp_grind"
)
cursor = db.cursor(buffered=True)

res  = requests.get("https://alfa-leetcode-api.onrender.com/Harshith-2007/submission?limit=50").json()
subs = res["submission"]

inserted = 0
seen     = set()

for sub in subs:
    title   = sub["title"]
    slug    = sub["titleSlug"]
    verdict = "AC" if sub["statusDisplay"] == "Accepted" else "WA"
    link    = f"https://leetcode.com/problems/{slug}/"
    solved_at = datetime.utcfromtimestamp(int(sub["timestamp"]))

    # insert problem if not exists
    cursor.execute(
        "INSERT IGNORE INTO problems (platform_id, name, difficulty, topic, link) VALUES (1, %s, 'Medium', 'Unknown', %s)",
        (title, link)
    )
    db.commit()

    # get problem id
    cursor.execute("SELECT id FROM problems WHERE name = %s", (title,))
    row = cursor.fetchone()
    if not row:
        continue
    problem_id = row[0]

    # skip duplicate AC
    if verdict == "AC" and title in seen:
        continue
    seen.add(title)

    # insert submission
    cursor.execute(
        "INSERT INTO submissions (problem_id, verdict, solved_at) VALUES (%s, %s, %s)",
        (problem_id, verdict, solved_at)
    )
    inserted += 1

db.commit()
cursor.close()
db.close()

print(f"synced {inserted} submissions into cp_grind 🖤")