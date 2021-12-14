#!/usr/bin/env python3
# Copyright (c) 2021 José Manuel Barroso Galindo <theypsilon@gmail.com>

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

# You can download the latest version of this tool from:
# https://github.com/theypsilon/BadAppleDB_MiSTer

import json
import time

def main():
    print('START!')

    db = {
        "db_id": 'bad_apple_db',
        "db_files": [],
        "files": {},
        "folders": {},
        "zips": {},
        "base_files_url": "",
        "default_options": {},
        "header": bad_apple_header(),
        "timestamp":  int(time.time())
    }

    save_json(db, "bad_apple_db.json")

def bad_apple_header():
    with open('data.txt', 'rt') as fin:
        data = fin.read()

    header = []
    for page in data.split("SPLIT"):
        header.append('\033[H\033[2J')
        header.append(page + '\r')
        header.append(0.0925)
    
    header.append(10.0)
    return header

def save_json(db, json_name):
    with open(json_name, 'w') as f:
        json.dump(db, f, sort_keys=True, indent=4)
    print('Saved ' + json_name)

if __name__ == "__main__":
    main()
