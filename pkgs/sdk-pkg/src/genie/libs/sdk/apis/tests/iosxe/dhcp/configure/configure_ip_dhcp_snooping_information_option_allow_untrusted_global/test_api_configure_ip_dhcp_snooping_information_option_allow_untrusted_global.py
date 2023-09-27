import os
import unittest
from pyats.topology import loader
from genie.libs.sdk.apis.iosxe.dhcp.configure import configure_ip_dhcp_snooping_information_option_allow_untrusted_global


class TestConfigureIpDhcpSnoopingInformationOptionAllowUntrustedGlobal(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        testbed = f"""
        devices:
          SW2:
            connections:
              defaults:
                class: unicon.Unicon
              a:
                command: mock_device_cli --os iosxe --mock_data_dir {os.path.dirname(__file__)}/mock_data --state connect
                protocol: unknown
            os: iosxe
            platform: c9500
            type: c9500
        """
        self.testbed = loader.load(testbed)
        self.device = self.testbed.devices['SW2']
        self.device.connect(
            learn_hostname=True,
            init_config_commands=[],
            init_exec_commands=[]
        )

    def test_configure_ip_dhcp_snooping_information_option_allow_untrusted_global(self):
        result = configure_ip_dhcp_snooping_information_option_allow_untrusted_global(self.device)
        expected_output = None
        self.assertEqual(result, expected_output)
