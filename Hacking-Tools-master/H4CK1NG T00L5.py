import os, random, time, socket, sys, requests, json

Colors = ['\033[31m', '\033[32m', '\033[33m', '\033[34m', '\033[35m', '\033[36m', '\033[37m', '\033[39m']
r = '\033[31m'
g = '\033[32m'
y = '\033[33m'
b = '\033[34m'
m = '\033[35m'
c = '\033[36m'
w = '\033[37m'
def Print_Logo():
    Logo = '''

         ____  ____  _    _      ______  ___  ____    __    ____  _____   ______   
        |_   ||   _|| |  | |   .' ___  ||_  ||_  _|  /  |  |_   \|_   _|.' ___  |  
          | |__| |  | |__| |_ / .'   \_|  | |_/ /    `| |    |   \ | | / .'   \_|  
          |  __  |  |____   _|| |         |  __'.     | |    | |\ \| | | |   ____  
         _| |  | |_     _| |_ \ `.___.'\ _| |  \ \_  _| |_  _| |_\   |_\ `.___]  | 
        |____||____|   |_____| `.____ .'|____||____||_____||_____|\____|`._____.'  
                               Coded By .::Shayan::.                                       
                    _________    ____      ____   _____     _______   
                    |  _   _  | .'    '.  .'    '.|_   _|   |  _____|  
                    |_/ | | \_||  .--.  ||  .--.  | | |     | |____    
                        | |    | |    | || |    | | | |   _ '_.____''. 
                       _| |_   |  `--'  ||  `--'  |_| |__/ || \____) | 
                      |_____|   '.____.'  '.____.'|________| \______.' 

                                  [*]Choose an option :

                        [1]Whois   | [2]Port Scanner | [3]Ping
                        [4]GeoIP   | [5]DNS Lookup   | [6]Admin Finder
                        [7]Headers | [8]Reverse IP   | [9]Cloudflare Bypasser
                                         [0]Exit
                           
                  
                  '''
    for Line in Logo.split('\n'):
        time.sleep(0.1)
        print(random.choice(Colors)+Line)
def Clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def Q():
    return random.choice(Colors)

def rmhttp(website):
    web = ''
    web = website.replace('http://','').replace('https://','').replace('www.','')
    web = web.split('/')[0]
    return web

def getip(website):
    ip = socket.gethostbyname(website)
    return ip

def whois():
    print('''{c1}Welcome To The Whois Part
{c2}Please Enter The Target IP Or Website Address'''.format(
    c1=Q(),
    c2=Q()))
    site = input(Q()+'=> ')
    print('\n\n')
    ip = getip(rmhttp(site))
    r = requests.get('http://api.hackertarget.com/whois/?q='+ip).text
    for line in r.split('\n'):
        print(Q()+line)
    input(Q()+'\n\nPress Enter Key To Continue . . .')
def port_scanner():
    print('''{c1}Welcome To The Port Scanner Part
{c2}Please Enter The Target IP Or Website Address'''.format(
    c1=Q(),
    c2=Q()))
    target = input(Q()+'=> ')
    print('\n\n')
    ip = getip(rmhttp(target))
    ports = [20,21,22,23,25,53,67,68,69,110,123,137,138,139,143,161,162,179,389,443,636,989,990,3389,80]
    for p in ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        res = s.connect_ex((ip,p))
        if res == 0:
            print(Q()+'[+]'+ip+':'+str(p)+' --> This Port Is Open!')
    input(Q()+'\n\nPress Enter Key To Continue . . .')
def ping():
    print('''{c1}Welcome To The Ping Part
{c2}Please Enter The Target IP Or Website Address'''.format(
    c1=Q(),
    c2=Q()))
    site = input(Q()+'=> ')
    ip = getip(rmhttp(site))
    r = requests.get('http://api.hackertarget.com/nping/?q='+ip).text
    print('\n\n')
    for Line in r.split('\n'):
        print(Q()+Line)
    input(Q()+'\n\nPress Enter Key To Continue . . .')

