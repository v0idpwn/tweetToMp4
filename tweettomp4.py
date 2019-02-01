#!/usr/bin/env/ python3

import sys
from secrets import *
from twtools import api_init, get_url, get_id

# "Pythonic" applies only to the bot :P
print(get_url(api_init(), get_id(sys.argv[1])))
