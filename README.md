# Maildir to Mbox Converter

A Python script for converting emails from Maildir format to Mbox format. This is useful for creating backups or migrating emails to another email client.

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

## Usage
- **Converting Emails**
Run the script using the following syntax:
   ```bash 
    python3 md2mb.py [path_to_maildir] [output_mbox_file]

Example:
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
- `LICENSE`: This project is licensed under the MIT License - see the LICENSE file for details.