<?php

$file = "source.json";

if (isset($_POST["save"])) {
  $powered = isset($_POST["powered"]);
  $phrase = $_POST["phrase"];
  $prefer = (int) $_POST["prefer"];
  $text = $_POST["text"];
  $audio = $_POST["audio"];
  $video = $_POST["video"];

  $data = [
      "powered" => $powered,
      "phrase" => $phrase,
      "prefer" => $prefer,
      "sources" => [
          "text" => $text,
          "audio" => $audio,
          "video" => $video
      ]
  ];

  $json_data = json_encode($data);
  file_put_contents($file, $json_data);
}

$json_data = file_get_contents($file);
$data = json_decode($json_data, true);

?>
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>Voice Assistant</title>
</head>
<body>
<form action="index.php" method="POST">
  <label for="powered">Powered:</label>
  <input type="checkbox" name="powered" id="powered" <?php if ($data["powered"]) echo "checked"; ?>>
  <br>

  <label for="phrase">Phrase:</label>
  <input type="text" name="phrase" id="phrase" placeholder="enter activation phrase..."
         value="<?php echo $data["phrase"]; ?>" autocomplete="off">
  <br><br>

  <label for="prefer">Prefer:</label>
  <select name="prefer" id="prefer">
    <option value="0" <?php if ($data["prefer"] == 0) echo "selected"; ?>>text</option>
    <option value="1" <?php if ($data["prefer"] == 1) echo "selected"; ?>>audio</option>
    <option value="2" <?php if ($data["prefer"] == 2) echo "selected"; ?>>video</option>
  </select>
  <br><br>

  <label for="text">Text:</label>
  <input type="text" name="text" id="text" placeholder="enter text..."
         value="<?php echo $data["sources"]["text"]; ?>" autocomplete="off">
  <br>

  <label for="audio">Audio (URL):</label>
  <input type="url" name="audio" id="audio" placeholder="enter url to audio..."
         value="<?php echo $data["sources"]["audio"]; ?>" autocomplete="off">
  <br>

  <label for="video">Video (URL):</label>
  <input type="url" name="video" id="video" placeholder="enter url to video..."
         value="<?php echo $data["sources"]["video"]; ?>" autocomplete="off">
  <br><br>

  <button type="submit" name="save">Save</button>
</form>
</body>
</html>