class CodeAnalyzer:
    def __init__(self):
        self.total_files = 0
        self.total_lines = 0
        self.file_records = []
    def analyze_file(self, filepath):
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                lines = f.readlines()
                valid_lines = 0
                for line in lines:
                    if line.strip() != "":
                        valid_lines += 1
                self.total_files += 1
                self.total_lines += valid_lines
                record = {"file": filepath, "lines": valid_lines}
                self.file_records.append(record)
                return valid_lines
        except FileNotFoundError:
            print(f"找不到文件: {filepath}")
            return -1
    def get_summary(self):
            return f"一共扫描了 {self.total_files} 个文件, 总共有 {self.total_lines} 行有效代码"
