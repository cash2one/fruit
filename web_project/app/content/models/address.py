#coding=utf-8
from django.db import models
from wi_cache.base import CachingManager
from django.db.models import Max
from common import Status
from common import BaseModel
import datetime


class ShoppingAddress(BaseModel):   

    name = models.CharField(verbose_name=u'名称',max_length=20)
    address = models.CharField(verbose_name=u'名称',max_length=50)
    phone = models.CharField(verbose_name=u'名称',max_length=15)
    position = models.IntegerField(verbose_name=u'展示位置', default=0, db_index=True)
    onlinetime = models.DateTimeField(verbose_name=u'上线时间', auto_now_add=True)

    class Meta:
        verbose_name = u"提货点"
        verbose_name_plural = verbose_name
        app_label = "content"


    def is_new(self):
    	"""上线1个月内==new"""
        n = datetime.datetime.now()
    	t = n - self.onlinetime 
        if t.days > 30:
            return False
        else:
            return True





