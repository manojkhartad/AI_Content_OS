import os

# Agar script project ke root me hai to "." use karo
ROOT_DIR = "."

OUTPUT_FILE = "project_code.txt"

# Jin folders ko ignore karna hai
IGNORE_DIRS = {
    "__pycache__",
    ".git",
    ".venv",
    "venv",
    "env",
    "node_modules",
    "build",
    "dist",
    ".idea",
    ".vscode"
}

with open(OUTPUT_FILE, "w", encoding="utf-8") as outfile:

    for foldername, subfolders, filenames in os.walk(ROOT_DIR):

        # Ignore folders
        subfolders[:] = [d for d in subfolders if d not in IGNORE_DIRS]

        for filename in sorted(filenames):

            if filename.endswith(".py"):

                file_path = os.path.join(foldername, filename)
                relative_path = os.path.relpath(file_path, ROOT_DIR)

                outfile.write("=" * 58 + "\n")
                outfile.write(f"FILE: {relative_path}\n")
                outfile.write("=" * 58 + "\n\n")

                try:
                    with open(file_path, "r", encoding="utf-8") as f:
                        outfile.write(f.read())
                except Exception as e:
                    outfile.write(f"Error reading file: {e}")

                outfile.write("\n\n")

print(f"Done! Output saved to '{OUTPUT_FILE}'")