from sklearn.preprocessing import OrdinalEncoder, OneHotEncoder
from sklearn.impute import SimpleImputer

categorical_config_dict = {
    "imputer_mf-one_hot": {
        "steps": [
            ("imputer", SimpleImputer(strategy="most_frequent")),
            ("encoding", OneHotEncoder(sparse=False)),
        ],
        "description": "Most frequent imputer with One-Hot encoding",
    },
    "imputer_mf-ordinal": {
        "steps": [
            ("imputer", SimpleImputer(strategy="most_frequent")),
            ("encoding", OrdinalEncoder()),
        ],
        "description": "Most frequent imputer with ordinal encoding",
    },
}
