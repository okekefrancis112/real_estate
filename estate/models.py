from email.mime import image
from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager
from django.core.validators import FileExtensionValidator
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from uuid import uuid4
from django.template.defaultfilters import slugify
from django.urls import reverse
from .utils import generate_ref_code

# Create your models here.
class CustomAccountManager(BaseUserManager):
    def create_user(self, user_name, full_name, email, residential_address, state,
                            account_name, account_number, date_of_birth,
                            phone_number, password, **other_fields):
        other_fields.setdefault('is_active',True)
        
        if not email:
            raise ValueError(_('You must provide an email address'))
        email = self.normalize_email(email)
        user = self.model(user_name=user_name, full_name=full_name, email=email,  
                          residential_address=residential_address, state=state, account_name=account_name,
                          account_number=account_number, date_of_birth=date_of_birth, phone_number=phone_number, **other_fields)
        user.set_password(password)
        
        user.save()
        return user
    
    def create_superuser(self, user_name, full_name, email, residential_address, state,
                                account_name, account_number, date_of_birth,
                                phone_number, password, **other_fields):
        
        other_fields.setdefault('is_superuser',True)
        other_fields.setdefault('is_staff',True)
        other_fields.setdefault('is_active',True)
        
        if other_fields.get('is_superuser') is not True:
                raise ValueError(_('Superuser must be assigned to is_superuser=True.'))

        if other_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must be assigned to is_staff=True.'))
        
        return self.create_user(user_name, full_name, email, residential_address, state,
                                account_name, account_number, date_of_birth,
                                phone_number, password, **other_fields)


class NewUser(AbstractBaseUser, PermissionsMixin):
    
    email = models.EmailField(_('email address'), unique=True)
    user_name = models.CharField(max_length=150, unique=True)
    full_name = models.CharField(max_length=250, blank=True)
    phone_number = models.IntegerField(null=True, blank=True)
    state = models.CharField(max_length=150, blank=True)
    residential_address = models.CharField(max_length=250, blank=True)
    account_name = models.CharField(max_length=250, blank=True)
    account_number = models.IntegerField(null=True, blank=True)
    date_of_birth = models.DateField(blank=True, null=True)
    
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    objects = CustomAccountManager()
    
    USERNAME_FIELD = 'user_name'
    REQUIRED_FIELDS = ['email', 'full_name', 'phone_number',
                       'state', 'date_of_birth', 'residential_address',
                       'account_name', 'account_number']
    
    def __str__(self):
        return self.user_name
    
    
User = get_user_model()

class Estate(models.Model):
    STATUS_CHOICES = (
        ('selling', 'Selling'),
        ('sold', 'Sold'),
    )
    title = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    price = models.PositiveIntegerField()
    property_type = models.CharField(max_length=255)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="Selling")
    area = models.PositiveIntegerField()
    beds = models.CharField(max_length=50)
    baths = models.CharField(max_length=50)
    garages = models.CharField(max_length=50)
    description = models.TextField(max_length=10000)
    video = models.FileField(null=True, blank = True, upload_to = "estate/videos/",validators = [FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])])
    image = models.ImageField(null=True, blank = True, upload_to = "estate/images/")
    uniqueId = models.CharField(null=True, blank=True, max_length=200)
    slug = models.SlugField(max_length=250, unique=True, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if self.created_at is None:
            self.created_at = timezone.localtime(timezone.now())
        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split('-')[4]
            self.slug = slugify('{}{}'.format(self.title, self.uniqueId))
        
        self.slug = slugify('{}{}'.format(self.title, self.uniqueId))
        self.last_updated = timezone.localtime(timezone.now())
        super(Estate, self).save(*args, **kwargs)
        
    def get_absolute_url(self):
        return reverse("estate_detail", kwargs={"slug": self.slug})
    

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(_('email address'))
    user_name = models.CharField(max_length=150)
    full_name = models.CharField(max_length=250, blank=True)
    phone_number = models.IntegerField(null=True, blank=True)
    state = models.CharField(max_length=150, blank=True)
    residential_address = models.CharField(max_length=250, blank=True)
    account_name = models.CharField(max_length=250, blank=True)
    account_number = models.IntegerField(null=True, blank=True)
    date_of_birth = models.DateField(max_length=8, blank=True, null=True)

    code = models.CharField(max_length=12, blank=True, null=True)
    recommended_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="ref_by")
    image = models.ImageField(blank=True, null=True, upload_to = "profile/images/")
    
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.user_name}-{self.code}"
    
    def return_profile(self):
        qs =  Profile.objects.all()
        return qs
    
    def get_recommended_profiles(self):
        qs =  Profile.objects.all()
        # my_rec = [p for p in qs if p.recommended_by is self.user]
        
        my_recs = []    
        for profile in qs:
            # print(profile)
            if profile.recommended_by == self.user:
                print(profile.recommended_by)
                print(self.user)
                my_recs.append(profile)
                print(my_recs)
        return my_recs
    def save(self, *args, **kwargs):
        if self.code is None:
            code = generate_ref_code()
            self.code = code
            # print(self.code)
        super(Profile, self).save(*args, **kwargs)