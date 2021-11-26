from sklearn.preprocessing import MinMaxScaler, OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer


categorical_config_dict = {
    "imputer_mf-one_hot": {
        "steps": [
            ("imputer", SimpleImputer(strategy="most_frequent")),
            ("encoding", OneHotEncoder(sparse=False)),
        ],
        "description": "Most frequent imputer with One-Hot encoding"
        "for categorical features",
    }
}
