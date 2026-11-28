# CodeStat  (Python 代码统计器)

这是一个基于 Python 开发的命令行代码统计工具，可以自动遍历指定目录下的所有 `.py` 文件，并统计每个文件的有效代码行数。

##  核心功能
- **自动扫描**：使用 `os.walk` 递归遍历目录，自动过滤虚拟环境（venv）等无用文件夹。
- **多模块解耦**：代码分为 Scanner（扫描）、Analyzer（分析）、Reporter（展示），架构清晰。
- **格式化输出**：在终端中以漂亮的格式输出统计报告。

##  快速开始
1. 克隆本仓库并进入目录
2. 创建并激活虚拟环境（Windows）：`python -m venv venv`，然后 `.\venv\Scripts\activate`
3. 安装依赖：`pip install -r requirements.txt`
4. 运行程序：`python main.py`