def geoip():
    print('''{c1}Welcome To The GeoIP Part
{c2}Please Enter The Target IP Or Website Address'''.format(
    c1=Q(),
    c2=Q()))
    site = input(Q()+'=> ')
    ip = getip(rmhttp(site))
    r = requests.get('http://api.hackertarget.com/geoip/?q='+ip).text
    print('\n\n')
    for Line in r.split('\n'):
        print(Q()+Line)
    input(Q()+'\n\nPress Enter Key To Continue . . .')

def dns_loookup():
    print('''{c1}Welcome To The DNS LookUp Part
{c2}Please Enter The Target IP Or Website Address'''.format(
    c1=Q(),
    c2=Q()))
    site = input(Q()+'=> ')
    ip = rmhttp(site)
    r = requests.get('http://api.hackertarget.com/dnslookup/?q='+ip).text
    print('\n\n')
    for Line in r.split('\n'):
        print(Q()+Line)
    input(Q()+'\n\nPress Enter Key To Continue . . .')

def admin_page_finder():
    php = ['admin/','administrator/','admin1/','admin2/','admin3/','admin4/','admin5/','usuarios/','usuario/','administrator/','access_admin/','moderator/','webadmin/','adminarea/','bb-admin/','adminLogin/','admin_area/','panel-administracion/','instadmin/',
'memberadmin/','administratorlogin/','adm/','admin/account.php','admin/index.php','admin/login.php','admin/admin.php','admin/account.php',
'admin_area/admin.php','admin_area/login.php','siteadmin/login.php','siteadmin/index.php','siteadmin/login.html','admin/account.html','admin/index.html','admin/login.html','admin/admin.html',
'admin_area/index.php','bb-admin/index.php','bb-admin/login.php','bb-admin/admin.php','admin/home.php','admin_area/login.html','admin_area/index.html',
'admin/controlpanel.php','admin.php','admincp/index.asp','admincp/login.asp','admincp/index.html','admin/account.html','adminpanel.html','webadmin.html',
'webadmin/index.html','webadmin/admin.html','webadmin/login.html','admin/admin_login.html','admin_login.html','panel-administracion/login.html',
'admin/cp.php','cp.php','administrator/index.php','administrator/login.php','nsw/admin/login.php','webadmin/login.php','admin/admin_login.php','admin_login.php',
'administrator/account.php','administrator.php','admin_area/admin.html','pages/admin/admin-login.php','admin/admin-login.php','admin-login.php',
'bb-admin/index.html','bb-admin/login.html','acceso.php','bb-admin/admin.html','admin/home.html','login.php','modelsearch/login.php','moderator.php','moderator/login.php',
'moderator/admin.php','account.php','pages/admin/admin-login.html','admin/admin-login.html','admin-login.html','controlpanel.php','admincontrol.php',
'admin/adminLogin.html','adminLogin.html','admin/adminLogin.html','home.html','rcjakar/admin/login.php','adminarea/index.html','adminarea/admin.html',
'webadmin.php','webadmin/index.php','webadmin/admin.php','admin/controlpanel.html','admin.html','admin/cp.html','cp.html','adminpanel.php','moderator.html',
'administrator/index.html','administrator/login.html','user.html','administrator/account.html','administrator.html','login.html','modelsearch/login.html',
'moderator/login.html','adminarea/login.html','panel-administracion/index.html','panel-administracion/admin.html','modelsearch/index.html','modelsearch/admin.html',
'admincontrol/login.html','adm/index.html','adm.html','moderator/admin.html','user.php','account.html','controlpanel.html','admincontrol.html',
'panel-administracion/login.php','wp-login.php','adminLogin.php','admin/adminLogin.php','home.php','admin.php','adminarea/index.php',
'adminarea/admin.php','adminarea/login.php','panel-administracion/index.php','panel-administracion/admin.php','modelsearch/index.php',
'modelsearch/admin.php','admincontrol/login.php','adm/admloginuser.php','admloginuser.php','admin2.php','admin2/login.php','admin2/index.php','usuarios/login.php',
'adm/index.php','adm.php','affiliate.php','adm_auth.php','memberadmin.php','administratorlogin.php']
    asp = ['admin/','administrator/','admin1/','admin2/','admin3/','admin4/','admin5/','moderator/','webadmin/','adminarea/','bb-admin/','adminLogin/','admin_area/','panel-administracion/','instadmin/',
'memberadmin/','administratorlogin/','adm/','account.asp','admin/account.asp','admin/index.asp','admin/login.asp','admin/admin.asp',
'admin_area/admin.asp','admin_area/login.asp','admin/account.html','admin/index.html','admin/login.html','admin/admin.html',
'admin_area/admin.html','admin_area/login.html','admin_area/index.html','admin_area/index.asp','bb-admin/index.asp','bb-admin/login.asp','bb-admin/admin.asp',
'bb-admin/index.html','bb-admin/login.html','bb-admin/admin.html','admin/home.html','admin/controlpanel.html','admin.html','admin/cp.html','cp.html',
'administrator/index.html','administrator/login.html','administrator/account.html','administrator.html','login.html','modelsearch/login.html','moderator.html',
'moderator/login.html','moderator/admin.html','account.html','controlpanel.html','admincontrol.html','admin_login.html','panel-administracion/login.html',
'admin/home.asp','admin/controlpanel.asp','admin.asp','pages/admin/admin-login.asp','admin/admin-login.asp','admin-login.asp','admin/cp.asp','cp.asp',
'administrator/account.asp','administrator.asp','acceso.asp','login.asp','modelsearch/login.asp','moderator.asp','moderator/login.asp','administrator/login.asp',
'moderator/admin.asp','controlpanel.asp','admin/account.html','adminpanel.html','webadmin.html','pages/admin/admin-login.html','admin/admin-login.html',
'webadmin/index.html','webadmin/admin.html','webadmin/login.html','user.asp','user.html','admincp/index.asp','admincp/login.asp','admincp/index.html',
'admin/adminLogin.html','adminLogin.html','admin/adminLogin.html','home.html','adminarea/index.html','adminarea/admin.html','adminarea/login.html',
'panel-administracion/index.html','panel-administracion/admin.html','modelsearch/index.html','modelsearch/admin.html','admin/admin_login.html',
'admincontrol/login.html','adm/index.html','adm.html','admincontrol.asp','admin/account.asp','adminpanel.asp','webadmin.asp','webadmin/index.asp',
'webadmin/admin.asp','webadmin/login.asp','admin/admin_login.asp','admin_login.asp','panel-administracion/login.asp','adminLogin.asp',
'admin/adminLogin.asp','home.asp','admin.asp','adminarea/index.asp','adminarea/admin.asp','adminarea/login.asp','admin-login.html',
'panel-administracion/index.asp','panel-administracion/admin.asp','modelsearch/index.asp','modelsearch/admin.asp','administrator/index.asp',
'admincontrol/login.asp','adm/admloginuser.asp','admloginuser.asp','admin2.asp','admin2/login.asp','admin2/index.asp','adm/index.asp',
'adm.asp','affiliate.asp','adm_auth.asp','memberadmin.asp','administratorlogin.asp','siteadmin/login.asp','siteadmin/index.asp','siteadmin/login.html']
    print('''{c1}Welcome To The Admin Page Finder Part
{c2}[!]Website Programming Language :{c3}
  [1]PHP{c4}
  [2]ASP'''.format(
    c1=Q(),
    c2=Q(),
    c3=Q(),
    c4=Q()))
    num = input(Q()+'=> ')
    target = input(Q()+'Enter the Target Address\n'+Q()+'=> ')
    target = 'http://'+rmhttp(target).lower()+'/'
    print('\n\n')
    if num == '1' or num.upper() == 'PHP':
        for page in php:
            try:
                url = target+page
                req = requests.get(url)
                if req.status_code == 200:
                    print(Q()+url+Q()+'=> '+Q()+' Founded!')
            except Exception:
                pass
    elif num == '2' or num.upper() == 'ASP':
        for page in asp:
            try:
                url = target+page
                req = requests.get(url)
                if req.status_code == 200:
                    print(Q()+url+Q()+' => '+Q()+' Founded!')
            except Exception:
                pass
    input('\n\nPress Enter Key To Continue . . .')

