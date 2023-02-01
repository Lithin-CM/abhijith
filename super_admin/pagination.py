from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def paggination(page,paginator):
    try:
        result = paginator.page(page)
        return result
    except PageNotAnInteger:
        result = paginator.page(1)
        return result
    except EmptyPage:
        result = paginator.page(paginator.num_pages)
        return result

