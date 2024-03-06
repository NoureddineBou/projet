from django.contrib import admin
from .models import User, OfferCategory, Offer, OfferImage, Booking, Payment, HomePage, SearchForm, Offerm, Review
# Register your models here.
admin.site.register(Booking)
admin.site.register(User)
admin.site.register(Offer)
admin.site.register(OfferCategory)
admin.site.register(OfferImage)
admin.site.register(Payment)
admin.site.register(HomePage)
admin.site.register(SearchForm)
admin.site.register(Offerm)
admin.site.register(Review)
