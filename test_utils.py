from utils import count_lines
import pytest
import os
@pytest.fixture
def sample_file(tmp_path):
    file = tmp_path / "test_code.txt"
    file.write_text("print('hello')", encoding="utf-8")
    return str(file)
def test_count_normal(sample_file):
    assert count_lines(sample_file) == 1
def test_count_empty_file(tmp_path):
    empty_file = tmp_path / "empty.txt"
    empty_file.write_text("", encoding="utf-8")
    assert count_lines("该文件不存在.txt") == -1
def test_count_all_blank(tmp_path):
    blank_file = tmp_path / "blank.txt"
    blank_file.write_text("\n  \n\t\n", encoding="utf-8")
    assert count_lines(str(blank_file)) == 0
