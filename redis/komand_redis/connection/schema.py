# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Input:
    DB = "db"
    HOST = "host"
    PORT = "port"
    

class ConnectionSchema(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "db": {
      "type": "integer",
      "title": "Db",
      "description": "DB to use usually (0-15)",
      "default": 0,
      "order": 3
    },
    "host": {
      "type": "string",
      "title": "Host",
      "description": "Host, e.g. 10.4.4.4",
      "order": 1
    },
    "port": {
      "type": "integer",
      "title": "Port",
      "description": "Port",
      "default": 6379,
      "order": 2
    }
  },
  "required": [
    "db",
    "host",
    "port"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
