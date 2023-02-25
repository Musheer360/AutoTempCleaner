import os

print("\n    + -------------------------------- +")
print("    |      AUTO TEMP FILE CLEANER      |")
print("    + -------------------------------- +\n")

dirs_to_clean = ["C:\\Windows\\Temp", "C:\\Users\\Musheer\\AppData\\Local\\Temp"]

for directory in dirs_to_clean:
    for file_name in os.listdir(directory):
        file_path = os.path.join(directory, file_name)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
                print(f"(OK) - Deleted file: {file_path}")
            else:
                print(f"(0) - Skipped non-file: {file_path}")
        except Exception as e:
            print(f"(X) - {e}")