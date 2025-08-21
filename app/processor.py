from collections import Counter
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.download('vader_lexicon')# Compute sentiment labels
# tweet = 'Skillcate is a great Youtube Channel to learn Data Science'
# score=SentimentIntensityAnalyzer().polarity_scores(tweet)
# print(score)

class Processor:
    def __init__(self,df):
        self.df = df.copy()

    def rarest_word(self):
        def rare(text):
            words = text.split()
            d = Counter(words)
            min_count = min(d.values())
            for word in words:
                if d[word] == min_count:
                    return word


        self.df["rarest_word"] = self.df['Text'].apply(rare)
        return self.df["rarest_word"]

    def sentiment(self):
        def senti(text):
            score = SentimentIntensityAnalyzer().polarity_scores(text)
            if score["compound"] >= 0.5:
                return "positive"
            elif score["compound"] <= -0.5:
                return "negative"
            else:
                return "neutral"
        self.df["sentiment"] = self.df["Text"].apply(senti)
        return self.df[["Text","sentiment"]]
    def weapon_detected(self):
        with open(r"C:\Users\shuki\Desktop\kodkod\hostile-tweets-ex\data\weapons.txt","r") as f:
            weapon_list = [weapon.strip() for weapon in f.readlines()]

        def detect(text):
            words = text.split()
            for i in range(len(words)):
                for weapon in weapon_list:
                    wep_len = len(weapon.split())

                    if " ".join(words[i:i+wep_len]) == weapon:
                        return " ".join(words[i:i+wep_len])


        self.df["weapons_detected"] = self.df["Text"].apply(detect)
        return self.df[["Text", "weapons_detected"]].head(50)

if __name__ == '__main__':
    from manager import Manager
    m = Manager().mongo_to_df()
    p = Processor(m)
    # print(p.rarest_word())
    # print(p.sentiment())
    print(p.weapon_detected())

