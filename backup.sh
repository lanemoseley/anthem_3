#!/bin/bash

source .env

echo "Backing up portfolio..."

BU_PATH=portfolio-backups

mkdir -p $BU_PATH/postgres
mkdir -p $BU_PATH/media
mkdir -p $BU_PATH/static

PGPASSWORD=$DB_PASSWORD pg_dump -U $DB_USER -h $DB_HOST $DB_NAME > $BU_PATH/postgres/backup_$(date +"%Y%m%d").sql

tar -czvf $BU_PATH/media/media_backup_$(date +"%Y%m%d").tar.gz media
cp .env $BU_PATH/dot_env_$(date +"%Y%m%d")
tar -czvf $BU_PATH/static/static_backup_$(date +"%Y%m%d").tar.gz static

echo "Backup complete."
