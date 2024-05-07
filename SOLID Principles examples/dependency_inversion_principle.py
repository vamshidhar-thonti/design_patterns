# Violates

class EmailService:
    def send_email(self, message, receiver):
        print(f"Sending email: {message} to {receiver}")

class SmsService:
    def send_sms(self, message, receiver):
        print(f"Sending sms: {message} to {receiver}")

class NotificationService:
    def __init__(self) -> None:
        self.email_service = EmailService()
        self.sms_service = SmsService()

    def send_notification(self, message, receiver, method):
        if method == "email":
            self.email_service.send_email(message, receiver)
        elif method == "sms":
            self.sms_service.send_sms(message, receiver)

# Fix

from abc import ABC, abstractmethod

class IMessageService(ABC):
    @abstractmethod
    def send(self, message, receiver):
        pass

class EmailService(IMessageService):
    def send(self, message, receiver):
        print(f"Sending email: {message} to {receiver}")

class SmsService(IMessageService):
    def send(self, message, receiver):
        print(f"Sending sms: {message} to {receiver}")

class NotificationService:
    def __init__(self, message_service: IMessageService) -> None:
        self.message_service = message_service

    def send_notification(self, message, receiver):
        self.message_service.send(message, receiver)
