<?php
/*
///////////////////////////////////////////////////////////////////////////////
///////////////////////////////////////////////////////////////////////////////
////                       _            _  __                              ////
////                      | |          (_)/ _|                             ////
////                   ___| |_   _  ___ _| |_ ___ _ __                     ////
////                  |_  / | | | |/ __| |  _/ _ \ '__|                    ////
////                   / /| | |_| | (__| | ||  __/ |                       ////
////                  /___|_|\__,_|\___|_|_| \___|_|                       ////
////                                                                       ////
///////////////////////////////////////////////////////////////////////////////
///////////////////////////////////////////////////////////////////////////////
*/
@ob_clean();
$file = 'nama_file_yang_ingin_dibuat_force_download.format_file'; // contoh: gambar.jpg
header('Content-Description: File Transfer');
header('Content-Type: application/octet-stream');
header('Content-Disposition: attachment; filename="'.basename($file).'"');
header('Expires: 0'); 
header('Cache-Control: must-revalidate');
header('Pragma: public');
header('Content-Length: ' . filesize($file));
readfile($file);
exit;
?>
