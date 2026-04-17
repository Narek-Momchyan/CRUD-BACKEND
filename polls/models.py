from django.db import models

# Create your models here.
from django.db import models

class Student(models.Model):
    # fullName-ը տեքստ է, առավելագույնը 255 նիշ
    fullName = models.CharField(max_length=255)
    # facultet-ը նույնպես տեքստ է
    facultet = models.CharField(max_length=100)
    # age-ը թիվ է (Integer)
    age = models.IntegerField()
    # phone-ը տեքստ է
    phone = models.CharField(max_length=20)
    # email-ի համար Django-ն ունի հատուկ տիպ, որը ստուգում է @ նշանը
    email = models.EmailField(unique=True)
    # about-ը երկար տեքստ է, դրա համար TextField
    about = models.TextField()

    def __str__(self):
        return self.fullName