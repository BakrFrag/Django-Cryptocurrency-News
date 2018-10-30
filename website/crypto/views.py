from django.shortcuts import render;
from .forms import ConvertForm;
import requests;
import json;
# Create your views here.
def home(request):
    #prices
    prices_url = "https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,XRP,BCH,EOS,LTC,XLM,ADA,USDT,MIOTA,TRX&tsyms=USD";
    #https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC&tsyms=USD,EUR
    prices = requests.get(prices_url);
    prices=json.loads(prices.content);
    #news
    news_url="https://min-api.cryptocompare.com/data/v2/news/?lang=EN";
    data=requests.get(news_url);
    news=json.loads(data.content)
    return render(request,"home.html",{'news':news,'prices':prices});
def news(request):
    news_url = "https://min-api.cryptocompare.com/data/v2/news/?lang=EN"
    data = requests.get(news_url)
    news = json.loads(data.content);
    return render(request,"news.html",{'news':news});
def prices_page(request):
    prices_url = "https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,XRP,BCH,EOS,LTC,XLM,ADA,USDT,MIOTA,TRX,MIOTA,DASH,BNB,NEO&tsyms=USD"
    #https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC&tsyms=USD,EUR
    prices = requests.get(prices_url)
    prices = json.loads(prices.content);
    return render(request,"prices.html",{'prices':prices});
def about(request):
    return render(request,"about.html");
