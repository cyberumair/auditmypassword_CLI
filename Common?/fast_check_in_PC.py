def fast_check():
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
        
    import os, platform, importlib.util

    tool_name('Common Password checker')
    password = input(f'{Fore.CYAN}Enter a Password to check: {Style.RESET_ALL}')

    # Highlight password in red always
    highlighted_pass = f"{Fore.RED}{Style.BRIGHT}{password}{Style.RESET_ALL}"

    pass_found = f"'{highlighted_pass}' is a Common password. Try to make it stronger 🥶"
    pass_not_found = f"'{highlighted_pass}' is Not a common password. Good 🫡"

    current_sys = platform.system()  # Checks which system is this

    print(f"\n{Fore.YELLOW}🔥 Brute Forcing 'rockyou.txt' ...\n{Style.RESET_ALL}")

    if current_sys in ['Linux', 'Darwin']:  # Darwin is for Mac OS
        os.system(f'grep -Fxq "{password}" rockyou.txt && echo "{pass_found}" || echo "{pass_not_found}"')

    elif current_sys in ['Windows']:
        os.system(f'Select-String -Pattern "^{password}$" -Path "rockyou.txt" > $null; if ($?) {{ Write-Host "{pass_found}" }} else {{ Write-Host "{pass_not_found}" }}')

    else:
        print(f"{Fore.RED}❗ Sorry, Your OS is not supported.{Style.RESET_ALL}")

    print()

if __name__ == '__main__':
    fast_check()
