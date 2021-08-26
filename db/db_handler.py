import os
from conf import settings
import pickle


def save_data(obj):
    class_name = obj.__class__.__name__
    user_dir_path = os.path.join(settings.DB_PATH, class_name)
    if not os.path.exists(user_dir_path):
        os.mkdir(user_dir_path)
    user_path = os.path.join(user_dir_path, obj.user)
    with open(user_path, 'wb') as file:
        pickle.dump(obj, file)


def select_data(obj):
    pass
