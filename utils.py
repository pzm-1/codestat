def  count_lines(filepath):
    """统计一个文件里有多少行有效代码"""
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            lines = f.readlines()
            valid_lines = 0
            for line in lines:
                if line.strip() != "":
                    valid_lines += 1
            return valid_lines
    except FileNotFoundError:
        return -1
        



        