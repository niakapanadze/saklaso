from .models import Product, Customer, Order

product_exact = Product.objects.filter(name__exact="Laptop")

customers_contains = Customer.objects.filter(last_name__contains="dze")

products_starts = Product.objects.filter(name__startswith="Samsung")

products_ends = Product.objects.filter(name__endswith="Plus")

products_gt = Product.objects.filter(price__gt=100)

products_gte = Product.objects.filter(price__gte=100)

products_lt = Product.objects.filter(price__lt=100)

products_lte = Product.objects.filter(price__lte=100)

products_range = Product.objects.filter(price__range=(100, 200))

products_in = Product.objects.filter(id__in=[1, 3, 5])

customers_no_email = Customer.objects.filter(email__isnull=True)