from django.db import models
from django.contrib.auth.models import User
from slugify import slugify
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey


# Create your models here.
class Product(models.Model):
    seller = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True, null=True)
    price = models.IntegerField(null=True, blank=True)
    image = models.ImageField(upload_to="posts/", blank=True, null=True)
    category = models.ForeignKey('category', related_name="categories", on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Category(MPTTModel):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    parent = TreeForeignKey(
        'self',
        blank=True,
        null=True,
        related_name='child',
        on_delete=models.CASCADE
    )

    class Meta:
        unique_together = ('slug', 'parent',)
        verbose_name_plural = "categories"

    def __str__(self):
        full_path = [self.name]
        k = self.parent
        while k is not None:
            full_path.append(k.name)
            k = k.parent

        return ' -> '.join(full_path[::-1])

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('computer_list_by_category', args=[self.slug])
