#!/bin/bash

if [ ! $# -eq 2 ]; then
	echo "Usage: ./create_forks.sh SUBMISSION_GROUP_ID PROJECT_TO_FORK"
	exit 1
fi

SUBMISSION_GROUP_ID=$1
PROJECT_TO_FORK=$2

SCRIPT_PATH=<YOUR_SCRIPT_PATH>
LOG_PATH=<YOUR_LOG_PATH>

source $SCRIPT_PATH/.venv/bin/activate
python3 $SCRIPT_PATH/create_forks.py $SUBMISSION_GROUP_ID $PROJECT_TO_FORK | ts '[%Y-%m-%d %H:%M:%S]' >> $LOG_PATH/cron.log
