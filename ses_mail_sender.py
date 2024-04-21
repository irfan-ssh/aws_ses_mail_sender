import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import scrolledtext
from tkinter import filedialog
import boto3
from botocore.exceptions import ClientError

def send_email():
    region = region_entry.get()
    aws_access_key_id = aws_access_key_id_entry.get()
    aws_secret_access_key = aws_secret_access_key_entry.get()
    sender = sender_entry.get()
    subject = subject_entry.get()
    body = body_entry.get("1.0", tk.END)

    recipients = []
    if recipient_individual.get():
        recipient = recipient_entry.get()
        recipients.append(recipient)
    elif recipient_file.get():
        file_path = file_path_entry.get()
        try:
            with open(file_path, 'r') as file:
                recipients.extend([line.strip() for line in file.readlines()])
        except FileNotFoundError:
            messagebox.showerror("Error", "File not found!")
            return

    success_count = 0
    failed_count = 0
    error_message = ""
    client = boto3.client('ses', region_name=region, aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)

    for recipient in recipients:
        try:
            response = client.send_email(
                Destination={'ToAddresses': [recipient]},
                Message={'Body': {'Text': {'Charset': 'UTF-8', 'Data': body}},
                         'Subject': {'Charset': 'UTF-8', 'Data': subject}},
                Source=sender
            )
            success_count += 1
        except ClientError as e:
            failed_count += 1
            error_message += f"Failed to send email to {recipient}: {e.response['Error']['Message']}\n"

    if failed_count > 0:
        messagebox.showerror("Error", f"{failed_count} emails failed to send.\n{error_message}")
    else:
        messagebox.showinfo("Success", f"{success_count} emails sent successfully!")

def browse_file():
    file_path = filedialog.askopenfilename()
    file_path_entry.delete(0, tk.END)
    file_path_entry.insert(tk.END, file_path)

def select_individual():
    recipient_individual.set(True)
    recipient_file.set(False)
    recipient_entry.config(state="normal")
    file_path_entry.config(state="disabled")
    browse_button.config(state="disabled")

def select_file():
    recipient_individual.set(False)
    recipient_file.set(True)
    recipient_entry.config(state="disabled")
    file_path_entry.config(state="normal")
    browse_button.config(state="normal")

# Create main window
root = tk.Tk()
root.title("AWS SES MAILER")

# Set minimum window size
root.minsize(400, 400)

# Configure AWS colors
aws_blue = "#232F3E"
aws_yellow = "#FF9900"
aws_gray = "#131A22"
aws_white = "#ffffff"
aws_black = "#030202"

# Set background color of the window
root.config(bg=aws_blue)

# Create and place widgets
title_label = tk.Label(root, text="AWS SES MAILER", font=("Helvetica", 16, "bold"), bg=aws_blue, fg=aws_yellow)
title_label.grid(row=0, column=0, columnspan=3, pady=10)

tk.Label(root, text="Region:", bg=aws_blue, fg=aws_white).grid(row=1, column=0, padx=5, pady=5, sticky="w")
region_entry = tk.Entry(root)
region_entry.grid(row=1, column=1, padx=5, pady=5, sticky="we")

tk.Label(root, text="AWS Access Key ID:", bg=aws_blue, fg=aws_white).grid(row=2, column=0, padx=5, pady=5, sticky="w")
aws_access_key_id_entry = tk.Entry(root)
aws_access_key_id_entry.grid(row=2, column=1, padx=5, pady=5, sticky="we")

tk.Label(root, text="AWS Secret Access Key:", bg=aws_blue, fg=aws_white).grid(row=3, column=0, padx=5, pady=5, sticky="w")
aws_secret_access_key_entry = tk.Entry(root, show="*")
aws_secret_access_key_entry.grid(row=3, column=1, padx=5, pady=5, sticky="we")

tk.Label(root, text="Sender Email:", bg=aws_blue, fg=aws_white).grid(row=4, column=0, padx=5, pady=5, sticky="w")
sender_entry = tk.Entry(root)
sender_entry.grid(row=4, column=1, padx=5, pady=5, sticky="we")

recipient_individual = tk.BooleanVar()
recipient_file = tk.BooleanVar()

individual_checkbox = tk.Checkbutton(root, text="Individual Recipient", variable=recipient_individual, command=select_individual, bg=aws_blue)
individual_checkbox.grid(row=5, column=0, padx=5, pady=5, sticky="w")
recipient_entry = tk.Entry(root, state="disabled")
recipient_entry.grid(row=5, column=1, padx=5, pady=5, sticky="we")

file_checkbox = tk.Checkbutton(root, text="Multiple Recipients from File", variable=recipient_file, command=select_file, bg=aws_blue)
file_checkbox.grid(row=6, column=0, padx=5, pady=5, sticky="w")
file_path_entry = tk.Entry(root, state="disabled")
file_path_entry.grid(row=6, column=1, padx=5, pady=5, sticky="we")
browse_button = tk.Button(root, text="Browse File", font=("Helvetica", 10, "bold"), command=browse_file, state="disabled", bg=aws_yellow, fg=aws_black)
browse_button.grid(row=6, column=2, padx=5, pady=5, sticky="we")

tk.Label(root, text="Subject:", bg=aws_blue, fg=aws_white).grid(row=7, column=0, padx=5, pady=5, sticky="w")
subject_entry = tk.Entry(root)
subject_entry.grid(row=7, column=1, padx=5, pady=5, sticky="we")

tk.Label(root, text="Body:", bg=aws_blue, fg=aws_white).grid(row=8, column=0, padx=5, pady=5, sticky="w")
body_entry = scrolledtext.ScrolledText(root, height=10, width=40)
body_entry.grid(row=8, column=1, padx=5, pady=5, sticky="we")

# Add resizable corner grip to text box
resize_grip = ttk.Sizegrip(root)
resize_grip.grid(row=9, column=2, padx=5, pady=5, sticky="se")

send_button = tk.Button(root, text="Send Email", font=("Helvetica", 10, "bold"), command=send_email, bg=aws_yellow, fg=aws_black)
send_button.grid(row=10, columnspan=2, padx=5, pady=5)

# Allow resizing of text box
body_entry.grid_propagate(False)

# Configure row and column to have weight
for i in range(11):
    root.grid_rowconfigure(i, weight=1)
for i in range(3):
    root.grid_columnconfigure(i, weight=1)

# Run the main loop
root.mainloop()
