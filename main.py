from analyzer import CodeAnalyzer
my_analyzer = CodeAnalyzer()
my_analyzer.analyze_file("utils.py")
my_analyzer.analyze_file("calculator.py")
my_analyzer.analyze_file("这个文件不存在.txt")
print(my_analyzer.get_summary())
