from django.db import models

class EmailRegister(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.email}"
    
class DetailRegistration(models.Model):
    full_name = models.CharField(max_length=100)
    business_name = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=300,null=True)
    email = models.ForeignKey(EmailRegister,on_delete=models.SET_NULL,null=True)
 

    def __str__(self):
        return f"{self.full_name} {self.business_name} {self.description} {self.location}"
    



    
