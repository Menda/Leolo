# coding=utf-8
# Copyright 2010 Rafa Muñoz Cárdenas
#
# Licensed under the Apache License, Version 2.0 (the "License"); you
# may not use this file except in compliance with the License.  You
# may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.  See the License for the specific language governing
# permissions and limitations under the License.

"""
Example settings for Leolo.
"""

import os

# Define db engine. e.g.: sqlite, postgresql, mysql...
# Important: must be a supported db by your SQLAlchemy version. and you
# must use the same syntax.
#LEOLO_ENGINE = "mysql://user:password@localhost/database"
LEOLO_ENGINE = "sqlite:///database.sqlite"

LEOLO_PARALLEL_DL = 4 # max parallel downloads

# whitelist domains (no http or www prefix needed)
LEOLO_WHITELIST = (
   "4shared.com",
   "badongo.com",
   "easy-share.com",
   "filefactory.com",
   "mediafire.com",
   "megaupload.com",
   "rapidshare.com",
   "usershare.net",
   "gigasize.com",
   "depositfiles.com",
   "sendspace.com",
   "storage.to",
   "zshare.net",
   "uploading.com",
)

LEOLO_BLACKLIST = (
)

# Optional parameter. It's the path where logs are stored
# Default path will be $HOME/.leolo
# LEOLO_PATH = os.path.join("my", "path", "leolo")

