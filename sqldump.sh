#!/usr/bin/env
mysqldump -u $1 -p$2 $3 $4 > "$4.sql"

