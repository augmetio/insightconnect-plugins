import insightconnect_plugin_runtime
from .schema import CheckIfIpIsInListInput, CheckIfIpIsInListOutput, Input, Output, Component
# Custom imports below
from icon_ip_list_manager.util.cache_help import CacheHelp
from ipaddress import ip_network, ip_address

class CheckIfIpIsInList(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='check_if_ip_is_in_list',
                description=Component.DESCRIPTION,
                input=CheckIfIpIsInListInput(),
                output=CheckIfIpIsInListOutput())

    def check_ip_in_range(self, ip: str, cidr: str) -> bool:
        ip = ip_address(ip)
        net = ip_network(cidr, False)
        return ip in net

    def run(self, params={}):
        ip_to_check = params.get(Input.IP_ADDRESS)

        helper = CacheHelp()
        ip_list = helper.retrieve_variable(helper.IP_LIST)

        matched = False
        for ip in ip_list:
            if self.check_ip_in_range(ip_to_check, ip):
                matched = True
                break

        return {Output.IS_IN_LIST: matched}


