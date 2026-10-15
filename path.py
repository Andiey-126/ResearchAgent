from pathlib import Path

root = Path(__file__).resolve().parent

notes_path = root / "notes"
output_path = root / "output"

if __name__ == "__main__":
    print("root=", root)
    print("notes_path=", notes_path)
    print("output_path=", output_path)