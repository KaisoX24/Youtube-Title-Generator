# 🎬 AI YouTube Title Generator using Groq + LLaMA 3

Generate 5 high-converting YouTube video titles from any topic using the powerful **Groq API** and **LLaMA 3.1-8B Instant**. Includes a built-in file save option via a simple command-line interface and `tkinter`.
---

## 📌 Features

- 🤖 Uses **Groq’s LLaMA 3.1-8B-Instant** model
- 🎯 Generates 5 click-optimized titles for any given topic
- 💾 Option to save results to a `.txt` file with one click
- 🧠 Custom template prompt with topic insertion
- 🧼 Graceful error handling and streaming output for natural effect

---

## ⚙️ Tech Stack

| Technology     | Purpose                                      |
|----------------|----------------------------------------------|
| Python         | Main programming language                    |
| `groq`         | API client to access LLaMA 3.1 model         |
| `tkinter`      | GUI file save dialog                         |
| `.env`         | Environment variable loading for API key     |

---

## 🔐 API Key Setup

You’ll need a **Groq API key**. Get one from:  
👉 [https://console.groq.com](https://console.groq.com)

Then, create a `.env` file in the same directory with:

```env
GROQ_API_KEY=your_api_key_here
```
---
## 📦Installation

### 1. Clone the Repository

```bash
git clone https://github.com/KaisoX24/Youtube-Title-Generator.git
cd Youtube-Title-Generator
```

### 2. Install Dependencies

```bash
pip install groq
```

### 3. Run the Script

```bash
python main.py
```
---
## 🧑‍💻 Author
Developed by Pramit Acharjya
---
## 🪪 License
MIT License — free to use, modify, and distribute.
