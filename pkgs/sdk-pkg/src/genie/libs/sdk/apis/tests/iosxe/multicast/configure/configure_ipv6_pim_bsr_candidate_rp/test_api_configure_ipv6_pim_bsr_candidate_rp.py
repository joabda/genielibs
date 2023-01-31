import os
import unittest
from pyats.topology import loader
from genie.libs.sdk.apis.iosxe.multicast.configure import configure_ipv6_pim_bsr_candidate_rp


class TestConfigureIpv6PimBsrCandidateRp(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        testbed = f"""
        devices:
          UUT1:
            connections:
              defaults:
                class: unicon.Unicon
              a:
                command: mock_device_cli --os iosxe --mock_data_dir {os.path.dirname(__file__)}/mock_data --state connect
                protocol: unknown
            os: iosxe
            platform: iosxe
            type: iosxe
        """
        self.testbed = loader.load(testbed)
        self.device = self.testbed.devices['UUT1']
        self.device.connect(
            learn_hostname=True,
            init_config_commands=[],
            init_exec_commands=[]
        )

    def test_configure_ipv6_pim_bsr_candidate_rp(self):
        result = configure_ipv6_pim_bsr_candidate_rp(self.device, '61::61', 'list1', None, None, None, True, None)
        expected_output = None
        self.assertEqual(result, expected_output)
