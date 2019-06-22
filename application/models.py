from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from PIL import Image
from django.core.validators import MinLengthValidator
# from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Name = models.CharField(max_length=55, default="")
    BRANCH_CHOICES = (
    ("Information Technology", "Information Technology"),
    ("Computer Science", "Computer Science"),
    ("Electrical and Communication", "Electrical and Communication"))

    Branch = models.CharField(max_length=50,choices=BRANCH_CHOICES,default='Information Technology')
    Linkedin_URL = models.URLField(default="")

    Hobbies = models.CharField(max_length=150, default="")
    Skills = models.CharField(max_length=150, default="")
    Contact_NO = models.CharField(max_length=10, validators=[MinLengthValidator(10)], blank=True)
    image = models.ImageField(default='default.png', upload_to='profile_pics')



    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


def create_profile(sender, **kwargs):
    if kwargs['created']:
        profile = Profile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)
