import pytest
import pandas as pd
from data import clean, read_data
from unittest import mock


def test_clean():
    plot = "\n\nHello\r\nWorld\'[1]"
    assert clean(plot) == " Hello World"


@mock.patch('data.os.path.isfile', return_value=False)
def test_read_data_bad_file(_):
    with pytest.raises(ValueError):
        read_data('test.csv')


@mock.patch('data.os.path.isfile', return_value=True)
@mock.patch('data.pd.read_csv', return_value=pd.DataFrame({
    'Genre': ['Horror'] * 150 + ['Romance'] * 50
}))
def test_read_data_filtering(mock_csv, mock_isfile):
    data_from_popular_genres = read_data('test.csv')
    assert set(data_from_popular_genres['Genre']) == {'Horror'}
    assert len(data_from_popular_genres) == 150


@mock.patch('data.os.path.isfile', return_value=True)
def test_read_data_bad_extension(_):
    with pytest.raises(ValueError):
        read_data('test.cv')





