from django.db import models


class Articles(models.Model):
    objects = None
    title = models.CharField('Վերնագիր', max_length=50)
    anons = models.CharField('Հայտարարություն', max_length=250)
    full_text = models.TextField('Հոդված')
    date = models.DateTimeField('Հրապարակման ամսաթիվը')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/news/{self.id}'

    class Meta:
        verbose_name = 'Հոդված'
        verbose_name_plural = 'Լուրեր'