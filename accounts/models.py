from django.db import models

class User(models.Model):
    id = models.BigAutoField(primary_key=True)  # Auto-incrementing primary key
    email = models.EmailField(unique=True)     # Unique email field
    firstName = models.CharField(max_length=150)  # First name with max length 150

    def __str__(self):
        return self.email
