import hashlib
import os

def calculate_hash(file_path):
    sha256 = hashlib.sha256()

    try:
        with open(file_path, "rb") as file:
            while True:
                data = file.read(4096)
                if not data:
                    break
                sha256.update(data)

        return sha256.hexdigest()

    except FileNotFoundError:
        print("File not found!")
        return None


def save_hash(file_path, hash_value):
    with open("hash_record.txt", "w") as file:
        file.write(f"{file_path}\n")
        file.write(hash_value)


def check_integrity(file_path):
    if not os.path.exists("hash_record.txt"):
        print("No previous hash record found.")
        return

    with open("hash_record.txt", "r") as file:
        old_file = file.readline().strip()
        old_hash = file.readline().strip()

    current_hash = calculate_hash(file_path)

    if current_hash == old_hash:
        print("\n[+] File Integrity Verified")
        print("File has not been modified.")
    else:
        print("\n[!] Warning!")
        print("File has been changed or tampered with.")


print("===== File Integrity Checker =====")
print("1. Generate Hash")
print("2. Verify File Integrity")

choice = input("Enter your choice (1/2): ")

if choice == "1":
    path = input("Enter file path: ")

    file_hash = calculate_hash(path)

    if file_hash:
        print("\nGenerated SHA-256 Hash:")
        print(file_hash)

        save_hash(path, file_hash)
        print("\nHash saved successfully.")

elif choice == "2":
    path = input("Enter file path to verify: ")
    check_integrity(path)

else:
    print("Invalid choice!")