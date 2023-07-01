from django.views.generic import ListView, UpdateView, CreateView, DetailView, DeleteView
from .models import Product, Category
from django.shortcuts import render
from django.views import View
from django.core.paginator import Paginator
from .filters import ProductFilter
from .forms import ProductForm # импортируем нашу форму

class ProductsList(ListView):
    model = Product
    template_name = 'products.html'
    context_object_name = 'products'
    ordering = ['-price']
    paginate_by = 1

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = ProductFilter(self.request.GET, queryset=self.get_queryset())
        return context

    # def get(self, request):
    #     products = Product.objects.order_by('-price')
    #     p = Paginator(products, 1)
    #
    #     products = p.get_page(request.GET.get('page', 1))
    #
    #     data = {'products': products}
    #     return render(request, 'products.html', data)

    # def post(self, request, *args, **kwargs):
    #     # # берём значения для нового товара из POST-запроса отправленного на сервер
    #     # name = request.POST['name']
    #     # quantity = request.POST['quantity']
    #     # category_id = request.POST['category']
    #     # price = request.POST['price']
    #     #
    #     # product = Product(name=name, quantity=quantity, category_id=category_id,
    #     #                   price=price)  # создаём новый товар и сохраняем
    #     # product.save()
    #
    #     form = self.form_class(request.POST)  # создаём новую форму, забиваем в неё данные из POST-запроса
    #
    #     if form.is_valid():  # если пользователь ввёл всё правильно и нигде не накосячил, то сохраняем новый товар
    #         form.save()
    #
    #     return super().get(request, *args, **kwargs)  # отправляем пользователя обратно на GET-запрос.


class ProductDetailView(DetailView):
    # model = Product
    template_name = 'simpleapp/product_detail.html'
    # context_object_name = 'product'
    queryset = Product.objects.all()

class ProductCreateView(CreateView):
    template_name = 'simpleapp/product_create.html'
    form_class = ProductForm


class ProductUpdateView(UpdateView):
    template_name = 'simpleapp/product_create.html'
    form_class = ProductForm

    # метод get_object мы используем вместо queryset, чтобы получить информацию об объекте который мы собираемся редактировать
    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Product.objects.get(pk=id)


# дженерик для удаления товара
class ProductDeleteView(DeleteView):
    template_name = 'simpleapp/product_delete.html'
    queryset = Product.objects.all()
    success_url = '/products/'
