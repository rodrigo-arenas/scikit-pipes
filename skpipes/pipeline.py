from sklearn.pipeline import Pipeline
from .config import get_config


class SkPipeline(Pipeline):
    """
    Main object of scikit-config to select the desired Pipeline

    Sequentially apply a list of transforms and a final estimator.
    Intermediate steps of the pipeline must be 'transforms', that is, they
    must implement `fit` and `transform` methods.
    The final estimator only needs to implement `fit`.
    The transformers in the pipeline can be cached using ``memory`` argument.
    The purpose of the pipeline is to assemble several steps that can be
    cross-validated together while setting different parameters. For this, it
    enables setting parameters of the various steps using their names and the
    parameter name separated by a `'__'`, as in the example below. A step's
    estimator may be replaced entirely by setting the parameter with its name
    to another estimator, or a transformer removed by setting it to
    `'passthrough'` or `None`.

    Parameters
    ----------
    name : str
        The name of one of the pre-defined pipelines from skpipes.config
    data_type : {'numerical', 'categorical'}
        It indicates the data type of the incoming features.
    memory : str or object with the joblib.Memory interface, default=None
        Used to cache the fitted transformers of the pipeline. By default,
        no caching is performed. If a string is given, it is the path to
        the caching directory. Enabling caching triggers a clone of
        the transformers before fitting. Therefore, the transformer
        instance given to the pipeline cannot be inspected
        directly. Use the attribute ``named_steps`` or ``steps`` to
        inspect estimators within the pipeline. Caching the
        transformers is advantageous when fitting is time consuming.
    verbose : bool, default=False
        If True, the time elapsed while fitting each step will be printed as it
        is completed.

    Attributes
    ----------

    named_steps : :class:`~sklearn.utils.Bunch`
        Dictionary-like object, with the following attributes.
        Read-only attribute to access any step parameter by user given name.
        Keys are step names and values are steps parameters.
    classes_ : ndarray of shape (n_classes,)
        The classes labels. Only exist if the last step of the pipeline is a
        classifier.
    n_features_in_ : int
        Number of features seen during :term:`fit`. Only defined if the
        underlying first estimator in `steps` exposes such an attribute
        when fit.
    feature_names_in_ : ndarray of shape (`n_features_in_`,)
        Names of features seen during :term:`fit`. Only defined if the
        underlying estimator exposes such an attribute when fit.
    """

    def __init__(self, name, data_type, memory=None, verbose=False):
        self.name = name
        self.data_type = data_type
        self.memory = memory
        self.verbose = verbose

        config = get_config(self.data_type)
        pipe = config.get(self.name)
        if not pipe:
            raise ValueError(
                f"The pipeline {name} wasn't found for this data_type, "
                f"make sure it's spelled correctly"
            )
        else:
            steps = pipe["steps"]

        self.description = pipe["description"]

        super(SkPipeline, self).__init__(
            steps=steps, memory=self.memory, verbose=self.verbose
        )

    def __str__(self):
        return self.description
