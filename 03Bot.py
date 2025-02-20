import pyautogui
import time
import pyperclip
from openai import OpenAI

client = OpenAI(
    api_key="<YOUR API KEY HERE>",
)

def is_last_message_from_sender(chat_log, sender_name="<YOUR SENDER NAME>"):
    #Split the chat log into individual messages
    messages = chat_log.strip().split("/2025]")[-1]
    if sender_name in messages:
        return True
    return False


    
    # Step 1: Click on the chrome icon at (1290, 1051)
pyautogui.click(1290, 1051)
time.sleep(1)  # Wait for any UI response

while True:
    time.sleep(4)
    
    # Step 2: Click and drag to select text from (688, 222) to (1863, 903)
    pyautogui.moveTo(688, 222)
    pyautogui.mouseDown()
    pyautogui.moveTo(1863, 903, duration=0.5)  # Drag smoothly
    pyautogui.mouseUp()

    # Step 3: Copy the selected text
    pyautogui.hotkey('ctrl', 'c')  # For Windows/Linux
    time.sleep(3)  # Give time for clipboard to update
    pyautogui.click(686,242)

    # Step 4: Retrieve text from clipboard
    chat_history = pyperclip.paste()

    print("Copied Text:", chat_history)
    print(is_last_message_from_sender(chat_history))

    if is_last_message_from_sender(chat_history):


        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a person named om who speaks english, hindi and marathi.You are from India and you are an engineer. You analyze chat history and respond like om. Output should be the next chat response (text message only) and dont type in marathi language. Change mood according how the chat is going. One more thing to keep in mind is that do not include my name and timestamp in the response."},
                {
                    "role": "user",
                    "content": chat_history
                }
            ]
        )

        response= completion.choices[0].message.content
        pyperclip.copy(response)


        # Step 5: Click at (1228, 960), paste the text, and press enter
        pyautogui.click(1228, 960)
        time.sleep(1)
        pyautogui.hotkey('ctrl', 'v')  # For Windows/Linux

        pyautogui.press('enter')












