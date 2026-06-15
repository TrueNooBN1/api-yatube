from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Разрешает редактирование/удаление только автору объекта.
    Для небезопасных методов (POST, PUT, PATCH, DELETE) проверяет авторство.
    """
    def has_object_permission(self, request, view, obj):
        # Чтение разрешено всем
        if request.method in permissions.SAFE_METHODS:
            return True
        # Запись/изменение/удаление – только автору
        return obj.author == request.user