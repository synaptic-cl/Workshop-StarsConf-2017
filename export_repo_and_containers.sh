#!/usr/bin/env bash
set -o errexit
set -o nounset
images=$(docker-compose images | awk '/back|front/ {print $2}')
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
OUTPUT_ZIP=workshop.zip

cd $DIR

mkdir -p export

cp import_repo_and_containers.* export/

# if git is not installed on target
git archive --format=zip -o export/workshop_repo.zip master
# else, use git clone <bundle>
git bundle create export/workshop_repo.bundle master

cd export
for image in $images
do
	docker save ${image} -o ${image}.docker
done

rm $OUTPUT_ZIP || true
zip -rm $OUTPUT_ZIP *
