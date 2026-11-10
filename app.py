from flask import Flask, render_template, request, redirect, url_for, session
import database
import datetime

app = Flask(__name__)
app.secret_key = "spendwise_global_secret_key"

database.init_db()

CURRENCIES = {
    "₦": "Nigerian Naira (₦)",
    "$": "US Dollar ($)",
    "€": "Euro (€)",
    "£": "British Pound (£)",
    "CA$": "Canadian Dollar (CA$)",
    "A$": "Australian Dollar (A$)",
    "¥": "Japanese Yen (¥)"
}

DAILY_TIPS = [
    "Pay yourself first: set aside savings before you start spending.",
    "Track every penny: awareness is the first step to financial control.",
    "Avoid impulse buying: wait 24 hours before making non-essential purchases.",
    "Review your subscriptions today—cancel what you no longer use.",
    "Build your emergency fund a little bit at a time; consistency is key.",
    "Small daily savings compound into massive freedom over time.",
    "Never rely on a single income stream; nurture a secondary skill or hustle.",
    "Distinguish clearly between your absolute needs and temporary wants.",
    "A budget doesn't restrict your freedom; it gives you clarity and control.",
    "Review your active category budgets today to stay well ahead of limits.",
    "Automate your savings so you never have to rely on willpower alone.",
    "High-interest debt is an emergency—tackle it aggressively.",
    "Invest in your own knowledge; financial literacy pays the best dividends.",
    "Audit your bank statements monthly to catch hidden fees or leaks.",
    "Always shop with a grocery list to prevent unnecessary cart additions.",
    "Live below your means today so you can live above them tomorrow.",
    "Define your financial goals clearly with specific timelines and amounts.",
    "Protect your income with adequate insurance coverage for peace of mind.",
    "Treat windfalls (bonuses, gifts) like savings opportunities, not spending sprees.",
    "Beware of lifestyle inflation as your income grows.",
    "Compound interest is the eighth wonder of the world—start early.",
    "Keep your fixed expenses as low as possible to maximize flexibility.",
    "Learn to say 'no' to social spending that doesn't align with your goals.",
    "Check your credit score regularly and maintain healthy credit habits.",
    "Compare prices online before making major appliance or tech purchases.",
    "Build a 3 to 6-month emergency cushion before jumping into riskier investments.",
    "Diversify your income streams to insulate yourself against economic shocks.",
    "Negotiate your bills and subscription rates annually.",
    "Remember that time in the market beats timing the market.",
    "Avoid buying things you don't need with money you don't have to impress people you don't like.",
    "Set up a sinking fund for predictable annual expenses like insurance or holidays.",
    "Keep your investment strategy simple, consistent, and long-term.",
    "Rebalance your portfolio or savings allocations at least once a year.",
    "Make saving a habit rather than an afterthought.",
    "Patience is your greatest asset when building long-term wealth.",
    "Avoid retail therapy; find healthier, free ways to destress.",
    "Keep a dedicated folder or digital vault for all important financial documents.",
    "Understand the difference between good debt (assets) and bad debt (liabilities).",
    "Don't invest in anything you don't fully understand.",
    "Celebrate small financial milestones to stay motivated on your journey.",
    "Plan your meals weekly to dramatically cut down on restaurant and takeout spending.",
    "Pay off your credit card balance in full every single month to avoid interest.",
    "Build an attitude of gratitude; contentment reduces the urge to overspend.",
    "Review your utility usage and find ways to cut energy and water waste.",
    "Treat your future self as your most important dependent.",
    "Keep your financial goals private and your discipline public.",
    "Always read the fine print before signing any financial contract or loan.",
    "Establish a monthly money date with yourself to review your ledger.",
    "Prioritize experiences over accumulating clutter.",
    "Learn basic cooking skills; eating out is one of the biggest wealth drains.",
    "Don't let emotions dictate your investment or spending decisions.",
    "Create a buffer in your checking account to avoid accidental overdraft fees.",
    "Give generously when you can, but never at the expense of your own stability.",
    "Take advantage of employer-matching retirement programs if available.",
    "Keep track of your net worth quarterly to watch your progress compound.",
    "Buy quality items that last longer rather than cheap items you must replace often.",
    "Always get a second opinion or quote before undertaking major repairs.",
    "Maintain a zero-based budget mindset: every unit of currency has a job.",
    "Avoid checking your investment balances every day to prevent emotional panic.",
    "Understand your risk tolerance before committing funds to volatile assets.",
    "Keep your emergency fund in a liquid, easily accessible high-yield account.",
    "Set clear boundaries with family and friends regarding lending money.",
    "Master the art of delayed gratification; it is the cornerstone of wealth.",
    "Learn to negotiate prices, whether buying a car or contracting a service.",
    "Cut your commute costs by carpooling, biking, or utilizing public transit when possible.",
    "Never invest money you cannot afford to lose or tie up long-term.",
    "Keep your passwords, financial logins, and backups ultra-secure.",
    "Read at least one foundational book on personal finance every year.",
    "Avoid lifestyle comparisons on social media; most of it is curated illusion.",
    "Use cash or debit instead of credit if you struggle with impulse spending.",
    "Check your tax deductions and credits to ensure you aren't overpaying.",
    "Build a resilient mindset that views financial setbacks as learning curves.",
    "Establish a sinking fund for vehicle maintenance and unexpected repairs.",
    "Keep your goals visible—print them out or set them as your wallpaper.",
    "Remember that financial freedom gives you the power to choose your path.",
    "Take time to understand inflation and how it impacts your purchasing power.",
    "Always maintain a healthy separation between your personal and business funds.",
    "Avoid co-signing loans unless you are fully prepared to pay them off yourself.",
    "Focus on increasing your earning potential through continuous skill acquisition.",
    "Keep your home energy-efficient to shave down monthly utility bills.",
    "Practice mindful spending: ask 'Does this add genuine value to my life?'",
    "Establish clear financial roles and open communication if you share finances.",
    "Avoid keeping large sums of cash sitting idle in low-yield checking accounts.",
    "Schedule periodic financial decluttering sessions to review assets and debts.",
    "Embrace frugality as a tool for freedom, not as a punishment.",
    "Don't try to time the economy; focus on your personal savings rate instead.",
    "Protect your physical and mental health—medical bills are a primary cause of debt.",
    "Keep your financial records organized so tax season is stress-free.",
    "Learn how compounding works against you when paying high interest rates.",
    "Build relationships with mentors who have achieved financial wisdom.",
    "Turn off shopping app notifications to reduce subconscious temptation.",
    "Invest in tools and software that save you time and protect your data.",
    "Reevaluate your insurance policies every few years to find better rates.",
    "Keep your financial vision anchored on long-term peace of mind.",
    "Celebrate progress, not perfection; every step forward counts.",
    "Understand your spending triggers and build healthy coping mechanisms.",
    "Protect your digital identity against phishing and financial fraud.",
    "Make peace with your financial past and focus entirely on your future.",
    "Commit to continuous financial learning; the economic landscape always evolves.",
    "Your wealth is measured by the peace of mind it buys, not just the numbers.",
    # Days 101 - 200
    "Review your insurance deductibles to find the sweet spot for your risk profile.",
    "Avoid holding excessive cash beyond your emergency fund; let idle money work.",
    "Separate your needs, wants, and savings into distinct mental or physical accounts.",
    "Schedule an annual review for all your monthly service providers and utilities.",
    "Learn the basics of tax-advantaged accounts available in your region.",
    "Practice the '30-day rule' for major non-essential purchases.",
    "Keep your emergency fund untouched except for genuine, unforeseen crises.",
    "Treat your career like a business; constantly upgrade your marketable skills.",
    "Understand that financial discipline is a muscle that strengthens with use.",
    "Avoid buying brand-new items when high-quality secondhand options exist.",
    "Maintain a clear record of all digital subscriptions and auto-renewals.",
    "Focus on reducing your cost of living before seeking complex investment vehicles.",
    "Cultivate patience; wealth accumulation is a marathon, not a sprint.",
    "Never underestimate the power of a small, consistent monthly contribution.",
    "Keep your financial aspirations aligned with your core personal values.",
    "Review your bank's fee schedule to ensure you aren't leaking money needlessly.",
    "Build a network of supportive peers who value financial growth and education.",
    "Set up automated notifications for low account balances to avoid overdrafts.",
    "Recognize that saying no to unnecessary expenses is saying yes to your future.",
    "Keep your debt-to-income ratio as low as possible for financial flexibility.",
    "Learn to differentiate between asset classes: stocks, real estate, cash, and bonds.",
    "Revisit your budget monthly to adjust for changing seasonal expenses.",
    "Avoid emotional spending triggered by stress, fatigue, or boredom.",
    "Ensure your beneficiaries and estate documents are updated regularly.",
    "Take full advantage of free educational resources and financial libraries.",
    "Keep your financial goals realistic yet challenging enough to inspire growth.",
    "Prioritize paying off high-fee consumer loans over low-interest obligations.",
    "Practice mindful grocery shopping to minimize food waste and save cash.",
    "Keep a running log of your monthly financial wins, no matter how small.",
    "Understand how currency fluctuations can impact your savings and purchasing power.",
    "Build a robust password management routine to safeguard your financial portals.",
    "Avoid chasing speculative trends or 'get rich quick' investment schemes.",
    "Embrace minimalist principles to reduce clutter and curb impulse buying.",
    "Verify that your emergency fund yield beats or matches baseline inflation.",
    "Schedule regular check-ins with your partner or family to discuss money goals.",
    "Keep your financial stress in check by focusing only on factors you can control.",
    "Invest in durable household goods that require fewer replacements over time.",
    "Learn the mechanics of compound inflation and how it erodes uninvested cash.",
    "Keep your financial records transparent and easily accessible for emergencies.",
    "Avoid upgrading your phone or tech gadgets until they stop serving your needs.",
    "Establish clear criteria before lending your time, money, or resources.",
    "Treat every dollar as an employee working hard for your future freedom.",
    "Review your investment fees annually; high expense ratios eat your returns.",
    "Build resilience by having multiple backup plans for your primary income.",
    "Keep your financial ledger up to date every single week without fail.",
    "Practice gratitude for what you have while striving for smart financial growth.",
    "Understand the tax implications of every investment vehicle you choose.",
    "Avoid keeping credit card details saved on retail websites to prevent impulse buys.",
    "Set aside time to study global economic trends and historical market cycles.",
    "Keep your long-term vision clear even when short-term market volatility strikes.",
    "Prioritize your health today to prevent catastrophic medical expenses tomorrow.",
    "Learn to negotiate your starting salary and benefits package professionally.",
    "Keep your fixed monthly overhead minimal to weather unexpected income dips.",
    "Avoid letting lifestyle creep absorb every single raise or promotion you receive.",
    "Establish a dedicated savings goal for your next major life milestone.",
    "Check your bank statements for unauthorized or forgotten recurring charges.",
    "Build a habit of reading financial news and expert analysis weekly.",
    "Understand that true wealth is freedom of time and peace of mind.",
    "Keep your investment portfolio diversified across various sectors and industries.",
    "Avoid making major financial decisions when experiencing intense emotions.",
    "Set up clear savings milestones with visual trackers to stay motivated.",
    "Practice intentional gift-giving that values thoughtfulness over high price tags.",
    "Keep your financial independence as a top priority throughout all life stages.",
    "Learn how to read financial statements and corporate balance sheets.",
    "Avoid keeping all your eggs in one basket; diversification protects capital.",
    "Take time to appreciate free recreational activities like hiking and reading.",
    "Keep your debt payments automated to avoid late fees and credit penalties.",
    "Understand the psychological triggers that encourage you to spend money.",
    "Build a sustainable financial routine that requires minimal daily willpower.",
    "Review your utility and grocery bills quarterly to catch creeping inflation.",
    "Keep your financial documents backed up securely in a digital vault.",
    "Avoid comparing your chapter one to someone else's chapter twenty.",
    "Prioritize paying down principal balances on loans whenever extra cash arrives.",
    "Learn the importance of asset allocation tailored to your specific age and goals.",
    "Keep your spending aligned with your deepest personal convictions.",
    "Avoid impulse purchases by walking away from the item for 48 hours.",
    "Establish a clear emergency communication plan for family financial crises.",
    "Understand how interest rates set by central banks affect your borrowing costs.",
    "Keep your investment strategy boring, disciplined, and consistent.",
    "Embrace the power of compounding by starting your savings journey today.",
    "Review your monthly subscriptions and eliminate any duplicate streaming services.",
    "Build a buffer in your savings account specifically for holiday and gift expenses.",
    "Keep your financial goals flexible enough to adapt to major life transitions.",
    "Avoid taking on debt to finance depreciating consumer assets.",
    "Prioritize building a strong credit history early in your adult life.",
    "Learn how to audit your monthly cash flow to find hidden savings opportunities.",
    "Keep your investment horizon long-term to ride out short-term market turbulence.",
    "Practice mindful consumption by repairing items instead of replacing them instantly.",
    "Establish clear financial boundaries when navigating social and family events.",
    "Understand the true cost of convenience spending versus cooking at home.",
    "Keep your focus on net worth growth rather than gross income display.",
    "Avoid letting fear paralyze you from making smart, calculated financial moves.",
    "Set up automatic alerts for any unusual activity on your financial accounts.",
    "Embrace the discipline of living below your means as a badge of honor.",
    "Review your professional skills and identify areas for high-ROI improvement.",
    "Keep your financial philosophy grounded in simplicity, patience, and consistency.",
    "Remember that every financial choice you make today shapes your tomorrow.",
    # Days 201 - 365
    "Master the art of cost-per-use calculation before buying expensive items.",
    "Keep your investment thesis simple: buy quality assets and hold them patiently.",
    "Avoid carrying balances on multiple credit cards simultaneously.",
    "Establish a routine for backing up all your digital financial records.",
    "Understand how fiscal policy and taxation influence your take-home pay.",
    "Keep your financial education ongoing through podcasts, books, and articles.",
    "Practice delayed gratification as a core philosophy in every area of life.",
    "Review your insurance policies annually to ensure adequate coverage limits.",
    "Avoid participating in crowd mentality or hype-driven financial bubbles.",
    "Build a contingency fund specifically for freelance or variable income drops.",
    "Keep your physical wallet lean by removing unused store credit cards.",
    "Understand the long-term cost of borrowing money for non-essential luxuries.",
    "Embrace frugality not as deprivation, but as targeted resource allocation.",
    "Review your investment portfolio risk exposure as you approach major milestones.",
    "Avoid co-signing loans unless you have fully accepted the risk of repayment.",
    "Establish a monthly ritual to celebrate your progress toward debt freedom.",
    "Keep your fixed expenses below 50% of your net take-home income.",
    "Learn how to evaluate corporate earnings reports and fundamental data.",
    "Avoid impulse buying online by clearing your saved payment card details.",
    "Build a strong relationship with your bank or credit union advisors.",
    "Keep your financial targets visible in your workspace as daily motivators.",
    "Understand the mechanics of inflation-protected securities and savings bonds.",
    "Practice gratitude daily; appreciation for what you have reduces spending urges.",
    "Review your career trajectory and negotiate compensation packages proactively.",
    "Avoid letting temporary market downturns derail your long-term strategy.",
    "Establish a dedicated savings allocation for continuous personal development.",
    "Keep your home maintenance proactive to avoid costly emergency repairs later.",
    "Understand the difference between being rich and building genuine wealth.",
    "Embrace the discipline of tracking every single transaction without exception.",
    "Review your utility providers annually to switch to more affordable tariffs.",
    "Avoid buying extended warranties on consumer electronics and appliances.",
    "Build an emergency plan for your digital assets and online accounts.",
    "Keep your financial expectations realistic and grounded in mathematical reality.",
    "Learn the value of networking with financially literate mentors and peers.",
    "Avoid making snap decisions on major purchases during holiday sales.",
    "Establish a clear succession plan and will for your estate and assets.",
    "Keep your investment approach disciplined, ignoring daily media noise.",
    "Understand how psychological accounting influences your spending habits.",
    "Practice mindful energy consumption to lower monthly utility overhead.",
    "Review your subscription list every ninety days without fail.",
    "Avoid funding your lifestyle with short-term payday loans or high-interest cash advances.",
    "Build a resilient mindset that views economic shifts as strategic opportunities.",
    "Keep your financial boundaries firm when dealing with high-pressure sales pitches.",
    "Learn the basics of estate planning and asset protection strategies.",
    "Avoid comparing your financial portfolio to unrealistic online benchmarks.",
    "Establish a sinking fund for annual travel and holiday vacations.",
    "Keep your savings automated so wealth building happens effortlessly in the background.",
    "Understand how compound interest accelerates your progress over decades.",
    "Embrace patience as your greatest ally in building generational stability.",
    "Review your credit report annually for errors and unauthorized inquiries.",
    "Avoid lifestyle inflation by saving 100% of every salary increase you receive.",
    "Build a comprehensive household inventory for insurance and security purposes.",
    "Keep your financial vision focused on long-term independence rather than status.",
    "Learn how to analyze risk-adjusted returns before entering new asset classes.",
    "Avoid letting greed cloud your judgment when evaluating investment opportunities.",
    "Establish a monthly habit of reviewing your net worth statement.",
    "Keep your fixed overhead minimal to maintain maximum personal freedom.",
    "Understand the importance of liquidity when structuring your financial portfolio.",
    "Practice intentional spending that aligns directly with your personal values.",
    "Review your tax withholding strategy annually with a qualified professional.",
    "Avoid keeping large balances in accounts that offer negligible interest rates.",
    "Build a habit of negotiating service fees, insurance rates, and contract prices.",
    "Keep your financial passwords secure and update your security protocols regularly.",
    "Understand the psychological impact of advertising and resist its subtle pulls.",
    "Embrace the discipline of living below your means as the ultimate superpower.",
    "Review your financial goals at the start of every new quarter.",
    "Avoid investing in complex financial products you cannot explain simply.",
    "Build a strong foundation of emergency savings before exploring riskier ventures.",
    "Keep your focus fixed on steady, predictable progress rather than overnight riches.",
    "Learn how to calculate your true hourly wage after factoring in commute costs.",
    "Avoid emotional attachments to declining assets or unprofitable investments.",
    "Establish clear financial milestones for every stage of your adult life.",
    "Keep your personal financial data completely confidential and secure.",
    "Understand the power of saying no to social pressure and lifestyle traps.",
    "Embrace continuous learning as the cornerstone of lifelong financial security.",
    "Review your banking and brokerage statements line by line every month.",
    "Avoid letting short-term financial setbacks distract you from your long-term vision.",
    "Build an attitude of abundance through gratitude, mindfulness, and smart planning.",
    "Keep your financial house in order so you can seize opportunities when they arise.",
    "Remember that true financial mastery is built one disciplined choice at a time."
]

