import os
import unittest
from pyats.topology import loader
from genie.libs.sdk.apis.iosxe.platform.configure import copy_file_with_sftp


class TestCopyFileWithSftp(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        testbed = f"""
        devices:
          VCR:
            connections:
              defaults:
                class: unicon.Unicon
              a:
                command: mock_device_cli --os iosxe --mock_data_dir {os.path.dirname(__file__)}/mock_data --state connect
                protocol: unknown
            os: iosxe
            platform: cat9k
            type: c9300
        """
        self.testbed = loader.load(testbed)
        self.device = self.testbed.devices['VCR']
        self.device.connect(
            learn_hostname=True,
            init_config_commands=[],
            init_exec_commands=[]
        )

    def test_copy_file_with_sftp(self):
        result = copy_file_with_sftp(self.device, '172.163.128.3', 'sh_switch_sftp.txt', 'root', 'cisco', None, 30)
        expected_output = ('Address or name of remote host [172.163.128.3]? \r\n'
 'Destination filename [sh_switch_sftp.txt]? \r\n'
 'SFTP send: Writing to /root/sh_switch_sftp.txt size 397\r\n'
 '!\r\n'
 '397 bytes copied in 0.204 secs (1946 bytes/sec)')
 # '\r\nT13-C9300-24T#')
        # Running UT on Mac drops the prompt from the device output.
        self.assertTrue(result.startswith(expected_output))
