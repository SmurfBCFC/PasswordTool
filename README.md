# 🛡️ Enterprise Password Generator

A professional-grade, modular Python tool designed to generate cryptographically secure passwords. Built with a focus on security best practices and clean architecture.

## 🚀 Key Features
* **Cryptographic Security**: Uses Python's `secrets` module (PEP 506) rather than the standard `random` library for true entropy.
* **Collision Resistance**: Integrates `uuid` suffixes to ensure unique password generation in distributed environments.
* **Clipboard Integration**: Automatically copies generated passwords to the system clipboard for immediate use.
* **Input Validation**: Strict enforcement of security standards (minimum 8 characters, character variety checks).

## 🛠️ Technical Architecture
The project follows a modular structure to separate business logic from the user interface:
* `main.py`: Handles user interaction, input sanitization, and clipboard operations.
* `security_tools/`: A dedicated package containing the core generation engine.
* `.venv`: Isolated environment management to ensure zero dependency conflicts.

## 📦 Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/SmurfBCFC/PasswordTool.git](https://github.com/SmurfBCFC/PasswordTool.git)
   cd PasswordTool