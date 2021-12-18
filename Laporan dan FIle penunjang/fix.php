$image = $_FILES['image']['name'];
// whitelist file ext
$fileExt = pathinfo($image, PATHINFO_EXTENSION);
$fileExtAllowed = array('jpg', 'jpeg', 'png');
if (!(in_array($fileExt, $fileExtAllowed))) {
    die("$fileExt not allowed extension,please upload images only");
}
// whitelist mime type
$fileType = $_FILES['image']['type'];
$fileTypeAllowed =  array('image/jpg', 'image/jpeg', 'image/png');
if (!(in_array($fileType, $fileTypeAllowed))) {
    
    die("$fileType not allowed mime type, please upload images only");
}

//Letakan code diatas pada file /pages/save_user.php pada bagian :

$image = $_FILES['image']['name'];

//letakan disini

$target = "../uploadImage/Profile/".basename($image);