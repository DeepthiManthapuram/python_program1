def apply_discount(price,discount):
    price-=(price*(discount/100))
    return price
def add_gst(price,gst_percent=18):
    price+=(price*(gst_percent/100))
    return price
def generate_invoice(cart,discount=0, gst_percent=18):
    print("----------Invoice--------")
    for k,v in cart.items():
        print(f"{k}: {v}")
    print("-------------------------")
    sum=0
    for i in cart.values():
        sum+=i
    d=apply_discount(sum,discount)
    g=add_gst(d)
    print("Subtotal: ",sum)
    print(f"After {discount}% discount: {d}")
    print(f"After {gst_percent}% gst: {g}")
    print("--------------------")
    print("thankyou for shopping with us")