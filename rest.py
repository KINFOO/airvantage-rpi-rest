#!/usr/bin/env python3
from argparse import ArgumentParser
import json
import requests
from time import time

# Parse arguments
parser = ArgumentParser(description="Using RESTful AirVantage.")
parser.add_argument("identifier",
  help="Your identifier, defined on AirVantage, here a trimmed a MAC address.")
parser.add_argument("password", help="REST password.")
args = parser.parse_args()

#
# Sending data to AirVantage
#
timestamp = int( time() )
# +1 and +2 are here to avoid aving several data points at the same time
data = [
  {
    "machine.temperature": [
      { "value" : "23.2", "timestamp" : timestamp },
      { "value" : "24.5", "timestamp" : timestamp + 1 },
      { "value" : "22.9", "timestamp" : timestamp + 2 }
    ]
  },
  {
    "machine.threshold": [
      { "value" : "30", "timestamp" : timestamp }
    ]
  }
]

# Using Basic Authentication
host = "https://na.airvantage.net"
url = "{}/device/messages".format( host )
print("Sending to {}.".format(url))
response = requests.post( url,
  auth=(args.identifier, args.password),
  data=json.dumps(data),
  headers={'Content-type': 'application/json'}
)
print("Response: {}. Content: {}".format(response.status_code, response.text))

# Check if there are messages
message_url = "{}/device/tasks".format( host )
print("Checking for messages at {}.".format(message_url))
response = requests.get( message_url,
  auth=(args.identifier, args.password),
  headers={'Content-type': 'application/json'}
)
print("Response: {}. Content: {}".format(response.status_code, response.text))
print("Done")
