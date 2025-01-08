#!/bin/bash

docker compose --env-file=./.env --profile flower up -d
