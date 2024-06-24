import pyautogui
import time
import pyperclip
# from openai import OpenAI

  # client = OpenAI(
  #   api_key="Your Api Key"
  # )


# Function to perform the sequence of actions
def perform_actions():
    # Click on the icon at (1377, 1045)
    pyautogui.click(1361, 1042)
    time.sleep(1)  # wait for 1 second for the link to load
    
    # Click on the link at (901, 649)
    pyautogui.click(901, 649)
    time.sleep(10)  # wait for 10 seconds for WhatsApp to open
    
    # Click on the first chat in WhatsApp at (212, 411)
    pyautogui.click(212, 411)
    time.sleep(5)  # wait for 5 second for the chat to open
    
    # Drag to select text from (578, 190) to (578, 1012)
    pyautogui.moveTo(615, 217)
    pyautogui.dragTo(1870, 940, duration=1)  # drag for 1 second
    
    # Copy the selected text to the clipboard
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(1)  # wait for 1 second to ensure the text is copied
    pyautogui.click(591, 321) # De-select the copied text
    
    # Get the text from the clipboard
    copied_text = pyperclip.paste()
    

    return copied_text

# Execute the function and print the copied text
copied_text = perform_actions()
print(f"Copied Text: {copied_text}")


# completion = client.chat.completions.create(
#   model="gpt-3.5-turbo",
#   messages=[
#     {"role": "system", "content": "You are a person named Soumyadeep and you speak Hindi Bengali aand English as well. You are from India and you are a coder. You analyse the chat history and respond like Soumyadeep. Your respond should be according the previous text detected and don't use obvious ai words so that they should not understand that they are talking to a bot."},
#     {"role": "user", "content": copied_text}
#   ]
# )

# response = print(completion.choices[0].message.content)


# def perform_functions():
#     response = response
    
#     # Click at (1145, 981) to focus on the chatbox
#     pyautogui.click(1145, 981)
#     time.sleep(1)  # wait for 1 second
    
#     # Type the response text
#     pyperclip.copy(response)
#     pyautogui.hotkey('ctrl', 'v')
#     time.sleep(0.5)  # wait for half a second
    
#     # Press Enter to send the message
#     pyautogui.press('enter')
    
#     return response
