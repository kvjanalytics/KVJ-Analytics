@echo off
echo =======================================================
echo KVJ Analytics Photo & Logo Carousel Updater
echo =======================================================
echo.
echo This script will automatically rename all files in the
echo "India", "International", and "Logos" folders to sequential
echo names (1, 2, 3...) so they appear correctly on the website.
echo.

:: Rename India photos
echo Processing India folder...
powershell.exe -NoProfile -ExecutionPolicy Bypass -Command "$ErrorActionPreference = 'SilentlyContinue'; $folder = '.\assets\Photos\India'; $i = 1; Get-ChildItem -Path $folder -File | Where-Object { $_.Extension -match '\.(jpg|jpeg|png|webp|avif|JPG|JPEG|PNG|WEBP|AVIF)$' } | Sort-Object Name | ForEach-Object { $tempName = \"temp_$i$($_.Extension)\"; Rename-Item $_.FullName -NewName $tempName; $i++ }; $i = 1; Get-ChildItem -Path $folder -File -Filter 'temp_*' | ForEach-Object { $newName = \"$i$($_.Extension)\"; Rename-Item $_.FullName -NewName $newName; $i++ }"
echo Done.
echo.

:: Rename International photos
echo Processing International folder...
powershell.exe -NoProfile -ExecutionPolicy Bypass -Command "$ErrorActionPreference = 'SilentlyContinue'; $folder = '.\assets\Photos\International'; $i = 1; Get-ChildItem -Path $folder -File | Where-Object { $_.Extension -match '\.(jpg|jpeg|png|webp|avif|JPG|JPEG|PNG|WEBP|AVIF)$' } | Sort-Object Name | ForEach-Object { $tempName = \"temp_$i$($_.Extension)\"; Rename-Item $_.FullName -NewName $tempName; $i++ }; $i = 1; Get-ChildItem -Path $folder -File -Filter 'temp_*' | ForEach-Object { $newName = \"$i$($_.Extension)\"; Rename-Item $_.FullName -NewName $newName; $i++ }"
echo Done.
echo.

:: Rename Client Logos
echo Processing Logos folder...
powershell.exe -NoProfile -ExecutionPolicy Bypass -Command "$ErrorActionPreference = 'SilentlyContinue'; $folder = '.\assets\Logos'; $i = 1; Get-ChildItem -Path $folder -File | Where-Object { $_.Extension -match '\.(jpg|jpeg|png|webp|avif|JPG|JPEG|PNG|WEBP|AVIF)$' } | Sort-Object Name | ForEach-Object { $tempName = \"temp_$i$($_.Extension)\"; Rename-Item $_.FullName -NewName $tempName; $i++ }; $i = 1; Get-ChildItem -Path $folder -File -Filter 'temp_*' | ForEach-Object { $newName = \"$i$($_.Extension)\"; Rename-Item $_.FullName -NewName $newName; $i++ }"
echo Done.
echo.

echo =======================================================
echo Update Complete!
echo You can now refresh your website in the browser.
echo =======================================================
pause
