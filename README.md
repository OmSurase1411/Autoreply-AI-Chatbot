# Autoreply-AI-Chatbot


## 🤖 **Auto-Reply AI Chatbot**  
An AI-powered chatbot designed to automate chat responses with humorous, roast-style replies using OpenAI's GPT-3.5-turbo model. Perfect for adding a fun twist to your conversations!

---

### 🚀 **Features**  
1. **Automated Chat Interaction:**  
   - Uses `pyautogui` to control mouse and keyboard, automating chat interactions without manual input.  
2. **Chat History Analysis:**  
   - Copies and analyzes chat history to identify messages from a specific user (e.g., *Rohan Das*).  
3. **Humorous Response Generation:**  
   - Leverages OpenAI's GPT-3.5-turbo to craft witty, roast-style replies.  
4. **Clipboard Operations:**  
   - Utilizes `pyperclip` to copy chat history and paste generated responses seamlessly.  
5. **Efficient Workflow:**  
   - Runs in a loop, continuously monitoring chats and responding when triggered.  

---

### 🔄 **Workflow**  
1. **Initialization:** Opens Chrome and navigates to the chat application.  
2. **Chat History Retrieval:** Copies recent messages from the chat.  
3. **Message Analysis:** Checks if the last message was sent by the target user.  
4. **Response Generation:** Sends chat history to GPT-3.5 for a witty reply.  
5. **Message Delivery:** Pastes and sends the response automatically.  

---

### 🛠️ **Tech Stack & Libraries**  
- **Python**: Core programming language.  
- **OpenAI API**: For generating AI-powered responses.  
- **pyautogui**: Automates mouse and keyboard interactions.  
- **pyperclip**: Manages clipboard operations.  
- **time**: Manages delays for smooth execution.  

