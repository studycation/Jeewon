from django.db import models

# Create your models here.
class enctyyor(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=200)
    
    created_at = models.DateTimeField(auto_now_add=True)    #현재시간기록
    update_at = models.DateField(auto_now=True)         #최근 수정일
    
    