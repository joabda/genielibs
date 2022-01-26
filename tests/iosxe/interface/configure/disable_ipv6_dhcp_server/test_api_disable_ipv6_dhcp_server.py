import unittest
from pyats.topology import loader
from genie.libs.sdk.apis.iosxe.interface.configure import disable_ipv6_dhcp_server


class TestDisableIpv6DhcpServer(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        testbed = """
        devices:
          Intrepid-DUT-1:
            connections:
              defaults:
                class: unicon.Unicon
              a:
                command: mock_device_cli --os iosxe --mock_data_dir mock_data --state connect
                protocol: unknown
            os: iosxe
            platform: C9600
            type: C9600
        """
        self.testbed = loader.load(testbed)
        self.device = self.testbed.devices['Intrepid-DUT-1']
        self.device.connect(
            learn_hostname=True,
            init_config_commands=[],
            init_exec_commands=[]
        )

    def test_disable_ipv6_dhcp_server(self):
        result = disable_ipv6_dhcp_server(device=self.device, interface='HundredGigE1/0/21')
        expected_output = None
        self.assertEqual(result, expected_output)