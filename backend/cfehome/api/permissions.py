from rest_framework import permissions

# def has_permission(self, request, view):
#     user = request.user

#     print(user.get_all_permissions())
#     if user.is_staff:
#         if user.has_perm("products.create_product"): # "app_name.verb_model_name". App posts = "posts.create_post"
#             return True
#         if user.has_perm("products.view_product"):
#             return True
#         if user.has_perm("products.change_product"):
#             return True
#         if user.has_perm("products.delete_product"):
#             return True
#         return False

#     return False

    # def has_permission(self, request, view):
    #     if not request.user.is_staff:
    #         return False

    #     return super().has_permission(request, view)


class IsStaffEditorPermission(permissions.DjangoModelPermissions):

    perms_map = {
        "GET": ["%(app_label)s.view_%(model_name)s"],
        "OPTIONS": [],
        "HEAD": [],
        "POST": ["%(app_label)s.add_%(model_name)s"],
        "PUT": ["%(app_label)s.change_%(model_name)s"],
        "PATCH": ["%(app_label)s.change_%(model_name)s"],
        "DELETE": ["%(app_label)s.delete_%(model_name)s"],
    }


