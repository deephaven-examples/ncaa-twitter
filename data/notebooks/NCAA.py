def installations():
    import os
    os.system("pip install nltk")
    import nltk
    nltk.download('punkt')
    nltk.download('vader_lexicon')
    import os
    os.system("pip install requests")
    os.system("pip install requests")
    os.system("pip install requests_oauthlib")
installations()

from requests_oauthlib import OAuth1Session
import requests
from datetime import datetime

import time
import re
import json
import textwrap
import threading
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk import word_tokenize,sent_tokenize
import requests
from requests_oauthlib import OAuth1Session




from deephaven.time import to_datetime, now, plus_period, to_period
from deephaven import DynamicTableWriter
import deephaven.dtypes as dht
from deephaven import new_table
from deephaven.column import string_col, int_col
from deephaven import agg as agg
from deephaven.constants import NULL_INT
from threading import Thread




bearer_token =  '<YOUR BEARER TOKEN>'
# Max results per time bin, 10-100
max_results = 100

# Time intervals to split data
time_bins = 15

#seconds between requests
time_to_sleep = 60

#how long to keep listening in minutes
time_alive = 10

# How many days to go back. Max 7 for non-acemdic searches
time_history = 1

max_id =int(1502096953148444672)
search_terms=[]  

teams =['acu_mbb', 'af_mbb', 'zipsmbb', 'alabamambb', 'bulldogs_hoops', 'bamastatembb', 'ualbanymbb', 'bravessports', 'au_mbasketball', 'appstatembb', 'aplayersprogram', 'sundevilhoops', 'razorbackmbb', 'astatemb', 'uapblionsroar', 'armywp_mbb', 'auburnmbb', 'austinpeaymbb', 'ballstatembb', 'baylormbb', 'buknightsmbb', 'belmontmbb', 'bcuhoops', 'binghamtonmbb', 'broncosportsmbb', 'bcmbb', 'terriermbb', 'bgsumhoops', 'bradleyumbb', 'brownbasketball', 'bryanthoops', 'bucknell_mbb', 'ubmenshoops', 'butlermbb', 'byubasketball', 'calpolymbb', 'csub_mbb', 'fullertonmbb', 'csunmbb', 'calmbball', 'cbumbb', 'gocamelsmbb', 'griffs_mbb', 'ucambb', 'ccsu_mbb', 'ucf_mbb', 'cmumensbball', 'cofcbasketball', 'csu_mbball', 'charlottembb', 'gomocsmbb', 'chicagostatembb', 'gobearcatsmbb', 'clemsonmbb', 'csu_basketball', 'coastalmbb', 'colgatembb', 'cubuffsmbb', 'csumbasketball', 'culionsmbb', 'uconnmbb', 'coppinmbb', 'cubigredhoops', 'bluejaymbb', 'dartmouthmbk', 'davidsonmbb', 'daytonmbb', 'delawarembb', 'dsumbb', 'du_mhoops', 'depaulhoops', 'detroitmbb', 'dixiestatebball', 'drakebulldogsmb', 'drexelmbb', 'dukembb', 'duqmbb', 'ecubasketball', 'etsu_mbb', 'eiubasketball', 'ekuhoops', 'emuhoops', 'ewumbb', 'elonmbasketball', 'ueathletics_mbb', 'stagsmensbball', 'fdu_mbb', 'gatorsmbk', 'famuathletics', 'fau_hoops', 'fgcu_mbb', 'fiuhoops', 'fsuhoops', 'fordhammbb', 'fresnostatembb', 'furmanhoops', 'gwu_mbk', 'masonmbb', 'gw_mbb', 'georgetownhoops', 'ugabasketball', 'gsathletics_mbb', 'georgiastatembb', 'gtmbb', 'zagmbb', 'gsu_tigers', 'gcu_mbb', 'gbphoenixmbb', 'hampton_mbb', 'hartfordmbb', 'harvardmbb', 'hawaiimbb', 'hpumbb', 'hofstrambb', 'hcrossmbb', 'uhcougarmbk', 'hbubasketball', 'humensbb', 'vandalhoops', 'idahostatebball', 'illinimbb', 'redbird_mbb', 'uicflamesmbb', 'uiwmbb', 'indianambb', 'indstmbb', 'ionagaelsmbb', 'iowahoops', 'cyclonembb', 'iupuimensbball', 'gojsutigersmbb', 'jax_mbb', 'jsu_mbb', 'jmumbasketball', 'kuhoops', 'kstatembb', 'ksuowlsmbb', 'kentstmbb', 'kentuckymbb', 'lasallembb', 'lafayettembb', 'lamarmbb', 'lehighmbb', 'libertymbb', 'lipscombmbb', 'littlerockmbb', 'lbsuhoops', 'liubasketball', 'longwoodmbb', 'ragincajunsmbb', 'latechhoops', 'ulm_mbb', 'louisvillembb', 'lmulionsmbb', 'ramblersmbb', 'loyolambb', 'lsubasketball', 'blackbearsmbb', 'jaspersmbb', 'maristmbb', 'marquettembb', 'herdmbb', 'terrapinhoops', 'eshawkshoops', 'umassbasketball', 'mcneesembb', 'memphis_mbb', 'mercermbb', 'merrimackmbb', 'caneshoops', 'miamioh_bball', 'umichbball', 'msu_basketball', 'mt_mbb', 'mke_mbb', 'gophermbb', 'hailstatembk', 'mvsudevilsports', 'mizzouhoops', 'msubearshoops', 'monmouthbball', 'montanagrizbb', 'msubobcatsmbb', 'msueaglesmbb', 'morganstbears', 'mounthoops', 'racershoops', 'navybasketball', 'huskerhoops', 'omahambb', 'nevadahoops', 'unhmbb', 'unmlobombb', 'nmstatembb', 'privateersmbb', 'niagarambb', 'nicholls_mbb', 'njithoops', 'nsu_bball', 'una_mbb', 'unc_basketball', 'ncatbasketball', 'nccu_mbb', 'packmensbball', 'undmbasketball', 'ndsumbb', 'ospreysmbb', 'meangreenmbb', 'gonumbasketball', 'naubasketball', 'unc_bears', 'gohuskiesmbb', 'unimbb', 'nkunorsembb', 'numensbball', 'nsudemonsmbb', 'ndmbb', 'oaklandmbb', 'ohiombasketball', 'ohiostatehoops', 'ou_mbball', 'osumbb', 'odumbb', 'olemissmbb', 'orumbb', 'oregonmbb', 'beavermbb', 'pacificmensbb', 'pennbasketball', 'pennstatembb', 'peppbasketball', 'pitt_mbb', 'pilothoops', 'psuviksmbb', 'pvamupanthers', 'bluehosehoops', 'princeton_hoops', 'pcfriarsmbb', 'boilerball', 'mastodonmbb', 'qu_mbb', 'radfordmbb', 'rhodymbb', 'ricebasketball', 'spidermbb', 'ridermbb', 'rmumbasketball', 'rutgersmbb', 'sachornetsmbb', 'shu_menshoops', 'sjuhawks_mbb', 'saintlouismbb', 'saintmaryshoops', 'peacocksmbb', 'bearkatsmbb', 'samfordmbb', 'usdmbb', 'aztec_mbb', 'usfdonsmbb', 'sjsumbb', 'santaclarahoops', 'seattleumbb', 'setonhallmbb', 'sienambb', 'siuembb', 'smubasketball', 'wearesouth_mbb', 'gamecockmbb', 'scstateathletic', 'upstatemb', 'sdcoyotesmbb', 'gojacksmbb', 'usfmbb', 'semombb', 'slu_hoops', 'jaguarhoops', 'siu_basketball', 'southernmissmbb', 'suubasketball', 'bonniesmbb', 'sfbkmbb', 'redflashmbb', 'stjohnsbball', 'stanfordmbb', 'sfa_mbb', 'stetsonmbb', 'stonybrookmbb', 'cuse_mbb', 'tarletonmbb', 'tcubasketball', 'tumbbhoops', 'vol_hoops', 'tsutigersmbb', 'ttu_basketball', 'skyhawkhoops', 'texasmbb', 'aggiembk', 'islandersmbb', 'tsumenshoops', 'txstatembb', 'texastechmbb', 'uta_mbb', 'citadelhoops', 'toledombb', 'towson_mbb', 'troytrojansmbb', 'greenwavembb', 'tumbasketball', 'uab_mbb', 'ucdavismbb', 'ucimbb', 'ucrmbb', 'ucsdmbb', 'ucsbbasketball', 'uclambb', 'riverhawkmbb', 'umbc_mbb', 'kcroosmbb', 'uncavlmbb', 'uncgbasketball', 'uncwmenshoops', 'therunninrebels', 'usc_hoops', 'utahmbb', 'usubasketball', 'uvumbb', 'utep_mbb', 'utrgvmbb', 'utsambb', 'valpobasketball', 'vandymbb', 'uvmmbb', 'novambb', 'uvamenshoops', 'vcu_hoops', 'vmi_basketball', 'hokiesmbb', 'wagner_mbb', 'wakembb', 'uw_mbb', 'wsumenshoops', 'weberstatembb', 'wvuhoops', 'wcu_mbb', 'wiumenshoops', 'wku basketball', 'wmumbb', 'goshockersmbb', 'wmtribembb', 'winthrop_mbb', 'badgermbb', 'woffordmbb', 'wsu_mbb', 'wyo_mbb', 'xaviermbb', 'yale_basketball', 'ysumenshoops']

