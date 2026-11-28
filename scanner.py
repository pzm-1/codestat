import os
def find_python_files(directory):
    """遍历制定目录,返回所有.py文件的路径列表"""
    py_files = []
    for root, dirs, files in os.walk(directory):
        if 'venv' in root or '__pycache__' in root or '.git' in root:
            continue
        for file in files:
            if file.endswith(".py"):
                full_path = os.path.join(root, file)
                py_files.append(full_path)
        return py_files