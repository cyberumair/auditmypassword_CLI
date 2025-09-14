import sys, os

def add_modules_paths():
    current_dir = os.path.abspath(os.path.dirname(__file__))
    while True:
        modules_path = os.path.join(current_dir, "Modules")
        if os.path.isdir(modules_path) and modules_path not in sys.path:
            sys.path.append(modules_path)

        # Go one level up
        parent_dir = os.path.dirname(current_dir)
        if parent_dir == current_dir:  # reached root
            break
        current_dir = parent_dir

add_modules_paths()
