from django.db import models


class StateJapan(models.Model):
    state_id = models.AutoField(primary_key=True)
    state_name = models.CharField(max_length=200)
    state_desc = models.CharField(max_length=2000, blank=True)
    created_date = models.DateTimeField('date created', blank=True, null=True)
    created_by = models.CharField(max_length=300, blank=True, null=True)
    updated_date = models.DateTimeField('date updated', blank=True, null=True)
    updated_by = models.CharField(max_length=300, blank=True, null=True)

    def __str__(self):
        return self.state_name


class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=200, unique=True)
    building_number = models.CharField(max_length=500)
    postal_code = models.CharField(max_length=12)
    locality = models.CharField(max_length=500)
    city = models.CharField(max_length=200)
    state = models.ForeignKey(StateJapan, on_delete=models.PROTECT)
    created_date = models.DateTimeField('date created', blank=True, null=True)
    created_by = models.CharField(max_length=300, blank=True, null=True)
    updated_date = models.DateTimeField('date updated', blank=True, null=True)
    updated_by = models.CharField(max_length=300, blank=True, null=True)

    def __str__(self):
        return self.company_name
