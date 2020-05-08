import insightconnect_plugin_runtime
from .schema import GetIpListInput, GetIpListOutput, Input, Output, Component
# Custom imports below
from icon_ip_list_manager.util.cache_help import CacheHelp

class GetIpList(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_ip_list',
                description=Component.DESCRIPTION,
                input=GetIpListInput(),
                output=GetIpListOutput())

    def run(self, params={}):
        helper = CacheHelp()
        ip_list = helper.retrieve_variable(helper.IP_LIST)
        return {Output.IP_LIST: ip_list}
