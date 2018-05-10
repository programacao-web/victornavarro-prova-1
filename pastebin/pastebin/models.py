from django.db import models


class Paste(models.Model):
    LANG = {
        1: "Python",
        2: "JavaScript",
        3: "Outros"
    }

    title = models.CharField(max_length=50)
    language = models.IntegerField()
    content = models.TextField()
