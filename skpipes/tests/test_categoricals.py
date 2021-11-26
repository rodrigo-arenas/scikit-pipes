import pandas as pd
import numpy as np
from ..pipeline import SkPipeline
from ..config import categorical_config_dict

data = [
    {"x1": "A", "x2": "Low"},
    {"x1": "A", "x2": "High"},
    {"x1": "B", "x2": "Medium"},
    {"x1": "C", "x2": "Low"},
    {"x1": "A", "x2": np.nan},
    {"x1": "D", "x2": "Low"},
]

df = pd.DataFrame(data)


def test_categorical_pipes():
    for pipe_name, value in categorical_config_dict.items():
        # Definition
        pipeline = SkPipeline(name=pipe_name, data_type="categorical")

        assert len(value["steps"]) == len(pipeline)
        assert pipeline.steps == value["steps"]
        assert str(pipeline) == value["description"]

        # Run
        X = pipeline.fit_transform(df)
        assert X.shape[0] == df.shape[0]
