
import boto3
from botocore.exceptions import ClientError


from core.settings import Settings

settings = Settings()

ses = boto3.client('ses',
                   endpoint_url=settings.AWS_ENDPOINT_URL,
                   region_name=settings.AWS_REGION_NAME,
                   aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
                   aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY)


def send_email(sender_email, recipient_email, subject, body):

    try:
        ses.verify_email_identity(EmailAddress=sender_email)
        ses.verify_email_identity(EmailAddress=recipient_email)

        # Specify the email subject and body
        email_subject = subject
        email_body = body

        # Create the message
        message = {
            'Subject': {'Data': email_subject},
            'Body': {'Text': {'Data': email_body}}
        }

        # Send the email
        response = ses.send_email(
            Source=sender_email,
            Destination={'ToAddresses': [recipient_email]},
            Message=message
        )


        print(f"Email sent! Message ID: {response['MessageId']}")

        return response
    except ClientError as e:
        print(f"Error: {e.response['Error']['Message']}")


def verify_email(sender_email, recipient_email):
    ses.verify_email_identity(EmailAddress=sender_email)
    ses.verify_email_identity(EmailAddress=recipient_email)

