from collections.abc import Iterable


def clean_dict(x):
    for k,v in x.items():
        if isinstance(v,Iterable):
            x[k] = "".join(map(str,x[k]))