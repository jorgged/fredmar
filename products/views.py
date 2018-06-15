from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, FormView, CreateView
from .models import Product, Product_card, carousel, logo, Contacto
from .form import ContactForm


def save_pregunta_form(request, form):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string('preguntarForm.html', context, request=request)
    return JsonResponse(data)


def Preguntar(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
    else:
        form = ContactForm()
    return save_pregunta_form(request, form)



class PreguntarView(CreateView):
    form_class = ContactForm
    success_url = reverse_lazy('products:home')
    # data = dict()
    #
    # def form_valid(self, form):
    #     form.save()
    #     self.data['form_is_valid'] = True
    #     return JsonResponse(self.data)
    #
    # def form_invalid(self, form):
    #     self.data['form_is_valid'] = False
    #     return JsonResponse(self.data)

    def post(self, request, *args, **kwargs):
        # import ipdb; ipdb.set_trace()
        data = dict()
        get_form = self.get_form()
        form = get_form
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            # return JsonResponse(data)
        else:
            data['form_is_valid'] = False
        return JsonResponse(data)


    def get(self, request, *args, **kwargs):
        # import ipdb; ipdb.set_trace()
        data = dict()
        context = {'form': ContactForm}
        data['html_form'] = render_to_string('preguntarForm.html', context, request=request)
        return JsonResponse(data)





class ContactView(CreateView):
    form_class = ContactForm
    success_url = reverse_lazy('products:home')
    template_name = 'contacto.html'


class AjaxCategoryResponseMixin(object):
    def json_to_response(self):
        data = dict()
        category = self.kwargs.get('category', None)
        pCard = Product_card.objects.filter(categories__name__contains=category)
        data['products_card'] = render_to_string('products.html',{'object_list': pCard})
        return JsonResponse(data)


class HomeView(ListView):
    model = Product_card
    template_name = 'products.html'

    def get(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        context = self.get_context_data()
        imglogo = logo.objects.all()
        imgCarousel = carousel.objects.all()
        context.update({
            'imgCarousel':imgCarousel,
            'imglogo':imglogo,
        })
        return self.render_to_response(context)

class Home(TemplateView):
    template_name = 'base.html'



class SearchCategory(ListView):
    model = Product_card
    template_name = 'products.html'


    def get_queryset(self):
        category = self.kwargs.get('category', None)
        if category is not None:
            list = Product_card.objects.filter(categories__name__contains=category)
        else:
            list = Product_card.objects.all()[:10]
        return list

    def get(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        context = self.get_context_data()
        imglogo = logo.objects.all()
        imgCarousel = carousel.objects.all()
        context.update({
            'imgCarousel':imgCarousel,
            'imglogo':imglogo,
        })
        return self.render_to_response(context)







class ProductListView(ListView):
    model = Product
    template_name = 'store.html'

class ProductSearchView(ListView):
    model = Product
    template_name = 'store.html'

    def get_queryset(self):
        query = self.request.GET.get('q',None)
        if  query is not None:
            list = Product.objects.filter(name__contains=query)[:10]
        else:
            list = Product.objects.all()[:10]
        return list