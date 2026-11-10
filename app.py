import datetime
from flask import Flask, render_template, request, redirect, url_for, session
import database

app = Flask(__name__)
app.secret_key = "your_secret_key_here"  # Needed for session management

# Initialize database tables on startup
database.init_db()

# Currency dictionary for the dropdown
CURRENCIES = {
    '₦': 'Nigerian Naira (NGN)',
    '$': 'US Dollar (USD)',
    '€': 'Euro (EUR)',
    '£': 'British Pound (GBP)',
    'C$': 'Canadian Dollar (CAD)',
    'A$': 'Australian Dollar (AUD)',
    '¥': 'Japanese Yen (JPY)',
    '₹': 'Indian Rupee (INR)'
}

DAILY_TIPS = [
    "Track every single expense, no matter how small—awareness is the first step to saving.",
    "Try the 50/30/20 rule: 50% needs, 30% wants, 20% savings.",
    "Always pay yourself first by putting money into savings before spending on discretionary items.",
    "Avoid impulse buying by waiting 24 hours before purchasing non-essential items.",
    "Review your subscriptions monthly and cancel any services you haven't used recently.",
    "Set clear financial goals so every dollar you save has a specific purpose.",
    "Cook meals at home instead of eating out to see massive savings over time."
]

@app.before_request
def before_request():
    if 'currency' not in session:
        session['currency'] = '₦'
    if 'user_name' not in session:
        session['user_name'] = 'Friend'  # Default greeting for regular visitors

@app.route("/set_currency", methods=["POST"])
def set_currency():
    selected_currency = request.form.get("currency")
    if selected_currency in CURRENCIES:
        session['currency'] = selected_currency
    return redirect(request.referrer or url_for('home'))

@app.route("/")
def home():
    return render_template("home.html", currency=session.get('currency', '₦'), currencies=CURRENCIES)

@app.route("/dashboard")
def index():
    current_user = session.get('user_name', 'Friend')
    expenses = database.get_expenses(current_user)
    total = database.get_total_spending(current_user)
    raw_budgets = database.get_budgets(current_user)
    goals = database.get_savings_goals(current_user)
    
    day_of_year = datetime.datetime.now().timetuple().tm_yday
    daily_tip = DAILY_TIPS[(day_of_year - 1) % len(DAILY_TIPS)]
    
    budgets = []
    for cat, limit in raw_budgets:
        spent = database.get_category_spending(cat, current_user)
        remaining = limit - spent
        percentage = (spent / limit * 100) if limit > 0 else 0
        budgets.append({
            "category": cat,
            "limit": limit,
            "spent": spent,
            "remaining": remaining,
            "percentage": round(percentage, 1)
        })
        
    return render_template("index.html", total=total, budgets=budgets, goals=goals, expenses=expenses[:5], 
                           currency=session.get('currency', '₦'), currencies=CURRENCIES, daily_tip=daily_tip)

@app.route("/expenses")
def expenses_page():
    current_user = session.get('user_name', 'Friend')
    expenses = database.get_expenses(current_user)
    total = database.get_total_spending(current_user)
    return render_template("expenses.html", expenses=expenses, total=total, 
                           currency=session.get('currency', '₦'), currencies=CURRENCIES)

@app.route("/budgets")
def budgets_page():
    current_user = session.get('user_name', 'Friend')
    raw_budgets = database.get_budgets(current_user)
    budgets = []
    for cat, limit in raw_budgets:
        spent = database.get_category_spending(cat, current_user)
        remaining = limit - spent
        percentage = (spent / limit * 100) if limit > 0 else 0
        budgets.append({
            "category": cat,
            "limit": limit,
            "spent": spent,
            "remaining": remaining,
            "percentage": round(percentage, 1)
        })
    return render_template("budgets.html", budgets=budgets, 
                           currency=session.get('currency', '₦'), currencies=CURRENCIES)

@app.route("/savings")
def savings_page():
    current_user = session.get('user_name', 'Friend')
    goals = database.get_savings_goals(current_user)
    return render_template("savings.html", goals=goals, 
                           currency=session.get('currency', '₦'), currencies=CURRENCIES)

@app.route("/reports")
def reports_page():
    current_user = session.get('user_name', 'Friend')
    daily_summary = database.get_daily_summary(current_user)
    monthly_summary = database.get_monthly_summary(current_user)
    return render_template("reports.html", daily=daily_summary, monthly=monthly_summary, 
                           currency=session.get('currency', '₦'), currencies=CURRENCIES)

