File Integrity Checker

A simple Python-based cybersecurity tool that checks whether a file has been modified by comparing its SHA-256 hash value with a previously stored hash.

Features

- Generate SHA-256 hash for any file
- Verify file integrity
- Detect file modifications or tampering
- Beginner-friendly Python project
- Command-line interface

Technologies Used

- Python
- hashlib
- os

How to Run

1. Clone the repository:

git clone <https://github.com/shravanidhaybar01/File_integrity_checker>

2. Navigate to the project folder:

cd File-Integrity-Checker

3. Run the program:

python file_integrity_checker.py

Usage

Generate Hash

- Select option "1"
- Enter the file path
- The hash will be generated and stored

Verify Integrity

- Select option "2"
- Enter the file path
- The program compares the current hash with the stored hash and reports whether the file has been modified

Example Output

===== File Integrity Checker =====
1. Generate Hash
2. Verify File Integrity

[+] File Integrity Verified
File has not been modified.

[!] Warning!
File has been changed or tampered with.

Learning Outcomes

- File Integrity Verification
- SHA-256 Hashing
- Python File Handling
- Basic Cybersecurity Concepts

Author
shravani dhaybar
Cybersecurity Student Project
