from db import models


def admin_register_interface(username, password):
    admin_obj = models.Admin(username, password)
    admin_obj.save()