def headers():
    print('''{c1}Welcome To The Get Response Headers Part
{c2}Please Enter The Target Website Address'''.format(
    c1=Q(),
    c2=Q()))
    site = input(Q()+'=> ')
    ip = rmhttp(site)
    r = requests.get('https://api.hackertarget.com/httpheaders/?q='+ip).text
    print('\n\n')
    for Line in r.split('\n'):
        print(Q()+Line)
    input(Q()+'\n\nPress Enter Key To Continue . . .')

def reverseip():
    print('''{c1}Welcome To The Reverse IP Part
{c2}Please Enter The Target Website Address'''.format(
    c1=Q(),
    c2=Q()))
    site = input(Q()+'=> ')
    ip = rmhttp(site)
    r = requests.post('https://domains.yougetsignal.com/domains.php',data={'remoteAddress':ip}).text
    print('\n\n')
    js = json.loads(r)
    for Val,Noth in js['domainArray']:
        print(Q()+Val)
    print(Q()+'Domains Count: '+Q()+js['domainCount'])
    input(Q()+'\n\nPress Enter Key To Continue . . .')

def cloudflare_bypasser():
    subdom = ['ftp', 'cpanel', 'webmail', 'localhost', 'local', 'mysql', 'forum', 'driect-connect', 'blog', 'vb', 'forums', 'home', 'direct', 'forums', 'mail', 'access', 'admin', 'administrator', 'email', 'downloads', 'ssh', 'owa', 'bbs', 'webmin', 'paralel', 'parallels', 'www0', 'www', 'www1', 'www2', 'www3', 'www4', 'www5', 'shop', 'api', 'blogs', 'test', 'mx1', 'cdn', 'mysql', 'mail1', 'secure', 'server', 'ns1', 'ns2', 'smtp', 'vpn', 'm', 'mail2', 'postal', 'support', 'web', 'dev']
    print('''{c1}Welcome To The Cloudflare Bypasser Part
{c2}Please Enter The Target Website Address'''.format(
    c1=Q(),
    c2=Q()))
    site = input(Q()+'=> ')
    site = rmhttp(site)
    print('\n\n')
    for sub in subdom:
        try:
            bypass = socket.gethostbyname(sub+'.'+site)
            print(Q()+'Cloudflare Bypassed ! '+Q()+'Real IP Address => '+Q()+bypass)
        except Exception:
            pass
    input(Q()+'\n\nPress Enter Key To Continue . . .')
while True:
    Clear()
    Print_Logo()
    op = input(Q()+'''┌─[H4CK1NG@T00L5]
└──╼ $ ''')
    if op == '1':
        Clear()
        whois()
    elif op == '2':
        Clear()
        port_scanner()
    elif op == '3':
        Clear()
        ping()
    elif op == '4':
        Clear()
        geoip()
    elif op == '5':
        Clear()
        dns_loookup()
    elif op == '6':
        Clear()
        admin_page_finder()
    elif op == '7':
        Clear()
        headers()
    elif op == '8':
        Clear()
        reverseip()
    elif op == '9':
        Clear()
        cloudflare_bypasser()
    elif op == '0':
        Clear()
        sys.exit()
    else:
        Clear()
        Print_Logo()