from django.shortcuts import render
from datetime import datetime, timedelta
import hmac
import hashlib
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

# Variables for jazz cash payment integration
JAZZCASH_MERCHANT_ID = 'MC105945'
JAZZCASH_PASSWORD = '0e110bsuua'
JAZZCASH_INTEGRITY_SALT = 'yc2724095u'
JAZZCASH_RETURN_URL = 'http://127.0.0.1:8000/success/'

@csrf_exempt
def success(request): 
    return render(request, 'payment/success.html')




def purchase(request): 
    product_name = "Subscribe Webcog"
    product_price = 100

    pp_Amount = (int(product_price) *100)

    current_datetime = datetime.now()
    pp_TxnDateTime = current_datetime.strftime('%Y%m%d%H%M%S')

    expiry_datetime = current_datetime + timedelta(hours=1)
    pp_TxnExpiryDateTime = expiry_datetime.strftime('%Y%m%d%H%M%S')

    pp_TxnRefNo = "T" + pp_TxnDateTime
    post_data = {
    "pp_Version": "1.1",
    "pp_TxnType": "MWALLET",
    "pp_Language": "EN",
    "pp_MerchantID": JAZZCASH_MERCHANT_ID,
    "pp_SubMerchantID": '',
    "pp_Password": JAZZCASH_PASSWORD,
    "pp_BankID": 'TBANK',
    "pp_ProductID": '1231314',
    "pp_TxnRefNo": pp_TxnRefNo,
    "pp_Amount": pp_Amount,
    "pp_DiscountedAmount": "",
    "pp_TxnCurrency": "PKR",
    "pp_TxnDateTime": pp_TxnDateTime,
    "pp_BillReference": "billref",
    "pp_Description": "Description of transaction",
    "pp_TxnExpiryDateTime": pp_TxnExpiryDateTime,
    "pp_ReturnURL": " http://127.0.0.1:8000/success/ ",
    "pp_SecureHash": "",
    "ppmpf_1": "1",
    "ppmpf_2": '2',
    "ppmpf_3": '3',
    "ppmpf_4": '4',
    "ppmpf_5": '5',
    }
    sorted_string = "&".join(f"{key}={value}" for key , value in sorted(post_data.items()) if value != "")
    pp_SecureHash = hmac.new(
        JAZZCASH_INTEGRITY_SALT.encode(),
        sorted_string.encode(),
        hashlib.sha256
    ).hexdigest()
    post_data['pp_SecureHash'] = pp_SecureHash

    context = {
        'product_name':product_name,
        "product_price":product_price,
        'post_data':post_data
    }
    return render(request, 'payment/purchase.html', context)