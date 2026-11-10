import sqlite3

def init_db():
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()
    
    # Drop old tables so they recreate with username isolation
    cursor.execute("DROP TABLE IF EXISTS expenses")
    cursor.execute("DROP TABLE IF EXISTS budgets")
    cursor.execute("DROP TABLE IF EXISTS savings_goals")
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            title TEXT NOT NULL,
            amount REAL NOT NULL,
            category TEXT NOT NULL,
            date TEXT NOT NULL
        )
    """)
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS budgets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            category TEXT NOT NULL,
            limit_amount REAL NOT NULL
        )
    """)
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS savings_goals (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
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
    
def add_expense(username, title, amount, category, date):
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO expenses (username, title, amount, category, date) VALUES (?, ?, ?, ?, ?)", 
                   (username, title, amount, category, date))
    conn.commit()
    conn.close()

def get_expenses(username):
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, title, amount, category, date FROM expenses WHERE username = ? ORDER BY date DESC", (username,))
    rows = cursor.fetchall()
    conn.close()
    return rows

def delete_expense(expense_id, username):
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM expenses WHERE id = ? AND username = ?", (expense_id, username))
    conn.commit()
    conn.close()

def clear_expenses(username):
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM expenses WHERE username = ?", (username,))
    conn.commit()
    conn.close()

def clear_budgets(username):
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM budgets WHERE username = ?", (username,))
    conn.commit()
    conn.close()

def delete_budget(category, username):
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM budgets WHERE category = ? AND username = ?", (category, username))
    conn.commit()
    conn.close()

def get_total_spending(username):
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()
    cursor.execute("SELECT SUM(amount) FROM expenses WHERE username = ?", (username,))
    total = cursor.fetchone()[0]
    conn.close()
    return total if total is not None else 0.0

def set_budget(username, category, limit_amount):
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()
    # Check if budget already exists for this user and category
    cursor.execute("SELECT id FROM budgets WHERE username = ? AND category = ?", (username, category.title()))
    row = cursor.fetchone()
    if row:
        cursor.execute("UPDATE budgets SET limit_amount = ? WHERE username = ? AND category = ?", (limit_amount, username, category.title()))
    else:
        cursor.execute("INSERT INTO budgets (username, category, limit_amount) VALUES (?, ?, ?)", (username, category.title(), limit_amount))
    conn.commit()
    conn.close()

def get_budgets(username):
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()
    cursor.execute("SELECT category, limit_amount FROM budgets WHERE username = ?", (username,))
    rows = cursor.fetchall()
    conn.close()
    return rows

def get_category_spending(category, username):
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()
    cursor.execute("SELECT SUM(amount) FROM expenses WHERE category = ? AND username = ?", (category, username))
    total = cursor.fetchone()[0]
    conn.close()
    return total if total is not None else 0.0

def add_savings_goal(username, name, target_amount, current_amount):
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO savings_goals (username, name, target_amount, current_amount) VALUES (?, ?, ?, ?)", 
                   (username, name.title(), target_amount, current_amount))
    conn.commit()
    conn.close()

def get_savings_goals(username):
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, target_amount, current_amount FROM savings_goals WHERE username = ?", (username,))
    rows = cursor.fetchall()
    conn.close()
    return rows

def delete_savings_goal(goal_id, username):
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM savings_goals WHERE id = ? AND username = ?", (goal_id, username))
    conn.commit()
    conn.close()

def get_daily_summary(username):
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()
    cursor.execute("""
        SELECT date, SUM(amount), COUNT(*) 
        FROM expenses 
        WHERE username = ?
        GROUP BY date 
        ORDER BY date DESC
    """, (username,))
    rows = cursor.fetchall()
    conn.close()
    return rows

def get_monthly_summary(username):
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()
    cursor.execute("""
        SELECT strftime('%Y-%m', date) as month, SUM(amount), COUNT(*) 
        FROM expenses 
        WHERE username = ?
        GROUP BY month 
        ORDER BY month DESC
    """, (username,))
    rows = cursor.fetchall()
    conn.close()
    return rows

# Blog functions remain global for the admin
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