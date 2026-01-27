from django.db import models

class PermitType(models.Model):
    # This matches "permitType" in response
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class GeneralConditionSection(models.Model):
    # This matches "generalConditionsSection" in response
    permit_type_id = models.IntegerField() # Or ForeignKey to PermitType
    title = models.CharField(max_length=255)
    updated_time = models.DateTimeField()

    def __str__(self):
        return self.title

class CertificateValiditySection(models.Model):
    # Matches "certificateValiditySection"
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title
