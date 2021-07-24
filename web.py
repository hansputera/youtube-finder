import asyncio
from json import dumps
from flask import Flask, Response, request, jsonify
from scraper import search
from os import getenv

PORT = getenv("PORT") or 3000

asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy()) # set policy for asyncio
loop = asyncio.new_event_loop()
app = Flask("Just yt finder api")
app.config["JSONIFY_PRETTYPRINT_REGULAR"] = True # pretty json

@app.route("/")
def index():
    return Response("Hello world", 200)

@app.route("/search")
def search_title():
    q = request.args.get("query", None) or request.args.get("q", None) or request.args.get("title", None)
    filter_ = request.args.get("filter", None)

    if q == None:
        return Response("No query provided", 400)
    else:
        res = loop.run_until_complete(search(q, filter_))
        return jsonify(res)

app.run("0.0.0.0", PORT)