#!/bin/bash
#
# list-monospace-fonts.sh - Lists all monospace font families.
#
# Author: Lain Musgrove (lain.proliant@gmail.com)
# Date: Thursday January 2, 2020
#
# Distributed under terms of the MIT license.
#

fc-list --format="%{family[0]}\n" | sort | uniq
