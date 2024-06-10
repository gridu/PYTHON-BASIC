import process_weather_data as pwd
import pytest
from tests.validate_xml import check_result
from unittest.mock import patch


def test_pwd(tmpdir):
    test_dir = tmpdir.mkdir('test')
    result_path = test_dir / 'result.xml'
    with patch('sys.argv', ['', '-i', 'practice/5_additional_topics/parsing_serialization_task/source_data', '-o', str(result_path)]):
        pwd.main()
    check_result(str(result_path))


if __name__ == '__main__':
    pytest.main([__file__])
