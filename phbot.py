from pornhub_api import PornhubApi

api = PornhubApi()

categories = api.video.categories()
tags = api.video.tags("a")


data = api.search.search(
    "bbc",
    ordering="mostviewed",
    period="year",
    tags=["bbc"],
    
    
)
for vid in data.videos:
    print(vid.title, vid.video_id)





