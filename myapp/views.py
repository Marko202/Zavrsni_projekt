from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from myapp.models import Product, Profile, Category, Order, Review, Message
from myapp.forms import ProductForm, ProfileForm, RegistracijaForma, UserProfileForm, CategoryForm, OrderForm, ReviewForm, MessageForm
from django.contrib.auth.models import User
#from django.contrib import message
from django.contrib.auth import get_user_model

# Home and Registration
def index(request):
    return render(request, 'main/index.html')

def register(request):
    if request.method == 'POST':
        form = RegistracijaForma(request.POST)
        if form.is_valid():
            user = form.save()  # Saves the user, including the password fields
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']  # The password1 entered
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')  # Redirect to your home page
    else:
        form = RegistracijaForma()
    return render(request, 'registration/register.html', {'form': form})

# Seller Products
class SellerProductList(ListView):
    template_name = 'main/seller_products.html'
    context_object_name = 'products'

    def get_queryset(self):
        self.user = get_object_or_404(Profile, user__username=self.kwargs['seller'])
        return Product.objects.filter(seller=self.user)

# Profiles CRUD
class ProfileListView(ListView):
    model = Profile
    template_name = 'main/profile_list.html'
    context_object_name = 'profiles'

class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'main/profile_detail.html'
    context_object_name = 'profile'

class ProfileCreateView(CreateView):
    model = Profile
    form_class = UserProfileForm
    template_name = 'main/profile_form.html'
    success_url = reverse_lazy('profile_list')
    
    def form_valid(self, form):
        # Save the user and profile in one go
        user = form.save()
        #messages.success(self.request, f'User {user.username} has been successfully created!')
        return redirect(self.success_url)

class ProfileUpdateView(UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'main/profile_edit_form.html'
    success_url = reverse_lazy('profile_list')  # This will redirect to /profiles/ after saving

    def get_object(self, queryset=None):
        # Fetch the Profile based on the pk
        return get_object_or_404(Profile, pk=self.kwargs['pk'])

    def form_valid(self, form):
        # Save the changes to the Profile and associated User if necessary
        profile = form.save(commit=False)
        profile.save()  # Save the profile
        return super().form_valid(form)  # Redirects after saving
    
    def get_success_url(self):
        # This returns the URL to redirect after the form is valid
        return reverse_lazy('profile_list')

class ProfileDeleteView(DeleteView):
    model = Profile
    template_name = 'main/profile_confirm_delete.html'
    success_url = reverse_lazy('profile_list')

# Products CRUD
class ProductListView(ListView):
    model = Product
    template_name = 'main/product_list.html'
    context_object_name = 'products'

class ProductDetailView(DetailView):
    model = Product
    template_name = 'main/product_detail.html'
    context_object_name = 'product'

class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'main/product_form.html'
    success_url = reverse_lazy('product_list')

class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'main/product_form.html'
    success_url = reverse_lazy('product_list')

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'main/product_confirm_delete.html'
    success_url = reverse_lazy('product_list')

# Categories CRUD
class CategoryListView(ListView):
    model = Category
    template_name = 'main/category_list.html'
    context_object_name = 'categories'

class CategoryDetailView(DetailView):
    model = Category
    template_name = 'main/category_detail.html'
    context_object_name = 'category'

class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'main/category_form.html'
    success_url = reverse_lazy('category_list')

class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'main/category_form.html'
    success_url = reverse_lazy('category_list')

class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'main/category_confirm_delete.html'
    success_url = reverse_lazy('category_list')

# Orders CRUD
class OrderListView(ListView):
    model = Order
    template_name = 'main/order_list.html'
    context_object_name = 'orders'

class OrderDetailView(DetailView):
    model = Order
    template_name = 'main/order_detail.html'
    context_object_name = 'order'

class OrderCreateView(CreateView):
    model = Order
    form_class = OrderForm
    template_name = 'main/order_form.html'
    success_url = reverse_lazy('order_list')

class OrderUpdateView(UpdateView):
    model = Order
    form_class = OrderForm
    template_name = 'main/order_form.html'
    success_url = reverse_lazy('order_list')

class OrderDeleteView(DeleteView):
    model = Order
    template_name = 'main/order_confirm_delete.html'
    success_url = reverse_lazy('order_list')

# Reviews CRUD
class ReviewListView(ListView):
    model = Review
    template_name = 'main/review_list.html'
    context_object_name = 'reviews'

class ReviewDetailView(DetailView):
    model = Review
    template_name = 'main/review_detail.html'
    context_object_name = 'review'

class ReviewCreateView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = 'main/review_form.html'
    success_url = reverse_lazy('review_list')

class ReviewUpdateView(UpdateView):
    model = Review
    form_class = ReviewForm
    template_name = 'main/review_form.html'
    success_url = reverse_lazy('review_list')

class ReviewDeleteView(DeleteView):
    model = Review
    template_name = 'main/review_confirm_delete.html'
    success_url = reverse_lazy('review_list')

# Messages CRUD
class MessageListView(ListView):
    model = Message
    template_name = 'main/message_list.html'
    context_object_name = 'messages'

class MessageDetailView(DetailView):
    model = Message
    template_name = 'main/message_detail.html'
    context_object_name = 'message'

class MessageCreateView(CreateView):
    model = Message
    form_class = MessageForm
    template_name = 'main/message_form.html'
    success_url = reverse_lazy('message_list')

class MessageDeleteView(DeleteView):
    model = Message
    template_name = 'main/message_confirm_delete.html'
    success_url = reverse_lazy('message_list')
