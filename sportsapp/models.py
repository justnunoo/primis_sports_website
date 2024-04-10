from django.db import models

# Create your models here.
class coaches(models.Model):
    name = models.CharField(max_length = 255)
    image = models.ImageField(default= "coaches_images/avatar.jpg", upload_to='coaches_images/')
    age = models.PositiveIntegerField()
    nationality = models.CharField(max_length=100, null=True)
    role = models.CharField(max_length=30)
    about =  models.TextField(null=True, blank = True)

    class Meta:
        verbose_name_plural = 'coaches'
    
    def __str__(self):
        return self.name + " - Coach"
    
class News(models.Model):
    header =  models.CharField(max_length=80)
    date = models.DateField(auto_now_add=True)
    content = models.TextField()
    image = models.ImageField(upload_to="news_images")
    # author = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'news'

    def __str__(self):
        return f"{self.date} : {self.header}"
    

class Sports(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Sports"

    def __str__(self):
        return self.name

class trainees(models.Model):
    firstName = models.CharField(max_length=40)
    lastName = models.CharField(max_length=40)
    email = models.EmailField(unique=True)
    phoneNumber = models.CharField(max_length=16)
    residence = models.CharField(max_length=100)
    birthday = models.DateField()
    sports = models.ManyToManyField(Sports)
    # prefered_location = models.CharField(max_length = 255)

    class Meta:
        verbose_name_plural = 'trainees info'

    def __str__(self):
        return f"{self.firstName} {self.lastName}"

    