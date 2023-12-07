from django.db import models
# Create your models here.

class Tracked(models.Model):
    Cam_MxID = models.CharField(max_length=50)
    incoming = models.IntegerField()
    outgoing = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.Cam_MxID
    

class StreamPhoto(models.Model):
    Cam_MxID = models.CharField(max_length=50)
    image = models.ImageField(upload_to='media/')

    def __str__(self) -> str:
        return self.Cam_MxID
    

class ConfigParameter(models.Model):

    COMES_FROM = (('Top','Top'), ('Bottom','Bottom'), ('Right','Right'), ('Left','Left'))

    Cam_MxID = models.CharField(max_length=50)
    Door_orientation = models.CharField(max_length=10, choices=COMES_FROM, null=True, blank=True)
    
    A_line_start_x = models.IntegerField(null=True, blank=True)
    A_line_start_y = models.IntegerField(null=True, blank=True)
    
    A_line_end_x = models.IntegerField(null=True, blank=True)
    A_line_end_y = models.IntegerField(null=True, blank=True)

    B_line_start_x = models.IntegerField(null=True, blank=True)
    B_line_start_y = models.IntegerField(null=True, blank=True)
    
    B_line_end_x = models.IntegerField(null=True, blank=True)
    B_line_end_y = models.IntegerField(null=True, blank=True)

    C_line_start_x = models.IntegerField(null=True, blank=True)
    C_line_start_y = models.IntegerField(null=True, blank=True)
    
    C_line_end_x = models.IntegerField(null=True, blank=True)
    C_line_end_y = models.IntegerField(null=True, blank=True)

    def __str__(self) -> str:
        return self.Cam_MxID