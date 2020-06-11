"""
returns the name of the happiest state as a string

You can ignore any tweets for which you cannot assign
a location in the United States

Note: Not every tweet will have a text field --- again,
real data is dirty! Be prepared to debug, and feel free
to throw out tweets that your code can't handle to get
something working. For example, you might choose to
ignore all non-English tweets.

Your script should print the two letter state
abbreviation of the state with the highest average
tweet sentiment to stdout.

Note that you may need a lot of tweets in order to get
enough tweets with location data. Let the live stream
run for a while if you wish.

"""


import sys
import json
import re
from collections import defaultdict


regex = re.compile("[^a-zA-Z0-9.'-]")


states = {
    'AK': 'Alaska',
    'AL': 'Alabama',
    'AR': 'Arkansas',
    'AS': 'American Samoa',
    'AZ': 'Arizona',
    'CA': 'California',
    'CO': 'Colorado',
    'CT': 'Connecticut',
    'DC': 'District of Columbia',
    'DE': 'Delaware',
    'FL': 'Florida',
    'GA': 'Georgia',
    'GU': 'Guam',
    'HI': 'Hawaii',
    'IA': 'Iowa',
    'ID': 'Idaho',
    'IL': 'Illinois',
    'IN': 'Indiana',
    'KS': 'Kansas',
    'KY': 'Kentucky',
    'LA': 'Louisiana',
    'MA': 'Massachusetts',
    'MD': 'Maryland',
    'ME': 'Maine',
    'MI': 'Michigan',
    'MN': 'Minnesota',
    'MO': 'Missouri',
    'MP': 'Northern Mariana Islands',
    'MS': 'Mississippi',
    'MT': 'Montana',
    'NA': 'National',
    'NC': 'North Carolina',
    'ND': 'North Dakota',
    'NE': 'Nebraska',
    'NH': 'New Hampshire',
    'NJ': 'New Jersey',
    'NM': 'New Mexico',
    'NV': 'Nevada',
    'NY': 'New York',
    'OH': 'Ohio',
    'OK': 'Oklahoma',
    'OR': 'Oregon',
    'PA': 'Pennsylvania',
    'PR': 'Puerto Rico',
    'RI': 'Rhode Island',
    'SC': 'South Carolina',
    'SD': 'South Dakota',
    'TN': 'Tennessee',
    'TX': 'Texas',
    'UT': 'Utah',
    'VA': 'Virginia',
    'VI': 'Virgin Islands',
    'VT': 'Vermont',
    'WA': 'Washington',
    'WI': 'Wisconsin',
    'WV': 'West Virginia',
    'WY': 'Wyoming'
}


def parse_json(fp):
    """
    ------
    input: tweets file handle
    output: list(tweets_place_usr), list(tweets_text)
    ------

    parses tweets to extract text field usr location data and place location data if available. Moreover, it maps both location information to a single list for None values
    """

    tweets = defaultdict(lambda: defaultdict(int))
    for i, line in enumerate(fp):
        if 'created_at' in json.loads(line) and not json.loads(line).get('is_quote_status', False) and not json.loads(line).get('text', 'RT').startswith('RT'):

            tweet = json.loads(line)

            tweets[i]['text'] = tweet['text']
            tweets[i]['state_usr'] = tweet['user'].get('location')
            if tweet['place'] is not None:
                tweets[i]['state_place'] = tweet['place'].get('full_name')
            elif tweet['place'] is None:
                tweets[i]['state_place'] = None
    return tweets
    # tweets_text = [json.loads(line)['text'] for line in fp
    #                if 'created_at' in json.loads(line)
    #                and not json.loads(line).get('is_quoted_status', False)
    #                and not json.loads(line).get('text', 'RT').startswith('RT')]
    # fp.seek(0)

    # tweets_state_usr = [json.loads(line)['user'].get('location') for line in fp
    #                     if 'created_at' in json.loads(line)
    #                     and not json.loads(line).get('is_quote_status', False)
    #                     and not json.loads(line).get('text', 'RT').startswith('RT')]
    # fp.seek(0)

    # tweets_state_place = []
    # for line in fp:
    #     if 'created_at' in json.loads(line) and not json.loads(line).get('is_quote_status', False) and not json.loads(line).get('text', 'RT').startswith('RT'):
    #         tweet = json.loads(line)
    #         if tweet['place'] is not None:
    #             tweets_state_place.append(tweet['place'].get('full_name'))
    #         else:
    #             tweets_state_place.append(None)

    # return tweets_text, tweets_state_usr


def sent_dict(fp):
    dict_afinn = {word: value.rstrip('\n') for line in fp
                  for word, value in (line.split('\t'),)}
    fp.seek(0)
    return dict_afinn


def tweet_sent(texts, scores):
    sentiments = []
    for text in texts:
        words = [regex.sub('', word) for word in text.split(
            ' ') if not word.startswith(("https"))]
        sentiments.append(sum(int(scores.get(word, 0)) for word in words))
    return sentiments


# def happiest_state(texts, sentiments, states):
    # for i, text in enumerate(texts):
    #     state =
    #     words = [regex.sub('', strip_punct(word).lower())
    #              for word in text.split(' ') if not word.startswith(("https"))]


def main():
    sent_file = open(sys.argv[1])
    json_file = open(sys.argv[2])
    #sent_scores = sent_dict(sent_file)
    tweets_text = parse_json(json_file)
    print(tweets_text)
    # print(len(tweets_text))
    # print(len(tweets_state))
    #sentiments = tweet_sent(tweets_text, sent_scores)
    # print(len(sentiments))
    # happiest_state(tweets_text, sentiments, tweets_state)


if __name__ == '__main__':
    main()
