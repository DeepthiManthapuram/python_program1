

product_list=[]
print("Cart Operations:1. Add Product2. Remove Product3. Search Product4. Display Cart5. Count Products6. Exit")



while(True):
        choice = int(input("Enter choice:"))

        if(choice == 1):
            product = input("Enter product to add:")
            product_list.append(product)
            print(f"{product} added to cart.")

        elif(choice == 2):
            p = input("Enter product to remove:")
            if(p in product_list):
                product_list.remove(p)
                print(f"{p} removed from cart.")

        elif(choice == 3):
            p= input("Enter product to search:")
            if p in product_list:
                print(f"{p} is in the cart.")

        elif(choice == 4):
            print("Products in cart:", product_list)

        elif(choice == 5):
            print("Total products in cart:",len(product_list))

        elif(choice == 6):
            product_list.sort()
            print("sorted cart items:",product_list)
        
        elif(choice == 7):
            product_list.clear()
            print(product_list)
        else:
            print("Exiting...")

        
    
