# from django.contrib import admin
# from graveyards.models import Graveyard, Parcel
#
#
# # Register your models here.
# @admin.register(Graveyard)
# class GraveyardAdmin(admin.ModelAdmin):
#     list_display = ('name', 'address', 'created_at', 'updated_at',)
#     ordering = ('name',)
#     search_fields = ('name',)
#
#     # def get_queryset(self, request):
#     #     queryset = super().get_queryset(request)
#     #     if not request.user.is_superuser:
#     #         return queryset.filter(owner=request.user)
#     #     return queryset
#
#
# @admin.register(Parcel)
# class ParcelAdmin(admin.ModelAdmin):
#     list_display = ('status', 'created_at', 'updated_at',)
#     ordering = ('status',)
#     # search_fields = ('status',)
#
#     def get_queryset(self, request):
#         queryset = super().get_queryset(request)
#         if not request.user.is_superuser:
#             return queryset.filter(graveyard=request.user)
#         return queryset