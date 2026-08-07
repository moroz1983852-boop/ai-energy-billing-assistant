import pymysql

def get_db_connection():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="",
        database="ai_billing_db",
        cursorclass= pymysql.cursors.DictCursor
    )

def init_db():
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS customers (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                email VARCHAR(100) UNIQUE NOT NULL
                )
            """)

            cursor.execute("""
            CREATE TABLE IF NOT EXISTS bills (
                id INT AUTO_INCREMENT PRIMARY KEY,
                customer_id INT,
                amount DECIMAL(10, 2) NOT NULL,
                is_paid TINYINT(1) DEFAULT 0,
                FOREIGN KEY (customer_id) REFERENCES customers(id)
                )
            """)

            cursor.execute("SELECT COUNT(*) AS total FROM customers")
            result = cursor.fetchone()

            if result["total"] == 0:
                cursor.execute("""
                    INSERT INTO customers (id, name, email)
                    VALUES (1, 'Vova', 'vova@energy-billing.de')
                """)

                cursor.execute("""
                INSERT INTO customers (id, name, email)
                VALUES (2, 'Max', 'max@energy-billing.de')
                """)

                cursor.execute("""
                    INSERT INTO bills (customer_id, amount, is_paid)
                    VALUES (1, 75.20, 1)
                """)

                cursor.execute("""
                    INSERT INTO bills (customer_id, amount, is_paid)
                    VALUES (1, 250.00, 0)
                """)

                cursor.execute("""
                    INSERT INTO bills (customer_id, amount, is_paid)
                    VALUES (2, 120.45, 1)
                """)

                print("Testdaten wurden erfolgreich hinzugefügt!")

            connection.commit()
            print("Tabelle 'customers' und 'bills' erfolgreich erstellt!")
    finally:
        connection.close()

def get_customer_debts(email: str):
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM customers WHERE email = %s", (email,))
            customer = cursor.fetchone()

            if not customer:
                return None
            cursor.execute("""
            SELECT SUM(amount) AS total_debt
            FROM bills 
            WHERE customer_id = %s AND is_paid = 0
            """, (customer["id"],))

            debt_result = cursor.fetchone()

            total_debt = debt_result["total_debt"] if debt_result["total_debt"] is not None else 0.00

            return {
                "name": customer["name"],
                "email": customer["email"],
                "total_debt": float(total_debt)
            }

    finally:
        connection.close()

def add_new_customer(name: str, email: str):
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT id FROM customers WHERE email = %s", (email,))
            existing_customer = cursor.fetchone()
            if existing_customer:
                return {"error": "Ein Kunde mit dieser E-Mail existiert bereits!"}

            cursor.execute("""
                INSERT INTO customers (name, email)
                VALUES (%s, %s)
            """, (name, email))

            connection.commit()
            return {"success": f"Kunde {name} erfolgreich registriert!"}
    finally:
        connection.close()