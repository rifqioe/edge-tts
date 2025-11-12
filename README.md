# 🗣️ Async Edge TTS

A simple asynchronous Text-to-Speech (TTS) implementation using [edge-tts](https://pypi.org/project/edge-tts/) and Python's built-in `asyncio`.  
Supports multiple languages and concurrent TTS generation.

---

## 📦 Requirements

- Python 3.8+
- Internet connection (for fetching Microsoft Edge voices)

---

## ⚙️ Installation

Clone this repository or copy the files, then run:

```bash
# Create virtual environment
python -m venv venv

# Activate venv (Windows)
venv\Scripts\activate

# or Linux / WSL
source venv/bin/activate

# Install dependencies
pip install edge-tts

#(Optional) Save your dependencies:
pip freeze > requirements.txt
```
