from django.db import models

class Brand(models.Model):
    name = models.CharField("Brend", max_length=30)

    created_at = models.DateField("Qoshilgan vaxti", auto_now_add=True)
    updated_at = models.DateField("Yangilangan vaxti", auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Brend "
        verbose_name_plural = "Brendlar "


class Category(models.Model):
    name = models.CharField("Categoriya", max_length=30)

    created_at = models.DateField("Qoshilgan vaxti", auto_now_add=True)
    updated_at = models.DateField("Yangilangan vaxti", auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Bolim "
        verbose_name_plural = "Bolimlar "

class Snakers(models.Model):
    model_name = models.CharField("Modeli", max_length=50)
    color = models.CharField("Rangi", max_length=50)
    price = models.FloatField("Narxi")
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, verbose_name="Brendi")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Categoriya")


