from sklearn.preprocessing import MinMaxScaler, StandardScaler, PolynomialFeatures
from sklearn.impute import SimpleImputer
from sklearn.feature_selection import VarianceThreshold
from sklearn.decomposition import PCA

numerical_config_dict = {
    "imputer_mean-minmax": {
        "steps": [
            ("imputer", SimpleImputer(strategy="mean")),
            ("scaler", MinMaxScaler()),
        ],
        "description": "Mean imputer with MinMax Scaler",
    },
    "imputer_median-minmax": {
        "steps": [
            ("imputer", SimpleImputer(strategy="median")),
            ("scaler", MinMaxScaler()),
        ],
        "description": "Median imputer with MinMax Scaler",
    },
    "std_sclr-v_threshold": {
        "steps": [("scaler", StandardScaler()), ("selector", VarianceThreshold())],
        "description": "Standard Scaler with Variance Threshold",
    },
    "imputer_median-polyfeatures2": {
        "steps": [
            ("imputer", SimpleImputer(strategy="median")),
            ("selector", PolynomialFeatures(2)),
        ],
        "description": "Median imputer with second degree polynomial features",
    },
    "imputer_median-std_sclr-PCA": {
        "steps": [
            ("imputer", SimpleImputer(strategy="median")),
            ("scaler", StandardScaler()),
            ("pca", PCA()),
        ],
        "description": "Median imputer with standard scaler and PCA ",
    },
}
