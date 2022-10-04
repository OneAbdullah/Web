from django.db import models

class images_to_binarize(models.Model):
    input_image = models.ImageField(blank=True,null=True)
    output_image = models.ImageField(blank=True,null=True)


class suggestion(models.Model):
    name = models.CharField(max_length=250,blank=True,null=True)
    email = models.CharField(max_length=250,blank=True,null=True)
    note = models.TextField(max_length=2500,blank=True,null=True)

    def __str__(self):
        return self.name