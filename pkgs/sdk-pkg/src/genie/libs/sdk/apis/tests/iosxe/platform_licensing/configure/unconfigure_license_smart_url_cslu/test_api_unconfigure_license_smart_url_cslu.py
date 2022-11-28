import os
import unittest
from pyats.topology import loader
from genie.libs.sdk.apis.iosxe.platform_licensing.configure import unconfigure_license_smart_url_cslu


class TestUnconfigureLicenseSmartUrlCslu(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        testbed = f"""
        devices:
          n10SVL:
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
        self.device = self.testbed.devices['n10SVL']
        self.device.connect(
            learn_hostname=True,
            init_config_commands=[],
            init_exec_commands=[]
        )

    def test_unconfigure_license_smart_url_cslu(self):
        result = unconfigure_license_smart_url_cslu(self.device)
        expected_output = None
        self.assertEqual(result, expected_output)
