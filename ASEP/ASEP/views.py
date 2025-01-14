from django.http import HttpResponse , HttpResponseRedirect
from django.shortcuts import render
from pycode import metroFairData
from destinations.models import destinations
import json

def index(request):
    # request.method ='the'
    searchdata=[]
    dataHolder= destinations.objects.all()
    for i in dataHolder:
        searchdata.append(i.dest_name)
    data = {
        'searchdata':json.dumps(searchdata)
    }
    print(searchdata)

    
    try: 
        if request.method == 'POST':
            place= request.POST.get('search')
            for i in dataHolder :
                if i.dest_name == place:
                    slug = i.dest_slug
            # return HttpResponse(f"the name of the place is : {place}")
            return HttpResponseRedirect(f'/destinations/{slug}')
    except Exception as e:
        print(e)
    
    return render(request, 'index.html',data)

# def search(request):
#     if request.method == 'GET':
#         place= request.GET.get('search')
#         return HttpResponse(f"the name of the place is : {place}")

def metroFair(reqeust):
    data = {
        'mfrom': "please select!",
        'mto': "please select!",
        'TOKEN_FARE': "0",
        'NUMBER_OF_INTERCHANGES': 0,
        'NUMBER_OF_STATION': 0,
        'METRO_GO_SMART_CARD_FARE':0,
        'TRAVEL_TIME': '--:--:--',
        'FIRST_TRAIN_TIMING': '--:-- --',
        'LAST_TRAIN_TIMING': '--:-- --',
        'remakr':'',

    }
    newdata={}
    if reqeust.method =='POST':

        mfrom = reqeust.POST.get('from')
        data['mfrom']=mfrom
        mto = reqeust.POST.get('to')
        data['mto'] = mto
        # rerender(reqeust,'loading.html')
        try:
            newdata = metroFairData.getMetroData(mfrom,mto)
            print(newdata)
            if newdata['TOKEN_FARE']!='₹':
                data.update(newdata)
            else:
                data["remark"] = "Data Not found!! Please try again later."
        except Exception as e :
            print(e)


        # reqeust.method = 'NONE'
        return render(reqeust,'metroFair.html',data)
    return render(reqeust,'metroFair.html',data)

def dest(reqeust):
    dataHolder= destinations.objects.all()
    data = {
        'title':'Destinations',
        'cardData':dataHolder
    }

    return render(reqeust,'destinations.html',data)    