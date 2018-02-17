import tweepy

def get_timeline(user):
	auth = tweepy.OAuthHandler("toi08Fyrx1pXNeUjxqxinfimz", "uYl34isj4B3QXDmrrjnC72rwis1mNwf8wQS47XpoVkb37gylwE")
	auth.set_access_token("962347956585291776-M7I33HieYEsNwR5cFfO8CDTgHqGiW94", "EycFvgDsgDF0O1Tv2W1hiFTL8YwNG6cm7OYwHv6BpFa86")
	api = tweepy.API(auth)
	return api.user_timeline(screen_name = user, count = 10)