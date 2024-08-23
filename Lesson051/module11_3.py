import inspect


class MyClass:

    def __init__(self, name, second_name):
        self.name = name
        self.second_name = second_name

    def my_method(self):
        print(f'Hello, {self.name}')


def introspection_info(obj):
    info = {}
    info.update({'type': type(obj)})

    module_name = str(inspect.getmodule(obj)).split()
    if module_name[0] == 'None':
        module_name = module_name[0]
        list_attr = []
    else:
        module_name = module_name[1].replace("'", "")
        list_attr = [attr for attr in obj.__dict__]
    list_methods = [x for x in dir(obj) if x not in list_attr]
    info.update({'attributes': list_attr, 'methods': list_methods, 'module': module_name})

    if type(obj) is MyClass:
        values = []
        for attr_name in list_attr:
            values.append(getattr(obj, attr_name))
        info.update({'values': values})

    return info


my_obj = MyClass('obj_1', 'my_obj')

number_info = introspection_info(42)
print(number_info)
number_info = introspection_info(my_obj)
print(number_info)
