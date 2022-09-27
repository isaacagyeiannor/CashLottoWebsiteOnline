from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
 
 

def less_than(value):
    if value > 90:
        raise ValidationError(
            _('%(value)s is greater than 90 '),
            params={'value': value},
        )

class BlogTestmonaials(models.Model):
    title = models.CharField(max_length=50,default="") 
    content =RichTextUploadingField(blank=True,null=True,default="")
    image = models.ImageField(upload_to='media\pages', max_length=30, null=True,default="media/pages/avatar.png")
    slug = models.SlugField(unique=True ,blank=True,default="")
    author = models.CharField(max_length=50,default="")  
    class Meta:
        abstract=True

   
class Blog(BlogTestmonaials):
    created = models.DateTimeField(auto_now_add=True,blank=True)
    
    def __str__(self):
        return self.title
    
    
class BlogComment(models.Model):
    post=models.ForeignKey(Blog,on_delete=models.CASCADE,related_name='comments',null=True)
    name=models.CharField(max_length=80,null=True)
    body=models.TextField()
    email=models.EmailField( blank=True, null=True)
    created_on=models.DateTimeField(auto_now_add=True)
    active=models.BooleanField(default=False)
    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)

class Testimonial(BlogTestmonaials):
    created = models.DateTimeField(auto_now_add=True,blank=True)
    
    def __str__(self):
        return self.title
    
    
class AddDraw(models.Model):
    TYPE = (
        ('Monday Special','Monday Special'),
        ('Lucky Tuesday','Lucky Tuesday'),
        ('Mid Week','Mid Week'),
        ('Fortune Thursday','Fortune Thursday'),
        ('Friday Bonaza','Friday Bonaza'),
        ('National Weekly Lotto','National Weekly Lotto'),
        ('Sunday Aseda','Sunday Aseda'),
    )
    
    draw_type=models.CharField(max_length=100, null=True,blank=True,choices=TYPE)
    date_select= models.CharField(max_length=50,default="") 
    
class AddWinDraw(models.Model):
    TYPE = (
        ('Monday Special','Monday Special'),
        ('Lucky Tuesday','Lucky Tuesday'),
        ('Mid Week','Mid Week'),
        ('Fortune Thursday','Fortune Thursday'),
        ('Friday Bonaza','Friday Bonaza'),
        ('National Weekly Lotto','National Weekly Lotto'),
        ('Sunday Aseda','Sunday Aseda'),
    )
    
    draw_type=models.CharField(max_length=100, null=True,blank=True,choices=TYPE)
    date_select= models.CharField(max_length=50,default="") 
    first_number=models.PositiveIntegerField(blank=True,null=True,default="",validators=[less_than])
    second_number=models.PositiveIntegerField(blank=True,null=True,default="",validators=[less_than])
    third_number=models.PositiveIntegerField(blank=True,null=True,default="",validators=[less_than])
    fourth_number=models.PositiveIntegerField(blank=True,null=True,default="",validators=[less_than])
    fifth_number=models.PositiveIntegerField(blank=True,null=True,default="",validators=[less_than])
    
class AllDraw(models.Model): 
    add_draw = models.ForeignKey(AddDraw, on_delete=models.CASCADE,blank=True,null=True)
    win_draw = models.ForeignKey(AddWinDraw, on_delete=models.CASCADE,blank=True,null=True)
    total_draw = models.CharField(max_length=50,blank=True,default="") 
    mobile_only = models.CharField(max_length=50,blank=True,default="") 
    total_price = models.CharField(max_length=50,blank=True,default="") 
    total_won = models.CharField(max_length=50,blank=True,default="") 
    title = models.CharField(max_length=50,blank=True,default="") 
    

    
    

    
    