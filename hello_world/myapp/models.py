from django.db import models

class Property(models.Model):
    PROPERTY_TYPE_CHOICES = [
        ('house', 'House'),
        ('apartment', 'Apartment'),
        ('condo', 'Condo'),
        ('townhouse', 'Townhouse'),
        ('land', 'Land'),
    ]

    STATUS_CHOICES = [
        ('available', 'Available'),
        ('sold', 'Sold'),
        ('under_offer', 'Under Offer'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    property_type = models.CharField(max_length=50, choices=PROPERTY_TYPE_CHOICES)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    country = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='available')
    listing_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)
    bedrooms = models.IntegerField()
    bathrooms = models.DecimalField(max_digits=3, decimal_places=1)
    square_feet = models.IntegerField()
    lot_size = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    garage_spaces = models.IntegerField(null=True, blank=True)
    is_published = models.BooleanField(default=True)
    agent = models.ForeignKey('Agent', on_delete=models.SET_NULL, null=True, blank=True, related_name='properties')

    def __str__(self):
        return f"{self.title} - {self.city}, {self.state}"

    class Meta:
        ordering = ['-listing_date']
        verbose_name_plural = "Properties"
