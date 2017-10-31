#!/usr/bin/env bash
set -o errexit
set -o nounset

GREEN='\033[0;32m'
NC='\033[0m'
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd $DIR

for image in $(find . -name '*.docker')
do
	docker load < $image
done

if command -v git ; then
	git clone workshop_repo.bundle -b master workshop
else
	mkdir -p workshop && unzip workshop_repo.zip -d workshop
fi

echo -e "${GREEN}"
echo "Ejecuta lo siguiente para levantar el ambiente:"
echo "$ cd workshop"
echo "$ docker-compose -f docker-compose.alt.yml up -d"
echo "$ docker-compose logs -f"
echo -e "${NC}"