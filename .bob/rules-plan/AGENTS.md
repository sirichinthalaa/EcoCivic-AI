# Project Architecture Rules (Non-Obvious Only)

- The AI classifier is pure keyword matching (no ML, no external API) — category detection is sequential `elif` chains; the first matching category wins, so order of conditions in `ai/analyzer.py` determines priority.
- MongoDB document shape is defined only by `complaint_data` dict in `backend/app.py` — there is no schema validation layer; any structural changes must be reflected manually in both the backend and `dashboard.js` field accesses.
- `uploads/` is created at Flask startup via `os.makedirs(..., exist_ok=True)` and is relative to the process cwd — uploaded images are not served back to the frontend (no static route for `/uploads/`).
- Status transitions are not enforced as a state machine — any of the three values (`Pending`, `In Progress`, `Resolved`) can be set from any other state via PUT.
- Frontend charts (Chart.js) are created once on `loadComplaints()` and never destroyed/recreated — adding a refresh mechanism would require destroying existing Chart instances first to avoid canvas reuse errors.
