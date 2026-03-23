let currentView = 'difficulty_stats';

function loadView(view) {
  currentView = view;
  fetch(`fetch_views.php?view=${view}`)
    .then(res => res.json())
    .then(data => {
      document.getElementById("error").style.display = "none";
      renderView(view, data);
    })
    .catch(() => document.getElementById("error").style.display = "block");
}

function renderView(view, data) {
  const content = document.getElementById("content");
  if (view === 'difficulty_stats') {
    let html = '<div id="stats">';
    let total = 0;
    data.forEach(row => {
      total += parseInt(row.cleared);
      html += `
        <div class="card ${row.difficulty.toLowerCase()}">
          <span class="num">${row.cleared}</span>
          <span class="label">${row.difficulty}</span>
        </div>`;
    });
    html = `<div class="card" id="total"><span class="num">${total}</span><span class="label">Total Solved</span></div>` + html;
    html += '</div>';
    content.innerHTML = html;
  } 
  else if (view === 'my_performance') {
    let html = '<table><tr><th>Problem</th><th>Difficulty</th><th>Topic</th><th>Platform</th><th>Verdict</th><th>Date</th></tr>';
    data.forEach(row => {
      html += `<tr>
        <td>${row.problem}</td>
        <td>${row.difficulty}</td>
        <td>${row.topic}</td>
        <td>${row.platform}</td>
        <td>${row.verdict}</td>
        <td>${new Date(row.solved_at).toLocaleDateString()}</td>
      </tr>`;
    });
    html += '</table>';
    content.innerHTML = html;
  }
  else if (view === 'weak_topics') {
    let html = '<table><tr><th>Topic</th><th>Tried</th><th>Solved</th><th>Accuracy</th></tr>';
    data.forEach(row => {
      html += `<tr>
        <td>${row.topic}</td>
        <td>${row.total_tried}</td>
        <td>${row.solved}</td>
        <td>${row.accuracy}%</td>
      </tr>`;
    });
    html += '</table>';
    content.innerHTML = html;
  }
  else if (view === 'streak_history') {
    let html = '<table><tr><th>Date</th><th>Solved</th><th>Streak</th></tr>';
    data.forEach(row => {
      html += `<tr>
        <td>${row.log_date}</td>
        <td>${row.solved_count}</td>
        <td>${row.streak}</td>
      </tr>`;
    });
    html += '</table>';
    content.innerHTML = html;
  }
}
// Tab switching
document.addEventListener('DOMContentLoaded', () => {
  document.querySelectorAll('.tab').forEach(btn => {
    btn.addEventListener('click', (e) => {
      document.querySelectorAll('.tab').forEach(b => b.classList.remove('active'));
      e.target.classList.add('active');
      loadView(e.target.dataset.view);
    });
  });
  loadView('difficulty_stats');
});