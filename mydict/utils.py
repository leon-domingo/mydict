import stringcase


SNAKE_CASE  = 'snake_case'
CAMEL_CASE  = 'camelCase'
PASCAL_CASE = 'PascalCase'
KEBAB_CASE  = 'kebab-case'


def ignore_case(obj):
    return obj


def object_hook(obj, case_type):
    """
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
