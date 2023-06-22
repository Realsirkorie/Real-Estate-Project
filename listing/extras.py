from .models import Listing 

def delete_realtors_listing_data(realtor_email):
    print('Entered Delete Realtors Function...')
    if Listing.objects.filter(realtor=realtor_email).exists():
        print('Entered If-Check...')
        Listing.objects.filter(realtor=realtor_email).delete()
        print('Deleted Listings for This Realtor...')