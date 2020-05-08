import os
import base64
import ast
import logging

class CacheHelp():
    # Global to store ip list
    IP_LIST = "ip_list"

    def __init__(self):
        self.log = logging.getLogger("TEST")
        cwd = os.getcwd()
        self.log.info(cwd)
        if "icon_ip_list_manager" in cwd:  # we are working locally
            self.DICT_FILE = os.path.join(os.getcwd(), "ip_list_management.dict")
        else:  # we are in the orcha
            self.DICT_FILE = "/var/cache/ip_list_management.dict"
        self.log.info(self.DICT_FILE)

    def store_variable(self, variable_to_store, value_to_store):
        cache_dict = self._get_dict_from_store()
        cache_dict[variable_to_store] = value_to_store
        self._save_dict_to_store(cache_dict)
        return True

    def retrieve_variable(self, variable_name):
        cache_dict = self._get_dict_from_store()
        retval = cache_dict.get(variable_name)
        if not retval:
            retval = []
        return retval

    def delete_variable(self, variable_name):
        cache_dict = self._get_dict_from_store()
        if variable_name in cache_dict.keys():
            cache_dict.pop(variable_name)
            self._save_dict_to_store(cache_dict)

    def check_for_variable(self, variable_name):
        cache_dict = self._get_dict_from_store()
        return variable_name in cache_dict.keys()

    def _check_dict_file(self, file):
        return os.path.isfile(file)

    def _get_dict_from_store(self):
        if self._check_dict_file(self.DICT_FILE):
            with open(self.DICT_FILE, 'rb') as file_:
                encoded_bytes = file_.read()
                encoded_string = encoded_bytes.decode()
                decoded_dict = base64.b64decode(encoded_string)
                plain_text_dict = decoded_dict.decode()
                return_value = ast.literal_eval(plain_text_dict)
                return return_value
        return {}

    def _save_dict_to_store(self, dict):
        bytes_dict = str(dict).encode()
        encoded_dict = base64.b64encode(bytes_dict)
        with open(self.DICT_FILE, 'wb') as file_:
            file_.write(encoded_dict)

    def _delete_dict_file(self):
        if self._check_dict_file(self.DICT_FILE):
            os.remove(self.DICT_FILE)
