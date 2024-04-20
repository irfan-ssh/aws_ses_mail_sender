import boto3
from botocore.exceptions import ClientError

def send_email(sender, recipient, subject, body, region, aws_access_key_id, aws_secret_access_key):
    # Create a new SES resource
    client = boto3.client('ses', region_name=region, aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)

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
region = "us-east-1"
aws_access_key_id = "AKIA47CRUURDNJNQDZY3"
aws_secret_access_key = "VmzvWP59CGQGW0T3vEBNcL9BDYL/ttTEGVYV7Qo/"
sender = 'irfanssh111@gmail.com'
recipient = 'irfanssh111@gmail.com'
subject = 'new from python code'
body = 'This is a test email sent using AWS SES.'

send_email(sender, recipient, subject, body, region, aws_access_key_id, aws_secret_access_key)
