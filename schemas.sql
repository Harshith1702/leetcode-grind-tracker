CREATE DATABASE cp_grind;
USE cp_grind;

CREATE TABLE platforms (
  id   INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(50)  NOT NULL,
  url  VARCHAR(100)
);

CREATE TABLE problems (
  id          INT AUTO_INCREMENT PRIMARY KEY,
  platform_id INT NOT NULL,
  name        VARCHAR(200) NOT NULL,
  difficulty  ENUM('Easy', 'Medium', 'Hard') NOT NULL,
  topic       VARCHAR(50)  NOT NULL,
  link        VARCHAR(200),
  FOREIGN KEY (platform_id) REFERENCES platforms(id)
);

CREATE TABLE submissions (
  id         INT AUTO_INCREMENT PRIMARY KEY,
  problem_id INT NOT NULL,
  verdict    ENUM('AC', 'WA', 'TLE', 'MLE') NOT NULL,
  attempts   INT DEFAULT 1,
  time_ms    INT,
  solved_at  DATETIME DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (problem_id) REFERENCES problems(id)
);

CREATE TABLE daily_log (
  id           INT AUTO_INCREMENT PRIMARY KEY,
  log_date     DATE DEFAULT (CURDATE()),
  solved_count INT DEFAULT 0,
  streak_alive BOOLEAN DEFAULT TRUE
);

INSERT INTO platforms (name, url) VALUES
('LeetCode',   'https://leetcode.com'),
('CodeChef',   'https://codechef.com'),
('Codeforces', 'https://codeforces.com');