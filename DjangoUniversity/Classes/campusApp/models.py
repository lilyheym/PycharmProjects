from django.db import models


class UniversityCampus(models.Model):
    Campus_Name = models.CharField(max_length=60, default="", blank=True, null=False)
    State = models.CharField(max_length=2, default="", blank=True, null=False)
    Campus_ID = models.IntegerField(default="", blank=True, null=False)

    object = models.Manager()

    # Removes added 's' that Django adds to the model name in the browser display

    class Meta:
        verbose_name_plural = "University Campus"
