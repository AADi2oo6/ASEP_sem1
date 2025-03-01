from django.http import HttpResponseRedirect
from django.shortcuts import render
from pycode import metroFairData
from destinations.models import destinations, emergincy
from django.db.models import Q
import json

searchdata=[]
dataHolder= destinations.objects.all()
for i in dataHolder:
    searchdata.append(i.dest_name)


def newIndex(request):
    return render(request,'Index2.html')
def index(request):
    global dataHolder
    data = {
        'searchdata':json.dumps(searchdata)
    }
    try: 
        if request.method == 'POST':
            place= request.POST.get('search')
            for i in dataHolder :
                if i.dest_name == place:
                    slug = i.dest_slug
                else:
                    return render(request, 'destNotFound.html')
            # return HttpResponse(f"the name of the place is : {place}")
            return HttpResponseRedirect(f'/destinfo/{slug}')
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

    return render(reqeust,'metroFair.html',data)

def dest(request):
    global dataHolder
    try: 
        if request.method == 'POST':
            search= request.POST.get('search')
            filter1 = request.POST.get('filter1')
            print(len(search),filter1,'---------------')
            if search != '':
                dataHolder=destinations.objects.filter(dest_name__icontains = search)
            elif filter1 == 'All':
                dataHolder = destinations.objects.all()
            elif search =='':
                dataHolder=destinations.objects.filter(dest_category = filter1.lower())
                
    except Exception as e:
        print(e)
    data = {
        'title':'Destinations',
        'cardData':dataHolder,
        'searchdata':json.dumps(searchdata)
    }

    return render(request,'destinations.html',data)    

def destinfo(request,destSlug):
    dataHolder= destinations.objects.filter(dest_slug=destSlug)
    data = {
        'cardData':dataHolder,
    }
    # for i in dataHolder:
    #     if i.dest_slug == destSlug:
    #         data['destData'] = i
    return render(request,'destinfo.html',data)


def timeTable(request):
    import csv
    import os
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path = os.path.join(base_dir, 'pycode', 'timeTable.csv')
    with open(file_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        l=[]
        for row in reader :
            if row not in l:
            # print(row['FROM'], row['TO'], row['TIMING'])
                l.append(row)
        time = 'Not Avilable'
        bfrom =''
        bto = ''
        if request.method == 'POST':
            fromPlace = request.POST.get('from')
            toPlace = request.POST.get('to')
            print(fromPlace,toPlace)
            for i in l:
                # if i['FROM'].strip() == fromPlace and i['TO'].strip() == toPlace:
                bfrom = fromPlace
                bto = toPlace
                if fromPlace in i['FROM'] and  toPlace in i['TO'].strip():
                    print(i['TIMING'])
                    time=i['TIMING']
                    bfrom = fromPlace
                    bto = toPlace
                    


        data = {
            'title':'Time Table',
            'timeTable':l,
            'timing':time,
            'bfrom':bfrom,
            'bto':bto
        }

        return render(request,'busTimeTable.html',data)
    
def emergency(request):
    # request.method = 'GET'
    searchdata=set()
    dataHoldere= emergincy.objects.all()
    for i in dataHoldere:
        if i not in searchdata:
            searchdata.add(i.area)
    print(searchdata,request.method)

    if request.method == 'GET':
        search = request.GET.get('search')
        filter1 = request.GET.get('filter')
        print(search,filter1,'---------------')
        if search != None :
            dataHoldere = emergincy.objects.filter(Q(area=search) | Q(catagory=filter1))
        elif filter1 == 'None':
            dataHoldere = emergincy.objects.all()
        # else:
        #     dataHoldere = emergincy.objects.filter(catagory=filter1)

    # dataHoldere = emergincy.objects.all()
    data = {
        'cardData':dataHoldere,
        'searchdata':json.dumps(list(searchdata))
    }
    return render(request,'emergency.html',data)

def contact(request):
    return render(request,'contact.html')