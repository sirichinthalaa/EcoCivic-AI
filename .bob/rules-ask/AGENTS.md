# Project Documentation Context (Non-Obvious Only)

- `ai/analyzer.py` contains its own runnable test suite in the `if __name__ == "__main__"` block — the only testing mechanism in the project.
- There is no build system, bundler, or package.json — the frontend is served directly as static files (open HTML in browser or serve with any static server).
- `database/` directory exists but is **empty** — schema lives only in the MongoDB collection structure implied by `complaint_data` in `backend/app.py`.
- The frontend has two separate entry points: `index.html` (complaint submission) and `dashboard.html` (admin view) — they are independent pages, not a SPA.
- API base URL (`http://127.0.0.1:5000`) is duplicated in both `frontend/script.js` and `frontend/dashboard.js` with no shared constant.
