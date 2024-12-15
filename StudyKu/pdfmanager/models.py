from django.db import models

class PDFDocument(models.Model):
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='pdfs/')

    def __str__(self):
        return self.name
