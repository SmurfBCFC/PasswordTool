import pyperclip
from security_tools.generator import generate_secure_password


def get_password_length() -> int:
    """Prompts the user for length and validates it's a number >= 8."""
    while True:
        user_input = input("Enter desired password length (minimum 8): ")

        # Check if input is a number
        if not user_input.isdigit():
            print("❌ Invalid input. Please enter a whole number.")
            continue

        length = int(user_input)

        # Check the business logic
        if length < 8:
            print("⚠️ Length is too short. Security standards require at least 8 characters.")
        else:
            return length


def get_choice(prompt: str) -> bool:
    """Helper to turn y/n input into a True/False boolean."""
    while True:
        choice = input(f"{prompt} (y/n): ").lower().strip()
        if choice in ['y', 'yes']:
            return True
        if choice in ['n', 'no']:
            return False
        print("Please enter 'y' or 'n'.")


def main():
    print("\n" + "=" * 40)
    print("🛡️  ENTERPRISE PASSWORD GENERATOR 🛡️")
    print("=" * 40 + "\n")

    # 1. Get length
    length = get_password_length()

    # 2. Get preferences
    use_upper = get_choice("Include uppercase letters?")
    use_digits = get_choice("Include digits?")
    use_symbols = get_choice("Include special symbols?")

    # 3. Generate the password
    # This calls the logic inside security_tools/generator.py
    try:
        password = generate_secure_password(
            length,
            use_upper=use_upper,
            use_digits=use_digits,
            use_symbols=use_symbols
        )

        # 4. Copy to clipboard
        pyperclip.copy(password)

        print("\n" + "-" * 40)
        print(f"✅ SUCCESS!")
        print(f"Your Password: {password}")
        print("📋 Copied to clipboard automatically.")
        print("-" * 40 + "\n")

    except Exception as e:
        print(f"❌ An error occurred: {e}")


if __name__ == "__main__":
    main()