from django.db import models

# Create your models here.
class childModel(models.Model):
    # MOOD_CHOICES = [
    #     ('Happy', 'Happy'),
    #     ('Sad', 'Sad'),
    #     ('Neutral', 'Neutral'),
    # ]
    # Mood = models.CharField(max_length=20, choices=MOOD_CHOICES)
    # Blood_Urea=models.FloatField()
    # Serum_Creatine=models.FloatField()
    # Packed_cell_volume=models.FloatField()
    # White_blood_count=models.FloatField()
    # Age = models.FloatField()
    Age = models.IntegerField(null=True, blank=True)
    Screen_Time = models.FloatField()
    Study_Hours = models.FloatField()
    Meals_Per_Day = models.FloatField()
    Sleep_Hours = models.FloatField()
