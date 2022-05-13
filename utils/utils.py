from collections.abc import Iterable
from joblib import Parallel, delayed


def clean_dict(x):
    for k, v in x.items():
        if isinstance(v, Iterable):
            x[k] = "".join(map(str, x[k]))
