from django.views.generic import ListView
from . import models



class ItemListView(ListView):

    model = 'Item'
    template_name = 'index.html'
    context_object_name = 'goods'


    def get_qs(request):
        qs = models.Item.objects.all()
        context = {
            "qs":qs,
            }

        return render(request, "index.html", context)
