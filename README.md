# 📚 Chatbot for Course Inquiry And Support

This project is a Flask-based chatbot designed to assist users with course inquiries, enrollment, technical support, account management, and more. The chatbot uses natural language processing (NLP) with SpaCy and a Support Vector Machine (SVM) model for intent classification. The frontend is built with HTML, CSS, and JavaScript, providing a user-friendly interface for interacting with the chatbot.

## 🚀 Features
- Intent Recognition: The chatbot can classify user queries into predefined intents such as greeting, course_inquiry, enrollment, technical_support, etc.

- Dynamic Responses: Based on the detected intent, the chatbot provides appropriate responses from a predefined set of replies.

- Interactive UI: A clean and responsive user interface with animations and a toggleable chatbot widget.

- CORS Support: The Flask app is configured with CORS to allow cross-origin requests, making it suitable for integration with web applications.

- Easy to Extend: The chatbot's responses and intents can be easily extended by modifying the responses dictionary and the training data.

## 🛠 Tech Stack
- Python
- Flask
- SpaCy
- Scikit-learn
- pandas
- HTML
- CSS
- JavaScript

## 📂 Project Structure
```

│── 📜 app.py              # Main Flask application
│── 📜 training_data.csv   # Training data for intent classification
│── 📜 index.html          # HTML file for the chatbot UI
│── 📜 style.css           # CSS file for styling the chatbot
│── 📜 script.js           # JavaScript for chatbot interactivity
│── 📜 requirements.txt    # Dependencies
└── 📜 README.md           # Project Documentation
```

## 🔧 Setup & Installation

1️⃣ Clone the repository:
```sh
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

2️⃣ Set up a virtual environment (optional but recommended):
```sh
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3️⃣ Install dependencies:
```sh
pip install -r requirements.txt
```

4️⃣ Download the SpaCY model:
```sh
python -m spacy download en_core_web_sm
```

5️⃣ Prepare the training data:
```
Ensure that your training data is stored in a CSV file named training_data.csv with two columns: input (user queries) and label (intents).
```

6️⃣ Run the Flask Application:
```sh
python app.py
```

7️⃣ Open the frontend:
```
Open the index.html file in your browser to interact with the chatbot.
```
## 👤 Usage
# Chatbot Interface
- Click the chatbot toggle button at the bottom-right corner to open the chat window.
- Type your query in the input box and press Enter or click the send button.
- The chatbot will respond based on the detected intent.

# Example Queries
- Greeting: "Hello", "Hi"
- Course Inquiry: "What courses do you offer?"
- Enrollment: "How do I enroll in a course?"
- Technical Support: "I can't access my course materials."
- Account Management: "How do I update my account information?"
- Payment Issues: "I have a problem with my payment."
- Goodbye: "Bye", "Goodbye"

## 👤 Customization
# Add New Intents
- Update the training_data.csv file with new examples and retrain the model.
- Add new intents and responses to the responses dictionary in app.py.

# Modify Responses
- Edit the responses dictionary in app.py to customize the chatbot's replies.

# Change Model
- You can replace the SVM model with another classifier (e.g., Naive Bayes) by modifying the model initialization in app.py.



## 📝 API Endpoints
| Method | Endpoint | Description |
|--------|----------|--------------|
| `POST` | `/chat` | Process user query and return chatbot response |
| `GET`  | `/` | Landing page |

## 📜 License
This project is open-source under the MIT License.

---

💡 **Contributions Welcome!** Feel free to open issues and pull requests to enhance this chatbot!
