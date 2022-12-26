import collections
import imp
import logging
from multiprocessing.spawn import import_main_path
from operator import imod
from django.db.models import DecimalField
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import send_mail, mail_admins, BadHeaderError, EmailMessage
import requests
from store.models import Collection, Order, Product, OrderItem, Customer
from tags.models import TaggedItem
from django.contrib.contenttypes.models import ContentType
from django.db.models.aggregates import Count,Max, Min, Sum
from django.db.models import Value, F, Func, ExpressionWrapper
from django.db.models.functions import Concat
from django.db import transaction, connection

from django.core.cache import cache
from django.views.decorators.cache import cache_page
from templated_mail.mail import BaseEmailMessage
from .tasks import notify_customers
from rest_framework.views import APIView
from django.utils.decorators import method_decorator
# Create your views here.
# request -> response
# request handler
# action

# LOGGERS
logger = logging.getLogger(__name__)

class HelloView(APIView):
    #@method_decorator(cache_page(5 * 60))
    def get(self, request, *args, **kw):
        try:
            
            logger.info('Calling HTTPBIN')
            response = requests.get('https://httpbin.org/delay/2')
            logger.info('Recieved HTTPBIN response')
            data = response.json()
            return render(request, 'hello.html', {'name': data})

        except requests.ConnectionError:
            logger.critical('HTTPBIN is offline')

# CACHING FOR FUNTIONS BASE VIEW
# @cache_page(5 * 60)
# def say_hello(request):
#     response = requests.get('https://httpbin.org/delay/2')
#     data = response.json()
#     return render(request, 'hello.html', {'name': data})
    
# def say_hello(request):
    # LOW LEVEL CACHE API
    # key = 'httpbin_result'
    # if cache.get(key) is None:
    #     response = requests.get('https://httpbin.org/delay/2')
    #     data = response.json()
    #     cache.set(key, data)
    #     # cache.set(key, data 10 * 60)
    # return render(request,'hello.html', {'name': cache.get(key), 'badheader': say_hello})

    #notify_customers.delay('Dragon')

    # Query_sets
    # to find query_sets api search in Google.
    #discounted_price = ExpressionWrapper(F('unit_price') * 0.5, output_field=DecimalField())
    #product = Product.objec s.order_by('id')
    #product = Product.objects.all()[0:20]
    #product = Product.objects.filter(id__in=OrderItem.objects.values('product_id').distinct()).order_by('title')
    #orders = Order.objects.select_related('customer').prefetch_related('orderitem_set__product').order_by('-placed_at')[:10]
    #results = Product.objects.filter(collection__id=1).aggregate(count=Count('id'), min_price=Min('unit_price'))

    #results = Customer.objects.annotate(new_id=F('id'))

    # results = Product.objects.annotate(
    #     #full_name = Func(F('first_name', Value(' '), F('last_name'), function='CONCAT'))
    #     #full_name = Concat('first_name', Value(' '), 'last_name')
    #     #order_count =Count('order')
    #     discounted_price = discounted_price
    # )
    #results = TaggedItem.objects.get_tags_for(Product, 1)
    # Queryset cache
    # First access all of the objects then take it will take it from the cache not directly from the database which will save time.

    # queryset = Product.objects.all()
    # list(queryset)

    # collection = Collection()
    # collection.title = 'Deleting one'
    # collection.featured_product = Product(pk=1)
    # collection.save()

    # one way deleting objects.
    # collection = Collection(pk=101)
    # collection.delete()

    # Another way of deleting objects.
    #Collection.objects.filter(id__gt=100).delete()
    
    #Collection.objects.filter(pk=12).update(featured_product=None, title='Health')
    #Collection.objects.create(title='Video', featured_product=Product(pk=1))

    # @transaction.atomic()
    # with transaction.atomic():
    #     order = Order()
    #     order.customer_id = 1
    #     order.save() 

    #     item = OrderItem()
    #     item.order = order
    #     item.product_id = 1
    #     item.quantity = 1
    #     item.unit_price = 30
    #     item.save()
         
    #Order.objects.filter(id__gt = 1000).delete()

    #with connection.cursor() as cursor:
        # cursor.execute(' SELECT * FROM storefront.store_customer')
        #cursor.callproc('get_customer')

    # result = OrderItem.objects \
    #         .select_related('order__customer') \
    #         .select_related('product') \
    #         .filter(id__gt=40, id__lt=100) \
    #         .order_by('order__customer__first_name').all() 
    
    #query_set = OrderItem.objects.filter(order_id=357).select_related('order__customer').select_related('product')
    #query_set = Customer.objects.filter(id=1).prefetch_related('order_set__orderitem_set__product').all()
    #product.images.all.0.id

    # SEND EMAILS:
    # try:
    #     #send_mail('subject', 'message', 'info@dragondevs.com', ['john@gmail.com'])
    #     #mail_admins('subject', 'message', html_message='message')

    #     # message = EmailMessage('subject', 'message', 'from@dragondevs.com', ['dragon@gmail.com'])
    #     # message.attach_file('playground\static\images\pic.png')
    #     # message.send()

    #     message = BaseEmailMessage(
    #         template_name='emails/hello.html',
    #         context={'name':'DRAGONROBUST'}
    #     )
    #     message.send(['Drh@gmail.com'])

    # except BadHeaderError:
    #     badErorr = "Email format was wrong."
    #     return badErorr


