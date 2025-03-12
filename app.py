# This project is licensed under the MIT License. See the LICENSE file for more details.
from flask import Flask, request, jsonify
from flask_cors import CORS
import spacy
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import SVC
import random
import pandas as pd

app = Flask(__name__)
CORS(app)

# Load SpaCy model
nlp = spacy.load('en_core_web_sm')

# Load the training data from the Excel file
training_data = pd.read_csv('training_data.csv', encoding='latin1')

# Separate the data into inputs and labels
texts = training_data['input'].tolist()
labels = training_data['label'].tolist()


# Convert the texts to feature vectors
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(texts)

# Train a Naive Bayes classifier
model = SVC(kernel='linear')
model.fit(X, labels)

# Define responses
responses = {
    # GREETING
    "greeting": ["Hello! How can I assist you today?", "Hi there! How can I help you?"],
    # COURSE INQUIRY
    "course_inquiry": ["We offer a wide variety of courses designed to meet your learning needs and career goals. You can explore the full list of our available courses by clicking <a href='https://live.ilearningscareer.com/s/store' target='_blank'><b>here</b></a>."],
    # ENROLLMENT
    "enrollment": ["To enroll in our courses, please follow these steps:\n<b>1. Create an Account</b>: Visit our website and register for a new account.\n<b>2. Browse Courses</b>: Explore our extensive catalog of courses to find the one that suits your needs.\n<b>3. Enroll</b>: Once you've selected a course, click the 'Enroll' button to join."],
    # TECHNICAL SUPPORT
    "technical_support": ["We apologize for any inconvenience. For assistance with accessing your course materials, please contact our support team at <a href='tel:+1234567890' target='_blank'>123-456-7890</a>"],
    # ACCOUNT MANAGEMENT
    "account_management": ["To update your account information, please adhere to the following steps:\n<b>1</b>. Click on the drop-down menu located at the top-right corner adjacent to the profile icon.\n<b>2</b>. From the drop-down menu, select 'My Profile.'\n<b>3</b>. You will be redirected to the account settings page where you can modify your account information.\n<b>4</b>. Upon completion of updating your account information, click on the 'Save' button located at the bottom of the page.\n<b>5</b>. Your account information has been successfully updated."],
    # FEEDBACK
    "feedback": ["We value your feedback. Please share your thoughts with us through our feedback form."],
    # PAYMENT
    "payment": ["We accept various payment methods including credit cards, debit cards, and PayPal."],
    # PAYMENT ISSUE
    "payment_issue": ["Thank you for reaching out. It appears that your course payment has not been received in our system. Please ensure the payment was successfully completed and check for a confirmation receipt.<br><br>If you have the confirmation, please provide the transaction ID or proof of payment. You can email these details to <a href='mailto:info@ilearningscareer.com' target='_blank'>info@ilearningscareer.com</a> or contact us at <a href='tel:+1234567890' target='_blank'>123-456-7890</a>.<br><br>We apologize for the inconvenience and appreciate your patience."],
    # CANCELLATION
    "cancellation": ["We do not issue refunds for non-tangible irrevocable goods ('digital products') once the order is confirmed and the product is sent. <a href='https://live.ilearningscareer.com/refundpolicy' target='_blank'><b>Refund Policy</b></a>.<br><br>We recommend contacting us for assistance if you experience any issues receiving or downloading our products. Contact us for any issues at <a href='tel:+1234567890'>123-456-7890</a>."],
    # DEADLINE
    "deadline": ["Enrollment deadlines vary by course. Please check the specific course page for details."],
    # THANKS
    "thanks": ["You're welcome! Is there anything else I can help with?", "Happy to help! Do you have any other questions?"],
    # GOODBYE
    "goodbye": ["Goodbye! Have a great day!", "Bye! Feel free to reach out if you have more questions."],
    # ORGANIZATION
    "organization": ["Making a socio-economic impact globally by becoming the world's largest contributor in Educational Technology. Formerly known as India ka learning Platform recognised as 'Leading E-Learning Platform Of The Year' in Dubai.\n\nOur vision is to make high-quality education accessible to everyone, regardless of their background barriers to learning and provide opportinities for personal and professional growth to learners globally."],
    # CHATBOT
    "chatbot": ["Hello! I'm I-Learning, an AI language model developed by <a href='https://www.linkedin.com/in/vaibhavagrawal1902' target='_blank'>Vaibhav Agrawal</a> . I'm here to assist you with your queries and provide helpful information. While there are some restrictions on the questions I can answer, I'll do my best to help you. How can I assist you today?"],
    # DEFAULT
    "default": ["I'm sorry, I didn't understand that. Could you please rephrase or ask something else?"]
}

def predict(text):
    X_new = vectorizer.transform([text])
    prediction = model.predict(X_new)
    return prediction[0]

# Route to handle POST request with user query
@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    if user_input:
        intent = predict(user_input)
        response = random.choice(responses[intent])
        return jsonify({"response": response})
    else:
        return jsonify({"response": "I didn't understand that. Can you please rephrase?"})

if __name__ == '__main__':
    app.run(debug=True)