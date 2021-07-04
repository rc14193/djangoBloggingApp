from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    img = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def save(self):
        super().save()

        image = Image.open(self.img.path)
        if image.height > 300 or image.width > 300:
            output_size = (300,300)
            image.thumbnail(output_size)
            image.save(self.img.path)

    def __str__(self):
        return f'{self.user.username} Profile'

