from goldentravel.tours.models import TourBanner


def get_banner_processor(request):
    pk = request.path.split('/')[-1]
    if not pk:
        tour_image_list = TourBanner.objects.all().order_by('-tour__pk')
    else:
        tour_image_list = []
        first = TourBanner.objects.get(tour__pk=int(pk))
        tour_image_list.append(first)
        another = TourBanner.objects.all().exclude(pk=first.id)
        for i in another:
            tour_image_list.append(i)
    return {"banner": tour_image_list}
