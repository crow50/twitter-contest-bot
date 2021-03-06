import time

class ReTweeter:
	SLEEP = 1

	def __init__(self, api, fav_keywords, follow_keywords):
		self.api = api
		self.fav_keywords = fav_keywords
		self.follow_keywords = follow_keywords

	def retweet_all(self, tweets):
		for tweet in tweets:
			self.retweet(tweet)

	def retweet(self, tweet):
		self.api.retweet(tweet)

		if self._shoud_follow(tweet):
			self.api.follow(tweet)

		if self._should_favotrite(tweet):
			self.api.favorite(tweet)

		time.sleep(self.SLEEP)

	def _shoud_follow(self, tweet):
		return self._tweet_contains_keyword(tweet, self.follow_keywords)

	def _should_favotrite(self, tweet):
		return self._tweet_contains_keyword(tweet, self.fav_keywords)

	def _tweet_contains_keyword(self, tweet, keywords):
		for keyword in keywords:
			if keyword.lower() in tweet.get_text().lower():
				return True
		return False
