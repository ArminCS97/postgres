import os
import pathlib
import importlib

def get_metadata_of_all_models():
    models_dir = pathlib.Path().absolute()
    # print(models_dir)
    # print(os.listdir(models_dir))
    metadata_objects = []
    print(os.listdir('D:\Projects\postgres\models'))
    for model_module in os.listdir('D:\Projects\postgres\models'):
        if model_module not in ['__init__.py', 'get_all.py', '__pycache__']:
            model_module_name = model_module[:-3]
            globals()[model_module_name] = importlib.import_module(model_module_name)
            metadata_objects.append(globals()[model_module_name].metadata)
    return metadata_objects

print(get_metadata_of_all_models())

modnames = ["os", "sys", "math"]
globalw = {} # it can be globals()
for lib in modnames:
    globalw[lib] = importlib.import_module(lib)

print(globalw['math'].sin(123))

