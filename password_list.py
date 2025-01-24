def generate_complex_passwords():
    passwords = set()  # Using a set to avoid duplicates
    
    # Add the initial list of passwords
    initial_passwords = [
        "00009", "0100", "0120", "0123", "2580", "1111", "2222", "3333", "4444", "5555",
        "6666", "7777", "8888", "9999", "768764", "098709", "1234", "4321", "000000", 
        "00001", "12345", "123456", "123123", "qwerty", "password", "abc123", "password1",
        "letmein", "welcome", "sunshine", "qwertyuiop", "iloveyou", "princess", "admin",
        "password123", "welcome1", "1q2w3e4r", "football", "monkey", "abc1234", "123qwe",
        "qwerty123", "111111", "1qaz2wsx", "qazwsx", "asdfgh", "55555", "123321", "qwerty1",
        "shadow", "qwert", "iloveu", "1q2w3e", "trustno1", "11111111", "123qweasd", "freedom",
        "welcome123", "password12", "qwertyui", "letmein1", "123abc", "1qazxsw2", "dragon",
        "qwerty1a", "letmein123", "12345abc", "qwerty12", "1q2w3e4r5t", "qwerty654", "test1234",
        "abc456", "abcdef", "qwerty789", "qwertyu", "asdf1234", "password1234", "trustno1!",
        "iloveyou1", "123!@#", "qwerty12a", "monkey1", "ilovemom", "test123", "12345qwerty",
        "1qaz2wsx3edc", "master", "admin123", "qwerty_1", "password1!", "1password"
    ]
    passwords.update(initial_passwords)
    
    # Generate numeric passwords from 4 to 11 digits
    for length in range(4, 12):
        start = 10 ** (length - 1)
        end = min(10 ** length, start + (1600 - len(passwords)))
        for num in range(start, end):
            passwords.add(f"{num:0{length}d}")
            if len(passwords) >= 1600:
                return list(passwords)

    # If we still haven't reached 1600 passwords, add more combinations
    import string
    import itertools

    chars = string.ascii_lowercase + string.digits
    for length in range(2, 12):
        for combo in itertools.product(chars, repeat=length):
            password = ''.join(combo)
            passwords.add(password)
            if len(passwords) >= 1600:
                return list(passwords)

    return list(passwords)

# Generate passwords
password_list = generate_complex_passwords()

print(f"Total unique passwords generated: {len(password_list)}")
print("First 10 passwords:", password_list)
# print("Last 10 passwords:", password_list[-10:])
