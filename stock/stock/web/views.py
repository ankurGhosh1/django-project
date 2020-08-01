from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import messages
import requests 
from django.contrib.auth.models import User, auth
from .models import Profile
# Create your views here.


def index(request):

    # Top Gainers API

    url = "https://yahoo-finance15.p.rapidapi.com/api/yahoo/ga/topgainers"

    headers = {
    'x-rapidapi-host': "yahoo-finance15.p.rapidapi.com",
    'x-rapidapi-key': "e9255b460cmsh863ffa7bd83b3bep19d626jsne90553c61953"
    }

    response = requests.request("GET", url, headers=headers)
    topGainersAPI = response.json()

    allGainers = []

    i = 0

    for eachGainer in topGainersAPI['quotes']:
        if (i >= 10):
            break;
        allGainers.append(eachGainer)
        i += 1

    # News API call    

    news = []

    response = requests.get('https://finnhub.io/api/v1/news?category=general&token=bs9jpfnrh5rahoaohehg')
    apiResponseNews = response.json()

    for allnews in apiResponseNews:
        news.append(allnews)

    # Earnings API call

    earnings = []
    symbols = []
    # logo = []

    response = requests.get('https://finnhub.io/api/v1/calendar/earnings?from=2020-07-21&to=2020-08-15&token=bs9jpfnrh5rahoaohehg')
    apiResponseEarnings = response.json()

    for allearnings in apiResponseEarnings['earningsCalendar']:
        symbol = allearnings['symbol']
        symbols.append(symbol)
        # if (allearnings['epsEstimate' and 'revenueEstimate']  != 0):  
        earnings.append(allearnings)
    

    # for eachlogo in symbols:
    #     # Company Profile API call 

    #     response = requests.get('https://finnhub.io/api/v1/stock/profile2?symbol=' + eachlogo + '&token=bs9jpfnrh5rahoaohehg') 
    #     apiResponseLogo = response.json()

    #     if(not apiResponseLogo['logo']):
    #         logo.append('eachlogo')

    # print(logo)
        
    
    # print(symbols)
        
    # Events API call

    events = []

    response = requests.get('https://finnhub.io/api/v1/calendar/economic?token=bs9jpfnrh5rahoaohehg')
    apiResponseEvents = response.json()

    for allevents in apiResponseEvents['economicCalendar']:
        events.append(allevents)

    # render HTML Template

    return render(request, 'home.html', {'news': news, 'earnings': earnings, 'events': events, 'allGainer': allGainers })


# Dynamic slug Route

def stock(request, searchText):
    searchText = request.GET["searchText"].upper()

    # Stock List API Call

    response = requests.get('https://finnhub.io/api/v1/stock/symbol?exchange=US&token=bs9jpfnrh5rahoaohehg')   
    apiResponseStockList = response.json()

    stockList = []

    for stock in apiResponseStockList:
        stockList.append(stock['symbol'])

    found = False

    for eachStock in stockList:
        if(eachStock == searchText):
            found = True
            break;

    # Routing Logic

    # Details API Call
    if found:
        response = requests.get('https://finnhub.io/api/v1/stock/profile2?symbol=' + searchText + '&token=bs9jpfnrh5rahoaohehg') 
        apiResponseProfile = response.json()

        # News of each stock API call

        response = requests.get('https://finnhub.io/api/v1/company-news?symbol=' + searchText + '&from=2020-04-30&to=2021-12-31&token=bs9jpfnrh5rahoaohehg')
        apiResponseNewsP2 = response.json()

        eachNews = []

        for eachStockNews in apiResponseNewsP2:
            eachNews.append(eachStockNews)

        # Each Stock Earning

        response = requests.get('https://finnhub.io/api/v1/calendar/earnings?from=2019-01-01&to=2020-12-15&symbol=' + searchText + '&token=bs9jpfnrh5rahoaohehg')
        eachEarningStock = response.json()

        eachEarning = []

        for eachStockEarning in eachEarningStock['earningsCalendar']:
            eachEarning.append(eachStockEarning)

        #Filings API Call
        
        response = requests.get('https://finnhub.io/api/v1/stock/filings?symbol=' + searchText + '&token=bs9jpfnrh5rahoaohehg')
        filingsAPI = response.json()

        # Quote API Call

        response = requests.get('https://finnhub.io/api/v1/quote?symbol=' + searchText + '&token=bs9jpfnrh5rahoaohehg')
        quoteAPI = response.json()

        # Description API Call

        url = "https://yahoo-finance15.p.rapidapi.com/api/yahoo/qu/quote/" + searchText + "/asset-profile"

        headers = {
            'x-rapidapi-host': "yahoo-finance15.p.rapidapi.com",
            'x-rapidapi-key': "e9255b460cmsh863ffa7bd83b3bep19d626jsne90553c61953"
            }

        response = requests.request("GET", url, headers=headers)
        desc = response.json()

        
        description = desc['assetProfile']

        # Key Stats API Call

        url = "https://yahoo-finance15.p.rapidapi.com/api/yahoo/qu/quote/" + searchText + "/default-key-statistics"

        headers = {
            'x-rapidapi-host': "yahoo-finance15.p.rapidapi.com",
            'x-rapidapi-key': "e9255b460cmsh863ffa7bd83b3bep19d626jsne90553c61953"
            }

        response = requests.request("GET", url, headers=headers)
        keyStats = response.json()
        
        keyStatistics = keyStats['defaultKeyStatistics']
        # print(keyStatistics)

        return render(request, 'stock.html', {'details': apiResponseProfile, 'news': eachNews, 'eachEarning': eachEarning, 'filing': filingsAPI, 'quote': quoteAPI, 'description': description, 'keyStatistics': keyStatistics})
    else:
        return JsonResponse({"message": "No stock"})


def signup(request):
    return render(request, 'signup.html')

def signupAuth(request):
    if request.method == 'POST':
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

    if(password == password2):
        user = User(username= username, first_name = firstname, last_name = lastname, email=email, password=password)
        user.set_password(password)
        user.save()
        messages.success(request, 'New User Created')
        return redirect('/signup/')
    else:
        messages.info(request, 'Passwords Do Not Match')
        return redirect('/signup/')

username = ''

def profile(request):
    if (request.user.is_authenticated):
        return render(request, 'profile.html', { 'username': username})
    else:
        return redirect('/signup/')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/profile/')
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('/signup/')


def logout(request):
    auth.logout(request)
    return redirect('/')

def upload(request): 
    if request.method == 'POST':
        avatar = request.FILES['avatar']
        Profile.objects.filter(user_id = request.user.id).update(avatar = avatar)
    print(request.user.id)
    return redirect('/profile/')

