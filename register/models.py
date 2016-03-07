from __future__ import unicode_literals
from testproject.email_functionality import email_admin, email_client
from django.db import models


class User(models.Model):
    salutation = models.CharField(max_length=6)
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    organisation = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=40)
    postcode = models.CharField(max_length=10)
    country = models.CharField(max_length=60)
    telephone = models.CharField(max_length=15)
    email = models.EmailField(max_length=60, unique=True)
    fee_normal = models.BooleanField(default=False)
    fee_student = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        sorted_self = [["Salutation", self.salutation], ["First name", self.first_name], ["Last Name", self.last_name],
                       ["Email", self.email], ["Telephone", self.telephone], ["Address", self.address],
                       ["City", self.city], ["Country", self.country], ["Postcode", self.postcode],
                       ["Organisation", self.organisation], ["Paying Normal Fee", str(self.fee_normal)],
                       ["Paying Student Fee", str(self.fee_student)],]

        email_client(self, "NUPP 2017 Conference Registration", "You are officially registered for NUPP 2017")
        email_admin(self, "New NUPP 2017 Registrant", "Please find enclosed the details for the new DISS "
                                                      "2017 registrant.", sorted_self)

        super(User, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.email

