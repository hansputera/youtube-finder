# YouTube Finder
Find youtube videos without having to use apikey.

This code was **taken** from https://github.com/DrKain/scrape-youtube and I changed it to python.
Can be deployed to heroku/replit/glitch. Just fork/clone it, and deploy.

# Usage
> I'm assuming you've run this project.

- Request to `/search` with query `q`, `query`, or `title`

Example: `/search?q=Damon+Empero+Veronica`, `/search?query=Damon+Empero+Veronica`, or `/search?title=Damon+Empero+Veronica`

- If successful you will get an object like this

```json
{
  "videos":[
    {
      "views":33871825,
      "uploaded":"4 years ago",
      "duration":221,
      "id":"ALzvSPXmeh8",
      "title":"Damon Empero ft. Veronica -  Vacation  [ King Step Release ] | Tropical House | | No Copyright |",
      "link":"https://youtu.be/ALzvSPXmeh8",
      "thumbnail":"https://i.ytimg.com/vi/ALzvSPXmeh8/hqdefault.jpg",
      "channel":{
        "id":"UCsGztxjStsz2AQaZYxVpXdA",
        "title":"Damon Empero",
        "link":"https://www.youtube.com/channel/UCsGztxjStsz2AQaZYxVpXdA",
        "verified":true,
        "thumbnail":"https://yt3.ggpht.com/ytc/AKedOLRiX57eLG-f-2gHBnGuRwQ5SxasooekggbDTEWAqg=s0?imgmax=0"
      }
    },
    {
      "views":1948716,
      "uploaded":"3 years ago",
      "duration":236,
      "id":"raiUPQJVDBI",
      "title":"Damon Empero ft. Timmy Commerford - Lost [ Outertone Release ] | Electro House | | No Copyright |",
      "link":"https://youtu.be/raiUPQJVDBI",
      "thumbnail":"https://i.ytimg.com/vi/raiUPQJVDBI/hqdefault.jpg",
      "channel":{
        "id":"UCsGztxjStsz2AQaZYxVpXdA",
        "title":"Damon Empero",
        "link":"https://www.youtube.com/channel/UCsGztxjStsz2AQaZYxVpXdA",
        "verified":true,
        "thumbnail":"https://yt3.ggpht.com/ytc/AKedOLRiX57eLG-f-2gHBnGuRwQ5SxasooekggbDTEWAqg=s0?imgmax=0"
      }
    },
    {
      "views":42819,
      "uploaded":"9 months ago",
      "duration":4518,
      "id":"xO6gGuzOZ8I",
      "title":"�DAMON EMPERO FULL ALBUM 2020",
      "link":"https://youtu.be/xO6g
GuzOZ8I",
      "thumbnail":"https://i.ytimg.com/vi/xO6gGuzOZ8I/hqdefault.jpg",
      "channel":{
        "id":"UCEVLal-mEFsIdXgbtuIcyrw",
        "title":"Knight Music",
        "link":"https://www.youtube.com/channel/UCEVLal-mEFsIdXgbtuIcyrw",
        "verified":false,
        "thumbnail":"https://yt3.ggpht.com/X-6qvubRTkIMCU8mUa5Sdz2VY-NLShX104WqzGPNkO26WNfCBPoLNi-_eqZnHqXjPEc53U3z=s0?imgmax=0"
      }
    },
    {
      "views":648975,
      "uploaded":"3 years ago",
      "duration":38787,
      "id":"75uHdU52z04",
      "title":"Damon Empero ft. Veronica - Vacation (10 Hour)",
      "link":"https://youtu.be/75uHdU52z04",
      "thumbnail":"https://i.ytimg.com/vi/75uHdU52z04/hqdefault.jpg",
      "channel":{
        "id":"UCFQHjckcODKQHHZnuB910vA",
        "title":"Anyone Wil",
        "link":"https://www.youtube.com/channel/UCFQHjckcODKQHHZnuB910vA",
        "verified":false,
        "thumbnail":"https://yt3.ggpht.com/ytc/AKedOLQHg0kYb4OuGsy0Hp7IIlap31ZLsM1g0tQqPgVBjw=s0?imgmax=0"
      }
    },
    {
      "views":69823,
      "uploaded":"1 year ago",
      "duration":2150,
      "id":"cH0F_x745lw",
      "title":"Top 10 Songs of Damon Empero - Best Of Damon Empero",
      "link":"https://youtu.be/cH0F_x745lw",
      "thumbnail":"https://i.ytimg.com/vi/cH0F_x745lw/hqdefault.jpg",
      "channel":{
        "id":"UCE5ztd4ZrGM7jiezf7pmHFw",
        "title":"SpiderMusicTV",
        "link":"https://www.youtube.com/channel/UCE5ztd4ZrGM7jiezf7pmHFw",
        "verified":false,
        "thumbnail":"https://yt3.ggpht.com/ytc/AKedOLSlqsNUelbnihbQdnCfqBemtM0C-0UZkViHMGr29A=s0?imgmax=0"
      }
    },
    {
      "views":3175611,
      "uploaded":"3 years ago",
      "duration":217,
      "id":"NMqcxdhBMZU",
      "title":"Damon Empero ft. Veronica - Vacation ( lyrics)",
      "link":"https://youtu.be/NMqcxdhBMZU",
      "thumbnail":"https://i.ytimg.com/vi/NMqcxdhBMZU/hqdefault.jpg",
      "channel":{
        "id":"UCIAd-Eu-r6Y-OgcM-qe17Nw",
        "title":"Amirul Ariff OFFICIAL",
        "link":"https://www.youtube.com/channel/UCIAd-Eu-r6Y-OgcM-qe17Nw",
        "verified":false,
        "thumbnail":"https://yt3.ggpht.com/ytc/AKedOLRG_ozy191hdzcXUQJyY_nc987tzX9qlQtSjWFbuw=s0?imgmax=0"
      }
    },
    {
      "views":204926,
      "uploaded":"2 years ago",
      "duration":301,
      "id":"iKjSeIpzwVs",
      "title":"Damon Empero ft. Sandra Bullet - The Emotions | Electro House |  | No Copyright |",
      "link":"https://youtu.be/iKjSeIpzwVs",
      "thumbnail":"https://i.ytimg.com/vi/iKjSeIpzwVs/hqdefault.jpg",
      "channel":{
        "id":"UCsGztxjStsz2AQaZYxVpXdA",
        "title":"Damon Empero",
        "link":"https://www.youtube.com/channel/UCsGztxjStsz2AQaZYxVpXdA",
        "verified":true,
        "thumbnail":"https://yt3.ggpht.com/ytc/AKedOLRiX57eLG-f-2gHBnGuRwQ5SxasooekggbDTEWAqg=s0?imgmax=0"
      }
    },
    {
      "views":217092,
      "uploaded":"6 months ago",
      "duration":254,
      "id":"HOOaEdxbOxQ",
      "title":"My Mobile Legends Gaming Music - Vacation by Damon Emparo",
      "link":"https://youtu.be/HOOaEdxbOxQ",
      "thumbnail":"https://i.ytimg.com/vi/HOOaEdxbOxQ/hqdefault.jpg",
      "channel":{
        "id":"UCeP0-OpzmdESIwNBW_gMvng",
        "title":"S T R 4 Y K E R",
        "link":"https://www.youtube.com/channel/UCeP0-OpzmdESIwNBW_gMvng",
        "verified":false,
        "thumbnail":"https://yt3.ggpht.com/xiCNuopQoh5olUjCLeFFb-g_j6RUXEldmm1OkMQ6Sdn9eujzn8kppmOdGKzN-sGL-3FQz64glg=s0?imgmax=0"
      }
    },
    {
      "views":136487,
      "uploaded":"1 year ago",
      "duration":214,
      "id":"ZKm_PUIM-24",
      "title":"Damon Empero ft. Veronica - Vacation [ King Step Release ] Tropical
House No Copyright",
      "link":"https://youtu.be/ZKm_PUIM-24",
      "thumbnail":"https://i.ytimg.com/vi/ZKm_PUIM-24/hqdefault.jpg",
      "channel":{
        "id":"UCa8saGNqaID8AdAw4nbvSIQ",
        "title":"AMC 095",
        "link":"https://www.youtube.com/channel/UCa8saGNqaID8AdAw4nbvSIQ",
        "verified":false,
        "thumbnail":"https://yt3.ggpht.com/ytc/AKedOLQipUMJvN34kQoGBiuwqaOABQdL637jwpuKsfCnDg=s0?imgmax=0"
      }
    },
    {
      "views":270604,
      "uploaded":"4 years ago",
      "duration":3740,
      "id":"JZT-HSsUToM",
      "title":"Damon Empero ft. Veronica - Vacation [Electro House] (1 Hour Loop)",
      "link":"https://youtu.be/JZT-HSsUToM",
      "thumbnail":"https://i.ytimg.com/vi/JZT-HSsUToM/hqdefault.jpg",
      "channel":{
        "id":"UC9yz68RvBi11fFt1GqQaAYQ",
        "title":"1HMNC - No Copyright Music",
        "link":"https://www.youtube.com/channel/UC9yz68RvBi11fFt1GqQaAYQ",
        "verified":false,
        "thumbnail":"https://yt3.ggpht.com/ytc/AKedOLSS9Vwl80WOTOlu4V2gCRbBpwuhRbOp6_iNs6JMPQ=s0?imgmax=0"
      }
    },
    {
      "views":23250,
      "uploaded":"2 years ago",
      "duration":39970,
      "id":"0QoXCvMBpTI",
      "title":"Damon Empero ft. Timmy Commerford - Lost [ Outertone Release ] | Electro House | (10+1 hour)",
      "link":"https://youtu.be/0QoXCvMBpTI",
      "thumbnail":"https://i.ytimg.com/vi/0QoXCvMBpTI/hqdefault.jpg",
      "channel":{
        "id":"UCFQHjckcODKQHHZnuB910vA",
        "title":"Anyone Wil",
        "link":"https://www.youtube.com/channel/UCFQHjckcODKQHHZnuB910vA",
        "verified":false,
        "thumbnail":"https://yt3.ggpht.com/ytc/AKedOLQHg0kYb4OuGsy0Hp7IIlap31ZLsM1g0tQqPgVBjw=s0?imgmax=0"
      }
    },
    {
      "views":158719,
      "uploaded":"3 years ago",
      "duration":189,
      "id":"epMM_jo-CyI",
      "title":"Nightcore - Vacation 「Damon Empero ft. Veronica」",
      "link":"https://youtu.be/epMM_jo-CyI",
      "thumbnail":"https://i.ytimg.com/vi/epMM_jo-CyI/hqdefault.jpg",
      "channel":{
        "id":"UCPfk_NUEPy_UduVocZ1l9Dw",
        "title":"Kirisaki",
        "link":"https://www.youtube.com/channel/UCPfk_NUEPy_UduVocZ1l9Dw",
        "verified":false,
        "thumbnail":"https://yt3.ggpht.com/ytc/AKedOLS8b7CvCps0JbHUwlD98QtYqCq9wvXGuCaqg3Xe=s0?imgmax=0"
      }
    },
    {
      "views":349163,
      "uploaded":"5 years ago",
      "duration":195,
      "id":"ZJiAtRmNg6c",
      "title":"Damon Empero - Eternal Summer | Electro House | | No Copyright |",
      "link":"https://youtu.be/ZJiAtRmNg6c",
      "thumbnail":"https://i.ytimg.com/vi/ZJiAtRmNg6c/hqdefault.jpg",
      "channel":{
        "id":"UCsGztxjStsz2AQaZYxVpXdA",
        "title":"Damon Empero",
        "link":"https://www.youtube.com/channel/UCsGztxjStsz2AQaZYxVpXdA",
        "verified":true,
        "thumbnail":"https://yt3.ggpht.com/ytc/AKedOLRiX57eLG-f-2gHBnGuRwQ5SxasooekggbDTEWAqg=s0?imgmax=0"
      }
    },
    {
      "views":19258991,
      "uploaded":"3 months ago",
      "duration":245,
      "id":"_n2fCJad7Dg",
      "title":"DJ Sakit Sekali Everybody Damon Vacation Tik Tok Remix Terbaru 2021 (DJ Cantik Remix)",
      "link":"https://youtu.be/_n2fCJad7Dg",
      "thumbnail":"https://i.ytimg.com/vi/_n2fCJad7Dg/hqdefault.jpg",
      "channel":{
        "id":"UCoOYmfwfkfDRyRviumtVglA",
        "title":"DJCantik",
        "link":"https://www.youtube.com/channel/UCoOYmfwfkfDRyRviumtVglA",
        "verified":false,
        "thumbnail":"https://yt3.ggpht.com/ytc/AKedOLTolGe9D53zsMSYMlZirSvzV21Vw3tmMopR8S-Ncw=s0?imgmax=0"
      }
    },
    {
      "views":723,
      "uploaded":"21 hours ago",
      "duration":647,
      "id":"PSf6sRAiBW8",
      "title":"PULAU DANA TELAH KEMBALI SETALAH DITERPA BADAI SEROJA",
      "link":"https://youtu.be/PSf6sRAiBW8",
      "thumbnail":"https://i.ytimg.com/vi/PSf6sRAiBW8/hqdefault.jpg",
      "channel":{
        "id":"UCNWSP9f-BIy9JNZyP7jWauw",
        "title":"MEX CHANNEL",
        "link":"https://www.youtube.com/channel/UCNWSP9f-BIy9JNZyP7jWauw",
        "verified":false,
        "thumbnail":"https://yt3.ggpht.com/9CPnNfgmtrFAj-KtFDWs9uq2jcImIPUT0nfP-hgolpS1Zu7GaibQKs6iX5Z_qPCS-24TPi6eZaU=s0?imgmax=0"
      }
    },
    {
      "views":8044,
      "uploaded":"12 hours ago",
      "duration":697,
      "id":"hoYug_kSKK0",
      "title":"HYBRID BUILD NATAN IS THE BEST WAY TO GO? | AkoBida Gameplay - MLBB",
      "link":"https://youtu.be/hoYug_kSKK0",
      "thumbnail":"https://i.ytimg.com/vi/hoYug_kSKK0/hqdefault.jpg",
      "channel":{
        "id":"UCCmWdfVQspVU-8sHKr_SOJw",
        "title":"AkoBida",
        "link":"https://www.youtube.com/channel/UCCmWdfVQspVU-8sHKr_SOJw",
        "verified":false,
        "thumbnail":"https://yt3.ggpht.com/ytc/AKedOLQ9HZuuSLCDyJTXJZX3FcXLULuBDDvLK9FbsyMkeQ=s0?imgmax=0"
      }
    },
    {
      "views":497549,
      "uploaded":"4 years ago",
      "duration":207,
      "id":"M48uhVXIu2A",
      "title":"Damon Empero - I Promise  | Electro House | | No Copyright |",
      "link":"https://youtu.be/M48uhVXIu2A",
      "thumbnail":"https://i.ytimg.com/vi/M48uhVXIu2A/hqdefault.jpg",
      "channel":{
        "id":"UCsGztxjStsz2AQaZYxVpXdA",
        "title":"Damon Empero",
        "link":"https://www.youtube.com/channel/UCsGztxjStsz2AQaZYxVpXdA",
        "verified":true,
        "thumbnail":"https://yt3.ggpht.com/ytc/AKedOLRiX57eLG-f-2gHBnGuRwQ5SxasooekggbDTEWAqg=s0?imgmax=0"
      }
    },
    {
      "views":256220,
      "uploaded":"3 years ago",
      "duration":224,
      "id":"UQPyyT4Lijc",
      "title":"Damon Empero ft.Veronica- Vacation [ King Step Release ] NCS✔️",
      "link":"https://youtu.be/UQPyyT4Lijc",
      "thumbnail":"https://i.ytim
g.com/vi/UQPyyT4Lijc/hqdefault.jpg",
      "channel":{
        "id":"UCTDQbg__umbmgMTArn1TRpA",
        "title":"Bảnh VN",
        "link":"https://www.youtube.com/channel/UCTDQbg__umbmgMTArn1TRpA",
        "verified":false,
        "thumbnail":"https://yt3.ggpht.com/4AVKo9gflvKzWfE9j4n8YcTE57FQyMj7IIvxuLNjBxUjjUNka6ZMWAH9Q-psVgj8P77BTUET=s0?imgmax=0"
      }
    }
  ],
  "streams":[
    {
      "watching":52,
      "id":"wDNRDX8_RMA",
      "title":"�LIVE (JOKI) OPEN BO , OPEN JOKI RANK - LIVE MOBILE
LEGEND",
      "link":"https://youtu.be/wDNRDX8_RMA",
      "thumbnail":"https://i.ytimg.com/vi/wDNRDX8_RMA/hqdefault.jpg",
      "channel":{
        "id":"UCGACSYsZujrP9gIxdq2LAww",
        "title":"Mazel Gaming",
        "link":"https://www.youtube.com/channel/UCGACSYsZujrP9gIxdq2LAww",
        "verified":false,
        "thumbnail":"https://yt3.ggpht.com/ytc/AKedOLQqwrB9AXcIBdI4Wye0dIWFVjpfena4yEksavOa=s0?imgmax=0"
      }
    }
  ],
  "playlists":[
    
  ],
  "channels":[
    {
      "id":"UCsGztxjStsz2AQaZYxVpXdA",
      "title":"Damon Empero",
      "thumbnail":"https://yt3.ggpht.com/ytc/AKedOLRiX57eLG-f-2gHBnGuRwQ5SxasooekggbDTEWAqg=s0?imgmax=0",
      "description":"Damon Empero - Youtube Music Channel EDM Music I'm Damon Empero, a 25 year old music producer from Croatia. I hope you\\xa0...",
      "link":"https://youtube.com/channel/UCsGztxjStsz2AQaZYxVpXdA",
      "verified":true,
      "subsCount":159000,
      "videosCount":0,
      "subs":"159K"
    }
  ]
}
```