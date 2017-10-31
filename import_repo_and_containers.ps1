$images = ls *.docker
$color="Green"

foreach ($image in $images){
	docker load --input $image
}

if (Get-Command git -errorAction SilentlyContinue) {
	git clone workshop_repo.bundle -b master workshop
} else {
	Add-Type -AssemblyName System.IO.Compression.FileSystem
	mkdir workshop
	[System.IO.Compression.ZipFile]::ExtractToDirectory((Get-Item -Path "workshop_repo.zip" -Verbose).FullName, (Get-Item -Path "workshop" -Verbose).FullName)
}

Write-Host "Ejecuta lo siguiente para levantar el ambiente:" -ForegroundColor $color
Write-Host "$ cd workshop" -ForegroundColor $color
Write-Host "$ docker-compose -f docker-compose.alt.yml up -d" -ForegroundColor $color
Write-Host "$ docker-compose logs -f" -ForegroundColor $color
