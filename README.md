# Maildir to Mbox Converter

A Python script for converting emails from Maildir format to Mbox format. This is useful for creating backups or migrating emails to another email client. 

## Context

This script can be particularly helpful for transferring email files from DirectAdmin (located at `imap/domain.nl/info/Maildir`) to another hosting service that only accepts importing emails in MIME or Mbox format. The resulting `output.mbox` file can then be imported into the Roundcube webmail interface.

## Requirements

- **Python 3.x**: Ensure that Python 3 is installed on your system. This script uses standard Python libraries, so no additional packages are required.

## Installation

1. **Clone or download the repository**:
   ```bash
   git clone https://github.com/yourusername/maildir-to-mbox-converter.git
   cd maildir-to-mbox-converter

2. **Make the script executable (optional):**
    ```bash
    chmod +x md2mb.py

## Steps to Convert Maildir to Mbox

1. **Go to DirectAdmin** and navigate to the folder, e.g., `imap/domain.nl/info/Maildir`.
2. **Compress the Maildir** folder into a `.zip` file and download it to your local machine.
3. **Extract the downloaded `.zip` file** to access the Maildir folder.
4. Run the following command to convert the Maildir to Mbox:
   ```bash
   python3 md2mb.py Maildir output.mbox


## Usage
- **Converting Emails**
Run the script using the following command:
    ```bash 
    python3 md2mb.py Maildir output.mbox 

## Explanation of Parameters

- **Maildir**: The path to your Maildir directory containing the emails.
- **output.mbox**: The name of the Mbox file that will be created. This file will contain all the emails converted from the Maildir format.

### Output

The script will create an Mbox file named `output.mbox` containing all emails from the specified Maildir.  
It will also create a directory named `output.mbox.sbd`, containing subdirectories for each subfolder in your Maildir, preserving the folder structure.

### What You Can Do with the Output

- The `output.mbox` file can be imported into various email clients (such as Thunderbird, Evolution, or Apple Mail) that support the Mbox format.
- The `output.mbox.sbd` directory can help maintain your folder hierarchy, allowing you to access subfolders in your email client.

### File Structure

- `md2mb.py`: The Python script for the conversion.
- `README.md`: This documentation.
- `LICENSE`: This project is licensed under the MIT License

