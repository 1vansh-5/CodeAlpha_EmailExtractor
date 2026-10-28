import re
from pathlib import Path


# Matches common email formats; it does not check whether an inbox exists.
EMAIL_PATTERN = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9-]+(?:\.[A-Za-z0-9-]+)*\.[A-Za-z]{2,}\b"


def extract_emails(text):
    matches = re.findall(EMAIL_PATTERN, text)
    emails = []
    seen = set()

    for email in matches:
        # Treat differently capitalized copies as duplicates for this project.
        if email.lower() not in seen:
            emails.append(email)
            seen.add(email.lower())

    return emails


def main():
    print("Email Address Extractor")
    project_folder = Path(__file__).resolve().parent
    user_path = input("Enter the text file path (Enter for sample.txt): ").strip().strip('"')
    input_file = Path(user_path).expanduser() if user_path else project_folder / "sample.txt"
    output_file = project_folder / "extracted_emails.txt"

    if input_file.resolve() == output_file.resolve():
        print("Choose a different input file so your source is not overwritten.")
        return

    try:
        text = input_file.read_text(encoding="utf-8-sig")
    except FileNotFoundError:
        print("File not found. Check the path and try again.")
        return
    except UnicodeError:
        print("Please save the input as a UTF-8 text file and try again.")
        return
    except OSError as error:
        print(f"Could not read the file: {error}")
        return

    emails = extract_emails(text)
    if not emails:
        print("No email addresses found. No output file was changed.")
        return

    print(f"\nFound {len(emails)} unique email address(es):")
    for email in emails:
        print(email)

    if output_file.exists():
        answer = input("\nextracted_emails.txt already exists. Replace it? (y/n): ")
        if answer.strip().lower() != "y":
            print("Save cancelled.")
            return

    try:
        output_file.write_text("\n".join(emails) + "\n", encoding="utf-8")
        print(f"\nSaved to: {output_file}")
    except OSError as error:
        print(f"Could not save the email addresses: {error}")


if __name__ == "__main__":
    main()
