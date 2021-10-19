<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta name="description" content="mp3 downloader one click">
    <title>Music mp3 Downloader</title>
    <link rel="stylesheet" href="css/aos.css" />
    <link rel="stylesheet" href="css/style.min.css">
    <link rel="stylesheet" href="css/style-me.css">
    <link rel="icon" href="img/icon.jpg">
    <script src="https://use.fontawesome.com/releases/v5.15.3/js/all.js" crossorigin="anonymous"></script>
    <script>
        function dnld(idd) {
            var xhr = new XMLHttpRequest();
            var url = "https://ytdl-api-rizky.herokuapp.com/download?id=" + idd + "&type=audio";
            xhr.onloadstart = function() {
                document.getElementById("butn").innerHTML = "Loading..";
            };
            xhr.onreadystatechange = function() {
                if (this.readyState == 4 && this.status == 200) {
                    var data = JSON.parse(this.responseText);
                    document.getElementById("butn").innerHTML = "Download";
                    window.open(data.download_url, '_blank');
                }
            };
            xhr.open("GET", url, true);
            xhr.send();
        }
    </script>
</head>
<body>
    <div class="intro-page mt-3 mb-4">
        <img src="img/musik.png" alt="Logo music" data-aos="zoom-in">
        <b data-aos="fade-up" data-aos-easing="ease" data-aos-delay="400">Download musik dengan sekali sentuhan</b>
    </div>
    <div class="mt-4 mb-4">
        <form action="" method="post">
            <div class="inp">
                <input type="text" placeholder="search you favorit music..." name="judul" class="inpt btn-rounded">
                <button type="submit" class="but" name="submit"><i class="fas fa-search"></i>
                </button>
            </div>
        </form>
    </div>
    <div class="page-content container-fluid">
      <?php
       if(isset($_POST["submit"])){
         $txt = $_POST["judul"];
         if($txt == ""){
           $judul = "baon cikadap lagu jorok";
         }else {
           $judul = $txt;
         }
         $rep = str_replace(" ", "+", $judul);
         $fgt = file_get_contents("https://ytdl-api-rizky.herokuapp.com/details?query=".$rep);
         $dec = json_decode($fgt, true);
         foreach ($dec["data"] as $z){
           ?>
           <div class="row mt-2">
            <div class="col-md-6 col-lg-4">
                <div class="card bor">
                    <img class="card-img-top" src="<?= $z["thumbnail"]; ?>" alt="Card image cap">
                    <div class="card-body">
                        <h4 class="mt-2 mb-4"><?= $z["judul"]; ?></h4>
                        <div class="row mt-4">
                            <div class="col border-end text-center">
                                <i class="fas fa-user-alt text-success fa-2x"></i>
                                <h5 class="fw-normal text-muted"><?= $z["chanel_name"]; ?></h5>
                            </div>
                            <div class="col border-end text-center">
                                <i class="far fa-clock text-warning fa-2x"></i>
                                <h5 class="fw-normal text-muted"><?= $z["durasi"]; ?></h5>
                            </div>
                            <div class="col text-center">
                                <i class="fas fa-headphones text-primary fa-2x"></i>
                                <h5 class="fw-normal text-muted"><?= $z["view"]; ?></h5>
                            </div>
                        </div>
                        <div class="mt-4 button-dl text-center">
                            <button type="button" class="btn btn-primary" data-toggle="modal" data-target="#<?= $z["id"]; ?>">
                                Play
                            </button>
                            <div class="modal fade" id="<?= $z["id"]; ?>" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
                                <div class="modal-dialog modal-dialog-centered" role="document">
                                    <div class="modal-content">
                                        <div class="modal-header">
                                            <h5 class="modal-title" id="exampleModalLabel"><?= $z["judul"]; ?></h5>
                                            <button type="button" class="btn-close" data-dismiss="modal" aria-label="Close"></button>
                                        </div>
                                        <div class="modal-body">
                                            <center><iframe style="border:none;border-radius: 1%" src="<?= "https://www.youtube.com/embed/".$z['id']."?playsinline=1"; ?>" rel="nofollow preconnect" width="90%" height="280" donotallowfullscreen></iframe></center>
                                        </div>
                                        <div class="modal-footer">
                                            <button type="button" class="btn btn-danger" data-dismiss="modal">Close</button>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <button id="butn" onclick="dnld('<?= $z["id"]; ?>')" class="btn btn-info">Download</button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
           <?php
         }
       }
      ?>
    </div>
    <script src="js/jquery.min.js"></script>
    <script src="js/popper.min.js"></script>
    <script src="js/bootstrap.min.js"></script>
    <script src="js/aos.js" type="text/javascript"></script>
    <script>
			AOS.init({
				easing: 'ease-out-back',
				duration: 1000
			});
		</script>
</body>
</html>