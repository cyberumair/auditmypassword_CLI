import os, urllib.request

# Check for Colorama
try:
    from colorama import Style, Fore, init

    init(autoreset=True)

except Exception as e:
    print(e)

    class Dummy:
        def __getattr__(self, name):
            return ""

    Style = Fore = Dummy()


def name_file(url):
    reverse_url = url[::-1]
    index = reverse_url.find("/")
    reverse_name = reverse_url[0:index]
    name = reverse_name[::-1]
    return name


def install_file(url):
    file = name_file(url)

    if not (os.path.exists(file)):
        try:
            print(f"\n{Fore.CYAN}Downloading:{Style.RESET_ALL} '{file}' ...")
            urllib.request.urlretrieve(url, file)
            print(
                f"\n{Fore.GREEN}✅ Done:{Style.RESET_ALL} '{file}' Successfully Downloaded!\n"
            )

        except Exception as e:
            print(f"{Fore.RED}❌ Error:{Style.RESET_ALL} {str(e)}\n")


if __name__ == "__main__":
    try:
        from showcase import show_tool

        show_tool(
            "FILE INSTALLER",
            "🌍 Download files easily",
            "✅ Auto name handling",
            "⚡ Prevents duplicate downloads",
            "Just call 'install_file(url)' with any file link 🎉",
        )

    except Exception as e:
        pass
