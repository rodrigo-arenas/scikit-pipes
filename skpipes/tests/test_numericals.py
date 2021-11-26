import pandas as pd
import numpy as np
from ..pipeline import SkPipeline
from ..config import numerical_config_dict

data = [
    {"x1": 1, "x2": 400, "x3": np.nan},
    {"x1": 4.8, "x2": 250, "x3": 50},
    {"x1": 3, "x2": 140, "x3": 43},
    {"x1": 1.4, "x2": 357, "x3": 75},
    {"x1": 2.4, "x2": np.nan, "x3": 42},
    {"x1": 4, "x2": 287, "x3": 21},
]

df = pd.DataFrame(data)


def test_numerical_pipes():
    for pipe_name, value in numerical_config_dict.items():
        # Definition
        pipeline = SkPipeline(name=pipe_name, data_type="numerical")

        assert len(value["steps"]) == len(pipeline)
        assert pipeline.steps == value["steps"]
        assert str(pipeline) == value["description"]

        # Run
        X = pipeline.fit_transform(df)
        assert X.shape[0] == df.shape[0]
