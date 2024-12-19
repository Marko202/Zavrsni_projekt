import random
from django.db import transaction
from django.core.management.base import BaseCommand
from myapp.models import Profile, Product, Category, Order, Review, Message
from myapp.factory import (
    ProfileFactory,
    ProductFactory,
    CategoryFactory,
    OrderFactory,
    OrderItemFactory,
    ReviewFactory,
    MessageFactory
)

# Broj objekata koji će biti generirani
NUM_PROFILES = 10
NUM_CATEGORIES = 5
NUM_PRODUCTS = 30
NUM_ORDERS = 20
NUM_REVIEWS = 50
NUM_MESSAGES = 40

class Command(BaseCommand):
    help = "Generates test data"

    @transaction.atomic
    def handle(self, *args, **kwargs):
        # Brisanje starih podataka
        self.stdout.write("Deleting old data...")
        models = [Profile, Product, Category, Order, Review, Message]
        for m in models:
            m.objects.all().delete()

        # Kreiranje novih podataka
        self.stdout.write("Creating new data...")

        # Generiranje kategorija
        categories = [CategoryFactory() for _ in range(NUM_CATEGORIES)]

        # Generiranje profila (korisnika)
        profiles = [ProfileFactory() for _ in range(NUM_PROFILES)]

        # Generiranje proizvoda
        for _ in range(NUM_PRODUCTS):
            product = ProductFactory(seller=random.choice(profiles))  # Proizvod je povezan s profilom

        # Generiranje narudžbi
        orders = [OrderFactory(buyer=random.choice(profiles)) for _ in range(NUM_ORDERS)]

        # Generiranje stavki u narudžbi (OrderItem)
        for _ in range(NUM_ORDERS):
            order = random.choice(orders)
            OrderItemFactory(order=order, product=random.choice(Product.objects.all()))

        # Generiranje recenzija
        for _ in range(NUM_REVIEWS):
            ReviewFactory(product=random.choice(Product.objects.all()), user=random.choice(profiles))

        # Generiranje poruka
        for _ in range(NUM_MESSAGES):
            MessageFactory(sender=random.choice(profiles), receiver=random.choice(profiles))

        self.stdout.write(self.style.SUCCESS(f'Successfully created {NUM_PROFILES} profiles, {NUM_CATEGORIES} categories, {NUM_PRODUCTS} products, {NUM_ORDERS} orders, {NUM_REVIEWS} reviews, and {NUM_MESSAGES} messages.'))
