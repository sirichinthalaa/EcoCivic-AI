# AGENTS.md

This file provides guidance to agents when working with code in this repository.

## Stack

- **Backend**: Python 3.14 + Flask, served from `backend/app.py`
- **AI module**: Pure-Python keyword classifier in `ai/analyzer.py` (no ML library — keyword matching only)
- **Database**: MongoDB on `mongodb://127.0.0.1:27017/`, database `EcoCivicAI`, collection `complaints`
- **Frontend**: Vanilla HTML/CSS/JS (no bundler, no framework) in `frontend/`
- **Python venv**: `venv/` at project root (Python 3.14)

## Commands

```bash
# Activate venv (Windows)
.\venv\Scripts\Activate.ps1

# Install dependencies (no requirements.txt — install manually)
pip install flask flask-cors pymongo

# Run backend
python backend/app.py          # starts Flask dev server on http://127.0.0.1:5000

# Run/test the AI analyzer standalone
python ai/analyzer.py          # runs built-in test cases at bottom of file
```

There is **no test framework, no lint config, and no package.json**. The only "test" is the `if __name__ == "__main__"` block in [`ai/analyzer.py`](ai/analyzer.py:141).

## Architecture

```
frontend/index.html + script.js  →  POST /api/complaints  (multipart/form-data)
frontend/dashboard.html + dashboard.js  →  GET /api/complaints, PUT /api/complaints/<id>/status
backend/app.py  →  calls analyze_complaint()  →  ai/analyzer.py
backend/app.py  →  stores result in MongoDB complaints collection
uploads/        →  image files saved here by Flask (created automatically)
```

## Critical Patterns

- `sys.path.append(...)` in `backend/app.py` is required so Flask (run from `backend/`) can import from `ai/` (one level up). **Do not remove it.**
- MongoDB `_id` (ObjectId) is manually converted to `str` before JSON serialization — there is no serializer helper; do this explicitly in every route that returns documents.
- AI analysis result always returns these 5 keys: `category`, `subcategory`, `priority`, `sustainability_area`, `summary`. All 5 must exist in every `complaint_data` dict stored to Mongo.
- Complaint status enum is enforced server-side: `"Pending"`, `"In Progress"`, `"Resolved"` — exact strings, case-sensitive.
- Summary is truncated to 150 characters (with `...`) inside `analyze_complaint()` — do not truncate elsewhere.
- No `requirements.txt` exists; dependencies must be inferred from imports: `flask`, `flask-cors`, `pymongo`.

## Code Style

- **Python**: Section headers as `# ---` banners every few lines; each logical step separated by blank lines — follow this vertical spacing pattern.
- **Python imports**: stdlib first (`os`, `sys`, `datetime`), then third-party (`flask`, `pymongo`, `bson`, `werkzeug`), then local (`from ai.analyzer import ...`).
- **JavaScript**: Each variable declaration on its own line with a blank line between groups; event delegation preferred (see `document.addEventListener("change", ...)` pattern in `dashboard.js`).
- **Frontend API base URL** is hardcoded to `http://127.0.0.1:5000` in both `script.js` and `dashboard.js` — update both files if the port changes.
