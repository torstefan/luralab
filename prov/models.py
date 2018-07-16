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
        return reverse('equipment-detail', kwargs={'slug': self.name, 'pk':str(self.id)})


    class Meta:
        ordering = ['name']

class Vrf(models.Model):
    name = models.CharField(max_length=200, help_text="Enter name of the vrf")

    equipment = models.ForeignKey('Equipment', on_delete=models.CASCADE, null=True, help_text="Equip VRF is connected to")

    loopback = models.CharField(max_length=200, help_text="Enter loopback addr, eg 1.1.1.1/32")
    linknet = models.CharField(max_length=200, help_text="Enter linknet addr, eg 1.1.1.1/31")


    def __str__(self):
        return self.name + " - " + self.loopback

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.
        """
        return reverse('vrf-detail', args=[str(self.id)])

    class Meta:
        ordering = ['name']

class Vlan(models.Model):
    name = models.CharField(max_length=200, help_text="Enter name of the vrf")
    vlan_id = models.IntegerField(help_text="Enter the VLAN ID")
    network_addr = models.CharField(max_length=200, help_text="Enter net_addr in / notation. Eg. 1.1.1.0/24 ")

    vrf = models.ForeignKey('Vrf', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.
        """
        return reverse('vlan-detail', args=[str(self.id)])

    class Meta:
        ordering = ['name']


class Emodel(models.Model):
    name = models.CharField(max_length=200, help_text="Enter name of the model")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.
        """
        return reverse('emodel-detail', args=[str(self.id)])


class Os(models.Model):
    name = models.CharField(max_length=200, help_text="Enter name of the Operating System")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.
        """
        return reverse('os-detail', args=[str(self.id)])


class Inventory(models.Model):
    name = models.CharField(max_length=200, help_text="Enter name of the Inventory")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.
        """
        return reverse('inventory-detail', args=[str(self.id)])



class Playbook(models.Model):
    name = models.CharField(max_length=200, help_text="Enter name of the Playbook")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.
        """
        return reverse('playbook-detail', args=[str(self.id)])