search_string=''
for i in range(0,len(teams)):
    search_string = search_string + teams[i] +' OR '
wrapper = textwrap.TextWrapper(width=512)

temp_terms = wrapper.wrap(text=search_string)
for element in temp_terms:
    if(element[:2]=='OR'):
        element = element[2:]
    if(element[-2:]=='OR ' or element[-2:]=='OR'):
        element = element[:len(element)-2]
    search_terms.append(element)

def make_table():
    return new_table([string_col("team", teams)])
teams_table = make_table()


#twitter function to create header
def create_headers(bearer_token):
        headers = {
            "Authorization": "Bearer {}".format(bearer_token),
            "User-Agent": "v2FullArchiveSearchPython"}
        return headers

# twitter url for recent tweets
search_url = "https://api.twitter.com/2/tweets/search/recent"

#connect to twitter with above header
def connect_to_endpoint(url, headers, params):
    response = requests.request("GET", search_url, headers=headers, params=params)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    if response.status_code == 429:
        raise Exception(response.status_code, response.text)
        time.sleep(120)
    return response.json()

# get tweets, if not enough data return null
def get_tweets(query_params):
    headers = create_headers(bearer_token)
    json_response = connect_to_endpoint(search_url, headers, query_params)
    try:
        if(len(json_response['data']))>2:
            return(json_response['data'])
        else: return " "
    except KeyError:
            print("KeyError in data")
    return " "
    
