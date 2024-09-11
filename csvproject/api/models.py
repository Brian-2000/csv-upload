from django.db import models

class CSVData(models.Model):
    data = models.JSONField()  # Stores JSON data
    uploaded_at = models.DateTimeField(auto_now_add=True)  # Timestamp for when the data is uploaded

    def __str__(self):
        return f"CSVData uploaded at {self.uploaded_at}"
