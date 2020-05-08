import sys
import os
sys.path.append(os.path.abspath('../'))

from unittest import TestCase
from icon_ip_list_manager.connection.connection import Connection
from icon_ip_list_manager.actions.check_if_ip_is_in_list import CheckIfIpIsInList
from icon_ip_list_manager.actions.add_ip_to_list import AddIpToList
from icon_ip_list_manager.actions.clear_ip_list import ClearIpList

import json
import logging


class TestCheckIfIpIsInList(TestCase):
    def test_integration_check_if_ip_is_in_list(self):
        log = logging.getLogger("Test")
        test_conn = Connection()
        test_action = CheckIfIpIsInList()
        test_add_ip = AddIpToList()
        test_clear_list = ClearIpList

        test_conn.logger = log
        test_action.logger = log
        test_add_ip.logger = log
        test_clear_list.logger = log

        try:
            with open("../tests/check_if_ip_is_in_list.json") as file:
                test_json = json.loads(file.read()).get("body")
                connection_params = test_json.get("connection")
        except Exception as e:
            message = """
            Could not find or read sample tests from /tests directory
            
            An exception here likely means you didn't fill out your samples correctly in the /tests directory 
            Please use 'icon-plugin generate samples', and fill out the resulting test files in the /tests directory
            """
            self.fail(message)

        test_conn.connect(connection_params)
        test_action.connection = test_conn
        test_add_ip.connection = test_conn
        test_clear_list.connection = test_conn

        ip_to_check_params = {
            "ip_address": "1.1.1.1"
        }

        ip_to_add1 = {
            "ip_address": "1.1.1.2"
        }

        ip_to_add2 = {
            "ip_address": "1.1.1.2/24"
        }


        test_add_ip.run(ip_to_add1)
        test_add_ip.run(ip_to_add2)

        results = test_action.run(ip_to_check_params)

        test_clear_list.run({})

        self.assertEquals({}, results)

