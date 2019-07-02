from django.db import models

# in the future this will be associated with user
# many to one relationship: one user, many cards

class Card(models.Model):
    name = models.CharField(max_length=60)
    
    def __str__(self):
        return self.name