from celery.decorators import task
from celery.utils.log import get_task_logger

from celery import shared_task

from .email import send_contact_email

logger = get_task_logger(__name__)

@task(name="send_contact_message_task")
def send_contact_message_task(full_name, email, phone_number, message):
    logger.info("Sent Contact Email")
    return send_contact_email(full_name, email, phone_number, message)


# For testing celery
@shared_task
def add(x, y):
    return x + y