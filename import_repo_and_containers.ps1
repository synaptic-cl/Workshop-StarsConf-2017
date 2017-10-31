$images = ls *.docker
$color="Green"

foreach ($image in $images){
	docker load --input $image
}

git clone workshop_repo.bundle -b master workshop

Write-Host "Ejecuta lo siguiente para levantar el ambiente:" -ForegroundColor $color
Write-Host "$ cd workshop" -ForegroundColor $color
Write-Host "$ docker-compose -f docker-compose.alt.yml up -d" -ForegroundColor $color
Write-Host "$ docker-compose logs -f" -ForegroundColor $color
