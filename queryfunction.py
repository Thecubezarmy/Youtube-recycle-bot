from youtube_search import YoutubeSearch
import json  


def youtubequery (search):
 x=""
 results = YoutubeSearch(search, max_results=1).to_dict()
 mydict = dict(results[0])
 y = mydict["id"]
 x = "https://www.youtube.com/watch?v=" + y
 return x



