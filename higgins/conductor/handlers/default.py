#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

"""Higgins Conductor default handler."""


# These are the database operations - They are executed by the conductor
# service.  API calls via AMQP trigger the handlers to be called.

class Handler(object):
    def __init__(self):
        super(Handler, self).__init__()

    def container_get(uuid):
        pass
