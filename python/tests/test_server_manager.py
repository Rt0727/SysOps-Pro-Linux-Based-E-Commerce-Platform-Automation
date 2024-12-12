import unittest
from server_manager import ServerManager

class TestServerManager(unittest.TestCase):
    def test_start_service(self):
        result = ServerManager.start_service("nonexistent_service")
        self.assertIn("Error", result)

    def test_check_disk_space(self):
        result = ServerManager.check_disk_space()
        self.assertIn("Filesystem", result)

if __name__ == "__main__":
    unittest.main()