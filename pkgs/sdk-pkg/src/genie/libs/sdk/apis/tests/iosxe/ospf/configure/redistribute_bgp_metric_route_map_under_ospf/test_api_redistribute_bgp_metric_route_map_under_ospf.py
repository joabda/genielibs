import os
import unittest
from pyats.topology import loader
from genie.libs.sdk.apis.iosxe.ospf.configure import redistribute_bgp_metric_route_map_under_ospf


class TestRedistributeBgpMetricRouteMapUnderOspf(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        testbed = f"""
        devices:
          9300-24UX-1:
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
        self.device = self.testbed.devices['9300-24UX-1']
        self.device.connect(
            learn_hostname=True,
            init_config_commands=[],
            init_exec_commands=[]
        )

    def test_redistribute_bgp_metric_route_map_under_ospf(self):
        result = redistribute_bgp_metric_route_map_under_ospf(self.device, 1, 1, 100, 'ospf_test')
        expected_output = None
        self.assertEqual(result, expected_output)
