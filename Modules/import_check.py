import importlib.util

def ensure_module(modules_list):
    for name in modules_list:
        if not(importlib.util.find_spec(name)):
            print("'{name}' Module is Missing. Run 'pip install -r requirements.txt' to install them.")
            exit(1)
