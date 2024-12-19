import factory
from factory.django import DjangoModelFactory
from faker import Faker
from myapp.models import Profile, Product, Category, Order,OrderItem, Review, Message
from django.contrib.auth.models import User

fake = Faker()

class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker('user_name')
    email = factory.Faker('email')
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    password = factory.Faker('password')

class ProfileFactory(DjangoModelFactory):
    class Meta:
        model = Profile

    user = factory.SubFactory(UserFactory)
    address = factory.Faker('address')
    phone_number = factory.Faker('phone_number')
    is_seller = factory.Faker('boolean')
    bio = factory.Faker('paragraph')

class CategoryFactory(DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.Faker('word')
    description = factory.Faker('paragraph')

class ProductFactory(DjangoModelFactory):
    class Meta:
        model = Product

    seller = factory.SubFactory(ProfileFactory)
    name = factory.Faker('word')
    description = factory.Faker('sentence', nb_words=10)
    price = factory.Faker('random_number', digits=3)
    quantity = factory.Faker('random_number', digits=2)
    image = factory.django.ImageField()
    is_available = factory.Faker('boolean')

class OrderFactory(DjangoModelFactory):
    class Meta:
        model = Order

    buyer = factory.SubFactory(ProfileFactory)
    is_completed = factory.Faker('boolean')
    total_price = factory.Faker('random_number', digits=4)

class OrderItemFactory(DjangoModelFactory):
    class Meta:
        model = OrderItem

    order = factory.SubFactory(OrderFactory)
    product = factory.SubFactory(ProductFactory)
    quantity = factory.Faker('random_number', digits=1)
    price = factory.Faker('random_number', digits=3)

class ReviewFactory(DjangoModelFactory):
    class Meta:
        model = Review

    product = factory.SubFactory(ProductFactory)
    user = factory.SubFactory(ProfileFactory)
    rating = factory.Faker('random_int', min=1, max=5)
    comment = factory.Faker('paragraph')

class MessageFactory(DjangoModelFactory):
    class Meta:
        model = Message

    sender = factory.SubFactory(ProfileFactory)
    receiver = factory.SubFactory(ProfileFactory)
    content = factory.Faker('text')
    is_read = factory.Faker('boolean')
