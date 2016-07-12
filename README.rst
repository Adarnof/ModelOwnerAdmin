====
ModelOwnerAdmin
====

ModelOwnerAdmin is a simple Django ModelAdmin base
to restrict admin access to individual models,
allowing only owners or superusers to change or delete
existing models while respecting the Django add_model,
change_model, and delete_model permissions.

Quick Start
-----------

1. Subclass django_extras.contrib.auth.models.OwnerMixinBase::

    class MyModel(OwnerMixinBase, models.Model)

2. Register the model with ModelOwnerAdmin or a subclass::

    admin.site.register(MyModel, ModelOwnerAdmin)
