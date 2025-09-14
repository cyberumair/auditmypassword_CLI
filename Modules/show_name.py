try:
    from colorify import Fore, Style
except ImportError as e:
    print(f"❌ Missing project module: '{e.name}'. Please re-clone Password-Audit.")
    exit(1)
    
def tool_name(name):
    name = name.upper()
    
    # Decorative lines
    len_lines = len(name) * 2
    lines = f"{Fore.BLUE}{'=' * len_lines}{Style.RESET_ALL}"
    
    print()
    print(lines)
    print(f'\t{Fore.WHITE}{Style.BRIGHT}{name}{Style.RESET_ALL}')
    print(lines)
    print()
