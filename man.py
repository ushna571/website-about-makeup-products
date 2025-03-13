import streamlit as st

# Sample data for products
products = [
    {"id": 1, "name": "Lipstick", "price": 20, "discount_price": 15, "category": "Makeup", "image": "lipstick.png"},
    {"id": 2, "name": "Foundation", "price": 30, "discount_price": 25, "category": "Makeup", "image": "foundation.png"},
    {"id": 3, "name": "Mascara", "price": 18, "discount_price": 14, "category": "Makeup", "image": "mascara.png"},
    {"id": 4, "name": "Blush", "price": 22, "discount_price": 18, "category": "Makeup", "image": "blush.png"},
    {"id": 5, "name": "Eyeshadow Palette", "price": 35, "discount_price": 30, "category": "Makeup", "image": "eyeshadow.png"},
    {"id": 6, "name": "Compact Powder", "price": 25, "discount_price": 20, "category": "Makeup", "image": "compact.png"},
    {"id": 7, "name": "Brushes", "price": 40, "discount_price": 35, "category": "Makeup", "image": "brushes.png"},
]

# Initialize session state for cart
if 'cart' not in st.session_state:
    st.session_state.cart = []

# Function to display products
def display_products(products, discount=False):
    for product in products:
        st.image(product["image"], width=150)
        price = product["discount_price"] * 0.9 if discount else product["discount_price"]
        st.write(f"**{product['name']}** - Original Price: ${product['price']} (Discounted Price: ${price:.2f})")
        if st.button(f"Add to Cart - {product['name']}", key=f"{'new_' if discount else ''}{product['id']}"):
            st.session_state.cart.append(product)
            st.success(f"Added {product['name']} to cart!")

# Function to add all products to cart
def add_all_products_to_cart(products):
    for product in products:
        st.session_state.cart.append(product)
    st.success("All products have been added to the cart!")

# Sidebar navigation
st.sidebar.image("logo.png", width=150)  # Add your logo image path here
st.sidebar.title("Celeste Cosmetics")
st.sidebar.header("Categories")
categories = ["Home", "Shop", "New Arrivals", "Customer Reviews", "Contact Us", "FAQs"]
selection = st.sidebar.radio("Go to", categories)

# Display cart in sidebar
st.sidebar.header("Your Cart")
if st.session_state.cart:
    for item in st.session_state.cart:
        st.sidebar.write(f"**{item['name']}** - ${item['price']} (Discount: ${item['discount_price']})")
else:
    st.sidebar.write("Your cart is empty.")

# Display pages based on selection
if selection == "Home":
    st.title("Welcome to Celeste Cosmetics")
    st.image("blush.png", width=300)  # Add your special product image here
    st.image("lipstick.png", width=300)  # Add your special product image here
    st.image("mascara.png", width=300)  # Add your special product image here
    if st.button("Add All Products to Cart"):
        add_all_products_to_cart(products)

elif selection == "Shop":
    st.title("Shop")
    display_products(products)
    if st.button("Add All Products to Cart"):
        add_all_products_to_cart(products)

elif selection == "New Arrivals":
    st.title("New Arrivals")
    st.write("Special discount for upcoming customers! Get an additional 10% off on all new arrivals.")
    display_products(products, discount=True)

elif selection == "Customer Reviews":
    st.title("Customer Reviews")
    st.write("We value your feedback! Please leave your review below.")
    
    # Form to submit a new review
    with st.form(key='review_form'):
        name = st.text_input("Name")
        review = st.text_area("Review")
        image = st.file_uploader("Upload an image of the product", type=["jpg", "jpeg", "png"])
        submit_button = st.form_submit_button(label='Submit Review')
        
        if submit_button:
            if name and review:
                st.success("Thank you for your review!")
                if image:
                    st.image(image, width=150)
                st.write(f"**{name}**: {review}")
            else:
                st.error("Please fill in all fields.")

elif selection == "Contact Us":
    st.title("Contact Us")
    st.write("Phone: +1234567890")
    st.write("Instagram: [@celeste_cosmetics](https://www.instagram.com/celeste_cosmetics)")
    st.write("Facebook: [Celeste Cosmetics](https://www.facebook.com/celeste_cosmetics)")

elif selection == "FAQs":
    st.title("Frequently Asked Questions")
    faqs = [
        ("What is your return policy?", "We accept returns within 30 days of purchase. Please ensure the product is unused and in its original packaging."),
        ("Do you offer international shipping?", "Yes, we offer international shipping. Shipping charges may vary based on the destination."),
        ("How can I track my order?", "Once your order is shipped, you will receive a tracking number via email."),
        ("Can I change or cancel my order?", "You can change or cancel your order within 24 hours of placing it. Please contact our customer service for assistance."),
        ("Do you offer gift wrapping?", "Yes, we offer gift wrapping for an additional charge. You can select this option at checkout."),
        ("Are your products cruelty-free?", "Yes, all our products are cruelty-free and not tested on animals."),
        ("How can I contact customer service?", "You can contact our customer service via phone, email, or social media. Visit the 'Contact Us' page for more details.")
    ]
    for question, answer in faqs:
        st.write(f"**Q: {question}**")
        st.write(f"A: {answer}")
    for question, answer in faqs:
        st.write(f"**Q: {question}**")
        st.write(f"A: {answer}")
