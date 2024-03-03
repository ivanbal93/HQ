from rest_framework import permissions

from .models import StudentProduct, Student, Product


class StudentAccessToProduct(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True

        try:
            return StudentProduct.objects.filter(
                product=obj,
                student=Student.objects.get(user__id=request.user.id)
            ).exists()
        except:
            return False
