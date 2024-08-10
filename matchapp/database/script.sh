# execute ./script.sh
sqlite3 matchapp.db < schema.sql
sqlite3 matchapp.db < data.sql
python3 dai.py