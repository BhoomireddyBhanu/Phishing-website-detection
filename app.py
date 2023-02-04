from email.utils import decode_params
from flask import Flask, render_template, request
from phishing import *
import whois
import pandas as pd
import sklearn
import pickle

app = Flask(__name__)
app.config['SECRET_KEY']='sasidharmankalaphishingwebsite'

# domains = ['GOOGLE.COM', 'google.com', 'YOUTUBE.COM', 'youtube.com', 'FACEBOOK.COM', 'TWITTER.COM', 'twitter.com', 'INSTAGRAM.COM', 'BAIDU.COM', 'baidu.com', 'WIKIPEDIA.ORG', 'wikipedia.org', 'YANDEX.RU', 'YAHOO.COM', 'yahoo.com', 'XVIDEOS.COM', 'xvideos.com', 'WHATSAPP.COM', 'XNXX.COM', 'xnxx.com', 'AMAZON.COM', 'amazon.com', 'NETFLIX.COM', 'netflix.com', 'LIVE.COM', 'live.com', 'PORNHUB.COM', 'pornhub.com', 'zoom.us', 'OFFICE.COM', 'office.com', 'REDDIT.COM', 'TIKTOK.COM', 'tiktok.com', 'LINKEDIN.COM', 'linkedin.com', 'VK.COM', 'XHAMSTER.COM', 'xhamster.com',
#            'DISCORD.COM', 'TWITCH.TV', 'twitch.tv', 'NAVER.COM', 'BING.COM', 'bing.com', 'BILIBILI.COM', 'bilibili.com', 'MAIL.RU', 'DUCKDUCKGO.COM', 'duckduckgo.com', 'ROBLOX.COM', 'roblox.com', 'MICROSOFTONLINE.COM', 'microsoftonline.com', 'PINTEREST.COM', 'pinterest.com', 'SAMSUNG.COM', 'QQ.COM', 'qq.com', 'MSN.COM', 'msn.com', 'GLOBO.COM', 'google.com.br', 'EBAY.COM', 'ebay.com', 'FANDOM.COM', 'bbc.co.uk', 'MIGUVIDEO.COM', 'miguvideo.com', 'ACCUWEATHER.COM', 'accuweather.com', 'REALSRV.COM', 'realsrv.com', 'powerlanguage.co.uk', 'WEATHER.COM', 'weather.com', 'amazon.in']

filename = 'static/model/phishing_detection_xg_boost_model.sav'
def predict_input(single_input):
    input_df = pd.DataFrame(single_input)
    loaded_model = pickle.load(open(filename, 'rb'))
    result = loaded_model.predict(input_df)
    print(result)
    return result




@app.route("/", methods=["GET", "POST"])
def phishing_detection():
    if request.method == "POST":
        url = request.form.get('url')
        # domainnames=whois.whois(url).domain_name
        # if domainnames!=None and type(domainnames)==list:
        #     if domainnames[0] in domains:
        #         return render_template('detectionpage.html', domainName=domainnames[0])
        # elif domainnames!=None and domainnames in domains:
        #     return render_template('detectionpage.html', domainName=domainnames)
        # else:
        print('hi')
        try:
            final = getAttributess(url)
            # print(final)
            # print('hi')
            # values = dict_making(feature_names,final)
            # print(values)
            final_values = predict_input(final)
            # (final_values[0])
            print(final_values[0])
            return render_template('detectionpage.html',prediction = final_values[0])
        except:
            final_values = [0]
            return render_template('detectionpage.html', prediction=final_values[0])
    return render_template('index.html')

if __name__ == "__main__":
    app.run()