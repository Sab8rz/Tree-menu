from django.db import models
from django.urls import reverse


class MenuPoint(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название пункта')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children',
                               verbose_name='Родительский пункт')
    menu_name = models.CharField(max_length=50, verbose_name='Название меню')
    url = models.CharField(max_length=200, blank=True, verbose_name='URL явный')
    named_url = models.CharField(max_length=100, blank=True, verbose_name='Имя URL из urls.py')

    class Meta:
        indexes = [models.Index(fields=['menu_name'])]
        verbose_name = 'Пункт меню'
        verbose_name_plural = 'Пункты меню'

    def get_absolute_url(self):
        if self.named_url:
            try:
                return reverse(self.named_url)
            except:
                return '#'
        return self.url if self.url else '#'

    def __str__(self):
        return self.title