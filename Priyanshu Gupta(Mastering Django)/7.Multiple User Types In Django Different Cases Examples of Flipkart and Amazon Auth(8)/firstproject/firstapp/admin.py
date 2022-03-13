from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Cart, Product, ProductInCart, Order, Deal, CustomUser,Customer,Seller#, UserType
from .forms import CustomUserChangeForm,CustomUserCreationForm

# Register your models here.

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('email', 'is_staff', 'is_active',)
    list_filter = ('email', 'is_staff', 'is_active',)
    fieldsets = (
        # (None, {'fields': ('email', 'password', 'usertype')}),
        (None, {'fields': ('email', 'password',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active','is_customer', 'is_seller')}),    
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2','is_staff', 'is_active',)}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)

# admin.site.unregister(User) 
admin.site.register(CustomUser, CustomUserAdmin)
# admin.site.register(User, UserAdmin)

class ProductInCartInline(admin.TabularInline):
    model=ProductInCart

class CartInline(admin.TabularInline):
    model=Cart #onetoonefield foreignkey

class DealInline(admin.TabularInline):
    model=Deal.user.through

# class UserAdmin(UserAdmin):
#     model=User
#     # list_display=('username','get_cart','is_staff','is_active',)
#     list_display=('username','is_staff','is_active',)
#     list_filter=('username','is_staff','is_active', 'is_superuser')
#     fieldsets=(
#         (None,{'fields':('username','password')}),
#         ('Permissions',{'fields':('is_staff',('is_active', 'is_superuser'),)}),
#         # ('Cart',{'fields':('get_cart',)})
#         ('Advance options',{'classes':('collapse',),'fields':('groups','user_permissions'),}),
#     )
#     add_fieldsets=(
#         (None,{
#             'classes':('wide',), #class for css
#             'fields': ('username','password1','password2','is_staff','is_active','is_superuser','groups') # fields shown on create user
#         }),
#     )
#     inlines=[
#         CartInline,DealInline
#     ]

#     # def get_cart(self,obj): # this function only works in list_display
#     #     return obj.cart     # through reverse related relationship
#     search_fields=('username',) # search_filter for search bar
#     ordering=('username',)


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    model=Cart
    list_display=('staff','user','created_on',) # here user__is_staff will not work
    list_filter=('user','created_on',)
    # fields=('staff') # either fields or fieldset
    fieldsets=(
        (None,{'fields':('user','created_on',)}), # only direct relationship no nested relationship('__') ex. user__is_staff
        # ('User',{'fields':('staff',)}),
    )
    inlines=(
        ProductInCartInline,
    )
    # To display only in list_display
    def staff(self,obj):
        return obj.user.is_staff
    # staff.empty_value_display='???'
    staff.admin_order_field='user__is_staff' # Allows column order sorting
    staff.short_description='Staff User' # Renames column head

    # filtering on side - for same reason, this works
    list_filter=['user__is_staff', 'created_on'] # with direct foreign key(user) no error but not show in filters, with function error 
    # ordering=['user',]
    search_fields=['user__name'] # with direct foreign key no error but filtering is not possible directly


class DealAdmin(admin.ModelAdmin):
    inlines=[
        DealInline,
    ]
    exclude=('user',)

admin.site.register(Product)
admin.site.register(ProductInCart)
admin.site.register(Order)
admin.site.register(Deal,DealAdmin)
# admin.site.register(UserType)
admin.site.register(Customer)
admin.site.register(Seller)