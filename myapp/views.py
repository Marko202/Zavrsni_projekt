from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from myapp.models import Product, Profile, Category, Order, Review, Message

class ProfileList(ListView):
    model = Profile
    
class ProductList(ListView):
    model = Product
    
class CategoryListView(ListView):
    model = Category

class OrderListView(ListView):
    model = Order

class ReviewListView(ListView):
    model = Review
    
class MessageListView(ListView):
    model = Message

def index(request):
    return render(request, 'main/index.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')

    else:
        form = UserCreationForm()

    context = {'form': form}

    return render(request, 'registration/register.html', context)

#dinamicko filtriranje
class SellerProductList(ListView):
    template_name = 'main/seller_products.html'

    def get_queryset(self):
        self.user = get_object_or_404(Profile, user__username=self.kwargs['seller'])
        return Product.objects.filter(seller=self.user)
    
#____________________________________
class ProfileListView(ListView):
    model = Profile
    template_name = 'main/profile_list.html'
    context_object_name = 'profiles'
    
    def get_queryset(self):
        queryset = super().get_queryset()
        is_seller = self.request.GET.get('is_seller')  # Filtriramo prema is_seller parametru iz URL-a
        if is_seller is not None:
            queryset = queryset.filter(is_seller=is_seller)
        return queryset

class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'main/profile_detail.html'
    context_object_name = 'profile'
    
#____________________________________
class ProductListView(ListView):
    model = Product
    template_name = 'main/product_list.html'
    context_object_name = 'products'
    
    def get_queryset(self):
        queryset = super().get_queryset()
        is_available = self.request.GET.get('is_available')
        if is_available is not None:
            queryset = queryset.filter(is_available=is_available)
        return queryset

class ProductDetailView(DetailView):
    model = Product
    template_name = 'main/product_detail.html'
    context_object_name = 'product'
       
#____________________________________   
class CategoryListView(ListView):
    model = Category
    template_name = 'main/category_list.html'
    context_object_name = 'categories'

class CategoryDetailView(DetailView):
    model = Category
    template_name = 'main/category_detail.html'
    context_object_name = 'category'
    
#____________________________________ 
class OrderListView(ListView):
    model = Order
    template_name = 'main/order_list.html'
    context_object_name = 'orders'
    
    def get_queryset(self):
        queryset = super().get_queryset()
        is_completed = self.request.GET.get('is_completed')
        if is_completed is not None:
            queryset = queryset.filter(is_completed=is_completed)
        return queryset

class OrderDetailView(DetailView):
    model = Order
    template_name = 'main/order_detail.html'
    context_object_name = 'order'
    
#____________________________________ 
class ReviewListView(ListView):
    model = Review
    template_name = 'main/review_list.html'
    context_object_name = 'reviews'
    
    def get_queryset(self):
        queryset = super().get_queryset()
        rating = self.request.GET.get('rating')
        if rating is not None:
            queryset = queryset.filter(rating=rating)
        return queryset

class ReviewDetailView(DetailView):
    model = Review
    template_name = 'main/review_detail.html'
    context_object_name = 'review'
    
#____________________________________ 
class MessageListView(ListView):
    model = Message
    template_name = 'main/message_list.html'
    context_object_name = 'messages'
    
    def get_queryset(self):
        queryset = super().get_queryset()
        is_read = self.request.GET.get('is_read')
        if is_read is not None:
            queryset = queryset.filter(is_read=is_read)
        return queryset

class MessageDetailView(DetailView):
    model = Message
    template_name = 'main/message_detail.html'
    context_object_name = 'message'