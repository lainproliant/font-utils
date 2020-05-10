#!/bin/bash
#
# apply.sh
#
# Author: Lain Musgrove (lain.proliant@gmail.com)
# Date: Thursday January 2, 2020
#
# Distributed under terms of the MIT license.
#

# Regen polybar's config.
pushd ~/.config/polybar
./generate.py > config
popd

# Restart polybar
polybar-msg cmd restart

# Restart qtile
qtile-cmd -o cmd -f restart

# Regen termite's config.
pushd ~/.config/termite
./generate.py > config
popd

# Tell all termites to reload their configs.
killall -USR1 termite