@app.before_request
def before_request():
    if 'currency' not in session:
        session['currency'] = '₦'
    if 'user_name' not in session:
        session['user_name'] = 'Ikeli'

@app.route("/set_currency", methods=["POST"])
def set_currency():
    selected_currency = request.form.get("currency")
    if selected_currency in CURRENCIES:
        session['currency'] = selected_currency
    return redirect(request.referrer or url_for('home'))

@app.route("/set_name", methods=["POST"])
def set_name():
    name = request.form.get("user_name")
    if name:
        session['user_name'] = name.title()
    return redirect(request.referrer or url_for('home'))

@app.route("/")
def home():
    return render_template("home.html", currency=session.get('currency', '₦'), currencies=CURRENCIES)

@app.route("/dashboard")
def index():
    expenses = database.get_expenses()
    total = database.get_total_spending()
    raw_budgets = database.get_budgets()
    goals = database.get_savings_goals()
    
    day_of_year = datetime.datetime.now().timetuple().tm_yday
    daily_tip = DAILY_TIPS[(day_of_year - 1) % len(DAILY_TIPS)]
    
    budgets = []
    for cat, limit in raw_budgets:
        spent = database.get_category_spending(cat)
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
    expenses = database.get_expenses()
    total = database.get_total_spending()
    return render_template("expenses.html", expenses=expenses, total=total, 
                           currency=session.get('currency', '₦'), currencies=CURRENCIES)

