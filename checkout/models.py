from django.db import models
from features.models import Feature
from django.utils import timezone

class Order(models.Model):
	full_name = models.CharField(max_length=50, blank=False)
	email = models.CharField(max_length=70, blank=False, default='')
	phone_number = models.CharField(max_length=20, blank=False)
	country = models.CharField(max_length=40, blank=False)
	post_code = models.CharField(max_length=20, blank=False)
	town_or_city = models.CharField(max_length=40, blank=True)
	street_address = models.CharField(max_length=40, blank=False)
	date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return "{0}-{1}-{2}".format(self.id, self.date, self.full_name)

class OrderLineItem(models.Model):
	order = models.ForeignKey(Order, null=False, on_delete=models.CASCADE)
	product = models.ForeignKey(Feature, null=False, on_delete=models.CASCADE)
	quantity = models.IntegerField(blank=False)

	def __str__(self):
		return "{0} {1} @ {2}".format(self.quantity, self.product.title, self.product.price)
