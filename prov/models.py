from django.db import models
from django.urls import reverse

# Create your models here.

class Equipment(models.Model):
    name = models.CharField(max_length=200, help_text="Enter name of the equipment")
    playbook = models.ForeignKey('Playbook', on_delete=models.SET_NULL, null=True)
    inventory = models.ForeignKey('Inventory', on_delete=models.SET_NULL, null=True)
    os = models.ForeignKey('Os', on_delete=models.SET_NULL, null=True)
    equip_model = models.ForeignKey('Emodel', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.
        """
        return reverse('model-detail-view', args=[str(self.id)])

class Emodel(models.Model):
    name = models.CharField(max_length=200, help_text="Enter name of the model")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.
        """
        return reverse('model-detail-view', args=[str(self.id)])

class Os(models.Model):
    name = models.CharField(max_length=200, help_text="Enter name of the Operating System")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.
        """
        return reverse('model-detail-view', args=[str(self.id)])

class Inventory(models.Model):
    name = models.CharField(max_length=200, help_text="Enter name of the Inventory")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.
        """
        return reverse('model-detail-view', args=[str(self.id)])

class Playbook(models.Model):
    name = models.CharField(max_length=200, help_text="Enter name of the Playbook")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.
        """
        return reverse('model-detail-view', args=[str(self.id)])
