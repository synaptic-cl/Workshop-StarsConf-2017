#!/usr/bin/env bash
set -o errexit
set -o nounset

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

for image in $(find . -name '*.docker')
do
	docker load < $image
done

# TODO clone repo
