AWS SES Mailer
Description
AWS SES Mailer is a Python script with a graphical user interface (GUI) built using Tkinter. It allows you to send emails using Amazon Simple Email Service (SES) directly from your desktop. You can specify the recipient(s), subject, and body of the email, either individually or by importing multiple recipients from a text file.

Features
Send emails using Amazon SES.
Supports sending emails to individual recipients or multiple recipients from a file.
Easy-to-use GUI interface.
Customizable AWS SES credentials and email content.
Requirements
Python 3.x installed on your system.
Boto3 library installed (pip install boto3).
Usage
Clone or download the repository to your local machine.
Install the required dependencies using pip install -r requirements.txt.
Open a terminal or command prompt and navigate to the project directory.
Run the script by executing python aws_ses_mailer.py.
Fill in the AWS SES credentials, sender email, recipient(s), subject, and body of the email in the GUI.
Choose whether you want to send the email to an individual recipient or multiple recipients from a file by checking the respective checkbox.
If sending to multiple recipients from a file, click the "Browse" button to select the file containing the list of recipients.
Click the "Send Email" button to send the email(s).
A success or error message will be displayed, indicating the status of the email(s) sent.