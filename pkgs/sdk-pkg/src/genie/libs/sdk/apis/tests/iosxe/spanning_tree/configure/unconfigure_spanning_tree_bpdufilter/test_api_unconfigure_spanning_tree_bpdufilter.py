import os
import unittest
from pyats.topology import loader
from genie.libs.sdk.apis.iosxe.spanning_tree.configure import unconfigure_spanning_tree_bpdufilter


class TestUnconfigureSpanningTreeBpdufilter(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        testbed = f"""
        devices:
          E-9500H_SVL_DIST1:
            connections:
              defaults:
                class: unicon.Unicon
              a:
                command: mock_device_cli --os iosxe --mock_data_dir {os.path.dirname(__file__)}/mock_data --state connect
                protocol: unknown
            os: iosxe
            platform: cat9k
            type: c9500
        """
        self.testbed = loader.load(testbed)
        self.device = self.testbed.devices['E-9500H_SVL_DIST1']
        self.device.connect(
            learn_hostname=True,
            init_config_commands=[],
            init_exec_commands=[]
        )

    def test_unconfigure_spanning_tree_bpdufilter(self):
        result = unconfigure_spanning_tree_bpdufilter(self.device, 'FortyGigabitEthernet2/0/9')
        expected_output = None
        self.assertEqual(result, expected_output)
