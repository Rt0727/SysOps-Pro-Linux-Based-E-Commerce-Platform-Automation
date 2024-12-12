class LogAnalyzer:
    def __init__(self, log_file):
        self.log_file = log_file

    def count_errors(self):
        error_count = 0
        with open(self.log_file, 'r') as file:
            for line in file:
                if "ERROR" in line:
                    error_count += 1
        return error_count

    def analyze_top_errors(self, top_n=5):
        error_map = {}
        with open(self.log_file, 'r') as file:
            for line in file:
                if "ERROR" in line:
                    error_map[line] = error_map.get(line, 0) + 1
        return sorted(error_map.items(), key=lambda x: x[1], reverse=True)[:top_n]