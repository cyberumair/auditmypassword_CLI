try:
    from colorama import Fore, Style, init
    init(autoreset=True)
        
except ModuleNotFoundError:
    print('''
    ⚠️ Colorama not installed. Run: pip install colorama
    👉 Continuing without colored output...
    ''')
    class Dummy:
        def __getattr__(self, name):    return ''
    Fore = Style = Dummy()

if __name__ == "__main__":
    try:
        from showcase import show_tool

        show_tool(
            "colorify module",
            "🛡 Handles Colorama safely",
            "✅ Works even if Colorama is not installed",
            "⚡ Keeps CLI output colorful and clean",
            "Just import check() from 'colorify' and use Fore , Style anywhere 🎉",
        )

    except:
        pass
