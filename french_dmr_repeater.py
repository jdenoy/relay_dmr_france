#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import json
for key in (requests.get("https://api.brandmeister.network/v1.0/repeater/?action=LIST")).json():
    if (key['repeaterid'].find("208")== 0) : # If 208 found at start of repeaterid, then it is French and we go on.
        if (int(key['status'])<4): # Filter out DMR Hotspot
            print(json.dumps(key)) # Print JSON format
