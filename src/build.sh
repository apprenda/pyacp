#!/usr/bin/env bash

# clean up distribution folder, just in case.
rm -f dist/*.whl

# get active branch, remove slashes
export active_branch=$(git branch | grep \* | sed s/\*[[:space:]]// | tr '/' '_')

python setup.py bdist_wheel

# rename the file so that we tag the branch in it
mv $(ls dist/*.whl) $(ls dist/*.whl | sed s/none/${active_branch}/g)