from django.db import models


class TestModel(models.Model):
    name = models.CharField('r_num', max_length=100)
