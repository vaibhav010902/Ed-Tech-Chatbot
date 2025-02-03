# 📚 EdTech Chatbot API

An AI-powered chatbot designed for an EdTech platform, built using Flask and NLTK.

## 🚀 Features
- Natural Language Processing (NLP) with NLTK
- Flask-based API for chatbot interaction
- Easy integration with EdTech platforms
- Lightweight and scalable

## 🛠 Tech Stack
- Python
- Flask
- NLTK
- SQLite (or other DB options)

## 📂 Project Structure
```
📁 edtech-chatbot-api
│── 📂 static         # Static files (CSS, JS, etc.)
│── 📂 templates      # HTML Templates
│── 📜 app.py        # Main Flask application
│── 📜 chatbot.py    # Chatbot logic with NLTK
│── 📜 database.py   # Database connection and models
│── 📜 requirements.txt # Dependencies
│── 📜 README.md     # Project Documentation
```

## 🔧 Setup & Installation

1️⃣ Clone the repository:
```sh
git clone https://github.com/yourusername/edtech-chatbot-api.git
cd edtech-chatbot-api
```

2️⃣ Create a virtual environment:
```sh
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3️⃣ Install dependencies:
```sh
pip install -r requirements.txt
```

4️⃣ Run the application:
```sh
python app.py
```

5️⃣ Access the chatbot at:
```
http://127.0.0.1:5000
```

## 📝 API Endpoints
| Method | Endpoint | Description |
|--------|----------|--------------|
| `POST` | `/chat` | Process user query and return chatbot response |
| `GET`  | `/` | Landing page |

## 📜 License
This project is open-source under the MIT License.

---

💡 **Contributions Welcome!** Feel free to open issues and pull requests to enhance this chatbot!
