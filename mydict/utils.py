import stringcase


SNAKE_CASE  = 'snake_case'
CAMEL_CASE  = 'camelCase'
PASCAL_CASE = 'PascalCase'


def ignore_case(key):
    """
    A trivial function to just return the key as it is without modifications.
    """
    return key


def object_hook(obj, case_type):
    """
    Args:
        obj: The object whose keys are gonna be altered.
        case_type: The type of case to apply to the keys of the object. None, default value, it means no transformation on the keys is applied.

    Returns:
        A custom object with its keys modified based on "case_type" param.
    """

    if case_type == SNAKE_CASE:
        case_function = getattr(stringcase, 'snakecase')

    elif case_type == CAMEL_CASE:
        case_function = getattr(stringcase, 'camelcase')

    elif case_type == PASCAL_CASE:
        case_function = getattr(stringcase, 'pascalcase')

    else:
        case_function = ignore_case

    custom_obj = {}
    for key in obj.keys():
        custom_obj[case_function(key)] = obj[key]

    return custom_obj
