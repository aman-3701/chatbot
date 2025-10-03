
---

# 🟢 `docs/setup_steps.md`  

```markdown
# Setup & Debugging Notes

## Day 1
- Installed Python 3.10
- Created GitHub repo
- Made folder structure

## Day 2
- Wrote `app.py` (command-line bot)
- Error: "No module named openai"
- Fix: `pip install openai`

## Day 3
- Added Streamlit UI (`streamlit_app.py`)
- Error: API key not set
- Fix: Learned to use environment variables (OPENAI_API_KEY)

## Day 4
- Tested both apps locally
- Added requirements.txt
- Wrote README.md
- Prepared deployment steps (Hugging Face + Render)

---

### Problems & Fixes
1. **Problem:** API key showing in code → Not safe  
   **Fix:** Used environment variables  

2. **Problem:** Streamlit app not loading properly  
   **Fix:** Installed correct version of streamlit (`pip install streamlit==1.27.2`)

3. **Problem:** First time commit failed  
   **Fix:** Added `.gitignore` and retried `git push`

---

✅ Everything is now working fine. Project is ready!
