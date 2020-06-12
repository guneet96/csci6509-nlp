import csv, pandas, re, json
df = pd.read_csv("tweets.csv")
profiles = df['screen_name'].unique()
df = df.drop(columns = ['id','created_at'])
df
data = {}
for i,j in zip(df['screen_name'],df['text']):
    data[i] = {}
    

# Regular ecpressions
HASHTAG_PATTERN = re.compile(r'#\w*')
URL_PATTERN=re.compile(r'(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:\'".,<>?\xab\xbb\u201c\u201d\u2018\u2019]))')
MENTION_PATTERN = re.compile(r'@\w*')
RESERVED_WORDS_PATTERN = re.compile(r'^(RT|FAV)')
EMOJIS_PATTERN = re.compile(u'([\U00002600-\U000027BF])|([\U0001f300-\U0001f64F])|([\U0001f680-\U0001f6FF])')
SMILEYS_PATTERN = re.compile(r"(?:X|:|;|=)(?:-)?(?:\)|\(|O|D|P|S){1,}", re.IGNORECASE)
EMOJIS_PATTERN2 = re.compile(u'([\u2600-\u27BF])|([\uD83C][\uDF00-\uDFFF])|([\uD83D][\uDC00-\uDE4F])|([\uD83D][\uDE80-\uDEFF])')
http_PATTERN = re.compile()
for i in profiles:
    data[i]['hashtag'] = []
    data[i]['tweets'] = []
    data[i]['words'] = []
# print(data)

c=0
for i,j in zip(df['screen_name'],df['text']):
    c+=1
    list_ = re.findall(HASHTAG_PATTERN, j)
    for k in list_:
        data[i]['hashtag'].append(k)
    
    tweet = re.sub(URL_PATTERN, "", j.lower())
    
    tweet = re.sub(MENTION_PATTERN, "", tweet)
    tweet = re.sub(HASHTAG_PATTERN, "", tweet)
    tweet = re.sub(EMOJIS_PATTERN, "", tweet)
    tweet = re.sub(EMOJIS_PATTERN2, "", tweet)
    tweet = re.sub(SMILEYS_PATTERN, "", tweet)
    tweet = re.sub(RESERVED_WORDS_PATTERN, "", tweet)
    data[i]['tweets'].append(tweet)
    words = j.split(" ")
    for k in words:
        data[i]['words'].append(k)

for i in profiles:
    word_l = data[i]['words']
    d_word = {}
    for j in word_l:
        if j not in d_word:
            d_word[j] = 1
        else:
            d_word[j]+=1
    popular_words = sorted(d_word, key = d_word.get, reverse = True)
    top10 = popular_words[:10]
    data[i]['top10'] = top10


# print(json.dumps(data, indent=2))
for i in profiles:
    print(i + ":")
    str_top = ", ".join(data[i]['top10'])
    print("* top 10 words: " + str_top)
    str_hash = ", ".join(data[i]['hashtag'])
    print("* hashtags: " + str_hash)
    print("* clean tweets:")
    c=0
    for k in data[i]['tweets']:
        c+=1
        print(str(c) + ". " + str(k))


