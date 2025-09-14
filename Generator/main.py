def generate_password():
    import string, random, secrets

    # Importing Custom Modules
    try:
        import path_fix
        from colorify import Fore, Style
        from show_name import tool_name

    except ImportError as e:
        print(f"❌ Missing project module: '{e.name}'. Please re-clone Password-Audit.")
        exit(1)

    lower_alphabets = list(string.ascii_lowercase)
    upper_alphabets = list(string.ascii_uppercase)
    integers = list(string.digits)
    special_chars = list(string.punctuation)

    pass_keys = []
    pass_keys.extend(lower_alphabets)
    pass_keys.extend(upper_alphabets)
    pass_keys.extend(integers)
    pass_keys.extend(special_chars)

    tool_name("Strong Password Generator")

    # Input Validation
    while True:
        password_len = input(f"{Fore.YELLOW}Enter Password Length (min 6): {Style.RESET_ALL}")

        if not password_len.isdigit():
            print(f"{Fore.RED}❗ Invalid Password length, Try Again{Style.RESET_ALL}")
            continue

        password_len = int(password_len)

        if password_len < 6:
            print(
                f"{Fore.RED}❗ Password length must be at least 6{Style.RESET_ALL}"
                )
            continue

        break

    # Password Creation
    password_list = [
        secrets.choice(lower_alphabets),
        secrets.choice(upper_alphabets),
        secrets.choice(integers),
        secrets.choice(special_chars),
    ]
    remaining_len = password_len - 4
    password_list += [secrets.choice(pass_keys) for i in range(remaining_len)]
    random.shuffle(password_list)

    password = "".join(password_list)

    print(f"\n{Fore.GREEN}✔ Your Strong Password is:{Style.RESET_ALL}", end="")
    print(f" {Fore.MAGENTA}{Style.BRIGHT}{password}{Style.RESET_ALL}\n")

if __name__ == '__main__':
    generate_password()
