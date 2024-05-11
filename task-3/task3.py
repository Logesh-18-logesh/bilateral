import mysql.connector
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Logesh18",
    database="ecommerce"
)

cursor = conn.cursor()

try:
    # 1. Verify Customer's Order
    cursor.execute("SELECT * FROM orders WHERE customer_id = 101 AND product_id = 1;")
    customer_order = cursor.fetchone()
    print("Customer's Order:", customer_order)

    # 2. Check Inventory Status
    cursor.execute("SELECT * FROM inventory WHERE product_id = 1;")
    inventory_status = cursor.fetchone()
    print("Inventory Status:", inventory_status)

    # 3. Review Order History
    cursor.execute("SELECT * FROM order_history WHERE product_id = 1 AND order_date <= '2024-05-10';")
    order_history = cursor.fetchall()
    print("Order History:")
    for history in order_history:
        print(history)

    # 4. Check for Recent Stock Updates
    cursor.execute("SELECT * FROM stock_updates WHERE product_id = 1 ORDER BY update_date DESC LIMIT 1;")
    recent_stock_update = cursor.fetchone()
    print("Recent Stock Update:", recent_stock_update)

except mysql.connector.Error as e:
    print("Error:", e)

finally:
    cursor.close()
    conn.close()
