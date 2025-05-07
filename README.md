# Data-Science-Assistance

# 🧠 Script Manager with Mistral AI Integration

![Streamlit](https://img.shields.io/badge/Built%20With-Streamlit-ff4b4b)
![License](https://img.shields.io/badge/License-MIT-green)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

A Streamlit-based web app that allows users to **view, run, and manage saved Python scripts** and integrates with **Mistral AI API** to generate new scripts from natural language prompts.

---

## 🚀 Features

- 📂 Browse and view saved Python files (`codes/`)
- ▶️ Execute scripts safely (supports `matplotlib` plots)
- 🧠 Use Mistral AI to generate and save Python code
- 🧹 Delete or refresh script list easily
- 💾 Extract code blocks automatically from generated responses

---

## 📁 Project Structure

```
.
├── streamlit_app.py         # Main Streamlit interface
├── helper_api.py            # Mistral API functions & helpers
├── codes/                   # Folder for saved/generated scripts
├── .env                     # Store your API key securely
└── README.md
```

---

## 💠 Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/script-manager.git
   cd script-manager
   ```

2. **Install dependencies**
   ```bash
   pip install streamlit matplotlib mistralai python-dotenv
   ```

3. **Create a `.env` file**
   ```env
   MISTRAL_API_KEY=your_mistral_api_key
   AGENT_ID=your_agent_id_if_required
   ```

4. **Run the app**
   ```bash
   streamlit run streamlit_app.py
   ```

---

## 🔐 Environment Variables

Use a `.env` file to store sensitive info like API keys:

```env
# .env
MISTRAL_API_KEY=your_secret_key_here
AGENT_ID=optional_agent_id
```

Then access it in Python:

```python
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("MISTRAL_API_KEY")
```

---

## 📌 Future Enhancements

- 🔐 Add user authentication
- 📂 Support cloud-based storage (e.g., AWS S3 or GDrive)
- ✏️ Inline code editing with syntax highlighting
- 📉 Visual output previews for other libraries (e.g., seaborn, plotly)

---

## 📃 License

This project is licensed under the [MIT License](LICENSE).

---

## 🙇‍♀️ Contributions

Feel free to fork and submit a pull request! Suggestions and improvements are welcome.
