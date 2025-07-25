$exclude = @("venv", "bot_fakturama2.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "bot_fakturama2.zip" -Force