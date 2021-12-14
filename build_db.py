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

import hashlib
import json
import time
import os

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
        "header": make_header(),
        "timestamp":  int(time.time())
    }

    save_json(db, "bad_apple_db.json")

def make_header():
    with open('data.txt', 'rt') as fin:
        data = fin.read()

    result = []
    for page in data.split("SPLIT"):
        result.append(page)
        result.append(0.32)
    
    return result

def hash(file):
    with open(file, "rb") as f:
        file_hash = hashlib.md5()
        chunk = f.read(8192)
        while chunk:
            file_hash.update(chunk)
            chunk = f.read(8192)
        return file_hash.hexdigest()

def size(file):
    return os.path.getsize(file)

def save_json(db, json_name):
    with open(json_name, 'w') as f:
        json.dump(db, f, sort_keys=True, indent=4)
    print('Saved ' + json_name)

def load_json(path):
    with open(path) as f:
        return json.load(f)

if __name__ == "__main__":
    main()