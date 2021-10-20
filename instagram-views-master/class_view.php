<?php
error_reporting(0);
date_default_timezone_set('Asia/Jakarta');
header('Content-Type: text/html; charset=utf-8');
function getStr($string,$start,$end){
    $str = explode($start,$string);
    $str = explode($end,$str[1]);
    return $str[0];
}
function curl($url, $data = 0, $header = 0, $cookie = 0) {
    $ch = curl_init();
    curl_setopt($ch, CURLOPT_URL, $url);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
    curl_setopt($ch, CURLOPT_FOLLOWLOCATION, 1);
    curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, 0);
    curl_setopt($ch, CURLOPT_SSL_VERIFYHOST, 0);
    // curl_setopt($ch, CURLOPT_VERBOSE, 1);
    curl_setopt($ch, CURLOPT_HEADER, 1);
    if($header) {
        curl_setopt($ch, CURLOPT_HTTPHEADER, $header);
        curl_setopt($ch, CURLOPT_ENCODING, "gzip");
    }
    if($data) {
        curl_setopt($ch, CURLOPT_POST, 1);
        curl_setopt($ch, CURLOPT_POSTFIELDS, $data);
    }
    if($cookie) {
        curl_setopt($ch, CURLOPT_COOKIEJAR, $cookie);
        curl_setopt($ch, CURLOPT_COOKIEFILE, $cookie);
    }
    $x = curl_exec($ch);
    curl_close($ch);
    return $x;
}

function curlNoHeader($url, $data = 0, $header = 0, $cookie = 0) {
    $ch = curl_init();
    curl_setopt($ch, CURLOPT_URL, $url);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
    curl_setopt($ch, CURLOPT_FOLLOWLOCATION, 1);
    curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, 0);
    curl_setopt($ch, CURLOPT_SSL_VERIFYHOST, 0);

    curl_setopt($ch, CURLOPT_HEADER, 0);
    if($header) {
        curl_setopt($ch, CURLOPT_HTTPHEADER, $header);
        curl_setopt($ch, CURLOPT_ENCODING, "gzip");
    }
    if($data) {
        curl_setopt($ch, CURLOPT_POST, 1);
        curl_setopt($ch, CURLOPT_POSTFIELDS, $data);
    }
    if($cookie) {
        curl_setopt($ch, CURLOPT_COOKIEJAR, $cookie);
        curl_setopt($ch, CURLOPT_COOKIEFILE, $cookie);
    }
    $x = curl_exec($ch);
    curl_close($ch);
    return $x;
}

function cekSesi($user, $csrf, $session){
    $url_view = 'https://www.instagram.com/'.$user.'/?__a=1';
    $header = array(
        'User-Agent: Mozilla/5.0 (iPhone; CPU iPhone OS 11_0_1 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A402 Safari/604.1',
        'X-CSRFToken: '.$csrf,
        'Cookie: csrftoken='.$csrf.'; sessionid='.$session
    );
    $curl = curlNoHeader($url_view, false, $header);
    $json = json_decode($curl);
    //if(is_null($json->graphql->user->restricted_by_viewer)){
    if($json->graphql->user->restricted_by_viewer === false){
        return 'live';
    } else {
        return 'die';
    }
}

function getPassword($prompt = "[?] Enter Password: ") {

    echo $prompt;
    $password = trim(fgets(STDIN));

    return $password;

}

function getUsername($prompt = "[?] Enter Username: ") {
    echo $prompt;

    $username = trim(fgets(STDIN));

    return $username;
}
function fetchCurlCookies($source) {
    preg_match_all('/^Set-Cookie:\s*([^;]*)/mi', $source, $matches);
    $cookies = array();
    foreach($matches[1] as $item) {
        parse_str($item, $cookie);
        $cookies = array_merge($cookies, $cookie);
    }
    return $cookies;
}


