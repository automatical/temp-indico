# This file is part of Indico.
# Copyright (C) 2002 - 2019 CERN
#
# Indico is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see the
# LICENSE file for more details.

import os
os.environ['INDICO_CONFIG'] = "/srv/www/indico/application/.indico.conf"

from indico.web.flask.app import make_app
application = make_app()
