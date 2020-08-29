import json
import stringcase
# from .. import MyDict
from .. import MyDict
from ..utils import (
    object_hook,
    SNAKE_CASE,
    CAMEL_CASE,
    PASCAL_CASE,
)


def get_dict(my_dict: MyDict, case_type=None) -> dict:
    """
    Returns a <dict> of the <MyDict> object

    Args:
        case_type: The type of case

    Returns:
        A <dict> representing the
    """

    def _get_dict(member, case_type):
        if isinstance(member, (dict, MyDict)):
            d = {}
            for k, v in member.items():
                custom_key = k
                if case_type == SNAKE_CASE:
                    custom_key = stringcase.snakecase(k)

                elif case_type == CAMEL_CASE:
                    custom_key = stringcase.camelcase(k)

                elif case_type == PASCAL_CASE:
                    custom_key = stringcase.pascalcase(k)

                d[custom_key] = _get_dict(v, case_type)

            return d

        elif isinstance(member, (list,)):
            lst = []
            for a in member:
                lst.append(_get_dict(a, case_type))

            return lst

        elif isinstance(member, (tuple,)):
            tpl = tuple()
            for a in member:
                tpl = tpl + (_get_dict(a, case_type),)

            return tpl

        elif isinstance(member, (set,)):
            st = set([])
            for a in member:
                st.add(_get_dict(a, case_type))

            return st

        else:
            return member

    return _get_dict(my_dict, case_type)


def to_json(my_dict, case_type=None) -> str:
    """Returns a JSON-like string representing this instance"""
    return json.dumps(get_dict(my_dict, case_type))


def from_json(json_source, case_type=None) -> MyDict:
    """
    Returns a "MyDict" instance from a:
        JSON string
        <file>-like containing a JSON string
    """

    def _object_hook(obj):
        return object_hook(obj, case_type)

    if isinstance(json_source, (str, bytes)):
        # decode bytes to str
        if isinstance(json_source, bytes):
            json_source = json_source.decode('utf8')

        json_load_func = getattr(json, 'loads')

    elif hasattr(json_source, 'read'):
        json_source.seek(0)
        json_load_func = getattr(json, 'load')

    json_obj = json_load_func(
        json_source,
        object_hook=_object_hook,
    )

    return MyDict(json_obj)
