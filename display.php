<?php
$dirname = "../kenzo/";
$images = glob($dirname."*.png");
foreach($images as $image) {
echo '<img src="'.$image.'" /><br />';
}

?>
