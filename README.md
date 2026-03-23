# ⚡ CP Grind Tracker

A full-stack competitive programming tracker that syncs LeetCode data into a MySQL database and visualizes performance through a web dashboard.

---

## 🚀 Overview

CP Grind Tracker started as a DBMS project and evolved into a full-stack system combining data engineering, backend APIs, and frontend visualization.

It helps track:
- Total solved problems
- Weak topics
- Difficulty distribution
- Daily solving streak

---

## 🧠 Features

- 📊 Difficulty-wise statistics (Easy / Medium / Hard)
- 📉 Weak topic analysis based on accuracy
- 📅 Daily streak tracking
- 🧾 Submission history viewer
- 🔄 Automated sync using Python
- ⚠️ Handles API rate limits and failures safely

---

## 🏗️ Architecture

```
LeetCode API
     ↓
sync.py (Python)
     ↓
MySQL (cp_grind)
     ↓
fetch_views.php
     ↓
Frontend (HTML + JS)
```

---

## 📁 Project Structure

```
cp-grind-tracker/

app.js
index.html
style.css

fetch_views.php
sync.py

database/
  ├── schemas.sql
  ├── views.sql
  ├── queries.sql

README.md
```

---

## ⚙️ Tech Stack

- Backend: Python, PHP  
- Database: MySQL  
- Frontend: HTML, CSS, JavaScript  
- API: LeetCode (via alfa-leetcode-api)

---

## 🔄 Data Pipeline

- Fetches recent submissions (last 50)
- Inserts into normalized database schema
- Uses SQL views for analytics
- Fetches accurate total solved separately from profile API
- Includes retry logic for API rate limits (429)

---

## 🧪 Setup Instructions

### 1. Clone repository

```
git clone https://github.com/Harshith1702/cp-grind-tracker.git
cd cp-grind-tracker
```

### 2. Setup MySQL database

```
CREATE DATABASE cp_grind;
```

Import:
- schemas.sql
- views.sql

### 3. Configure database credentials

Update in `sync.py` and `fetch_views.php`:

```
host = localhost
user = root
password = your_password
database = cp_grind
```

### 4. Run sync script

```
python sync.py
```

### 5. Start server (XAMPP / Apache)

```
http://localhost/cp-grind-tracker/index.html
```

---

## ⚠️ Limitations

- API only returns last 50 submissions  
- Full historical reconstruction is not possible  
- Depends on external API availability and rate limits  

---

## 🔮 Future Improvements

- Full submission history via pagination  
- Charts (Chart.js)  
- Multi-platform support (Codeforces, CodeChef)  
- Better topic classification  
- User authentication  

---

## 💡 Motivation

I built this to understand where I was weak in competitive programming instead of just counting solved problems.

Now every mistake is tracked and analyzed.

---

## 👤 Author

Harshith  
CSE Undergraduate | Backend & Systems Enthusiast  

---

## ⭐ If you like this project

Star it or build your own improved version.
