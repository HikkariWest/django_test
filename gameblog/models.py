from django.db import models

from django.template.defaultfilters import slugify as django_slugify

alphabet = {'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'yo', 'ж': 'zh', 'з': 'z', 'и': 'i',
            'й': 'j', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't',
            'у': 'u', 'ф': 'f', 'х': 'kh', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch', 'ы': 'i', 'э': 'e', 'ю': 'yu',
            'я': 'ya'}


def slugify(s):
    """
    Overriding django slugify that allows to use russian words as well.
    """
    return django_slugify(''.join(alphabet.get(w, w) for w in s.lower()))


# Create your models here.
class Post(models.Model):
    CATEGORIES = [
        (0, 'Все'),
        (1, 'Игровые новости'),
        (2, 'Технологии'),
        (3, 'Софт'),
        (4, 'Новости киноиндустрии'),
    ]
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    category = models.SmallIntegerField(choices=CATEGORIES, default=0)
    publish = models.BooleanField(default=False)
    slug = models.SlugField(null=False, unique=True, blank=True)

    class Meta:
        ordering = ('id', 'publish')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
