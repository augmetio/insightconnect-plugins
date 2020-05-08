import insightconnect_plugin_runtime
from .schema import ClearIpListInput, ClearIpListOutput, Input, Output, Component
# Custom imports below
from icon_ip_list_manager.util.cache_help import CacheHelp

class ClearIpList(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='clear_ip_list',
                description=Component.DESCRIPTION,
                input=ClearIpListInput(),
                output=ClearIpListOutput())

    def run(self, params={}):
        helper = CacheHelp()
        helper.delete_variable(helper.IP_LIST)
        return {Output.SUCCESS: True}
