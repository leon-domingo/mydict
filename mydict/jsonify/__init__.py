import json
import stringcase
from .. import MyDict
from ..utils import (
    object_hook,
    ignore_case,
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
        CASE_FUNCS = {
            SNAKE_CASE: stringcase.snakecase,
            CAMEL_CASE: stringcase.camelcase,
            PASCAL_CASE: stringcase.pascalcase,
        }

        if isinstance(member, (dict, MyDict)):
            return {
                CASE_FUNCS.get(case_type, ignore_case)(k): _get_dict(v, case_type)
                for k, v in member.items()
            }

        elif isinstance(member, (list,)):
            return [_get_dict(a, case_type) for a in member]

        elif isinstance(member, (tuple,)):
            return tuple(_get_dict(a, case_type) for a in member)

        elif isinstance(member, (set,)):
            return {_get_dict(a, case_type) for a in member}

        return member

    return _get_dict(my_dict, case_type)


def to_json(my_dict: MyDict, case_type=None) -> str:
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
