from django.shortcuts import render
import requests

# Create your views here.
def get_geographic_info(request):
    # ip = request.META.get('HTTP_X_FORWARDED_FOR',"") or request.META.get('REMOTE_ADDR')
    # url='http://api.ipstack.com/'+str(ip)+'?access_key=67d0797a14ba2df12b52601992891b9b'
    url='http://api.ipstack.com/103.168.164.143?access_key=67d0797a14ba2df12b52601992891b9b'
    response=requests.get(url)
    data=response.json()
    return render(request,'app1/info.html',data)



    # d0797a14ba2df12b52601992891b9b
    # http: // api.ipstack.com / 103.168.164.143?access_key = 67d0797a14ba2df12b52601992891b9b