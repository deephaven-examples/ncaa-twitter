from deephaven import read_csv

elite_8_mens =['razorbackmbb', 'dukembb', 'uhcougarmbk', 'kuhoops', 'caneshoops', 'peacocksmbb', 'unc_basketball', 'novambb']
elite_8_womens =['stanfordwbb', 'texaswbb', 'gamecockwbb', 'creightonwbb', 'uconnwbb', 'packwomensbball', 'uoflwbb', 'umichwbball']
final_4_mens = ['dukembb', 'kuhoops', 'unc_basketball', 'novambb']
final_4_womens =['stanfordwbb', 'gamecockwbb', 'uconnwbb', 'uoflwbb']



tweets = read_csv("https://raw.githubusercontent.com/deephaven/examples/main/NCAA/tweets.csv")

teams_grouped = read_csv("https://raw.githubusercontent.com/deephaven/examples/main/NCAA/teams_grouped.csv")


tweets_final4 =tweets.where(["DateTime >'2022-03-28T08:00:00 NY'"])

from deephaven import agg as agg
teams_filtered  = tweets_final4.agg_by([agg.avg(["Avg_Pos= Positive"]),\
                agg.avg(["Avg_Neg= Negative"]),\
                agg.avg(["Avg_Compound= Compound"]),\
                agg.avg(["Avg_retweet= Retweet_count"]),\
                agg.count_("Number_tweets")], ["team"])\
                .sort_descending(["Number_tweets"])


from deephaven.time import to_datetime, lower_bin, to_nanos

nanosBin = to_nanos("00:01:00")

agg_list_tweets = [
    agg.count_("Count_tweet"),
    agg.avg(["Average_negative = Negative"]),
    agg.avg(["Average_neutral = Neutral"]),
    agg.avg(["Average_positive = Positive"]),
    agg.avg(["Average_compound = Compound"]),
    agg.weighted_avg("Retweet_count", ["Weight_negative = Negative"]),
    agg.weighted_avg("Retweet_count",["Weight_neutral = Neutral"]),
    agg.weighted_avg("Retweet_count",["Weight_positive = Positive"]),
    agg.weighted_avg("Retweet_count",["Weight_compound = Compound"])
]

combined_tweets = tweets.update(["Time_bin = (DateTime)lower_bin(DateTime,nanosBin)"])\
                    .agg_by(agg_list_tweets, ["Time_bin", "team"]).where(["Weight_negative <100","Weight_negative>-100"])\

from deephaven.plot.figure import Figure
figure = Figure()

plot_tweets = figure.plot_xy(series_name ="Positive Sentiment", t = combined_tweets.where(["team = `kuhoops`"]),  x ="Time_bin", y = "Average_positive")\
    .plot_xy(series_name ="Negative Sentiment", t = combined_tweets,  x ="Time_bin",  y = "Average_negative")\
    .show()
