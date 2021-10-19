from requests import get,post
from flask import Flask,render_template
import json,re

def vtt(srt):
	r = get(srt).text
	vtt = ["WEBVTT\n\n"]
	for i in r.split("\n"):
		if "-->" in i:
			vtt.append(i.replace(",","."))
		else:
			vtt.append(i)
	with open("static/sub.vtt","w") as f:
		f.write("\n".join(vtt))
	return "/static/sub.vtt"
def srt(url):
  r = get(url).content
  with open("static/sub.srt","wb") as f:
    f.write(r)
  return "/static/sub.srt"
def layarkacaxxi_org(url):
	data= {"r":url,"d":"layarkacaxxi.org"}
	id  = url.split("/")[-1]
	u = "https://layarkacaxxi.org/api/source/"+id
	r = post(u,data=data)
	jsn = json.loads(r.text)["data"][0]["file"]
	print(jsn)
def bioskopkeren_network():
	url = "https://bioskopkeren.network/nonton-drama-its-okay-to-not-be-okay-2020-subtitle-indonesia/2/"
	r = get(url).text
	print(r)
def layarkaca21(url):
	head = {'Host': '', 'Connection': 'keep-alive', 'Content-Length': '18', 'Accept': '*/*', 'X-Requested-With': 'XMLHttpRequest', 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8', 'Origin': '', 'Referer': '', 'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7', 'User-Agent': 'Mozilla/5.0 (Linux; Android 9; Redmi Note 5A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Mobile Safari/537.36'}
	base = re.search(r'(.*?\/\/\d+\.\d+\.\d+\.\d+)\/(.*?)\/',url)
	domain = base.group(1)
	slug = base.group(2)
	head.update({"Host":domain.replace("http://","").replace("https://",""),"Referer":url,"Origin":domain})
	film_id = post(domain+"/ajax/movie.php",data={"slug":slug},headers=head).text
	id = re.search(r'href\=\"(.*?\/\/.*?)\/v\/(.*?)\"',film_id)
	post_url = id.group(1)
	id = id.group(2)
	r = post(post_url+"/api/source/"+id,data={"r":domain+"/","d":post_url.replace("https://","").replace("http://","")}).json()
	film = r["data"][1]["file"]
	print(film)
def filmbioskop21(url):
	r = get(url).text
	print(r)
	d = re.search(r"film\_popup\(\'(.*?)\/v\/(.*?)\'\,",r)
	post_url = d.group(1)
	id = d.group(2)
	film_data = post(post_url+"/api/source/"+id,data={"r":url.split("movie")[0],"d":post_url.replace("https://","").replace("http://","")}).json()
	film = film_data["data"][0]["file"]
	print(film)
def bioskopkeren_life(url):
	app = Flask(__name__)
	r = get(url).text
	id = re.search(r'main\.php\?id\=(.*?)\"',r).group(1)
	film_data  = post("https://subtitle.bioskopkeren.pro/bk1.php",data={"id":id,"image":"","type":"mp4"}).json()
	if film_data["drivestatus"] == "alive":
		film = film_data["src"][0]["file"]
		subt = film_data["sub"]
		type = "video/mp4"
		mp4 = True
	else:
		film_data  = post("https://subtitle.bioskopkeren.pro/bk1.php",data={"id":id,"image":"","type":"hls"}).json()
		u = film_data["src"].split("subvtt=")
		film = u[0].replace("?","")
		subt = u[1].split("&")[0]
		type = "video/mp4"
		mp4 = False
	sub = vtt(subt)
	print(film)
	
	@app.route("/")
	def index():
		return render_template("bioskop.html",film=film,tipe=type,mp4=mp4,sub=sub)
	app.run(debug=True)
bioskopkeren_life("https://bioskopkeren.life/nonton-drama-its-okay-to-not-be-okay-2020-subtitle-indonesia/7/")
