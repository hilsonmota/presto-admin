# -*- coding: utf-8 -*-

#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
___version___ = '0.1.0'  # Make sure to update setup.py too

from fabric.api import env

import errno
import os

__all__ = ['topology']

config_root = os.getenv('WORKSPACE', '~')
env.config_directory = os.path.join(os.path.expanduser(config_root), '.fabric')
try:
    os.makedirs(env.config_directory)
except OSError as ex:
    if ex.errno != errno.EEXIST:
        raise

env.roledefs = {
    'coordinator': [],
    'worker': [],
    'all': [],
}

import topology