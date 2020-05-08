import insightconnect_plugin_runtime
from .schema import AddIpToListInput, AddIpToListOutput, Input, Output, Component
# Custom imports below
from icon_ip_list_manager.util.cache_help import CacheHelp

class AddIpToList(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='add_ip_to_list',
                description=Component.DESCRIPTION,
                input=AddIpToListInput(),
                output=AddIpToListOutput())

    def run(self, params={}):
        ip_to_store = params.get(Input.IP_ADDRESS)

        helper = CacheHelp()
        ip_list = helper.retrieve_variable(helper.IP_LIST)
        if not ip_to_store in ip_list:
            ip_list.append(ip_to_store)
        helper.store_variable(helper.IP_LIST, ip_list)

        return {Output.IP_ADDRESS: ip_to_store}
