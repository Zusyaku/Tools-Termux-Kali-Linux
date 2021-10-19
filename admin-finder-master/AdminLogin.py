#!/system/bin/python

import time, os, sys, time, random, socket, subprocess, httplib

def Logo():
	run()
	subprocess.call("toilet -f standard -F gay TheSploit",shell=True)



def run():
	if sys.platform == "linux" or sys.platform == "linux2":
		subprocess.call("clear",shell=True)
	else:
		subprocess.call("cls",Shell=True)

# Set Warna ######

A = '\033[0m' #putih
B = '\033[37m' #cyan
C = '\033[35m' #ungu or purple
D = '\033[34m' #Biru or blue
E = '\033[36m' #hijau muda
F = '\033[33m' #orange in zsh or yellow in bash
G = '\033[31m' #merah or red
I = '\033[32m' #hijau or green

# Restart ##############################
def restart_program():
   python = sys.executable
   os.execl(python, python, * sys.argv)
   curdir = os.getcwd()
########################################

def mengetik(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(random.random() * 0.1) 
angka = 0
while(angka<1):
    run()
    mengetik(D+'\n  SCAN ADMIN LOGIN WEBSITE')
    mengetik(C+"  By: TheSploit")
    mengetik(G+"  Team: Solo No Team")
    mengetik(I+"  Thanks To: Anda Semua yang Menggunakannya")
    mengetik(I+"  Website Tanpa http:// !!")

    angka+=1
    time.sleep(1)


site00 = raw_input("Masukan Website :")
site = site00.replace("http://","").rsplit("/",1)[0] 
site = site.lower()

admin_path = ['admin/login/php/login.php','admin/filemanager/login','admin/login/cpanel/','admin/cpanel/login/','admin/login','admin-login','connect-admin-login','admin/login.asp','admin/login.html','admin-login','admin/login.php','admin/login.do','admin/login.cfm','Admin/Login.aspx','Admin/Login.php','elusive-admin-login-button-on-scrolling-pages','Admin/Login.aspx','admin-login','programs/continuing-education/mot/mot-admin-login','admin1.php','admin1.html','admin2.php','admin2.html','yonetim.php','yonetim.html','yonetici.php','yonetici.html','ccms/','ccms','login.php','ccms/index.php','maintenance/','webmaster/','adm/','configuration/','configure/','websvn/','admin/','admin/account.php','admin/account.html','admin/index.php','admin/index.html','admin/login.php','admin/login.html','admin/home.php','admin/controlpanel.html','admin/controlpanel.php','admin.php','admin.html','admin/cp.php','admin/cp.html','cp.php','cp.html','administrator/','administrator/index.html','administrator/index.php','administrator/login.html','administrator/login.php','administrator/account.html','administrator/account.php','administrator.php','administrator.html','login.php','login.html','modelsearch/login.php','moderator.php','moderator.html','moderator/login.php','moderator/login.html','moderator/admin.php','moderator/admin.html','moderator/','account.php','account.html','controlpanel/','controlpanel.php','controlpanel.html','admincontrol.php','admincontrol.html','adminpanel.php','adminpanel.html','admin1.asp','admin2.asp','yonetim.asp','yonetici.asp','admin/account.asp','admin/index.asp','admin/login.asp','admin/home.asp','admin/controlpanel.asp','admin.asp','admin/cp.asp','cp.asp','administrator/index.asp','administrator/login.asp','administrator/account.asp','administrator.asp','login.asp','modelsearch/login.asp','moderator.asp','moderator/login.asp','moderator/admin.asp','account.asp','controlpanel.asp','admincontrol.asp','adminpanel.asp','fileadmin/','fileadmin.php','fileadmin.asp','fileadmin.html','administration/','administration.php','administration.html','sysadmin.php','sysadmin.html','phpmyadmin/','myadmin/','sysadmin.asp','sysadmin/','ur-admin.asp','ur-admin.php','ur-admin.html','ur-admin/','Server.php','Server.html','Server.asp','Server/','wp-admin/','administr8.php','administr8.html','administr8/','administr8.asp','webadmin/','webadmin.php','webadmin.asp','webadmin.html','administratie/','admins/','admins.php','admins.asp','admins.html','administrivia/','Database_Administration/','WebAdmin/','useradmin/','sysadmins/','admin1/','system-administration/','administrators/','pgadmin/','directadmin/','staradmin/','ServerAdministrator/','SysAdmin/','administer/','LiveUser_Admin/','sys-admin/','typo3/','panel/','cpanel/','cPanel/','cpanel_file/','platz_login/','rcLogin/','blogindex/','formslogin/','autologin/','support_login/','meta_login/','manuallogin/','simpleLogin/','loginflat/','utility_login/','showlogin/','memlogin/','members/','login-redirect/','sub-login/','wp-login/','login1/','dir-login/','login_db/','xlogin/','smblogin/','customer_login/','UserLogin/','login-us/','acct_login/','admin_area/','bigadmin/','project-admins/','phppgadmin/','pureadmin/','sql-admin/','radmind/','openvpnadmin/','wizmysqladmin/','vadmind/','ezsqliteadmin/','hpwebjetadmin/','newsadmin/','adminpro/','Lotus_Domino_Admin/','bbadmin/','vmailadmin/','Indy_admin/','ccp14admin/','irc-macadmin/','banneradmin/','sshadmin/','phpldapadmin/','macadmin/','administratoraccounts/','admin4_account/','admin4_colon/','radmind-1/','Super-Admin/','AdminTools/','cmsadmin/','SysAdmin2/','globes_admin/','cadmins/','phpSQLiteAdmin/','navSiteAdmin/','server_admin_small/','logo_sysadmin/','server/','database_administration/','power_user/','system_administration/','ss_vms_admin_sm/','adminarea/','bb-admin/','adminLogin/','panel-administracion/','instadmin/','memberadmin/','administratorlogin/','admin/admin.php','admin_area/admin.php','admin_area/login.php','siteadmin/login.php','siteadmin/index.php','siteadmin/login.html','admin/admin.html','admin_area/index.php','bb-admin/index.php','bb-admin/login.php','bb-admin/admin.php','admin_area/login.html','admin_area/index.html','admincp/index.asp','admincp/login.asp','admincp/index.html','webadmin/index.html','webadmin/admin.html','webadmin/login.html','admin/admin_login.html','admin_login.html','panel-administracion/login.html','nsw/admin/login.php','webadmin/login.php','admin/admin_login.php','admin_login.php','admin_area/admin.html','pages/admin/admin-login.php','admin/admin-login.php','admin-login.php','bb-admin/index.html','bb-admin/login.html','bb-admin/admin.html','admin/home.html','pages/admin/admin-login.html','admin/admin-login.html','admin-login.html','admin/adminLogin.html','adminLogin.html','home.html','rcjakar/admin/login.php','adminarea/index.html','adminarea/admin.html','webadmin/index.php','webadmin/admin.php','user.html','modelsearch/login.html','adminarea/login.html','panel-administracion/index.html','panel-administracion/admin.html','modelsearch/index.html','modelsearch/admin.html','admincontrol/login.html','adm/index.html','adm.html','user.php','panel-administracion/login.php','wp-login.php','adminLogin.php','admin/adminLogin.php','home.php','adminarea/index.php','adminarea/admin.php','adminarea/login.php','panel-administracion/index.php','panel-administracion/admin.php','modelsearch/index.php','modelsearch/admin.php','admincontrol/login.php','adm/admloginuser.php','admloginuser.php','admin2/login.php','admin2/index.php','adm/index.php','adm.php','affiliate.php','adm_auth.php','memberadmin.php','administratorlogin.php','admin/admin.asp','admin_area/admin.asp','admin_area/login.asp','admin_area/index.asp','bb-admin/index.asp','bb-admin/login.asp','bb-admin/admin.asp','pages/admin/admin-login.asp','admin/admin-login.asp','admin-login.asp','user.asp','webadmin/index.asp','webadmin/admin.asp','webadmin/login.asp','admin/admin_login.asp','admin_login.asp','panel-administracion/login.asp','adminLogin.asp','admin/adminLogin.asp','home.asp','adminarea/index.asp','adminarea/admin.asp','adminarea/login.asp','panel-administracion/index.asp','panel-administracion/admin.asp','modelsearch/index.asp','modelsearch/admin.asp','admincontrol/login.asp','adm/admloginuser.asp','admloginuser.asp','admin2/login.asp','admin2/index.asp','adm/index.asp','adm.asp','affiliate.asp','adm_auth.asp','memberadmin.asp','administratorlogin.asp','siteadmin/login.asp','siteadmin/index.asp','ADMIN/','paneldecontrol/','login/','cms/','panel.php','admin/login.php','login.php','adm.php','administracion.php','administrator/','admon/','ADMON/','administrador/','ADMIN/login.php','panelc/','ADMIN/login.html','admin./','adm./','admincp./','admcp./','cp./','modcp./','moderatorcp./','adminare./','admins./','cpanel./','controlpanel./','redaktor','@webadmin','redaktorweb','adm','rehasia','rehasiaweb']

print

try:
	for admin in admin_path:
		admin = admin.replace("\n","")
		admin = "/" + admin
		connection = httplib.HTTPConnection(site)
		connection.request("GET",admin)
		response = connection.getresponse()
		print "%s %s %s" % (admin, response.status, response.reason)
except(KeyboardInterrupt,SystemExit):
		raise
except:
		pass