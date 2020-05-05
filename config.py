#
# Copyright 2018-2019 IBM Corp. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

# Flask settings
DEBUG = False

# Flask-restplus settings
RESTPLUS_MASK_SWAGGER = False
SWAGGER_UI_DOC_EXPANSION = 'none'

# API metadata
API_TITLE = 'MAX Recommender'
API_DESC = 'Generate personalized recommendations'
API_VERSION = '1.0.0'

# default model
MODEL_NAME = 'NCF'
DEFAULT_MODEL_PATH = 'assets/{}'.format(MODEL_NAME)


MODEL_META_DATA = {
    'id': '{}'.format(MODEL_NAME.lower()),
    'name': API_TITLE,
    'description': API_DESC,
    'type': 'recommendation',
    'source': 'https://developer.ibm.com/exchanges/models/all/max-recommender/',
    'license': 'Apache V2'
}
