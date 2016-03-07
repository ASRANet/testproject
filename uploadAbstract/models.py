from __future__ import unicode_literals
from testproject.email_functionality import email_admin, email_client
from django.db import models


class SubmittedAbstract(models.Model):
    salutation = models.CharField(max_length=6)
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    email = models.EmailField(max_length=60, unique=True)
    paper_title = models.CharField(max_length=60)
    abstract = models.CharField(max_length=2000)

    def save(self, *args, **kwargs):

        sorted_self = [["Salutation", self.salutation], ["First name", self.first_name], ["Last Name", self.last_name],
                       ["Email", self.email], ["Paper Title", self.paper_title], ["Abstract", self.abstract],
                       ]

        email_client(self, "NUPP 2017 Abstract Upload", "You have uploaded an abstract.")
        email_admin(self, "New NUPP 2017 Abstract", "Please find enclosed the details for the new NUPP "
                                                    "2017 abstract upload.", sorted_self)
        super(SubmittedAbstract, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.email

