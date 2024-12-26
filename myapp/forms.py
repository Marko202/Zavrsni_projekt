from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Product, Profile, Category, Order, Review, Message

class RegistracijaForma(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'quantity', 'image', 'is_available']

class UserProfileForm(UserCreationForm):
    email = forms.EmailField(required=True)
    address = forms.CharField(max_length=255)
    phone_number = forms.CharField(max_length=15, required=False)
    is_seller = forms.BooleanField(initial=False, required=False)
    bio = forms.CharField(widget=forms.Textarea, required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        # First, save the user object
        user = super().save(commit=False)
        if commit:
            user.save()

        # Now, create the profile
        profile = Profile(
            user=user,
            address=self.cleaned_data['address'],
            phone_number=self.cleaned_data.get('phone_number'),
            is_seller=self.cleaned_data['is_seller'],
            bio=self.cleaned_data.get('bio')
        )
        profile.save()

        return user

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['address', 'phone_number', 'is_seller', 'bio']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['buyer', 'is_completed', 'total_price']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['product', 'user', 'rating', 'comment']

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['sender', 'receiver', 'content', 'is_read']
