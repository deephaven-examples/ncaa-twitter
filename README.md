# ncaa-twitter

This repository integrates [Deephaven](http://deephaven.io/) with [Twitter](https://twitter.com/) and [Python's Natural Language Toolkit (NLTK)](https://www.nltk.org/) to pull recent tweets and evaluate sentiment in real-time. We start by pulling data related to NCAA teams' Twitter usernames, and then run a `SentimentIntensityAnalyzer` on each tweet. Next, we aggregate the posts to see the overall positivity or negativity of that term on Twitter at a given time.

Run `./ncaa-twitter.sh` and launch Deephaven on [http://localhost:10000/ide](http://localhost:10000/ide).

## How it works


### Components

* `Dockerfile` - The Dockerfile for the application. This extends the default Deephaven images to add dependencies. See our guide, [How to install Python packages](https://deephaven.io/core/docs/how-to-guides/install-python-packages/#add-packages-to-a-custom-docker-image), for more information.
* `docker-compose.yml` - The Docker Compose file for the application. This is mostly the same as the [Deephaven docker-compose file](https://raw.githubusercontent.com/deephaven/deephaven-core/main/containers/python-examples/docker-compose.yml) with modifications to run (NLTK)](https://www.nltk.org/) with [Twitter V2 API](https://twitter.com/) and custom dependencies.
* `ncaa-twitter.sh` - A simple helper script to launch the application.
* `data/notebooks/ncaa.py` - A Deephaven sample query to pull tweets.


### High level overview

Twitter provides a continous stream of real-time data from which - if used properly - we can learn a lot about social sentiment. When it comes to sports, you can harness the data to potentially make better predictions when forming a bracket or fantasy team. Most of the time, you can scroll Twitter for a long time and not glean much insight. With Deephaven and a little bit of natural language processing, we can quickly determine the overall sentiment about a team and perhaps apply our knowledge to weigh the odds of a team's success. 

We'll show you how to pull in Twitter data and process that in Deephaven. This data can then be combined with other data - for example, game statistics and outcomes. The possibilities are endless.

## Dependencies

* The [Deephaven-core dependencies](https://github.com/deephaven/deephaven-core#required-dependencies) are required to build and run this project.

## Launch

To launch the latest release, you can clone the repository via:

```shell
git clone https://github.com/deephaven-examples/ncaa-twitter.git
cd ncaa-twitter
```

A start script will install the needed Python modules. It will also start the Deephaven IDE.

To run it, execute:

```shell
sh ncaa-twitter.sh
```

Running this script will start several Docker containers that work together to launch Deephaven with the needed dependancies. To view the data navigate to [http://localhost:10000/ide](http://localhost:10000/ide).  To view the data you need to edit the `keys.py` file with your infomration.


## Prereqs

[Twitter](https://developer.twitter.com/en/docs/twitter-api) provides an API to make it easy to pull public tweets. In order to use this code as-is, you need to also have a Twitter Developer account and copy your Bearer Token.


### Run the program

This program is intended to be fine-tuned to fit your data needs. As is, this will pull in the live tweets for the NCAA teams. We recommend filtering the handles to the teams in the current round. The code will perform sentiment analysis on the tweets and aggregate the tweets to assess if that team is trending positive/negative in the public's eye.

## Your turn

This code provides a basic starter. You can use it to make your own searches, tie to other programs, or just see how social media is doing.

We hope this program inspires you. If you make something of your own or have an idea to share, we'd love to hear about it on in our [Discussions](https://github.com/deephaven/deephaven-core/discussions) or on [Slack](https://join.slack.com/t/deephavencommunity/shared_invite/zt-11x3hiufp-DmOMWDAvXv_pNDUlVkagLQ).



## Related documentation

- [Simple Kafka import](https://deephaven.io/core/docs/how-to-guides/kafka-simple/)
- [Kafka introduction](https://deephaven.io/core/docs/conceptual/kafka-in-deephaven/)
- [How to connect to a Kafka stream](https://deephaven.io/core/docs/how-to-guides/kafka-stream/)
- [Kafka basic terminology](https://deephaven.io/core/docs/conceptual/kafka-basic-terms/)
- [consumeToTable](https://deephaven.io/core/docs/reference/data-import-export/Kafka/consumeToTable/)