@app.route("/budgets")
def budgets_page():
    raw_budgets = database.get_budgets()
    budgets = []
    for cat, limit in raw_budgets:
        spent = database.get_category_spending(cat)
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
    goals = database.get_savings_goals()
    return render_template("savings.html", goals=goals, 
                           currency=session.get('currency', '₦'), currencies=CURRENCIES)

@app.route("/reports")
def reports_page():
    daily_summary = database.get_daily_summary()
    monthly_summary = database.get_monthly_summary()
    return render_template("reports.html", daily=daily_summary, monthly=monthly_summary, 
                           currency=session.get('currency', '₦'), currencies=CURRENCIES)

@app.route("/blog")
def blog_page():
    posts = database.get_blog_posts()
    return render_template("blog.html", posts=posts, currency=session.get('currency', '₦'), currencies=CURRENCIES)

@app.route("/admin/blog", methods=["GET", "POST"])
def admin_blog():
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
    database.delete_blog_post(post_id)
    return redirect(url_for("admin_blog"))

@app.route("/add", methods=["POST"])
def add():
    title = request.form.get("title").title()
    amount = float(request.form.get("amount"))
    category = request.form.get("category").title()
    date = request.form.get("date")
    database.add_expense(title, amount, category, date)
    return redirect(url_for("expenses_page"))

