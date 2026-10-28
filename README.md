# CodeAlpha-EmailExtractor
# Email Address Extractor

A Python script that extracts email addresses from a text file, removes duplicates, and saves the results to another file.

## Requirements

- Python 3 installed on your computer.
- No additional packages are needed.

Check your installation with `python --version`. If Python is missing, install it from https://www.python.org/downloads/ . On Windows, select the option to add Python to PATH, then reopen your terminal.

## Included files

- `email_extractor.py`: the program.
- `sample.txt`: sample input for trying the program.

## How to run

1. Download and extract `CodeAlpha_EmailExtractor.zip`.
2. Open the extracted folder containing `email_extractor.py` and `sample.txt`.
3. Open a terminal in that folder. On Windows, open the folder in File Explorer, type `cmd` in the address bar, and press Enter.
4. Run:

```sh
python email_extractor.py
```

If needed, use `py email_extractor.py` on Windows or `python3 email_extractor.py` on macOS/Linux.

## Try the sample

At this prompt, press Enter without typing a path:

```text
Enter the text file path (Enter for sample.txt):
```

The program reads the included sample and finds three unique addresses:

```text
alice@example.com
bob@example.org
support.team@example.com
```

It saves them to `extracted_emails.txt` beside the script.

## Use your own file

1. Save your input as a plain `.txt` file using UTF-8 encoding.
2. Run the program.
3. Enter the full path to your file at the prompt, for example:

```text
C:\Users\YourName\Documents\contacts.txt
```

A relative path such as `contacts.txt` also works if the file is in your terminal's current folder. Word documents and PDFs are not supported as input.

## Output and behavior

- Each extracted address is saved on a separate line.
- Duplicates are removed, ignoring differences in capitalization.
- The first spelling and original order are preserved.
- If the output file exists, enter `y` to replace it or another answer to cancel saving.
- If no addresses are found, no output file is created or changed.
- The script matches common email formats. It does not verify inboxes or cover every possible valid email format.

## Troubleshooting

- **Python is not recognized:** try `py` on Windows or `python3` on macOS/Linux.
- **Cannot open the script:** extract the ZIP and open a terminal in the folder containing `email_extractor.py`.
- **File not found:** check the input path and `.txt` extension.
- **Encoding error:** save the input as UTF-8 and try again.
- **Cannot save:** keep the project in a folder where you have write permission.
