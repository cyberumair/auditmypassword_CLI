def humanize_from_logs(log10_seconds, log10_years):
    # if less than one year, show smaller units
    if log10_years < 0:
        seconds = 10 ** log10_seconds

        if seconds >= 1:
            minutes = seconds / 60.0
            if minutes < 1:
                return f"{int(seconds)} seconds (approx.)"
            hours = minutes / 60.0
            if hours < 1:
                return f"{int(minutes)} minutes (approx.)"
            days = hours / 24.0
            if days < 1:
                return f"{int(hours)} hours (approx.)"
            years = days / 365.0
            return f"{int(days)} days (approx.)"

        # Handle small times
        if seconds >= 1e-3:   # milliseconds
            return f"{int(seconds*1e3)} ms (approx.)"
        elif seconds >= 1e-6: # microseconds
            return f"{int(seconds*1e6)} µs (approx.)"
        else:                 # nanoseconds and smaller
            return f"{int(seconds*1e9)} ns (approx.)"

    else:
        years = 10 ** log10_years
        if years < 1e6:
            return f"{int(years)} years (approx.)"
        power = log10(years)
        return f"10^{int(power)} years (approx.)"

def check(func):
    return [i for i in password if func(i)]

def check_strength():    
    import string
    
    global password
    password = input('🔒 Enter a Password: ')
    tool_name('🔐 Password Strength Report') 
       
    print(f"{Fore.CYAN}📝 {Style.BRIGHT}Length: {Style.RESET_ALL}{len(password)}")
    print()
    
    contain_upper = check(str.isupper)
    contain_lower = check(str.islower)
    contain_digit = check(str.isdigit)
    symbols_list = list(string.punctuation)
    contain_symbol = [i for i in password if i in symbols_list]

    variety = []
    if len(contain_upper) > 0:
        variety.append('UpperCase ')
    if len(contain_lower) > 0:
        variety.append('LowerCase ')
    if len(contain_digit) > 0:
        variety.append('Digits ')
    if len(contain_symbol) > 0:
        variety.append('Symbols ')

    var_string = ("".join(variety))[:-1]
    print(f"{Fore.BLUE}🎨 {Style.BRIGHT}Variety: {Style.RESET_ALL}{var_string.replace(' ', ', ')}")
    print()
    
    # Calculating Entropy
    char_size = {'UpperCase':26, 'LowerCase':26, 'Digits':10, 'Symbols':32}
    total_char_size = [0]
    for i in variety:
        size = char_size.get(i.strip())
        total_char_size[0] += size

    entropy = int(len(password) * log2(total_char_size[0]))
    print(f"{Fore.YELLOW}⚡ {Style.BRIGHT}Entropy: {Style.RESET_ALL}{entropy} bits")
    print()
    
    # Crack Time Estimating
    seconds_per_year = 31536000.0
    attempts = 1e7

    log10_seconds = entropy * log10(2) - log10(attempts) 
    log10_years = log10_seconds - log10(seconds_per_year)

    crack_time = humanize_from_logs(log10_seconds, log10_years)
    print(f"{Fore.GREEN}⏳ {Style.BRIGHT}Crack Time: {Style.RESET_ALL}{crack_time}")
    print()
    
    # Verdict Logic
    
    if ( entropy >= 25 and entropy <= 36 ) and crack_time < '1 year':
        print(f"🟡 {Fore.YELLOW}{Style.BRIGHT}Verdict: {Style.RESET_ALL}Medium")
        print()
        print(f'{Fore.YELLOW}{Style.BRIGHT}Review:', '🔒 Decent, your password can hold for now, but stay cautious.')
        
    elif entropy >= 50 and crack_time >= '1 year':
        print(f"🟢 {Fore.GREEN}{Style.BRIGHT}Verdict: {Style.RESET_ALL}Strong")
        print()
        print(f'{Fore.GREEN}{Style.BRIGHT}Review:', '🏰 Fantastic, using this password makes you as secure as Fort Knox.')

    else:
        print(f"🔴 {Fore.RED}{Style.BRIGHT}Verdict: {Style.RESET_ALL}Weak")
        print()
        print(f'{Fore.RED}{Style.BRIGHT}Review:', '⚠️ Unsafe, this password is like leaving your door unlocked.')

    
if __name__ == '__main__':
    from math import log2, log10
    
    # Importing Custom Modules
    try:
        import path_fix
        from colorify import Fore, Style
        from show_name import tool_name
    
    except ImportError as e:
        print(f"❌ Missing project module: '{e.name}'. Please re-clone Password-Audit.")
        exit(1)
            
    print()
    check_strength()
    print()
