<?php
include 'class_view.php';
$banner = banner();
echo "\n\n";
$u = getUsername();
if(file_exists( __DIR__."/sesi/".$u.".json")){
    echo "[!] Saved cookie found! Use cookie mode.\n";
    $logvia = "cookie";
    $saved_cookie = __DIR__."/sesi/".$u.".json";
    $read_cookie = file_get_contents($saved_cookie);
    $json_cookie = json_decode($read_cookie);
    $login = login($json_cookie->csrftoken, $json_cookie->sessionid, "cookie");
} else {
    echo "[!] No cookie saved! Use normal mode.\n";
    $logvia = "normal";
    $p = getPassword();
    $login = login($u, $p);
}


echo "[?] Enter Username Target: ( Multiple use | without @ symbol ) : ";
$username_tar = trim(fgets(STDIN));
$pecah = explode("|", $username_tar);

echo "[?] Enter Sleep second(s) : ";
$sleep = trim(fgets(STDIN));

if ($login['status'] == 'success') {
    if($logvia == "normal"){
        echo "\n[*] Login as ".$login['username']." Success !\n\n";
        $data_login = array(
            'username' => $login['username'],
            'csrftoken'	=> $login['csrftoken'],
            'sessionid'	=> $login['sessionid']
        );
    } else {
        echo "[!] Checking session.\n";
        $cekSesi = cekSesi($u, $login['csrftoken'], $login['sessionid']);
        if($cekSesi == "live"){
            echo "\n[*] Login as ".$u." Success !\n\n";
            $data_login = array(
                'username' => $u,
                'csrftoken'	=> $login['csrftoken'],
                'sessionid'	=> $login['sessionid']
            );
        } else {
            echo "\n[*] Login as ".$u." Failed, session die !\n";
            echo "\n[*] Relogin please !\n\n";
            unlink($saved_cookie);
            exit();
        }
    }
    foreach ($pecah as $username_target) {
        $berhasil = 0;
            $search_target = findProfile($username_target, $data_login);
            if ($search_target['status'] == 'success') {
                echo '[*] Target: '.$search_target['username'].' | Name: '.$search_target['fullname'].'  | Followers: '.$search_target['followers'].' | Following: '.$search_target['following'].' | Post: '.$search_target['post'].' [*] '.PHP_EOL.PHP_EOL;
                baca:
                $fetch_target = get_stories_target($login, $search_target['id'], $endCursor);
                foreach ($fetch_target['data'] as $id) {
                    $ids = $id['node']['id'];
                    $seen = $id['node']['reel']['seen'];
                    $get_id = get_id($ids, $login);
                    foreach ($get_id as $id_ig) {
                        foreach ($id_ig['items'] as $baca) {
                            //echo "id :".$baca['id']." owner: ".$baca['owner']['id']." time:".$baca['taken_at_timestamp']."\n";
                            echo "[".date("d-m-Y").'-'.date("h:i:s")."] View Story -> [ @".$baca['owner']['username']." ] -> ".$baca['id']."-> ";
                            $view = view_story($login, $baca['id'], $baca['owner']['id'], $baca['owner']['id'], $baca['taken_at_timestamp']);
                            if (preg_match('/{"status": "ok"}/', $view)) {
                                echo "\033[1;32mSuccess\033[0m\n";
                                $berhasil++;
                            } else {
                                echo "\033[1;31mPlease wait a few minutes before you try again\033[0m\n";
                            }
                            sleep($sleep);
                        }
                    }
                }
            
                $endCursor = $fetch_target['ec'];
                if (!empty($endCursor)) {
                    sleep(rand(5, 20));
                    echo "[*] Bypass Limit Page\n";
                    goto baca;
                } else {
                    echo "[+] Success View ".$berhasil." Stories @".$username_target."\n";
                    continue;
                }
            }else {
                echo "[*] Oops target private / Error get target\n";
                continue;
            }
    }
} else {
    echo "[*] Failed Login !\n\n";
}
