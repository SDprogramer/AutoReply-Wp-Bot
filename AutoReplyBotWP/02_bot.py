import pyautogui
import time
import pyperclip
from openai import OpenAI

client = OpenAI(
    api_key="sk-proj-lJIDt6kI9ZIMq429rSVRT3BlbkFJ5rE1F5SNBeyEra4Xr75a"
)

# Function to perform the sequence of actions
def Perform_actions():
    # Click on the icon at (1377, 1045)
    pyautogui.click(1377, 1045)
    time.sleep(1)  # wait for 1 second for the link to load
    
    # Click on the link at (901, 649)
    pyautogui.click(901, 649)
    time.sleep(6)  # wait for 6 seconds for WhatsApp to open
    
    # Click on the first chat in WhatsApp at (212, 411)
    pyautogui.click(212, 411)
    time.sleep(1)  # wait for 1 second for the chat to open
    
    # Drag to select text from (578, 190) to (578, 1012)
    pyautogui.moveTo(615, 217)
    pyautogui.dragTo(1870, 904, duration=1)  # drag for 1 second
    
    # Copy the selected text to the clipboard
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(1)  # wait for 1 second to ensure the text is copied
    pyautogui.click(591, 321) # De-select the copied text
    
    # Get the text from the clipboard
    copied_text = pyperclip.paste()

    return copied_text

# Execute the function and print the copied text
copied_text = Perform_actions()
print(f"Copied Text: {copied_text}")

completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a person named Soumyadeep who speaks hindi english and bengali all 3 languages. He is from India and he is a coder. You analyze chat history and respond like soumyadeep"},
        {"role": "user", "Content": copied_text}
    ]
)

response = completion.choices[0].message.content

def Enter_text():  
    pyautogui.click(873, 979)
    time.sleep(1)  # wait for 1 second

    # Type the copied text
    pyautogui.write(response)
    time.sleep(0.5)  # wait for half a second
        
    # Press Enter
    pyautogui.press('enter')
        
    return response
text = Enter_text()
print(f"Text: {text}")