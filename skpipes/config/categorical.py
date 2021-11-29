from sklearn.preprocessing import OrdinalEncoder, OneHotEncoder
from sklearn.impute import SimpleImputer, KNNImputer

categorical_config_dict = {
    "mf_imputer-one_hot": {
        "steps": [
            ("imputer", SimpleImputer(strategy="most_frequent")),
            ("encoding", OneHotEncoder(sparse=False)),
        ],
        "description": "Most frequent imputer with One-Hot encoding",
    },
    "mf_imputer-ordinal": {
        "steps": [
            ("imputer", SimpleImputer(strategy="most_frequent")),
            ("encoding", OrdinalEncoder()),
        ],
        "description": "Most frequent imputer with ordinal encoding",
    },
}