function findProfile($username, $session = 0)
{
    $url = 'https://instagram.com/'.$username;
    if ($session != 0) {
        $header = array();
        $header[] = 'Cookie: sessionid='.$session['sessionid'].';';
        $get = curl($url,0,$header);

    }else{

        $get = curl($url);
    }
    if (strpos($get, 'The link you followed may be broken, or the page may have been removed.')) {

        $data = array(
            'status' => 'error',
            'details' => 'user not found'
        );

    }else{

        $data_ouput = getStr($get, '<script type="text/javascript">window._sharedData = ', ';</script>');
        $data_array = json_decode($data_ouput);
        $result = $data_array->entry_data->ProfilePage['0']->graphql->user;
        if (empty($result->edge_owner_to_timeline_media->edges) && $result->edge_owner_to_timeline_media->count >= 1) {

            $data = array(
                'status' => 'error',
                'details' => 'account private'
            );

        }else{

            $result = $data_array->entry_data->ProfilePage['0']->graphql->user;
            // $vid = ($result->is_video == 1) ? "yes" : "no" ;
            $is_follow = ($result->followed_by_viewer) ? 'true' : 'false' ;
            $is_private = ($result->is_private) ? 'true' : 'false' ;
            $is_verified = ($result->is_verified) ? 'true' : 'false' ;
            $is_polbek = ($result->follows_viewer) ? 'true' : 'false' ;

            $data = array(
                'status' => 'success',
                'username' => $username,
                'fullname' => $result->full_name,
                'followers' => $result->edge_followed_by->count,
                'following' => $result->edge_follow->count,
                'is_follow' => $is_follow,
                'is_private' => $is_private,
                'is_polbek' => $is_polbek,
                'id' => $result->id,
                'is_verif' => $is_verified,
                'post' => $result->edge_owner_to_timeline_media->count,
            );

        }
    }

    return $data;
}
function login($username, $password, $type = false)
{
    if($type == "cookie"){
        $data = array(
            'action' => 'login',
            'status' => 'success',
            'username' => $username,
            'csrftoken' => $username,
            'sessionid' => $password,
        );
        return $data;
        exit();
    }

    $url_login = 'https://www.instagram.com/accounts/login/ajax/';
    $url_ig = 'https://www.instagram.com/accounts/login/';

    $get = curl($url_ig);
    $cookie = fetchCurlCookies($get);
    $csrf = $cookie['csrftoken'];
    $mid = $cookie['mid'];

    $header = array(
        'User-Agent: Mozilla/5.0 (iPhone; CPU iPhone OS 11_0_1 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A402 Safari/604.1',
        'X-CSRFToken: '.$csrf,
        'Content-Type: application/x-www-form-urlencoded',
        'Cookie: rur=FTW; mid='.$mid.'; csrftoken='.$csrf.'',
    );

    $body = 'username='.$username.'&enc_password=#PWD_INSTAGRAM_BROWSER:0:1589682409:'.$password.'&queryParams=%7B%7D&optIntoOneTap=false';

    $post = curl($url_login, $body, $header);

    if (strpos($post, '{"authenticated": false')) {

        $data = array(
            'action' => 'login',
            'status' => 'error',
            'username' => $username,
        );

    }elseif(strpos($post, '{"authenticated": true')){

        $cookie_log = fetchCurlCookies($post);
        $data = array(

            'action' => 'login',
            'status' => 'success',
            'username' => $username,
            'csrftoken' => $cookie_log['csrftoken'],
            'sessionid' => $cookie_log['sessionid'],
        );
        $myfile = fopen( __DIR__."/sesi/".$username.".json", "w") or die("Unable to open file!");
        $txt = json_encode(['csrftoken' => $cookie_log['csrftoken'], 'sessionid' => $cookie_log['sessionid']]);
        fwrite($myfile, $txt);
        fclose($myfile);

    }else{

        $data = $post;
    }

    return $data;

}
function get_stories_target($login,$id_target,$endCursor = '')
{
    $header = array();
    $header[] = 'Cookie: sessionid='.$login['sessionid'].';';
    $url = "https://www.instagram.com/graphql/query/?query_hash=c76146de99bb02f6415203be841dd25a&variables=%7B%22id%22%3A%22".$id_target."%22%2C%22include_reel%22%3Atrue%2C%22fetch_mutual%22%3Afalse%2C%22first%22%3A12%2C%22after%22%3A%22".$endCursor."%22%7D";
    $response = curlNoHeader($url,0,$header);
    $json_decode = json_decode($response,true);
    return array(
        "ec" => $json_decode['data']['user']['edge_followed_by']['page_info']['end_cursor'],
        "data" => $json_decode['data']['user']['edge_followed_by']['edges']
    );
}
function get_id($id,$login)
{
    $header = array();
    $header[] = 'Cookie: sessionid='.$login['sessionid'].';';
    $url = "https://www.instagram.com/graphql/query/?query_hash=5ec1d322b38839230f8e256e1f638d5f&variables=%7B%22reel_ids%22%3A%5B%22".$id."%22%5D%2C%22tag_names%22%3A%5B%5D%2C%22location_ids%22%3A%5B%5D%2C%22highlight_reel_ids%22%3A%5B%5D%2C%22precomposed_overlay%22%3Afalse%2C%22show_story_viewer_list%22%3Atrue%2C%22story_viewer_fetch_count%22%3A50%2C%22story_viewer_cursor%22%3A%22%22%2C%22stories_video_dash_manifest%22%3Afalse%7D";
    $response = curlNoHeader($url,0,$header);
    $json_decode = json_decode($response,true);
    return $json_decode['data']['reels_media'];
}

function view_story($login,$reelMediaId,$reelMediaOwnerId,$reelId,$reelMediaTakenAt)
{
    $url_view = 'https://www.instagram.com/stories/reel/seen';
    $header = array(
        'User-Agent: Mozilla/5.0 (iPhone; CPU iPhone OS 11_0_1 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A402 Safari/604.1',
        'X-CSRFToken: '.$login['csrftoken'],
        'Cookie: csrftoken='.$login['csrftoken'].'; sessionid='.$login['sessionid']
    );
    $body = 'reelMediaId='.$reelMediaId.'&reelMediaOwnerId='.$reelMediaOwnerId.'&reelId='.$reelId.'&reelMediaTakenAt='.$reelMediaTakenAt.'&viewSeenAt='.$reelMediaTakenAt.'';
    $post = curl($url_view, $body, $header);
    return $post;
}

function banner(){
    $str = "ICAgIF9fXyBfICBfIF9fXyBfX19fXyBfICAgX19fIF9fXyAgICBfICAgX18gIF9fIAogICB8XyBffCBcfCAvIF9ffF8gICBfL19cIC8gX198IF8gXCAgL19cIHwgIFwvICB8CiAgICB8IHx8IC5gIFxfXyBcIHwgfC8gXyBcIChfIHwgICAvIC8gXyBcfCB8XC98IHwKICAgfF9fX3xffFxffF9fXy8gfF8vXy8gXF9cX19ffF98X1wvXy8gXF9cX3wgIHxffApBdXRvIFZpZXdzIFN0b3JpZXMgVGFyZ2V0IHYxIHwgQ29kZSBieSBzYW5kcm8ucHV0cmFhIAogICAgICAgUmVjb2RlIGJ5IERhbmR5LCBhZGRlZCBzZXNzaW9uIHN0b3Jl";
    return print_r(base64_decode($str));
}
