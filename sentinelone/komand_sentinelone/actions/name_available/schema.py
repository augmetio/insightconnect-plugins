# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Is the account name available for this account"


class Input:
    NAME = "name"
    

class Output:
    AVAILABLE = "available"
    

class NameAvailableInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "name": {
      "type": "string",
      "title": "Name",
      "description": "Account Name to validate",
      "order": 1
    }
  },
  "required": [
    "name"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class NameAvailableOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "available": {
      "type": "boolean",
      "title": "Available",
      "description": "Account Name to validate",
      "order": 1
    }
  },
  "required": [
    "available"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
