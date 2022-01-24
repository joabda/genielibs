import unittest
from pyats.topology import loader
from genie.libs.sdk.apis.iosxe.sudi.configure import configure_service_private_config_encryption


class TestConfigureServicePrivateConfigEncryption(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        testbed = """
        devices:
          Switch:
            connections:
              defaults:
                class: unicon.Unicon
              a:
                command: mock_device_cli --os iosxe --mock_data_dir mock_data --state connect
                protocol: unknown
            os: iosxe
            platform: Switch
            type: Switch
        """
        self.testbed = loader.load(testbed)
        self.device = self.testbed.devices['Switch']
        self.device.connect(
            learn_hostname=True,
            init_config_commands=[],
            init_exec_commands=[]
        )

    def test_configure_service_private_config_encryption(self):
        result = configure_service_private_config_encryption(self.device)
        expected_output = None
        self.assertEqual(result, expected_output)
