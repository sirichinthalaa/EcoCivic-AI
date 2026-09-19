# Project Coding Rules (Non-Obvious Only)

- `sys.path.append` in `backend/app.py` must stay — it lets Flask import `ai/` from the parent directory. Removing it breaks the import.
- Every MongoDB route must manually convert `_id` via `str(complaint["_id"])` — no serializer is registered.
- `analyze_complaint()` in `ai/analyzer.py` uses `text.split()` (word-boundary) for the Green Environment category but `in text` (substring) for all others — keep these different when adding new categories.
- All 5 keys (`category`, `subcategory`, `priority`, `sustainability_area`, `summary`) must always be present in the dict returned by `analyze_complaint()`; the route maps them directly to MongoDB without a default fallback.
- Flask runs from `backend/` directory; `UPLOAD_FOLDER = "uploads"` resolves relative to the **cwd at launch**, which is the project root when started with `python backend/app.py` from root.
- No requirements.txt exists — add one if new dependencies are introduced.
