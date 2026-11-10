import sqlite3

def init_db():
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            amount REAL NOT NULL,
            category TEXT NOT NULL,
            date TEXT NOT NULL
        )
    """)
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS budgets (
            category TEXT PRIMARY KEY,
            limit_amount REAL NOT NULL
        )
    """)
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS savings_goals (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            target_amount REAL NOT NULL,
            current_amount REAL DEFAULT 0.0
        )
    """)
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS blog_posts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            image_url TEXT,
            date TEXT NOT NULL
        )
    """)
    
    conn.commit()
    conn.close()

def add_expense(title, amount, category, date):
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO expenses (title, amount, category, date) VALUES (?, ?, ?, ?)", 
                   (title, amount, category, date))
    conn.commit()
    conn.close()

def get_expenses():
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM expenses ORDER BY date DESC")
    rows = cursor.fetchall()
    conn.close()
    return rows

def delete_expense(expense_id):
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM expenses WHERE id = ?", (expense_id,))
    conn.commit()
    conn.close()

def clear_expenses():
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM expenses")
    cursor.execute("DELETE FROM sqlite_sequence WHERE name='expenses'")
    conn.commit()
    conn.close()

def clear_budgets():
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM budgets")
    conn.commit()
    conn.close()

def delete_budget(category):
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM budgets WHERE category = ?", (category,))
    conn.commit()
    conn.close()

def get_total_spending():
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()
    cursor.execute("SELECT SUM(amount) FROM expenses")
    total = cursor.fetchone()[0]
    conn.close()
    return total if total is not None else 0.0

def set_budget(category, limit_amount):
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO budgets (category, limit_amount) 
        VALUES (?, ?)
        ON CONFLICT(category) DO UPDATE SET limit_amount = ?
    """, (category.title(), limit_amount, limit_amount))
    conn.commit()
    conn.close()

def get_budgets():
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM budgets")
    rows = cursor.fetchall()
    conn.close()
    return rows

def get_category_spending(category):
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()
    cursor.execute("SELECT SUM(amount) FROM expenses WHERE category = ?", (category,))
    total = cursor.fetchone()[0]
    conn.close()
    return total if total is not None else 0.0

def add_savings_goal(name, target_amount, current_amount):
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO savings_goals (name, target_amount, current_amount) VALUES (?, ?, ?)", 
                   (name.title(), target_amount, current_amount))
    conn.commit()
    conn.close()

def get_savings_goals():
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM savings_goals")
    rows = cursor.fetchall()
    conn.close()
    return rows

def delete_savings_goal(goal_id):
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM savings_goals WHERE id = ?", (goal_id,))
    conn.commit()
    conn.close()

def get_daily_summary():
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()
    cursor.execute("""
        SELECT date, SUM(amount), COUNT(*) 
        FROM expenses 
        GROUP BY date 
        ORDER BY date DESC
    """)
    rows = cursor.fetchall()
    conn.close()
    return rows

def get_monthly_summary():
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()
    cursor.execute("""
        SELECT strftime('%Y-%m', date) as month, SUM(amount), COUNT(*) 
        FROM expenses 
        GROUP BY month 
        ORDER BY month DESC
    """)
    rows = cursor.fetchall()
    conn.close()
    return rows

def add_blog_post(title, content, image_url, date):
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO blog_posts (title, content, image_url, date) VALUES (?, ?, ?, ?)", 
                   (title, content, image_url, date))
    conn.commit()
    conn.close()

def get_blog_posts():
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM blog_posts ORDER BY id DESC")
    rows = cursor.fetchall()
    conn.close()
    return rows

def delete_blog_post(post_id):
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM blog_posts WHERE id = ?", (post_id,))
    conn.commit()
    conn.close()