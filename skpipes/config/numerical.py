from sklearn.preprocessing import (
    MinMaxScaler,
    StandardScaler,
    PolynomialFeatures,
    RobustScaler,
)
from sklearn.impute import SimpleImputer
from sklearn.feature_selection import VarianceThreshold
from sklearn.decomposition import PCA

numerical_config_dict = {
    "mean_impute-minmax": {
        "steps": [
            ("imputer", SimpleImputer(strategy="mean")),
            ("scaler", MinMaxScaler()),
        ],
        "description": "Mean imputer with MinMax Scaler",
    },
    "median_imputer-minmax": {
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
    "median_imputer-robust_sclr": {
        "steps": [
            ("imputer", SimpleImputer(strategy="median")),
            ("scaler", RobustScaler()),
        ],
        "description": "Median imputer with robust scaler ",
    },
    "median_imputer-polyfeatures2": {
        "steps": [
            ("imputer", SimpleImputer(strategy="median")),
            ("selector", PolynomialFeatures(2)),
        ],
        "description": "Median imputer with second degree polynomial features",
    },
    "median_imputer-std_sclr-PCA": {
        "steps": [
            ("imputer", SimpleImputer(strategy="median")),
            ("scaler", StandardScaler()),
            ("pca", PCA()),
        ],
        "description": "Median imputer with standard scaler and PCA ",
    },
    "median_imputer-robust_sclr-PCA": {
        "steps": [
            ("imputer", SimpleImputer(strategy="median")),
            ("scaler", RobustScaler()),
            ("pca", PCA()),
        ],
        "description": "Median imputer with robust scaler and PCA ",
    },
}
