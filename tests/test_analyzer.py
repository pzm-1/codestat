import pytest
from analyzer import CodeAnalyzer
@pytest.fixture
def fresh_analyzer(tmp_path):
    test_file = tmp_path / "test.py"
    test_file.write_text("print('hello')", encoding="utf-8")
    analyzer = CodeAnalyzer()
    return analyzer, str(test_file)
def test_initial_state():
    analyzer = CodeAnalyzer()
    assert analyzer.total_files == 0
    assert analyzer.total_lines == 0
    assert analyzer.file_records == []
def test_analyze_normal(fresh_analyzer):
    analyzer, filepath = fresh_analyzer
    result = analyzer.analyze_file(filepath)
    assert result == 1
    assert analyzer.total_files == 1
    assert analyzer.total_lines == 1
def test_analyze_not_found():
    analyzer = CodeAnalyzer()
    result = analyzer.analyze_file("假文件.txt")
    assert result == -1
    assert analyzer.total_files == 0
    assert analyzer.total_lines == 0