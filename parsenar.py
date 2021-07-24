from re import sub

def getChannelBadges(video):
    ownerBadges = video.get("ownerBadges", [])
    badges = []
    for badge in ownerBadges:
        badges.append(badge["metadataBadgeRenderer"]["style"])
    return badges

def isVerified(video):
    badges = getChannelBadges(video)
    for badge in badges:
        return True if badge == "BADGE_STYLE_TYPE_VERIFIED_ARTIST" or badge == "BADGE_STYLE_TYPE_VERIFIED" else False

def getChannelLink(channel):
    return "https://www.youtube.com/channel/" + channel["navigationEndpoint"]["browseEndpoint"]["browseId"]

def compress(key):
    data = []
    for run in key["runs"]:
        data.append(run.get("text"))
    return "".join(data)

def parseDuration(text: str):
    nums = text.split(":")
    sum_num = 0
    multi = 1

    while(len(nums) > 0):
        sum_num += int(nums.pop() or "-1") * multi
        multi *= 60
    return sum_num

def getUploadDate(video):
    pubs = video.get("publishedTimeText", None)
    let = ""
    if pubs != None:
        let = pubs["simpleText"]
    
    return let.replace("Streamed", "").strip()

def getWatchers(result):
    try:
        return int(sub(r'[^0-9]', "", result["viewCountText"]["runs"][0]["text"]))
    except:
        return 0

def getViews(video):
    try:
        return int(sub(r'[^0-9]', "", video["viewCountText"]["simpleText"]))
    except:
        return 0

def getVideoCount(channel):
    try:
        return getWatchers(channel)
    except:
        return 0

def getSubscriberCount(channel):
    try:
        return channel["subscriberCountText"]["simpleText"].split(" ")[0]
    except:
        return "0"

def convertSubs(channel):
    count = getSubscriberCount(channel)
    char = count[-1].lower()
    slicedCount = int(count[0:-1])

    if char == "k":
        slicedCount *= 1000
    elif char == "m":
        slicedCount *= 1e6
    elif char == "b":
        slicedCount *= 1e9
    return ~~slicedCount

def getChannelThumbnail(video):
    try:
        thumbRenders = video["channelThumbnailSupportedRenderers"]
        url = thumbRenders["channelThumbnailWithLinkRenderer"]["thumbnail"]["thumbnails"][0]["url"]
        return url.split("=")[0] + "=s0?imgmax=0"
    except:
        return "https://www.gstatic.com/youtube/img/originals/promo/ytr-logo-for-search_160x160.png"

def getVideoThumbnail(id: str):
    return f"https://i.ytimg.com/vi/{id}/hqdefault.jpg"

def getLink(id: str, playlist = False):
    url = "https://www.youtube.com/playlist?list=" if playlist == True else "https://youtu.be/"
    return url + id

def getBiggestThumbnail(thumbnails):
    return "https:" + thumbnails[0]["url"].split("=")[0] + "=s0?imgmax=0"

def getChannelRenderData(channel):
    return {
        "id": channel["channelId"],
        "title": channel["title"]["simpleText"],
        "thumbnail": getBiggestThumbnail(channel["thumbnail"]["thumbnails"]),
        "description": compress(channel.get("descriptionSnippet", None) or channel.get("snippetHoverText", { "runs": [{"text": ""}]})),
        "link": f"https://youtube.com/channel/{channel['channelId']}",
        "verified": False if isVerified(channel) == None else isVerified(channel),
        "subsCount": convertSubs(channel),
        "videosCount": getVideoCount(channel),
        "subs": getSubscriberCount(channel)
    }

def getChannelData(video):
    channel = (video.get("ownerText", None) or video.get("longBylineText", { "runs": [{"text": ""}]}))["runs"][0]
    return {
        "id": channel["navigationEndpoint"]["browseEndpoint"]["browseId"],
        "title": channel["text"],
        "link": getChannelLink(channel),
        "verified": False if isVerified(video) == None else isVerified(video),
        "thumbnail": getChannelThumbnail(video)
    }

def getPlaylistThumbnail(result):
    return getVideoThumbnail(result["navigationEndpoint"]["watchEndpoint"]["videoId"])

def getPlaylistResultData(result):
    id = result["playlistId"]
    return {
        "id": id,
        "title": result["title"]["simpleText"],
        "link": getLink(id, True),
        "thumbnail": getPlaylistThumbnail(result),
        "channel": getChannelData(result)
    }

def getResultData(result):
    return {
        "id": result["videoId"],
        "title": compress(result["title"]),
        "link": getLink(result["videoId"]),
        "thumbnail": getVideoThumbnail(result["videoId"]),
        "channel": getChannelData(result),
    }

def getPlaylistVideo(child):
    return {
        "id": child["videoId"],
        "title": child["title"]["simpleText"],
        "link": getLink(child["videoId"]),
        "thumbnail": getVideoThumbnail(child["videoId"]),
        "duration": parseDuration(child["lengthText"]["simpleText"])
    }

def getVideoData(result):
    obj = {
        "views": getViews(result),
        "uploaded": getUploadDate(result),
        "duration": parseDuration(result["lengthText"]["simpleText"]) if result.get("lengthText", None) != None else 0,
    }
    obj.update(getResultData(result))
    return obj

def getPlaylistData(result):
    cvideos = []
    for video in result["videos"]:
        try:
            cvideos.append(getPlaylistVideo(video["childVideoRenderer"]))
        except:
            # I don't want handle this error
            pass
    obj = {
        "videoCount": +result["videoCount"],
        "videos": cvideos
    }
    obj.update(getPlaylistResultData(result))
    return obj

def getStreamData(result):
    obj = {
        "watching": getWatchers(result)
    }
    obj.update(getResultData(result))
    return obj