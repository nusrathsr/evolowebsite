from django.db import models


INTERESTED_IN = (
    ("1", "Option1"),
    ("2", "Option2"),
)


class Customer(models.Model):
    image = models.ImageField(upload_to="customers/")

    class Meta:
        db_table = "web_customers"
        ordering = ["-id"]


class Service(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField()
    image = models.FileField(upload_to="services/")

    class Meta:
        db_table = "web_services"
        ordering = ["-id"]

    def __str__(self):
        return self.title


class Team(models.Model):
    avatar = models.FileField(upload_to="teams/")
    name = models.CharField(max_length=128)
    designation = models.CharField(max_length=128)
    facebook_url = models.CharField(max_length=128)
    twitter_url = models.CharField(max_length=128)

    class Meta:
        db_table = "web_teams"
        ordering = ["-id"]

    def __str__(self):
        return self.name


class Contact(models.Model):
    full_name = models.CharField(max_length=128)
    email = models.EmailField()
    phone = models.CharField(max_length=128)
    interested_in = models.CharField(max_length=128, choices=INTERESTED_IN)
    user_agreement = models.BooleanField(default=False)

    class Meta:
        db_table = "web_contacts"
        ordering = ["-id"]

    def __str__(self):
        return self.full_name


class Plan(models.Model):
    title = models.CharField(max_length=128)
    short_description = models.CharField(max_length=128)
    price = models.IntegerField()
    feature_email = models.BooleanField(default=False)
    feature_admin = models.BooleanField(default=False)
    feature_list = models.BooleanField(default=False)
    feature_data = models.BooleanField(default=False)
    feature_planning = models.BooleanField(default=False)

    class Meta:
        db_table = "web_plans"
        ordering = ["-id"]

    def __str__(self):
        return self.title
