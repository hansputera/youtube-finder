from parsenar import getChannelRenderData, getPlaylistData, getStreamData, getVideoData
from urllib.parse import urlencode
import aiohttp
from json import loads
from util import buildTraceback

# Basic configuration
base_url = "https://www.youtube.com/"
search_url = lambda q, sp: base_url + "results?" + urlencode({"search_query": q, "sp": sp})

def spFilter(t):
    if t == "any":
        return "CAA%253D"
    elif t == "video":
        return "EgIQAQ%253D%253D"
    elif t == "channel":
        return "EgIQAg%253D%253D"
    elif t == "playlist":
        return "EgIQAw%253D%253D"
    elif t == "movie":
        return "EgIQBA%253D%253D"
    elif t == "live":
        return "EgJAAQ%253D%253D"
    else:
        return spFilter("video")

def extract(json):
    render = None
    contents = []

    sectionListRenderer = json.get("sectionListRenderer", None)
    if sectionListRenderer != None:
        render = []
        for section in sectionListRenderer.get("contents", []):
            if "itemSectionRenderer" in section and "contents" in section["itemSectionRenderer"]:
                for item in section["itemSectionRenderer"]["contents"]:
                    if len(item.get("videoRenderer", []) or item.get("playlistRenderer", []) or item.get("channelRenderer", [])) > 0:
                        render.append(section)
        if len(render) > 0:
            contents = render[0]["itemSectionRenderer"]["contents"]
    
    richGridRenderer = json.get("richGridRenderer", None)
    if richGridRenderer != None:
        contents = richGridRenderer.get("contents", [])
        _contents = []

        for content in contents:
            if "richItemRenderer" in content and "content" in content["richItemRenderer"]:
                _contents.append(content["richItemRenderer"]["content"])
        contents = _contents
    
    return contents

def parseData(json: list):
    results = {
        "videos": [],
        "streams": [],
        "playlists": [],
        "channels": []
    }
    for item in json:
        # Channel
        if "channelRenderer" in item:
            try:
                result = getChannelRenderData(item["channelRenderer"])
                results["channels"].append(result)
            except Exception as e:
                raise Exception(buildTraceback(e))

        # Video
        if "videoRenderer" in item and "lengthText" in item["videoRenderer"]:
            try:
                result = getVideoData(item.get("videoRenderer"))
                results["videos"].append(result)
            except Exception as e:
                raise Exception(buildTraceback(e))

        # Live Stream Video
        if "videoRenderer" in item and "lengthText" not in item["videoRenderer"]:
            try:
                result = getStreamData(item["videoRenderer"])
                results["streams"].append(result)
            except Exception as e:
                raise Exception(buildTraceback(e))
        
        # Playlist
        if "playlistRenderer" in item:
            try:
                result = getPlaylistData(item["playlistRenderer"])
                results["playlists"].append(result)
            except Exception as e:
                raise Exception(buildTraceback(e))
        
    # Returning response 
    return results

async def search(query: str, sp = "video"):
    json1 = await request(query, sp)
    extracted = extract(json1)
    return parseData(extracted)

async def request(query: str, sp: str):
    url = search_url(query, sp)

    # Initializing request
    session = aiohttp.ClientSession()
    # Requesting page
    response = await session.get(url)
    # Manage response
    context = await response.text()
    context = ("=".join(("".join(context.split("\n"))).split("var ytInitialData")[1].split("=")[1:])).split(";</script>")[0]
    # Closing session
    await session.close()

    return loads(context)["contents"]["twoColumnSearchResultsRenderer"]["primaryContents"]

