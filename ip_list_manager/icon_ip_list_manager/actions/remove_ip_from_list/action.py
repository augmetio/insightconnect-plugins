import insightconnect_plugin_runtime
from .schema import RemoveIpFromListInput, RemoveIpFromListOutput, Input, Output, Component
# Custom imports below
from icon_ip_list_manager.util.cache_help import CacheHelp

class RemoveIpFromList(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='remove_ip_from_list',
                description=Component.DESCRIPTION,
                input=RemoveIpFromListInput(),
                output=RemoveIpFromListOutput())

    def run(self, params={}):
        ip_to_remove = params.get(Input.IP_ADDRESS)
        helper = CacheHelp()
        ip_list = helper.retrieve_variable(helper.IP_LIST)

        success = True
        try:
            ip_list.remove(ip_to_remove)
        except ValueError:
            success = False

        return {Output.SUCCESS: success}
