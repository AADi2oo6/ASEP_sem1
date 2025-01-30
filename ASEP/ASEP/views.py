from django.http import HttpResponse , HttpResponseRedirect
from django.shortcuts import render
from pycode import metroFairData
from destinations.models import destinations, emergincy
from django.db.models import Q
# from ASEP.pycode import TimeTableWriter
import json
def newIndex(request):
    return render(request,'Index2.html')
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


        # reqeust.method = 'NONE'
        return render(reqeust,'metroFair.html',data)
    return render(reqeust,'metroFair.html',data)

def dest(request):
    
    # dataHolder= destinations.objects.all()
    searchdata=[]
    dataHolder= destinations.objects.all()
    for i in dataHolder:
        searchdata.append(i.dest_name)
    print(searchdata)

    
    try: 
        if request.method == 'POST':
            search= request.POST.get('search')
            filter1 = request.POST.get('filter1')
            print(len(search),filter1,'---------------')
            if search != '':
                dataHolder=destinations.objects.filter(Q(dest_name__icontains = search) | Q(dest_category = filter1))
            if search =='':
                dataHolder=destinations.objects.filter(dest_category = filter1)
                
            
            # return HttpResponse(f"the name of the place is : {place}" )

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
    with open(r'C:/Users/adish/Documents/GitHub/ASEP_sem1/ASEP/pycode/timeTable.csv', 'r') as csvfile:
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

    # dataHoldere = emergincy.objects.all()
    data = {
        'cardData':dataHoldere,
        'searchdata':json.dumps(list(searchdata))
    }
    return render(request,'emergency.html',data)