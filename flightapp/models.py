from django.db import models

# Create your models here.
class AirportRoute(models.Model):
    airport_code = models.CharField(max_length=10)

    parent = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        related_name='children',
        on_delete=models.CASCADE
    )

    POSITION_CHOICES = (
        ('L', 'Left'),
        ('R', 'Right'),
    )
    position = models.CharField(
        max_length=1,
        choices=POSITION_CHOICES,
        null=True,
        blank=True
    )

    duration = models.PositiveIntegerField()

    def __str__(self):
        return self.airport_code