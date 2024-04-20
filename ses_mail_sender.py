import boto3
from botocore.exceptions import ClientError

def send_email(sender, recipient, subject, body, region):
    # Create a new SES resource
    client = boto3.client('ses', region_name= region)

    # Try to send the email
    try:
        response = client.send_email(
            Destination={
                'ToAddresses': [
                    recipient,
                ],
            },
            Message={
                'Body': {
                    'Text': {
                        'Charset': 'UTF-8',
                        'Data': body,
                    },
                },
                'Subject': {
                    'Charset': 'UTF-8',
                    'Data': subject,
                },
            },
            Source=sender,
        )
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        print("Email sent! Message ID:", response['MessageId'])

# Usage example
region  = "us-east-1"
sender = 'irfanssh111@gmail.com'
recipient = 'irfanssh444@gmail.com'
subject = 'Test Email from code'
body = 'This is a test email sent using AWS SES.'


send_email(sender, recipient, subject, body, region)
