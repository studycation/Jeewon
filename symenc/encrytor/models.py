from django.db import models

# Create your models here.
class Encrytor(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=200)
    
    created_at = models.DateTimeField(auto_noriginal_file = models.FileField(upload_to='uploads/%Y/%m/%d/', blank=True) ow_add=True)    #현재시간기록
    update_at = models.DateField(auto_now=True)         #최근 수정일


class UploadedFile(models.Model):
    original_file = models.FileField(upload_to='uploads/%Y/%m/%d/', blank=True) #uploads/2025/08/21/파일명.txt로 저장
    enc_file = models.FileField(upload_to='uploads/%Y/%m/%d/', blank=True)  #암호화된 파일을 따로 저장할 공간
    original_name = models.CharField(max_length=250)
    size = models.BigIntegerField(default=0)        #BigIntegerField: 파일 저장
    
    created_at = models.DateTimeField(auto_now_add=True)    #현재시간기록
    uploaded_at = models.DateField(auto_now=True)           #최근 수정일
    
    #django admin이나 shell에서 객체 출력 시 사람이 보기 쉽게 원본 파일명으로 표시하도록 함
    #ex.UploadFile.objects.all() 하면 리스트에 example.txt 처럼 보이게 함
    def __str__(self):
        return self.original_name