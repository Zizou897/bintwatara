from django.db import models
from tinymce.models import HTMLField

# Create your models here.
class Convention(models.Model):
    publish = models.BooleanField(default=True)
    date_add = models.DateField(auto_now=False, auto_now_add=True)
    date_update = models.DateField(auto_now=True, auto_now_add=False)

    class Meta:
        abstract = True

class Web(Convention):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=50)
    location = models.CharField(max_length=250)
    opening = models.CharField(max_length=250)
    
    class Meta:
        verbose_name = "Info du site"
        verbose_name_plural = "Infos du site"
        
    def __str__(self):
        return self.name

class Banner(Convention):
    picture = models.FileField(upload_to='img_banner')
    description = models.TextField()
    title = models.CharField(max_length=50)
    
    class Meta:
        verbose_name = 'bannière'
        verbose_name_plural = 'bannières'

    def __str__(self):
        return self.title

class About(Convention):
    picture = models.FileField(upload_to='img_about')
    picture1 = models.FileField(upload_to='img_about')
    lebele = HTMLField()
    title = models.CharField(max_length=50)
    title1 = models.CharField(max_length=50)
    description =HTMLField()
    experience = models.IntegerField()
    
    class Meta:
        verbose_name = 'A propos de nous'
        verbose_name_plural = 'A propos de nous'
    
    def __str__(self):
        return self.title



class ProcessOfConstruction(Convention):
    picture = models.FileField(upload_to='img_process')
    title = models.CharField(max_length=50)
    description = models.TextField()
    order = models.IntegerField()
    
    class Meta:
        verbose_name = 'procédure de constrution'
        verbose_name_plural = 'procédure de construtions'
        
    def __str__(self):
        return self.title


class Team(Convention):
    picture = models.FileField(upload_to='img_team')
    name = models.CharField(max_length=250)
    work = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    order = models.IntegerField()

    class Meta:
        verbose_name = 'équipe'
        verbose_name_plural = 'équipes'
    def __str__(self):
        return self.name


class Testimony(Convention):
    picture = models.FileField(upload_to='img_testi')
    name = models.CharField(max_length=250)
    work = models.CharField(max_length=50)
    description = models.TextField()

    class Meta:
        verbose_name = 'témoignage'
        verbose_name_plural = 'témoignages'
    def __str__(self):
        return self.name


class Social(Convention):
    name = models.CharField(max_length=250)
    icon = models.CharField(max_length=250)
    link = models.URLField(max_length=200)
    

    class Meta:
        verbose_name = 'réseau social'
        verbose_name_plural = 'réseau sociaux'
    def __str__(self):
        return self.name


class Service(Convention):
    picture = models.FileField(upload_to='img_service')
    title = models.CharField(max_length=250)
    description = models.TextField()
    order = models.IntegerField()

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'
    def __str__(self):
        return self.title


class ConfigWeb(Convention):
    title = models.CharField(max_length=250)
    titleAbout1 = models.CharField(max_length=250)
    titleAbout = models.CharField(max_length=250)
    titleService = models.CharField(max_length=250)
    titleRVD = models.CharField(max_length=250)
    titleTestimony = models.CharField(max_length=250)
    libeleNewsletter = models.TextField()
    descriptionRDV = models.TextField()
    descriptionTeam = models.TextField()
    descriptionTesti = models.TextField()

    class Meta:
        verbose_name = 'Configuration du site'
        verbose_name_plural = 'Configuration du site'
    def __str__(self):
        return self.title
    

#les points fort de l'entreprise ex: qualite=é
class CompanyFeatures(Convention):
    libele =  models.TextField()
    description = models.TextField()
    
    class Meta:
        verbose_name = 'Point fort du site'
        verbose_name_plural = 'Point fort du site'
    def __str__(self):
        return self.libele


class Newsletter(Convention):
    email = models.EmailField(max_length=254)

    class Meta:
        verbose_name = 'abonnement'
        verbose_name_plural = 'abonnement'
    def __str__(self):
        return self.email


class Appointment(Convention):
    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=50)
    service = models.CharField(max_length=250)
    message = models.TextField()
    

    class Meta:
        verbose_name = 'Prise de RDV'
        verbose_name_plural = 'Prises de RDV'
    def __str__(self):
        return self.name


class Contact(Convention):
    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=254)
    sujet = models.CharField(max_length=250)
    message = models.TextField()
    

    class Meta:
        verbose_name = 'Ceux qui nous ont contacté'
        verbose_name_plural = 'Ceux qui nous ont contacté'
    def __str__(self):
        return self.name
