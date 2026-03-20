USE cp_grind;

DROP VIEW IF EXISTS my_performance;
DROP VIEW IF EXISTS weak_topics;
DROP VIEW IF EXISTS platform_stats;
DROP VIEW IF EXISTS difficulty_stats;
DROP VIEW IF EXISTS streak_history;

CREATE VIEW my_performance AS
SELECT p.name AS problem, p.difficulty, p.topic,
  pl.name AS platform, s.verdict, s.attempts, s.solved_at
FROM submissions s
JOIN problems  p  ON p.id  = s.problem_id
JOIN platforms pl ON pl.id = p.platform_id
ORDER BY s.solved_at DESC;

CREATE VIEW weak_topics AS
SELECT p.topic, COUNT(*) AS total_tried,
  SUM(s.verdict = 'AC') AS solved,
  ROUND(SUM(s.verdict = 'AC') * 100.0 / COUNT(*), 1) AS accuracy
FROM submissions s
JOIN problems p ON p.id = s.problem_id
GROUP BY p.topic ORDER BY accuracy ASC;

CREATE VIEW platform_stats AS
SELECT pl.name AS platform, COUNT(*) AS total,
  SUM(s.verdict = 'AC') AS solved,
  ROUND(SUM(s.verdict = 'AC') * 100.0 / COUNT(*), 1) AS win_rate
FROM submissions s
JOIN problems  p  ON p.id  = s.problem_id
JOIN platforms pl ON pl.id = p.platform_id
GROUP BY pl.name ORDER BY win_rate DESC;

CREATE VIEW difficulty_stats AS
SELECT p.difficulty, COUNT(*) AS attempted,
  SUM(s.verdict = 'AC') AS cleared,
  ROUND(SUM(s.verdict = 'AC') * 100.0 / COUNT(*), 1) AS clear_rate
FROM submissions s
JOIN problems p ON p.id = s.problem_id
GROUP BY p.difficulty
ORDER BY FIELD(p.difficulty, 'Easy', 'Medium', 'Hard');

CREATE VIEW streak_history AS
SELECT log_date, solved_count,
  IF(streak_alive, 'alive', 'dead') AS streak
FROM daily_log ORDER BY log_date DESC;