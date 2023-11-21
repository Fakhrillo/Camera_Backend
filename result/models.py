from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.


class Tracked(models.Model):
    mxid = models.CharField(max_length=50)
    incoming = models.IntegerField()
    outgoing = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.mxid
    

class StreamPhoto(models.Model):
    mxid = models.CharField(max_length=50)
    image = models.ImageField(upload_to='media/')

    def __str__(self) -> str:
        return self.mxid
    

class ConfigParameter(models.Model):

    COMES_FROM = (('above','above'), ('left','left'), ('right','right'))

    mxid = models.CharField(max_length=100)
    line_coor = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(1.0)])
    comes_from = models.CharField(max_length=10, choices=COMES_FROM, null=True, blank=True)
    square_x_top_left = models.IntegerField(null=True, blank=True)
    square_y_top_left = models.IntegerField(null=True, blank=True)
    square_x_bottom_right = models.IntegerField(null=True, blank=True)
    square_y_bottom_right = models.IntegerField(null=True, blank=True)
    line1_A_point_x = models.IntegerField(null=True, blank=True)
    line1_A_point_y = models.IntegerField(null=True, blank=True)
    line1_B_point_x = models.IntegerField(null=True, blank=True)
    line1_B_point_y = models.IntegerField(null=True, blank=True)
    line2_A_point_x = models.IntegerField(null=True, blank=True)
    line2_A_point_y = models.IntegerField(null=True, blank=True)
    line2_B_point_x = models.IntegerField(null=True, blank=True)
    line2_B_point_y = models.IntegerField(null=True, blank=True)

    def __str__(self) -> str:
        return self.mxid