def build_default_sia_classifier_func(classifier):
    def a(strn):
        sentiment = classifier.polarity_scores(strn)
        return [sentiment["pos"], sentiment["neu"], sentiment["neg"], sentiment["compound"]]
    return a

classifier = build_default_sia_classifier_func(SentimentIntensityAnalyzer())


# twitter paramters for tweets from eariler in day
def get_query_params_hist(search_term, start_time, end_time):
    return {'query': search_term,
                    'start_time': start_time,
                    'end_time': end_time,
                    'max_results': max_results,
                    'tweet.fields': 'id,text,author_id,in_reply_to_user_id,geo,conversation_id,created_at,lang,public_metrics,referenced_tweets,reply_settings,source',
                    'user.fields': 'id,name,username,created_at,description,public_metrics,verified',
                    'next_token': {}}

#twitter paramters for live tweets
def get_query_params_live(search_term, max_id):
    return {'query': search_term,
                    'since_id': max_id,
                    'max_results': max_results,
                    'tweet.fields': 'id,text,author_id,in_reply_to_user_id,geo,conversation_id,created_at,lang,public_metrics,referenced_tweets,reply_settings,source',
                    'user.fields': 'id,name,username,created_at,description,public_metrics,verified',
                    'next_token': {}}

def write_data(all_text, tableWriter):
    for t in all_text:
        try:
            id = float(t['id'])
            if max_id < float(t['id']):
                globals()['max_id'] = int(t['id'])
            dateTime = t['created_at'][:-1]+" NY"
            retweet_count = t['public_metrics']['retweet_count']
            reply_count = t['public_metrics']['reply_count']
            like_count = t['public_metrics']['like_count']
            quote_count= t['public_metrics']['quote_count']
            tableWriter.write_row(t['text'].lower(), to_datetime(dateTime), int(retweet_count), int(reply_count), int(like_count), int(quote_count), t['id'])
  
        except TypeError:
            print("string indices must be integers")
        return max_id

def thread_func(search_terms, tableWriter):
    global max_id
    for i in range(1, time_bins):
        for search_term in search_terms:
            start_time = str(plus_period(to_datetime(str(now())[:11]+'00:00:00.000 NY'),to_period("T"+str(int(i-1))+"H")))[:-9]+'Z'
            end_time = str(plus_period(to_datetime(str(now())[:11]+'00:00:00.000 NY'),to_period("T"+str(int(i))+"H")))[:-9]+'Z'
            query_params = get_query_params_hist(search_term, start_time, end_time)
            all_text = get_tweets(query_params)
            max_id = write_data(all_text, tableWriter)

    for i in range(time_alive*time_to_sleep):
        for search_term in search_terms:
            query_params = get_query_params_live(search_term, max_id)
            all_text = get_tweets(query_params)
            max_id = write_data(all_text, tableWriter)
        time.sleep(time_to_sleep)

def make_table(term):
    tableWriter = DynamicTableWriter(
        {"Text":dht.string, "DateTime":dht.DateTime, "Retweet_count":dht.int_, "Reply_count":dht.int_, "Like_count":dht.int_, "Quote_count":dht.int_, "Id":dht.string})
    thread = Thread(target=thread_func, args=[term, tableWriter])
    thread.start()
    return tableWriter.table

data_sia= make_table(search_terms).update(["Sentiment = (org.jpy.PyListWrapper)classifier(Text)",
    "Positive = (double)Sentiment[0]",
    "Neutral = (double)Sentiment[1]",
    "Negative = (double)Sentiment[2]",
    "Compound = (double)Sentiment[3]"]).sort_descending(["DateTime"])

def match_text(text):
    return [ele for ele in teams if(ele in text)]

tweet_matching = data_sia.update(["team =  (org.jpy.PyListWrapper)match_text(Text)"]).where(["(team).size()>0"]).update(["team =(String)team[0]"])


teams_table_sia = teams_table.join(tweet_matching,["team=team"], ["Positive, Negative,Compound,Retweet_count"])\
    .sort(["team"])\
    .agg_by([agg.avg(["Avg_Pos= Positive"]),agg.avg(["Avg_Neg= Negative"]),agg.avg(["Avg_Compound= Compound"]),agg.avg(["Avg_retweet= Retweet_count"]),agg.count_("Number_tweets")], ["team"])

