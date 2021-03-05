from django.shortcuts import render
from django.db.models import Q
from mainapp.models import Upload

# Create your views here.


def search(request):
    if request.method == 'GET':
        query= request.GET.get('q')

        submitbutton= request.GET.get('submit')

        if query is not None:
            lookups= Q(title__icontains=query) | Q(text__icontains=query)

            results= Upload.objects.filter(lookups).distinct()

            context={
                'results': results,
                'submitbutton': submitbutton,
               }

            return render(request, 'search.html', context)

        else:
            return render(request, 'search.html')

    else:
        return render(request, 'search.html')

