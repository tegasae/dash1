#!/bin/bash
# Remote backup script (run from the remote host)

DOCKER_HOST="tega@192.168.100.147"
CONTAINER="work_http-app"
DB_PATH="/app/data/telebot.db"
BACKUP_NAME="backup_$(date +%Y%m%d_%H%M%S).db"

# 1. Create and stream the binary backup
ssh $DOCKER_HOST "\
  docker exec $CONTAINER sqlite3 $DB_PATH '.backup /tmp/backup.db' \
  && docker exec $CONTAINER cat /tmp/backup.db" \
  > $BACKUP_NAME

echo "Backup saved to: $BACKUP_NAME"
cp ${BACKUP_NAME} telebot.db
#sqlite3 telebot.db <statuses.sql