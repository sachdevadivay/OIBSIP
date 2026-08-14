# 🔐 Password Generator

A Python-based GUI application that generates random passwords based on the user's selected preferences.

## 📌 Features

- 🔢 Set password length
- 🔠 Include uppercase letters (A-Z)
- 🔡 Include lowercase letters (a-z)
- 🔢 Include numbers (0-9)
- 🔣 Include special characters/symbols
- 🔐 Generate random passwords
- 📋 Copy generated password to clipboard
- 🧹 Clear input fields
- ❌ Error handling for invalid input

## 🛠️ Technologies Used

- Python
- Tkinter
- Random
- String

## 📂 Project Structure

```text
Task3_PasswordGenerator/
│
├── main.py
├── requirements.txt
└── README.md
```

## ▶️ How to Run

### 1. Open the project folder

```bash
cd Task3_PasswordGenerator
```

### 2. Run the program

```bash
python3 main.py
```

## 💡 How It Works

1. Enter the required password length.
2. Select the character types you want to include.
3. Click **Generate Password**.
4. The application creates a random password.
5. Click **Copy** to copy the password to the clipboard.
6. Click **Clear** to reset the fields.

## ⚠️ Input Validation

- Password length must be at least 4 characters.
- The password length must be a valid number.
- At least one character type must be selected.

## 🔐 Character Types

| Option | Characters |
|---|---|
| Uppercase | A-Z |
| Lowercase | a-z |
| Numbers | 0-9 |
| Symbols | !@#$%^&* etc. |

## 👨‍💻 Author

**Divay Sachdeva**

B.Tech CSE – UPES

OASIS Infobyte Python Programming Internship
