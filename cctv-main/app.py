# Coded By Rizky | hekelpro
# Dont Change Name Author

from requests import *
from bs4 import BeautifulSoup as par
import re
from concurrent.futures import ThreadPoolExecutor
from flask import Flask, request, jsonify

url = []
lokasi = []
country = ['United States', 'Japan', 'Italy ', 'Korea ', 'France ', 'Germany ', 'Taiwan ', 'Russian Federation', 'United Kingdom', 'Netherlands ', 'Czech Republic', 'Turkey ', 'Austria ', 'Switzerland ', 'Spain ', 'Canada', 'Sweden', 'Israel ', 'Iran ', 'Poland ', 'India ', 'Norway ', 'Romania', 'Viet Nam', 'Belgium', 'Brazil ', 'Bulgaria ', 'Indonesia ', 'Denmark', 'Argentina', 'Mexico', 'Finland ', 'China ', 'Chile ', 'South Africa', 'Slovakia ', 'Hungary ', 'Ireland ', 'Egypt ', 'Thailand ', 'Ukraine ', 'Serbia ', 'Hong Kong', 'Greece ', 'Portugal ', 'Latvia ', 'Singapore ', 'Iceland ', 'Malaysia ', 'Colombia ', 'Tunisia ', 'Estonia ', 'Dominican Republic', 'Sloveania ', 'Ecuador ', 'Lithuania ', 'Palestinian ', 'New Zealand', 'Bangladeh ', 'Panama ', 'Moldova', 'Nicaragua ', 'Malta ', 'Trinidad And', 'Soudi Arabia', 'Croatia ', 'Cyprus ', 'Pakistan', 'United Arab', 'Kazakhstan ', 'Kuwait', 'Venezuela ', 'Georgia ', 'Montenegro ', 'El Salvador', 'Luxembourg ', 'Curacao ', 'Puerto Rico', 'Costa Rica', 'Belarus ', 'Albania ', 'Liechtenstein ', 'Bosnia And Herzegowina', 'Paraguay ', 'Philippines ', 'Faroe Islands', 'Guatemala ', 'Nepal ', 'Peru', 'Uruguay']
kode    = ['US', 'JP', 'IT', 'KR', 'FR', 'DE', 'TW', 'RU', 'GB', 'NL', 'CZ', 'TR', 'AT', 'CH', 'ES', 'CA', 'SE', 'IL', 'PL', 'IR', 'NO', 'RO', 'IN', 'VN', 'BE', 'BR', 'BG', 'ID', 'DK', 'AR', 'MX', 'FI', 'CN', 'CL', 'ZA', 'SK', 'HU', 'IE', 'EG', 'TH', 'UA', 'RS', 'HK', 'GR', 'PT', 'LV', 'SG', 'IS', 'MY', 'CO', 'TN', 'EE', 'DO', 'SI', 'EC', 'LT', 'PS', 'NZ', 'BD', 'PA', 'MD', 'NI', 'MT', 'IT', 'SA', 'HR', 'CY', 'PK', 'AE', 'KZ', 'KW', 'VE', 'GE', 'ME', 'SV', 'LU', 'CW', 'PR', 'CR', 'BY', 'AL', 'LI', 'BA', 'PY', 'PH', 'FO', 'GT', 'NP', 'PE', 'UY']

def multi(kode):
	sesi_page = par(get("http://www.insecam.org/en/bycountry/"+kode, headers={"User-Agent":"chrome"}).text, "html.parser").find("ul", class_="pagination").find("script")
	cari_page = re.search(", (\d+),",str(sesi_page)).group(1)

	#-> Hanya 20 Halaman Gak boleh Lebih
	if int(cari_page) > 21:
		jmlh = 20
	elif int(cari_page) < 21:
		jmlh = int(cari_page)

	for page in range(jmlh):
		cek = par(get("http://www.insecam.org/en/bycountry/"+kode+"/?page="+str(page+1), headers={"User-Agent":"chrome"}).text, "html.parser")
		for scr in cek.find_all("div", class_="row thumbnail-items"):
			cari_site = re.findall(r"http://\d+.\d+.\d+.\d+:\d+", str(scr))
			[url.append(site) for site in cari_site]
			for city in scr.find_all("div", class_="thumbnail-item__caption"):
				[lokasi.append(tempat.text) for tempat in city.find_all("p")]

app = Flask(__name__)
@app.route("/")
def index():
	try:
		coun = request.args.get("country")
		if coun == "":
			data = [
			{
				"negara":negara.strip(),
				"country":singkatan
			} for negara, singkatan in zip(country,kode)]
			return jsonify(
			{
				"status":"error",
				"parameter":"country",
				"example":data,
			})

		#-> Kehabisan Name Variable Bro
		ngontol = get("http://www.insecam.org/en/bycountry/"+coun.lower(), headers={"User-Agent":"chrome"}).text
		if "Page not found (404)" in ngontol:
			return jsonify({"status":"error","message":"Country Tidak Ada Didalam List Bro"})

		#-> Jika Lolos Dari Pemeriksaan
		with ThreadPoolExecutor(max_workers=5) as rizky:
			rizky.submit(multi,coun.lower())

		db = [
		{
			"url_page":link,
			"lokasi":tempat
		} for link, tempat in zip(url, lokasi)]
		return jsonify(
		{
			"status":"succes",
			"message":"berhasil mengambil data cctv wilayah",
			"data":db
		})
	except:
		data = [
		{
			"negara":negara.strip(),
			"country":singkatan
		} for negara, singkatan in zip(country,kode)]
		return jsonify(
		{
			"status":"error",
			"parameter":"country",
			"example":data,
		})

if __name__=="__main__":
	app.run(debug=True)
