import os
import unittest
from pyats.topology import loader
from genie.libs.sdk.apis.iosxe.dhcp.configure import unconfigure_ip_dhcp_pool_host


class TestUnconfigureIpDhcpPoolHost(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        testbed = f"""
        devices:
          pipr-9300-1:
            connections:
              defaults:
                class: unicon.Unicon
              a:
                command: mock_device_cli --os iosxe --mock_data_dir {os.path.dirname(__file__)}/mock_data --state connect
                protocol: unknown
            os: iosxe
            platform: cat9k
            type: switch
        """
        self.testbed = loader.load(testbed)
        self.device = self.testbed.devices['pipr-9300-1']
        self.device.connect(
            learn_hostname=True,
            init_config_commands=[],
            init_exec_commands=[]
        )

    def test_unconfigure_ip_dhcp_pool_host(self):
        result = unconfigure_ip_dhcp_pool_host(self.device, 'test-pool', '100.10.10.10 255.255.255.0', None, None, 'pi-dhcp-client')
        expected_output = None
        self.assertEqual(result, expected_output)
