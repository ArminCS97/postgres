from flask import current_app
import application

print(current_app.extensions['migrate'].db.engine.url)

def get_metadata_of_all_models():
    # Attention: we have to set the python path to models folder so that we dont get an error
    # set PYTHONPATH=%PYTHONPATH%;D:\Projects\postgres\models
    metadata_objects = []
    for model_module in os.listdir('D:\Projects\postgres\models'):
        if model_module not in ['__init__.py', 'get_all.py', '__pycache__']:
            model_module_name = model_module[:-3]
            globals()[model_module_name] = importlib.import_module(model_module_name, package='models')
            metadata_objects.append(globals()[model_module_name].metadata)
    return metadata_objects