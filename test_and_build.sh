#!/bin/bash

set -e

DIR="$(dirname "$0")"

cd "$DIR"

# This will create pylock files for all environments regardless of environment
# lock settings, but hatch will only use a given pylock file for a given
# environment if the environment is locked. And hatch seems to have a problem
# with locking test and default environments.
# hatch env lock --export-all .

# hatch check fmt

hatch check code

hatch check types

hatch test -vvv --all --cover-xml |
tee tmp/test_results.txt

hatch run csv2xlsx --version

hatch run csv2xlsx --help

hatch build

exit "$?"
