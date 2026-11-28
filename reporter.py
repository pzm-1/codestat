def print_report(analyzer):
    """接收分析器对象，把结果打印成漂亮的格式"""
    print("\n" + "="*40)
    print("代码统计报告 (CodeStat)")
    print("="*40)
    
    for record in analyzer.file_records:
        filename = record["file"]
        lines = record["lines"]
        print(f" 📄 {filename}: {lines} 行")
        
    print("-" * 40)
    print(analyzer.get_summary())
    print("="*40 + "\n")