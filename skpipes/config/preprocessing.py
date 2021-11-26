from .numerical import numerical_config_dict
from .categorical import categorical_config_dict


def get_config(data_type):
    config = {
        "numerical": numerical_config_dict,
        "categorical": categorical_config_dict,
    }
    pipelines = config.get(data_type)

    if not pipelines:
        raise ValueError(
            f"{data_type} data type is not defined, "
            f"it should be one of {'numerical', 'categorical'}"
        )

    return pipelines
