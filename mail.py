import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
def send_email( empfänger_email, diziplinen):
    sender_email=os.environ["mail"]
    # Create the email
    msg = MIMEMultipart()
    empfänger_email="faxe@punkmail.org"
    mail_psw = os.environ["psw_mail"]
    msg['From'] = sender_email
    msg['To'] = empfänger_email
    msg['Subject'] = "Bestätigung Anmeldung Heideseeschwimmen"
    body = mail_text(diziplinen)
    # Attach the email body
    mail_server = os.environ["mail_server"]
    msg.attach(MIMEText(body, 'plain'))

    try:
        # Connect to the server
        print("start")
        server = smtplib.SMTP(mail_server, 587)  # Use your SMTP server and port
        print("verbindung hergestellt")
        server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
        print()
        server.login(sender_email, mail_psw)
        print("login ")
        # Send the email
        print(msg.as_string())
        server.sendmail(sender_email, empfänger_email, msg.as_string())

        # Disconnect from the server
        server.quit()

    except Exception as e:
        print(f"Failed to send email. Error: {e}")
def mail_text(disziplin):
    footer_datei = open("static/footer.txt","r")
    footer_text = footer_datei.read()
    if len(disziplin) == 1:
        if disziplin[0] == "400m":
            text = ("Hiermit bestätigen wir ihre Anmeldung für die 400 Meter Strecke beim Heideseeschwimmen " + footer_text)
        elif disziplin[0] == "1000m":
            text = ("Hiermit bestätigen wir ihre Anmeldung für die 1000 Meter Strecke beim Heideseeschwimmen" + footer_text)
        elif disziplin[0] == "2500m":
            text = ("Hiermit bestätigen wir ihre Anmeldung für die 2500 Meter Strecke beim Heideseeschwimmen" + footer_text)
    elif len(disziplin) == 2:
        if disziplin[0] == "400m":
            if disziplin[1] == "1000m":
                text = ( "Hiermit bestätigen wir ihre Anmeldung für die Strecken 400 Meter und 1000 Meter beim Heideseeschwimmen" + footer_text)
            else:
                text = ("Hiermit bestätigen wir ihre Anmeldung für die Strecken 400 Meter und 2500 Meter beim Heideseeschwimmen" + footer_text)
        else:
            text = ("Hiermit bestätigen wir ihre Anmeldung für die Strecken 1000 Meter und 2500 Meter beim Heideseeschwimmen" + footer_text)
    elif len(disziplin) == 3:
        text = ("Hiermit bestätigen wir ihre Anmeldung für die Strecken 400 Meter, 1000 Meter und 2500 Meter beim Heideseeschwimmen" + footer_text)
    return text