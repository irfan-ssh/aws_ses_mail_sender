import tkinter as tk
from tkinter import messagebox
import boto3
from botocore.exceptions import ClientError

def send_email():
    region = region_entry.get()
    aws_access_key_id = aws_access_key_id_entry.get()
    aws_secret_access_key = aws_secret_access_key_entry.get()
    sender = sender_entry.get()
    recipient = recipient_entry.get()
    subject = subject_entry.get()
    body = body_entry.get("5.0", tk.END)

    try:
        client = boto3.client('ses', region_name=region, aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)

        response = client.send_email(
            Destination={'ToAddresses': [recipient]},
            Message={'Body': {'Text': {'Charset': 'UTF-8', 'Data': body}},
                     'Subject': {'Charset': 'UTF-8', 'Data': subject}},
            Source=sender
        )
        messagebox.showinfo("Success", "Email sent! Message ID: {}".format(response['MessageId']))
    except ClientError as e:
        messagebox.showerror("Error", e.response['Error']['Message'])

# Create main window
root = tk.Tk()
root.title("Send Email via AWS SES")

# Create and place widgets
tk.Label(root, text="Region:").grid(row=0, column=0, sticky="w")
region_entry = tk.Entry(root)
region_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="AWS Access Key ID:").grid(row=1, column=0, sticky="w")
aws_access_key_id_entry = tk.Entry(root)
aws_access_key_id_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(root, text="AWS Secret Access Key:").grid(row=2, column=0, sticky="w")
aws_secret_access_key_entry = tk.Entry(root, show="*")
aws_secret_access_key_entry.grid(row=2, column=1, padx=5, pady=5)

tk.Label(root, text="Sender Email:").grid(row=3, column=0, sticky="w")
sender_entry = tk.Entry(root)
sender_entry.grid(row=3, column=1, padx=5, pady=5)

tk.Label(root, text="Recipient Email:").grid(row=4, column=0, sticky="w")
recipient_entry = tk.Entry(root)
recipient_entry.grid(row=4, column=1, padx=5, pady=5)

tk.Label(root, text="Subject:").grid(row=5, column=0, sticky="w")
subject_entry = tk.Entry(root)
subject_entry.grid(row=5, column=1, padx=5, pady=5)

tk.Label(root, text="Body:").grid(row=6, column=0, sticky="w")
body_entry = tk.Text(root, height=10, width=30)
body_entry.grid(row=6, column=1, padx=5, pady=5)

send_button = tk.Button(root, text="Send Email", command=send_email)
send_button.grid(row=7, columnspan=2, padx=5, pady=5)

# Run the main loop
root.mainloop()