@app.route("/set_budget", methods=["POST"])
def set_budget():
    category = request.form.get("category").title()
    limit_amount = float(request.form.get("limit_amount"))
    database.set_budget(category, limit_amount)
    return redirect(url_for("budgets_page"))

@app.route("/add_goal", methods=["POST"])
def add_goal():
    name = request.form.get("name").title()
    target_amount = float(request.form.get("target_amount"))
    current_amount = float(request.form.get("current_amount") or 0.0)
    database.add_savings_goal(name, target_amount, current_amount)
    return redirect(url_for("savings_page"))

@app.route("/delete/<int:expense_id>")
def delete(expense_id):
    database.delete_expense(expense_id)
    return redirect(url_for("expenses_page"))

@app.route("/delete_budget/<string:category>")
def delete_budget(category):
    database.delete_budget(category)
    return redirect(url_for("budgets_page"))

@app.route("/delete_goal/<int:goal_id>")
def delete_goal(goal_id):
    database.delete_savings_goal(goal_id)
    return redirect(url_for("savings_page"))

@app.route("/clear_prompt")
def clear_prompt():
    return render_template("clear_prompt.html", currency=session.get('currency', '₦'), currencies=CURRENCIES)

@app.route("/execute_clear", methods=["POST"])
def execute_clear():
    choice = request.form.get("clear_budgets")
    database.clear_expenses()
    if choice == "yes":
        database.clear_budgets()
    return redirect(url_for("expenses_page"))

if __name__ == "__main__":
    app.run(debug=True)