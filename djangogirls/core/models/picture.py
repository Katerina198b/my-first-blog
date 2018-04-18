# -*- coding: utf-8 -*-
from django.db import models


class Picture(models.Model):

    class Meta:
        ordering = ["created_at"]
        verbose_name = "Картинка"
        verbose_name_plural = verbose_name

    category = models.CharField(
        max_length=255,
        verbose_name="Категория",
        default="Без категории"
    )

    file = models.FileField(
        upload_to='uploads/%Y/%m/%d/',
        null=True,
        blank=True,
    )

    created_at = models.DateTimeField(auto_now_add=True)

