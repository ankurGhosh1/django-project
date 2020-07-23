from django.shortcuts import render
from django.http import JsonResponse
import requests 

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

    for eachGainer in topGainersAPI['quotes']:
        allGainers.append(eachGainer)
    

    # News API call    

    news = []

    response = requests.get('https://finnhub.io/api/v1/news?category=general&token=bs9jpfnrh5rahoaohehg')
    apiResponseNews = response.json()

    for allnews in apiResponseNews:
        news.append(allnews)

    # Earnings API call

    earnings = []
    symbol = ''

    response = requests.get('https://finnhub.io/api/v1/calendar/earnings?from=2020-07-21&to=2020-08-15&token=bs9jpfnrh5rahoaohehg')
    apiResponseEarnings = response.json()
    #reverserEarning = reversed(apiResponseEarnings)  
    #print(reverserEarning)

    for allearnings in apiResponseEarnings['earningsCalendar']:
        symbol = allearnings['symbol']
        # if (allearnings['epsEstimate' and 'revenueEstimate']  != 0):  
        earnings.append(allearnings)

    # Company Profile API call 

    response = requests.get('https://finnhub.io/api/v1/stock/profile2?symbol=' + symbol + '&token=bs9jpfnrh5rahoaohehg') # trying to use this as image link for earnings table
    apiResponseProfile = response.json()

        
    # Events API call

    events = []

    response = requests.get('https://finnhub.io/api/v1/calendar/economic?token=bs9jpfnrh5rahoaohehg')
    apiResponseEvents = response.json()

    for allevents in apiResponseEvents['economicCalendar']:
        events.append(allevents)

    # render HTML Template

    return render(request, 'home.html', {'news': news, 'earnings': earnings, 'events': events, 'companyProfile': apiResponseProfile, 'allGainer': allGainers })


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

        return render(request, 'stock.html', {'details': apiResponseProfile, 'news': eachNews, 'eachEarning': eachEarning, 'filing': filingsAPI, 'quote': quoteAPI})
    else:
        return JsonResponse({"message": "No stock"})
        