from django import admin

class ModelOwnerAdmin(admin.ModelAdmin):
    """
    A base ModelAdmin to be used with django_extras
    ModelOwner mixins. Checks if requesting user is
    the model owner or a superuser. Superusers are
    owners of all models implicitely.
    """
    def has_add_permission(self, request, obj=None):
        if obj:
            return super(OwnerModelAdmin, self).has_add_permission(request, obj=obj) and obj.is_owned_by(request.user, include_superuser=True)
        else:
            return super(OwnerModelAdmin, self).has_add_permission(request, obj=obj)

    def has_change_permission(self, request, obj=None):
        if obj:
            return super(OwnerModelAdmin, self).has_change_permission(request, obj=obj) and obj.is_owned_by(request.user, include_superuser=True)
        else:
            return super(OwnerModelAdmin, self).has_change_permission(request, obj=obj)

    def has_delete_permission(self, request, obj=None):
        if obj:
            return super(OwnerModelAdmin, self).has_delete_permission(request, obj=obj) and obj.is_owned_by(request.user, include_superuser=True)
        else:
            return super(OwnerModelAdmin, self).has_delete_permission(request, obj=obj)

    def get_queryset(self, request):
        qs = super(MyModelAdmin, self).get_queryset(request)
        return qs.owned_by(request.user, include_superuser=True)

    def get_form(request, obj=None, **kwargs):
        """
        Hides the owner field from non-superusers.
        """
        if request.user.is_superuser:
            return super(ModelOwnerAdmin, self).get_form(request, obj=obj, **kwargs)
        else:
            if 'exclude' in kwargs:
                kwargs['exclude'] = kwargs['exclude'] + (self.model.objects.owner_filter,)
            else:
                kwargs['exclude'] = (self.model.objects.owner_filter,)
            return super(ModelOwnerAdmin, self).get_form(request, obj=obj, **kwargs)
