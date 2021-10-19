import requests as r, json, random, time
from bs4 import BeautifulSoup as par
from flask import Flask, jsonify, request
from flask_cors import CORS

def get_music(key):
	check = r.get("https://x2convert.com/ajax2/getFile.ashx?linkinfo=https://youtu.be/"+str(key.replace("https://youtu.be/",""))+"&lang=id&option=100&country=ID").json()
	if check["Status"] == "-1":
		return "not-valid"
	else:
		next = par(r.get(check["Message"]).text, "html.parser")
		url = next.find("a", {"class":"btn btn-lg btn-success"})["href"]
		return url

def get_video(key):
	kumpulkan = int(time.time())
	check = r.get("https://www.videovor.com/en/getlinks?url=https://youtu.be/"+key+"&r=0."+str(kumpulkan)+"&retry=false")
	if check.text == "invalidurl":
		return "not-valid"
	else:
		z = check.json()
		data = {
			"videoid": z["videoid"],
			"videourl": z["links"][0]["url"],
			"rurl": z["hdaudio"],
			"ext": z["links"][0]["ext"],
			"conv": z["links"][0]["conv"],
			"format": z["links"][0]["frmt"],
			"sourceurl": z["sourceurl"],
			"audiourl": z["hdaudio"],
			"st": z["srv"]
		}
		sat = r.post("https://www.videovor.com/en/prepare?r=0."+str(kumpulkan), data=data)
		dua = par(r.get("https://www.videovor.com/en/end?id="+z["videoid"]).text, "html.parser")
		link = dua.find("a", {"title":"DOWNLOAD"})["href"]
		return link

def get_details(teks):
	teks = teks.replace(" ","+")
	api = r.get("https://api.mp3download.to/v1/external/search/?query="+teks).text
	parse = json.loads(api)

	return [
		{
			"title": _["title"],
			"id": _["id"],
			"thumbnails": random.choice(_["thumbnails"]),
			"duration": _["duration"],
			"chanel": _["extra_data"]["channel_title"],
			"publish": _["extra_data"]["publishedAt"],
			"view": _["extra_data"]["viewCount"]
		} for _ in parse["data"]["items"]
	]

app = Flask(__name__)
CORS(app)
error = lambda teks: jsonify({
		"author": "rizkydev",
		"status": "error",
		"msg": teks
	})

@app.route("/")
def index():
	return "<h1>/download?id=id_yt&type={audio/video} untuk mengambil link lagu<br>/details?query=query, untuk mengambil detail semua lagu</h1>"

@app.route("/download", methods=["GET"])
def get_audio():
	try:
		id = request.args.get("id")
		type = request.args.get("type")
		if id == "":
			return error("parameter id harus diisi")

		if type == "":
			return error("parameter type harus diisi")
		elif type == "audio":
			typ = get_music
		elif type == "video":
			typ = get_video
		else:
			return error("type hanya audio dan video")

		try:
			oh = typ(id.replace("https://youtu.be/",""))
		except Exception as err:
			return error(str(err))
		if "not-valid" in oh:
			return error("id tidak valid")
		else:
			return jsonify({
				"author": "rizkydev",
				"status": "success",
				"msg": "berhasil mengambil link download",
				"download_url": oh
			})
	except Exception as ex:
		return error(str(ex))

@app.route("/details", methods=["GET"])
def details():
	try:
		query = request.args.get("query")
		if query == "":
			return error("parameter query harus diisi")
		rep = query.replace("+"," ")
		try:
			oh = get_details(rep)
		except Exception as err:
			return error(str(err))
		susun = [
				{
					"judul": OoO["title"],
					"id": OoO["id"],
					"thumbnail": OoO["thumbnails"],
					"durasi": OoO["duration"],
					"chanel_name": OoO["chanel"],
					"publish": OoO["publish"],
					"view": OoO["view"]
				} for OoO in oh
			]
		return jsonify({
			"author": "rizkydev",
			"status": "success",
			"msg": "berhasil mengambil data youtube",
			"data": susun
		})
	except Exception as ex:
		return error(str(ex))

if __name__ == "__main__":
	app.run(debug=True)
