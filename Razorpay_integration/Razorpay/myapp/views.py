from django.shortcuts import render
from myapp.models import Product
import razorpay
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt


razorpay_client= razorpay.Client(
                        auth=(settings.RAZORPAY_API_KEY, settings.RAZORPAY_API_SECRET_KEY))
# Create your views here.
def Homepage(request):
    products = Product.objects.all()
    if request.method == "POST" :
        id = (request.POST['submit'])
        product = Product.objects.get(id = id)
        
        razorpay_payment = razorpay_client.order.create(
            dict(amount=product.price, currency='INR'))

        order_id = razorpay_payment['id']
        order_status = razorpay_payment['status']

        
        return render(request,'myapp/cart.html',{'product' : product,'id':order_id,'status':order_status})
    
    # razorpay_order = razorpay_client.order.create(dict(amount=final_price*100, currency=order_currency, notes = notes, receipt=order.order_id, payment_capture='0'))
    # print(razorpay_order['id'])
    # order.razorpay_order_id = razorpay_order['id']
    return render(request,'myapp/index.html',{'products':products})


@csrf_exempt
def success(request):
    response = request.POST
    params_dict = {
        'razorpay_order_id': response['razorpay_order_id'],
        'razorpay_payment_id': response['razorpay_payment_id'],
        'razorpay_signature': response['razorpay_signature'],
    }

    client = razorpay.Client(
        auth=('rzp_test_m0YSZRrMdLzIrK', 'n77X9UkHL7SNJP28z7r8IA0e'))

    try:
        status = client.utility.verify_payment_signature(params_dict)
        return render(request, 'myapp/success.html', {'status': True})
    except:
        return render(request, "myapp/success.html", {'status': False})
    
