const chatbotToggleButton = document.querySelector(".chatbot-toggle-button");
const chatbotCloseButton = document.querySelector(".chatbot-close-button");
const chatboxMessages = document.querySelector(".chatbox-messages");
const chatInputContainer = document.querySelector(".chat-input-container textarea");
const sendMessageButton = document.querySelector(".chat-input-container span");

let inputInitHeight = chatInputContainer.offsetHeight; // Get the initial height of the textarea

const createChatLi = (message, className) => {
    const li = document.createElement("li");
    li.classList.add("chat-message", className);

    // Use innerHTML to correctly render links
    let innerHTML = `<p>${message}</p>`;
    if (className === "incoming-message") {
        innerHTML = `<span class="material-symbols-outlined">robot_2</span>${innerHTML}`;
    }
    li.innerHTML = innerHTML;

    return li;
};

const generateResponse = async (userMessage) => {
    try {
        const response = await fetch("http://127.0.0.1:5000/chat", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ message: userMessage })
        });
        const data = await response.json();
        return data.response;
    } catch (error) {
        console.error("Error:", error);
        return "Sorry, there was an error processing your request.";
    }
};

const handleChat = async () => {
    const userMessage = chatInputContainer.value.trim(); // Get user entered message and remove extra whitespace
    if (!userMessage) return;

    // Clear the input textarea and set its height to default
    chatInputContainer.value = "";
    chatInputContainer.style.height = `${inputInitHeight}px`;

    chatboxMessages.appendChild(createChatLi(userMessage, "outgoing-message"));
    chatboxMessages.scrollTo(0, chatboxMessages.scrollHeight);

    setTimeout(async () => {
        const incomingChatLi = createChatLi("...", "incoming-message");
        chatboxMessages.appendChild(incomingChatLi);
        chatboxMessages.scrollTo(0, chatboxMessages.scrollHeight);
        const response = await generateResponse(userMessage);
        incomingChatLi.querySelector("p").innerHTML = response;
    }, 600);
};

chatInputContainer.addEventListener("input", () => {
    chatInputContainer.style.height = `${inputInitHeight}px`;
    chatInputContainer.style.height = `${chatInputContainer.scrollHeight}px`;
});

chatInputContainer.addEventListener("keydown", (e) => {
    // If Enter key is pressed without Shift key and the window 
    // width is greater than 800px, handle the chat
    if (e.key === "Enter" && !e.shiftKey && window.innerWidth > 800) {
        e.preventDefault();
        handleChat();
    }
});

sendMessageButton.addEventListener("click", handleChat);
chatbotCloseButton.addEventListener("click", () => document.body.classList.remove("show-chatbot"));
chatbotToggleButton.addEventListener("click", () => document.body.classList.toggle("show-chatbot"));
