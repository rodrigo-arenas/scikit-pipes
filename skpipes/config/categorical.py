from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.impute import SimpleImputer

categorical_config_dict = {
    "imputer_mf-one_hot": {
        "steps": [
            ("imputer", SimpleImputer(strategy="most_frequent")),
            ("encoding", OneHotEncoder(sparse=False)),
        ],
        "description": "Most frequent imputer with One-Hot encoding",
    },
    "imputer_mf-label": {
        "steps": [
            ("imputer", SimpleImputer(strategy="most_frequent")),
            ("encoding", LabelEncoder()),
        ],
        "description": "Most frequent imputer with Label encoding",
    }
}
