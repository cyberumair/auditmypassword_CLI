def check_password():
    # Importing Custom Modules
    try:
        import path_fix
        from colorify import Fore, Style
        from show_name import tool_name
        from file_downloader import install_file
        
    except ImportError as e:
        print(f"❌ Missing project module: '{e.name}'. Please re-clone Password-Audit.")
        exit(1)
    
    # Checking rockyou.txt
    import os
    try:
        if not(os.path.exists('rockyou.txt')):
            install_file("https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt") # Install rockyou.txt
    except:
        pass
               
    import time, importlib.util
        
    tool_name('Common Password Checker')
            
    password = input(f"{Fore.CYAN}Enter password to check: {Style.RESET_ALL}")
        
    # Highlight password in red always
    highlighted_pass = f"{Fore.RED}{Style.BRIGHT}{password}{Style.RESET_ALL}"
        
    pass_found = f"'{highlighted_pass}' is a Common password. Try to make it stronger 🥶"
    pass_not_found = f"'{highlighted_pass}' is Not a common password. Good 🫡"
        
    found = False
        
    print(f"\n{Fore.YELLOW}🔥 Brute Forcing 'rockyou.txt' ...{Style.RESET_ALL}")
        
    start_time = time.time()
        
    with open("rockyou.txt", "r", errors="ignore") as f:
        for line in f:
            if line.strip() == password:
                found = True
                break
        
    total_time = round(time.time() - start_time, 2)
        
    print('')
    if found:
        print(pass_found, f"{Fore.CYAN}(Checked in {total_time} seconds){Style.RESET_ALL}")
    else:
        print(pass_not_found, f"{Fore.CYAN}(Checked in {total_time} seconds){Style.RESET_ALL}")

if __name__ == '__main__':
    check_password()
