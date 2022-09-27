import os
import unittest
from pyats.topology import loader
from genie.libs.sdk.apis.iosxe.aaa.configure import unconfigure_aaa_authentication_enable


class TestUnconfigureAaaAuthenticationEnable(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        testbed = f"""
        devices:
          NG_SVL_switch:
            connections:
              defaults:
                class: unicon.Unicon
              a:
                command: mock_device_cli --os iosxe --mock_data_dir {os.path.dirname(__file__)}/mock_data --state connect
                protocol: unknown
            os: iosxe
            platform: cat9k
            type: Nyquist
        """
        self.testbed = loader.load(testbed)
        self.device = self.testbed.devices['NG_SVL_switch']
        self.device.connect(
            learn_hostname=True,
            init_config_commands=[],
            init_exec_commands=[]
        )

    def test_unconfigure_aaa_authentication_enable(self):
        result = unconfigure_aaa_authentication_enable(self.device)
        expected_output = None
        self.assertEqual(result, expected_output)
