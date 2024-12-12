import unittest
from log_analyzer import LogAnalyzer

class TestLogAnalyzer(unittest.TestCase):
    def test_count_errors(self):
        log_analyzer = LogAnalyzer("sample.log")
        with open("sample.log", "w") as file:
            file.write("INFO: System running smoothly\n")
            file.write("ERROR: Something went wrong\n")
        self.assertEqual(log_analyzer.count_errors(), 1)

    def test_analyze_top_errors(self):
        log_analyzer = LogAnalyzer("sample.log")
        with open("sample.log", "w") as file:
            file.write("ERROR: Database connection failed\n")
            file.write("ERROR: Database connection failed\n")
        top_errors = log_analyzer.analyze_top_errors()
        self.assertEqual(top_errors[0][1], 2)

if __name__ == "__main__":
    unittest.main()