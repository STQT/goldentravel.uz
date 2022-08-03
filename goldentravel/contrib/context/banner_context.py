from goldentravel.tours.models import TourBanner


def get_banner_processor(request):
    tour_image_list = TourBanner.objects.all()
    return {"banner": tour_image_list}
