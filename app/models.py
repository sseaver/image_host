from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save


class Profile(models.Model):
    user = models.OneToOneField('auth.User')


@receiver(post_save, sender="auth.User")
def create_user_profile(**kwargs):
    created = kwargs.get('created')
    instance = kwargs.get('instance')
    if created:
        Profile.objects.create(user=instance)


class Category(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    image = models.FileField()
    categories = models.ManyToManyField(Category)
    created_by = models.ForeignKey('auth.User')
    created_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-created_time",)

    @property
    def image_url(self):
        if self.image:
            return self.image.url
        return "https://www.dunkindonuts.com/content/dunkindonuts/en/menu/beverages/hotbeverages/specialitycoffee/latte/_jcr_content/block/image.img.png/1466490202242.png"


class Comment(models.Model):
    content = models.TextField()
    relation_post = models.ForeignKey(Post)
    created_by = models.ForeignKey('auth.User')
    created_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-created_time",)
