import pytest
from ..pipeline import SkPipeline


@pytest.mark.parametrize("data_type", ["numerical", "categorical"])
def test_wrong_name(data_type):
    with pytest.raises(Exception) as excinfo:
        pipeline = SkPipeline(name="dummy", data_type=data_type)

    assert (
        str(excinfo.value) == "The pipeline dummy wasn't found for this data_type, "
        "make sure it's spelled correctly"
    )


@pytest.mark.parametrize("data_type", ["numbers", "categories"])
def test_wrong_data_type(data_type):
    with pytest.raises(Exception) as excinfo:
        pipeline = SkPipeline(name="imputer_mean-minmax", data_type=data_type)

    assert (
        str(excinfo.value) == f"{data_type} data type is not defined, "
        f"it should be one of {'numerical', 'categorical'}"
    )
