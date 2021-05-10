from django.conf import settings
from  property.models import BuildingType, SaleType


def site_details(request):
    context_data = dict()
    context_data['custom_site_name'] = "HABSHA INTERNATIONAL"
    context_data['custom_site_author'] = "Mustapha Habib Adam"
    context_data['custom_site_keywords'] = "real estate, project"
    context_data['custom_site_telephone'] = '+234 8032496816'
    context_data['custom_site_email'] = 'Habshainternational@gmail.com'
    context_data['custom_site_address'] = 'Tukuntawa along radio station, Kano, Nigeria'

    # context_data['MEDIA_URL'] = settings.MEDIA_URL
    context_data['property_sale_type_list'] = SaleType.objects.all()
    context_data['property_building_type_list'] = BuildingType.objects.all()

    context_data['MEDIA_URL'] = settings.MEDIA_URL

    return context_data