# --- SECURE BLOG & ADMIN ROUTES ---

@app.route("/blog")
def blog_page():
    posts = database.get_blog_posts()
    return render_template("blog.html", posts=posts, currency=session.get('currency', '₦'), currencies=CURRENCIES)

@app.route("/admin/login", methods=["GET", "POST"])
def admin_login():
    if request.method == "POST":
        passcode = request.form.get("passcode")
        if passcode == "mysecretpassword":  # Owner passcode
            session['is_admin'] = True
            session['user_name'] = 'Ikeli'  # Automatically sets your owner name when you log in
            return redirect(url_for("admin_blog"))
        else:
            return render_template("admin_login.html", error="Incorrect Passcode", currency=session.get('currency', '₦'), currencies=CURRENCIES)
    return render_template("admin_login.html", currency=session.get('currency', '₦'), currencies=CURRENCIES)

@app.route("/admin/blog", methods=["GET", "POST"])
def admin_blog():
    if not session.get('is_admin'):
        return redirect(url_for("admin_login"))
        
    if request.method == "POST":
        title = request.form.get("title")
        content = request.form.get("content")
        image_url = request.form.get("image_url")
        date = request.form.get("date")
        database.add_blog_post(title, content, image_url, date)
        return redirect(url_for("blog_page"))
        
    posts = database.get_blog_posts()
    return render_template("admin_blog.html", posts=posts, currency=session.get('currency', '₦'), currencies=CURRENCIES)

@app.route("/admin/blog/delete/<int:post_id>")
def delete_blog(post_id):
    if not session.get('is_admin'):
        return redirect(url_for("admin_login"))
    database.delete_blog_post(post_id)
    return redirect(url_for("admin_blog"))

# --- USER DATA ACTION ROUTES ---

@app.route("/add", methods=["POST"])
def add():
    current_user = session.get('user_name', 'Friend')
    title = request.form.get("title").title()
    amount = float(request.form.get("amount"))
    category = request.form.get("category").title()
    date = request.form.get("date")
    database.add_expense(current_user, title, amount, category, date)
    return redirect(url_for("expenses_page"))

@app.route("/set_budget", methods=["POST"])
def set_budget():
    current_user = session.get('user_name', 'Friend')
    category = request.form.get("category").title()
    limit_amount = float(request.form.get("limit_amount"))
    database.set_budget(current_user, category, limit_amount)
    return redirect(url_for("budgets_page"))

@app.route("/add_goal", methods=["POST"])
def add_goal():
    current_user = session.get('user_name', 'Friend')
    name = request.form.get("name").title()
    target_amount = float(request.form.get("target_amount"))
    current_amount = float(request.form.get("current_amount") or 0.0)
    database.add_savings_goal(current_user, name, target_amount, current_amount)
    return redirect(url_for("savings_page"))

@app.route("/delete/<int:expense_id>")
def delete(expense_id):
    current_user = session.get('user_name', 'Friend')
    database.delete_expense(expense_id, current_user)
    return redirect(url_for("expenses_page"))

@app.route("/delete_budget/<string:category>")
def delete_budget(category):
    current_user = session.get('user_name', 'Friend')
    database.delete_budget(category, current_user)
    return redirect(url_for("budgets_page"))

@app.route("/delete_goal/<int:goal_id>")
def delete_goal(goal_id):
    current_user = session.get('user_name', 'Friend')
    database.delete_savings_goal(goal_id, current_user)
    return redirect(url_for("savings_page"))

@app.route("/clear_prompt")
def clear_prompt():
    return render_template("clear_prompt.html", currency=session.get('currency', '₦'), currencies=CURRENCIES)

@app.route("/execute_clear", methods=["POST"])
def execute_clear():
    current_user = session.get('user_name', 'Friend')
    choice = request.form.get("clear_budgets")
    database.clear_expenses(current_user)
    if choice == "yes":
        database.clear_budgets(current_user)
    return redirect(url_for("expenses_page"))

@app.route("/login", methods=["GET", "POST"])
def user_login():
    if request.method == "POST":
        name = request.form.get("user_name")
        if name:
            session['user_name'] = name.title()
        return redirect(url_for('home'))
    return render_template("user_login.html", currency=session.get('currency', '₦'), currencies=CURRENCIES)

if __name__ == "__main__":
    app.run(debug=True)