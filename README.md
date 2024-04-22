# AWS SES Mailer

## Description
AWS SES Mailer is a Python script with a graphical user interface (GUI) built using Tkinter. It allows you to send emails using Amazon Simple Email Service (SES) directly from your desktop. You can specify the recipient(s), subject, and body of the email, either individually or by importing multiple recipients from a text file.

## Features
- Send emails using Amazon SES.
- Supports sending emails to individual recipients or multiple recipients from a file.
- Easy-to-use GUI interface.
- Customizable AWS SES credentials and email content.

## Requirements
- Python 3.x installed on your system.
- Boto3 library installed (`pip install boto3`).

## Usage
1. Clone or download the repository to your local machine.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Open a terminal or command prompt and navigate to the project directory.
4. Run the script by executing `python aws_ses_mailer.py`.
5. Fill in the AWS SES credentials, sender email, recipient(s), subject, and body of the email in the GUI.
6. Choose whether you want to send the email to an individual recipient or multiple recipients from a file by checking the respective checkbox.
7. If sending to multiple recipients from a file, click the "Browse" button to select the file containing the list of recipients.
8. Click the "Send Email" button to send the email(s).
9. A success or error message will be displayed, indicating the status of the email(s) sent.

## Example
Here's how you can use the AWS SES Mailer script:

```bash
git clone https://github.com/your_username/aws-ses-mailer.git
cd aws-ses-mailer
pip install -r requirements.txt
python aws_ses_mailer.py
