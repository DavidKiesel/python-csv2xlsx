#!/bin/bash

set -e

DIR="$(dirname "$0")"

cd "$DIR"

# rm -f \
#     pylock*.toml

# rm -rf \
#     requirements.txt \
#     requirements/

rm -f \
    .coverage \
    .coverage.* \
    coverage.xml

rm -rf \
    .pytest_cache/ \
    .ruff_cache/

# https://stackoverflow.com/questions/28991015/remove-pycache-folders-and-pyc-files-from-python-project
find \
    . \
    -type f \
    -name '*.py[co]' \
    -delete \
    -o \
    -type d \
    -name __pycache__ \
    -delete

hatch env prune

hatch clean

# rm -rf \
#     "$HOME/.local/share/hatch/env/virtual/helloworld/"

# rm -rf \
#     "$HOME/.cache/hatch/"

exit "$?"
