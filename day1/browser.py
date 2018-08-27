import webbrowser

query = ["아이유", "수지", "설현"]
url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query="

for search in query:

    webbrowser.open(url + search)
