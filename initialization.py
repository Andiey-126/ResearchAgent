from path import root

def initialize_notes():
    folder_path = root / "notes"
    folder_path.mkdir(parents=True, exist_ok=True)