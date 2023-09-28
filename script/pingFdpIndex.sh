#!/bin/bash

curl -X POST -H 'Content-Type: application/json' -d "{\"clientUrl\": \"${FDP_URL}\"}" ${FDP_INDEX_URL} --fail-with-body && echo "asked <${FDP_INDEX_URL}> to index <${FDP_URL}>"
