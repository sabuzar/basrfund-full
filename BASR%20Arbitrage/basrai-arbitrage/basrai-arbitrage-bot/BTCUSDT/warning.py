
import smtplib



def error_note():
    sender_email = 'abuzarmehdi4433@gmail.com'
    receiver_email = 'abuzar@basrfunds.com'

    subject = "Code Stopped Due error"
    message = 'code stopped '
    text = f"Subject: {subject}\n\n{message}"

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        app_password = 'rija mqra iywq xbpw'
        server.login(sender_email, app_password)
        server.sendmail(sender_email, receiver_email, text)
    except Exception as e:
        print(f"Failed to send email: {e}")

    finally:
        server.quit()
