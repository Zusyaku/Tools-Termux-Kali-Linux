package main

import (
    "fmt"
    "net/http"
    "strings"

    "github.com/fatih/color"
)

var admins = []string{"admin/login.html", "admin/login.htm", "admin/controlpanel.html", "admin/controlpanel.htm", "admin/adminLogin.html", "admin/adminLogin.htm", "admin.htm", "admin.html", "adminitem/", "adminitems/", "administrator/", "administrator/login", "administrator", "administration/", "administration", "adminLogin/", "adminlogin", "admin_area/admin", "admin_area/", "admin_area/login", "manager/", "superuser/", "superuser", "access/", "access", "sysadm/", "sysadm", "superman/", "supervisor/", "panel", "control/", "member/", "member", "members/", "user/", "user", "cp/", "uvpanel/", "manage/", "manage.", "management/", "signin/", "log-in/", "sign-in", "users/", "accounts/", "bb-admin/login", "bb-admin/admin", "bb-admin/admin.html", "administrator/account", "relogin.htm", "relogin.html", "check", "relogin", "blog/wp-login", "user/admin", "users/admin", "registration/", "processlogin", "checklogin", "checkuser", "checkadmin", "isadmin", "authenticate", "authentication", "auth", "authuser", "authadmin", "cp", "modelsearch/login", "moderator", "moderator/", "controlpanel/", "controlpanel", "admincontrol", "adminpanel", "fileadmin/", "fileadmin", "sysadmin", "admin1", "admin1.html", "admin1.htm", "admin2", "admin2.html", "yonetim", "yonetim.html", "yonetici", "yonetici.html", "phpmyadmin/", "myadmin/", "ur-admin", "ur-admin/", "Server", "Server/", "wp-admin/", "administr8", "administr8/", "webadmin/", "webadmin", "administratie/", "admins", "admins", "administrivia/", "Database_Administration/", "useradmin/", "sysadmins/", "sysadmins/", "admin1/", "system-administration", "administrators", "pgadmin", "directadmin/", "staradmin/", "ServerAdministrator", "SysAdmin", "administer/", "LiveUser_Admin/", "sys-admin/", "typo3/", "panel", "cpanel", "cpanel_file", "platz_login", "rcLogin/", "blogindex/", "formslogin/", "autologin", "manuallogin/", "simpleLogin/", "loginflat/", "utility_login/", "showlogin/", "memlogin/", "login-redirect/", "sub-login/", "wp-login/", "login1/", "dir-login", "login_db", "xlogin", "smblogin", "customer_login", "UserLogin", "login-us", "acct_login", "bigadmin", "project-admins/", "phppgadmin", "pureadmin", "sql-admin", "radmind", "openvpnadmin/", "wizmysqladmin", "vadmind/", "ezsqliteadmin", "hpwebjetadmin", "newsadmin/", "adminpro", "Lotus_Domino_Admin", "bbadmin", "vmailadmin", "Indy_admin/", "ccp14admin", "irc-macadmin", "banneradmin", "sshadmin", "phpldapadmin/", "macadmin/", "administratoraccounts", "admin4_account", "admin4_colon/", "radmind-1", "Super-Admin", "AdminTools", "cmsadmin", "SysAdmin2", "globes_admin", "cadmins", "phpSQLiteAdmin", "navSiteAdmin", "server_admin_small", "logo_sysadmin", "power_user", "system_administration", "ss_vms_admin_sm", "bb-admin", "panel-administracion", "instadmin", "memberadmin", "administratorlogin", "adm", "admin_login", "panel-administracion/login", "pages/admin/admin-login", "pages/admin", "acceso", "admincp/login", "admincp", "adminarea", "admincontrol", "affiliate", "adm_auth", "memberadmin", "administratorlogin", "modules/admin", "administrators", "siteadmin", "siteadmin", "adminsite", "kpanel", "vorod", "vorod", "vorud", "vorud", "adminpanel", "PSUser", "secure", "webmaster", "webmaster", "autologin", "userlogin", "admin_area", "cmsadmin", "security", "usr", "root", "secret", "admin/login", "admin/adminLogin", "moderator.php", "moderator.html", "moderator/login", "moderator/admin", "yonetici", "0admin/", "0manager/", "aadmin/", "cgi-bin/login", "login1", "login_admin", "login_admin", "login_out", "login_out", "login_user", "loginerror", "loginok", "loginsave", "loginsuper", "loginsuper", "login", "logout", "logout", "secrets", "super1", "super1", "super_index", "super_login", "superman", "superuser", "supervise", "supervise/Login", "super"}

var (
    domain   string
    protocol string
    Green    = color.New(color.FgGreen).Add(color.Bold)
    Red      = color.New(color.FgRed).Add(color.Bold)
    Magenta  = color.New(color.FgMagenta).Add(color.Bold)
)

func header1() {
    print("coded by")
    Magenta.Print(" >> ")
    Green.Println("nikait")
    print("telegram")
    Magenta.Print(" >> ")
    Green.Println("@aaanikit")
    fmt.Println("\n")
}

func header2() {
    Green.Println(strings.Repeat("-", 74))
    Green.Print("|   ")
    Magenta.Print(" status    ")
    Green.Print("|                          ")
    Magenta.Print("url")
    Green.Println("                            |")
    Green.Println(strings.Repeat("-", 74))
}

func main() {
    header1()
    Green.Print("enter domain >> ")
    fmt.Scan(&domain)
    Green.Println("choose the protocol:\nhttps - 1\nhttp - 2")
    Green.Print(">> ")
    fmt.Scan(&protocol)

    if protocol == "1" {
        protocol = "https://"
    } else {
        protocol = "http://"
    }

    header2()
    for _, i := range admins {
        resp, _ := http.Get(protocol + domain + "/" + i)
        if resp.StatusCode != 404 {
            Green.Print("      OK       |     ")
        } else {
            Red.Print("    failed     ")
            Green.Print("|     ")
        }
        fmt.Println(protocol + domain + "/" + i)
    }
    Green.Println(strings.Repeat("-", 74))
}
