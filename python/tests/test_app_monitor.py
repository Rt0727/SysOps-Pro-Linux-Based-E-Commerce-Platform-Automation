import unittest
from unittest.mock import patch
import app_monitor

class TestAppMonitor(unittest.TestCase):
    @patch("app_monitor.requests.get")
    def test_monitor_application(self, mock_get):
        mock_get.return_value.status_code = 200
        app_monitor.monitor_application("http://mockurl.com", interval=0)
        mock_get.assert_called_with("http://mockurl.com")

if __name__ == "__main__":
    unittest.main()