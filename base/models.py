from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    first_name=models.CharField(max_length=20,null=True,blank=True)
    last_name=models.CharField(max_length=20,null=True,blank=True)
    img=models.ImageField(upload_to='myimages',null=True,blank=True)
    email=models.EmailField()
    Address=models.TextField(null=True,blank=True)
    is_patient = models.BooleanField(default=False)
    is_doctor = models.BooleanField(default=False)


    def __str__(self):
        return self.username

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    def __str__(self):
        return self.user.first_name

 

class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    def __str__(self):
        return self.user.first_name



category_choice=[
    ('Mental health','Mental health'),
    ('heart disease','heart disease'),
    ('covid 19','covid 19'),
    ('immunitization','immunitization'),
]

mark_blog=[
    ('is_draft','is_draft'),
    ('not_draft','not_draft')
]
class BlogPost(models.Model):
    created_doctor=models.ForeignKey(Doctor,on_delete=models.CASCADE)
    title=models.CharField(max_length=30,null=True,blank=True)
    post_img=models.ImageField(upload_to='myimages',null=True,blank=True)
    category=models.CharField(max_length=20,choices=category_choice)
    summary=models.TextField(null=True,blank=True)
    content=models.TextField(null=True,blank=True)
    is_draft=models.CharField(max_length=20,choices=mark_blog)
    created_date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
   









# class Doctor(models.Model):
#     first_name=models.CharField(max_length=20,null=True,blank=True)
#     last_name=models.CharField(max_length=20,null=True,blank=True)
#     username=models.CharField(max_length=20,null=True,blank=True)
#     img=models.ImageField(upload_to='myimages',null=True,blank=True)
#     email=models.EmailField()
#     password=models.CharField(max_length=20)
#     Address=models.TextField(null=True,blank=True)
#     is_doctor=models.BooleanField(default=False)

#     def __str__(self):
#         return self.username
    

# class Patient(models.Model):
#     first_name=models.CharField(max_length=20,null=True,blank=True)
#     last_name=models.CharField(max_length=20,null=True,blank=True)
#     username=models.CharField(max_length=20,null=True,blank=True)
#     img=models.ImageField(upload_to='myimages',null=True,blank=True)
#     email=models.EmailField()
#     password=models.CharField(max_length=20)
#     is_Patient=models.BooleanField(default=False)
#     Address=models.TextField(null=True,blank=True)

#     def __str__(self):
#         return self.username





