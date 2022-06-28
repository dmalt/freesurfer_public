#!/bin/bash

# Add local user
# Either use the LOCAL_USER_ID if passed in at runtime or
# fallback

USER_ID=${LOCAL_USER_ID:-9001}

echo "Starting with UID : $USER_ID"
useradd --shell /bin/bash -u $USER_ID -o -c "" -m user
export HOME=/home/user

mv /usr/local/freesurfer/subjects /subjects
export SUBJECTS_DIR="/subjects"
chown -R user:user $SUBJECTS_DIR

cp -r /code/* $HOME/
cd $HOME

exec /usr/local/bin/gosu user python3 -u -m doit "$@"
