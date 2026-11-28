import sys
from scanner import find_python_files
from analyzer import CodeAnalyzer
from reporter import print_report
def main():
    target_dir = sys.argv[1] if len(sys.argv) > 1 else "."
    print(f"正在扫描目录: {target_dir} ...")
    files = find_python_files(target_dir)
    if not files:
        print("没有找到 .py文件")
        return
    my_analyzer = CodeAnalyzer()
    for file in files:
        my_analyzer.analyze_file(file)
    print_report(my_analyzer)
if __name__ == "__main__":
    main()
