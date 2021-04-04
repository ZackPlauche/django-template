import dbsettings
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.text import slugify
from tinymce.models import HTMLField
from django.utils import timezone

# Settings
class SiteSettings(dbsettings.Group):
    company_name = dbsettings.StringValue(default='Your Company Name')
    company_email = dbsettings.EmailValue(default='support@yourcompanyname.com')
    company_phone = dbsettings.StringValue(default='+1 (234) 567-8910')
    facebook_url = dbsettings.StringValue(default='', help_text='Enter the URL to your company\'s Facebook page.')
    instagram_url = dbsettings.StringValue(default='', help_text='Enter the URL to your company\'s Instagram page.')
    twitter_url = dbsettings.StringValue(default='', help_text='Enter the URL to your company\'s twitter page.')
    linkedin_url = dbsettings.StringValue(default='', help_text='Enter the URL to your company\'s LinkedIn page.')
    github_url = dbsettings.StringValue(default='', help_text='Enter the URL to your company\'s GitHub page.')
    twitch_url = dbsettings.StringValue(default='', help_text='Enter the URL to your company\'s Twitch page.')
    youtube_url = dbsettings.StringValue(default='', help_text='Enter the URL to your company\'s Youtube page.')
    stackoverflow_url = dbsettings.StringValue(default='', help_text='Enter the URL to your company\'s Stack Overflow page.')

    maintenance_mode = dbsettings.BooleanValue(default=False, help_text='Turn on or off maintenance mode. If on, everyone who is not an admin will be sent to a maintenance page.')

options = SiteSettings()


# Models 
class UserManager(BaseUserManager):

    def create_user(self, email, first_name, last_name, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name
        )

        user.set_password(password)
        user.save(using=self._db)  
        return user

    def create_superuser(self, email, first_name, last_name, password=None):
        user = self.create_user(
            email,
            first_name=first_name,
            last_name=last_name,
            password=password,
        )

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class User(AbstractUser):
    username = None
    email = models.EmailField('email address', unique=True)
    profile_pic = models.ImageField(upload_to="media", null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = UserManager()

    def __str__(self):
        return self.email


class Section(models.Model):

    class Page(models.TextChoices):
        HOME = 'home'
        ABOUT = 'about'
        CONTACT = 'contact'
        FAQ = 'faq'

    class SectionType(models.TextChoices):
        HERO = 'Hero'
        SIDE_IMAGE = 'side-image'

    page = models.CharField(max_length=20, choices=Page.choices, default='', help_text="Which page would you like this section to appear?")
    section_type = models.CharField("Type", max_length=20, choices=SectionType.choices, default='')
    image = models.ImageField(upload_to="section_images", null=True, blank=True)
    title = models.CharField(max_length=50, null=True)
    subtitle = HTMLField(null=True, blank=True)
    button_1_link = models.URLField(null=True, blank=True)
    button_1_text = models.CharField(max_length=10, null=True, blank=True)
    button_2_link = models.URLField(null=True, blank=True)
    button_2_text = models.CharField(max_length=10, null=True, blank=True)
    order = models.PositiveSmallIntegerField(default=0, blank=False, null=False, )
    display = models.BooleanField(default=True)

    class Meta:
        ordering = ['order', 'display', 'page']

    def __str__(self):
        return self.title
