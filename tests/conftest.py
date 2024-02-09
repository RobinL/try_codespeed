import pytest
from splink.datasets import splink_datasets


@pytest.fixture
def historical_50k_df():
    return splink_datasets.historical_50k
