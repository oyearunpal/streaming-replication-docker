#!/usr/bin/env bash

set -a
source ../primary.env
source ../replica.env
set +a

python3 wr_to_primary.py
echo "Lets read from replica now.."
sleep 1
python3 read_from_replica.py
