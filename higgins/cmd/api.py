# -*- encoding: utf-8 -*-
#
# Copyright 2013 Hewlett-Packard Development Company, L.P.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

"""The Higgins Service API."""

import sys

from oslo_config import cfg

from higgins.common import service as higgins_service

CONF = cfg.CONF


def main():
    # Parse config file and command line options, then start logging
    higgins_service.prepare_service(sys.argv)

    # Enable object backporting via the conductor
    # TODO(yuanying): Uncomment after rpc services are implemented
    # base.higginsObject.indirection_api = base.higginsObjectIndirectionAPI()

    # Build and start the WSGI app
    launcher = higgins_service.process_launcher()
    server = higgins_service.WSGIService(
        'higgins_api',
        CONF.api.enable_ssl_api
    )
    launcher.launch_service(server, workers=server.workers)
    launcher.wait()

if __name__ == '__main__':
    sys.exit(main())
