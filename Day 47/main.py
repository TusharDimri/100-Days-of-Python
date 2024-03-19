import smtplib
import product

BUY_PRICE = 200
url = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"

product_details = product.get_product_price(url=url)

if product_details.price < BUY_PRICE:
    message = f"{product_details.title} is now {product_details.price}"

    with smtplib.SMTP("YOUR_SMTP_ADDRESS", port=587) as connection:
        connection.starttls()
        result = connection.login("YOUR_EMAIL", "YOUR_PASSWORD")
        connection.sendmail(
            from_addr="YOUR_EMAIL",
            to_addrs="YOUR_EMAIL",
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}".encode("utf-8")
        )