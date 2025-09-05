import os
import ssl
import pytz
import smtplib
import logging
import datetime
from dotenv import load_dotenv

load_dotenv()
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def send_mail(subject: str, message: str, e_to: str, e_from: str, password: str) -> None:
    port = 465  # For SSL
    full_msg = f"Subject: {subject}\n\n{message}"
    logger.debug("Establishing connection!")
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(user=e_from, password=password)
        logger.debug(f"Successfully logged in!")
        server.sendmail(from_addr=e_from, to_addrs=e_to, msg=full_msg)
        logger.debug("Mail sent!")
    logger.debug("Connection successfully closed!")


def check_date() -> tuple[bool, datetime.date]:
    start_date = datetime.date(year=2023, month=12, day=20)
    today_date = datetime.datetime.now(pytz.timezone('Australia/Sydney')).date()
    day_delta = today_date - start_date
    if day_delta.days % 14 == 0:
        return True, today_date
    else:
        return False, today_date


def main():
    # check that the date is correct
    is_right_day, today = check_date()
    if not is_right_day:
        logger.info(f"Today: {today} is not the right week!")
        return None
    logger.info(f"Today: {today} is the right week!")
    subject = "[AUTO] Rent Due"
    msg = "Reminder to pay rent today!!!"
    email_to = os.getenv("EMAIL_TO")
    email_from = os.getenv("EMAIL_FROM")
    password = os.getenv("EMAIL_PASSWORD")
    send_mail(subject, msg, email_to, email_from, password)
    logger.info(f"Mail sent on: {today} from {email_from} to {email_to}!")


if __name__ == "__main__":
    main()