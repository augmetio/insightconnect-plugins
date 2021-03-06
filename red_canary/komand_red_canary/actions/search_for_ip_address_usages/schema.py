# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Find usages of an IP address"


class Input:
    IP_ADDRESS = "ip_address"
    MAX_RESULTS = "max_results"
    

class Output:
    RESULTS = "results"
    

class SearchForIpAddressUsagesInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "ip_address": {
      "type": "string",
      "title": "IP Address",
      "description": "IPv4 or IPv6 address to find usages for",
      "order": 1
    },
    "max_results": {
      "type": "integer",
      "title": "Max Results",
      "description": "Maximum number of results to return",
      "default": 100,
      "order": 2
    }
  },
  "required": [
    "ip_address"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class SearchForIpAddressUsagesOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "results": {
      "type": "array",
      "title": "Results",
      "description": "Search results",
      "items": {
        "$ref": "#/definitions/search_result"
      },
      "order": 1
    }
  },
  "required": [
    "results"
  ],
  "definitions": {
    "search_result": {
      "type": "object",
      "title": "search_result",
      "properties": {
        "attributes": {
          "$ref": "#/definitions/search_result_attributes",
          "title": "Attributes",
          "description": "Attributes of the resource",
          "order": 2
        },
        "type": {
          "type": "string",
          "title": "Type",
          "description": "Type of object",
          "order": 1
        }
      },
      "definitions": {
        "search_result_attributes": {
          "type": "object",
          "title": "search_result_attributes",
          "properties": {
            "result_association_type": {
              "type": "string",
              "title": "Result Association Type",
              "description": "Type of the association to the IP or MAC address",
              "order": 1
            }
          }
        }
      }
    },
    "search_result_attributes": {
      "type": "object",
      "title": "search_result_attributes",
      "properties": {
        "result_association_type": {
          "type": "string",
          "title": "Result Association Type",
          "description": "Type of the association to the IP or MAC address",
          "order": 1
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
