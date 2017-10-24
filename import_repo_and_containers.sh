#!/usr/bin/env bash
set -o errexit
set -o nounset

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd $DIR

for image in $(find . -name '*.docker')
do
	docker load < $image
done

git clone workshop_repo.bundle -b master workshop
