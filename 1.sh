#!/bin/bash
# Remote backup script (run from the remote host)

DOCKER_HOST="tega@192.168.100.147"
CONTAINER="work_http-app"
DB_PATH="/app/data/telebot.db"
BACKUP_NAME="backup_$(date +%Y%m%d_%H%M%S).db"
FILE_SQL="statuses.sql"
# 1. Create and stream the binary backup
ssh $DOCKER_HOST  "cat > '/tmp/$FILE_SQL' && docker cp /tmp/$FILE_SQL $CONTAINER:/tmp && docker exec $CONTAINER sqlite3 $DB_PATH < '/tmp/$FILE_SQL' && echo 111 " <$FILE_SQL
#sqlite3 /app/data/telebot.db </tmp/$FILE_SQL" < $FILE_SQL
#ssh $DOCKER_HOST "docker exec $CONTAINER cat >'/tmp/123'" < 
