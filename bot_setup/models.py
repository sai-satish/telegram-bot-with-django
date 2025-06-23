from django.db import models

class TelegramUser(models.Model):
    user_name = models.CharField(max_length=255)  # Store the username
    chat_creation_timestamp = models.DateTimeField()  # Store the timestamp

    def __str__(self):
        return self.user_name