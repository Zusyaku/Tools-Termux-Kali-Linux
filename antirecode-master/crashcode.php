<?php
        // Print out main menu..
    echo "=======================\n";
    echo "Tools Penghancur code\n";
    echo "=======================\n";
echo "Select an option..\n\n";
    echo "    1) Encode Md5\n";
    echo "    2) Encode Base64\n";
    echo "    3) Encode Sha1\n";
    echo "    4) Encode Md4\n";
    echo "    5) Encode Semua type\n";
    echo "    x) Exit\n";
    echo "Pilih Type Encode : ";
    switch(trim(fgets(STDIN,256)))
        {
            case 1:
                echo "Masukkan Kata Yang Akan di Encode : ";
                $kata = trim(fgets(STDIN,256));
                echo "Encode Md5 :",md5($kata),"\n";
                exit();
            case 2:
                echo "Masukkan Kata Yang Akan di Encode : ";
                $kata = trim(fgets(STDIN));
                echo "Encode Base64 :",base64_encode($kata),"\n";
                exit();
            case 3:
                echo "Masukkan Kata Yang Akan di Encode : ";
                $kata = trim(fgets(STDIN));
                echo "Encode Base64 :",sha1($kata),"\n";
                exit();
            case 4:
                echo "Masukkan Kata Yang Akan di Encode : ";
                $kata = trim(fgets(STDIN));
                echo "Encode Md4 :",crypt('md4',$kata);
                exit();
            case 5:
                echo "Masukan Kata Yang Akan di Encode : ";
                $kata = trim(fgets(STDIN));
                foreach (hash_algos() as $v) {
                $r = hash($v, $kata, false);
                printf("%-12s %3d %s\n", $v, strlen($r), $r);
                }
                exit();
            case "x":
                exit();
        }
    // Close standard in..
    fclose(STDIN);
?>
