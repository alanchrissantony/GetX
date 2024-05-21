from cart.models import Cart, CartItem
from cart.views import cart_id
from wallet.models import Wallet



def CartCounter(request, total=0, quantity=0):
    
    user = request.user
    if user.id:
        cart_items = CartItem.objects.filter(user=user, is_active=True)
    else:
        try:
            cart = Cart.objects.get(cart_id=cart_id(request))
            cart_items = CartItem.objects.filter(cart=cart, is_active=True)
        except:
            cart_items = {}

    for cart_item in cart_items:
        total += (cart_item.product.price * cart_item.quantity)
        quantity += cart_item.quantity

    context = {
        'cart_view':cart_items,
        'cart_quantity':quantity,
        'cart_total':total
    }
    return context

def WalletProcessor(request, balance=0):
    user = request.user
    if user.id:
        wallet = Wallet.objects.filter(user=user).first()
        if wallet:
            balance = wallet.balance
    context={
        'wallet_balance':balance
    }
    return context
