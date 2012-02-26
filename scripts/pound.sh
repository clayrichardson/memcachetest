#!/bin/bash

../memcache -t 50 -l -v -P 100 -i 1000000 $(python ./rs_tags.py)
