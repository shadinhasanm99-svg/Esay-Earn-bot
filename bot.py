"""
Esay Earn Bot - SM SHADIN Tasks Bot
=====================================
SM SHADIN VPN শপের বৈধ প্রচার (promotion) কাজের জন্য টাস্ক বট।

মেনু:
  📋 টাস্ক, 💰 ব্যালান্স, 💸 উইথড্র,
  🎁 আমার রেফারেল, 🛟 সাপোর্ট, 🆕 আমি নতুন

টাস্ক (শুধু নিজের শপের বৈধ প্রচার, প্রতিটা একবার করে):
  * @smshadinproxy চ্যানেলে জয়েন — যাচাই সহ (getChatMember) — ৳5
  * @socialmarketing22 চ্যানেলে জয়েন — যাচাই সহ (getChatMember) — ৳5
  * শপের লিংক শেয়ার (https://sm-shadin.netlify.app) — ৳2

রেফারেল: রেফার করা বন্ধু প্রথম টাস্ক শেষ করলে রেফারার ৳5 বোনাস পায়।
উইথড্র: কমপক্ষে ৳50, বিকাশ/নগদ নম্বরে; অ্যাডমিন Approve করলে
টাকা কাটা হবে, Reject করলে ব্যালান্স আগের মতোই থাকবে।

এই বটে যা নেই (ইচ্ছে করেই বানানো হয়নি):
  Gmail টাস্ক নেই, Gmail অ্যাকাউন্ট বানানো নেই, ইমেইল/ইউজারনেম/
  পাসওয়ার্ড দেখানো নেই, টাকার বিনিময়ে অ্যাকাউন্ট খোলার সিস্টেম নেই,
  ফেক লাইক/ফলো নেই, ফেক আর্নিং মেকানিজম নেই।

Render FREE Web Service-এ চলে: $PORT-এ Flask health server +
SQLite ডাটাবেস (tasks.db)। ব্যালান্স ফাইলে থাকে, রিস্টার্টে মুছে না।
তবে Render free-তে redeploy হলে ফাইল মুছে যেতে পারে, তাই অ্যাডমিন
মাঝে মাঝে /stats দিয়ে হিসাব মিলিয়ে রাখবেন।

অ্যাডমিন কমান্ড:
  /stats, /users, /broadcast, /addbalance, /reply,
  /approve_withdraw, /reject_withdraw

================ SETUP গাইড (এই ফাইলের ভেতরেই সব আছে) ================
আর আলাদা কোনো ফাইল লাগবে না — শুধু এই bot.py আর requirements.txt,
এই দুইটাই GitHub-এ আপলোড দিলেই হবে।

১. বট তৈরি — @BotFather:
   - Telegram-এ @BotFather খুলে /newbot লিখুন।
   - বটের নাম: Esay Earn Bot
   - Username: sm_esay_earn_bot (esay_earn_bot নেওয়া হয়ে গেছে, ওটা দিলে
     BotFather নেবে না)।
   - BotFather যে token দেবে, সেটা কপি করে রাখুন (কাউকে দেখাবেন না)।
   - নিজের Telegram numeric ID নিন: @userinfobot-কে /start লিখলে ID দেখাবে।

২. GitHub-এ আপলোড:
   - নতুন repository বানান (যেমন: sm-shadin-tasks-bot)।
   - শুধু ২টা ফাইল আপলোড করুন: bot.py আর requirements.txt।
   - খেয়াল: bot.py ফাইলের নাম ঠিক এটাই রাখবেন।
   - requirements.txt-এ python-telegram-bot==22.6 আছে — এটাই রাখবেন।
     পুরনো 20.8 দিলে Render-এর Python 3.14-এ বট crash করে
     (Updater-এর missing slot বাগ, PTB v21.0-তে ঠিক হয়েছে)।

৩. Render-এ Deploy (Free):
   - render.com → New + → Web Service → GitHub repo সিলেক্ট করুন।
   - Runtime: Python 3
   - Build Command: pip install -r requirements.txt
   - Start Command: python bot.py
   - Plan: Free
   - Environment Variables-এ এগুলো বসান (token কখনো ফাইলে লিখবেন না):
       BOT_TOKEN    = BotFather-এর token
       ADMIN_ID     = আপনার Telegram numeric ID
       BOT_USERNAME = sm_esay_earn_bot
       BOT_NAME     = Esay Earn Bot
   - Deploy চাপুন। লগে "Esay Earn Bot cholche..." দেখা গেলে বট চালু।

৪. চ্যানেলে অ্যাডমিন বানানো (জরুরি!):
   জয়েন যাচাই কাজ করতে হলে বটকে দুই চ্যানেলের অ্যাডমিন বানাতে হবে:
   - @smshadinproxy → সেটিংস → Administrators → বটকে Add করুন।
   - @socialmarketing22-তেও একইভাবে বটকে অ্যাডমিন বানান।
   বট অ্যাডমিন না হলে জয়েন যাচাই হবে না, ইউজাররা টাস্ক শেষ করতে
   পারবে না।

৫. টেস্ট:
   - Telegram-এ বট খুলে /start লিখুন।
   - 📋 টাস্ক → চ্যানেলে জয়েন → যাচাই করুন → ব্যালান্সে ৳5 যোগ হবে।
   - 🎁 আমার রেফারেল → লিংক ঠিক আছে কিনা দেখুন।
   - 💸 উইথড্র → ৳50 লিখে দেখুন (ব্যালান্স কম থাকলে মেসেজ আসবে)।

ডাটা ব্যাকআপ: ব্যালান্স tasks.db (SQLite) ফাইলে থাকে। Render free-তে
restart/redeploy হলে ফাইল মুছে যেতে পারে — তাই /stats দিয়ে মাঝে মাঝে
হিসাব মিলিয়ে রাখুন।

লোকালে চালাতে চাইলে:
  pip install -r requirements.txt
  BOT_TOKEN=... ADMIN_ID=... python bot.py
"""

import html
import logging
import os
import sqlite3
import threading
import urllib.parse

from flask import Flask
from telegram import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    KeyboardButton,
    ReplyKeyboardMarkup,
    Update,
)
from telegram.ext import (
    ApplicationBuilder,
    CallbackQueryHandler,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters,
)

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)

# ---------------- Config (env থেকে, file-এ কখনো টোকেন লিখবে না) ----------------

BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
ADMIN_ID = os.environ.get("ADMIN_ID", "")
BOT_USERNAME = os.environ.get("BOT_USERNAME", "")
BOT_NAME = os.environ.get("BOT_NAME", "Esay Earn Bot")
DB_PATH = os.environ.get("DB_PATH", "tasks.db")

# টাকার অঙ্ক (সব ৳-তে, ডলার কোথাও নেই):
REFERRAL_BONUS = 5        # রেফার করা বন্ধুর প্রথম টাস্কে রেফারারের বোনাস
MIN_WITHDRAW = 50         # কমপক্ষে উইথড্র
SHOP_LINK = "https://sm-shadin.netlify.app"
CHANNEL_PROXY = "@smshadinproxy"
CHANNEL_PROXY_LINK = "https://t.me/smshadinproxy"
CHANNEL_COMMUNITY = "@socialmarketing22"
CHANNEL_COMMUNITY_LINK = "https://t.me/socialmarketing22"
PAYMENT_NUMBER = "01879173170"  # শপের বিকাশ/নগদ নম্বর (তথ্যের জন্য)

# (task_key, নাম, পুরস্কার ৳, চ্যানেল, লিংক)
TASKS = [
    ("join_proxy", "📢 @smshadinproxy চ্যানেলে জয়েন করুন", 5,
     CHANNEL_PROXY, CHANNEL_PROXY_LINK),
    ("join_community", "📢 @socialmarketing22 চ্যানেলে জয়েন করুন", 5,
     CHANNEL_COMMUNITY, CHANNEL_COMMUNITY_LINK),
    ("share_shop", "🔗 শপের লিংক শেয়ার করুন", 2, None, SHOP_LINK),
]
TASK_REWARD = {key: reward for key, _name, reward, _ch, _link in TASKS}

WAITING_WITHDRAW_AMOUNT = "waiting_withdraw_amount"
WAITING_WITHDRAW_NUMBER = "waiting_withdraw_number"
WAITING_SUPPORT = "waiting_support"

MAIN_MENU = ReplyKeyboardMarkup(
    [
        [KeyboardButton("📋 টাস্ক"), KeyboardButton("💰 ব্যালান্স")],
        [KeyboardButton("💸 উইথড্র"), KeyboardButton("🎁 আমার রেফারেল")],
        [KeyboardButton("🛟 সাপোর্ট"), KeyboardButton("🆕 আমি নতুন")],
    ],
    resize_keyboard=True,
)


def admin_id_int():
    try:
        return int(ADMIN_ID)
    except (TypeError, ValueError):
        return None


def is_admin(user_id):
    admin = admin_id_int()
    return admin is not None and user_id == admin


def esc(value):
    """HTML-escape a value for use inside an HTML-parsed Telegram message."""
    return html.escape(str(value), quote=False)


def code(value):
    """Wrap ONE copyable value in <code> so tapping it copies just that value."""
    return f"<code>{esc(value)}</code>"


def customer_label(user):
    if user.username:
        return f"{user.full_name} (@{user.username})"
    return user.full_name


def raw_command_text(update, skip_tokens):
    """Command-এর পরের raw text ফেরত দিন (নতুন লাইন ঠিক রেখে)."""
    text = update.message.text or ""
    parts = text.split(None, skip_tokens)
    if len(parts) > skip_tokens:
        return parts[-1]
    return ""


# ---------------- Database ----------------

def get_conn():
    return sqlite3.connect(DB_PATH)


def init_db():
    conn = get_conn()
    conn.execute(
        "CREATE TABLE IF NOT EXISTS users ("
        "user_id INTEGER PRIMARY KEY, "
        "username TEXT, "
        "first_name TEXT, "
        "balance INTEGER NOT NULL DEFAULT 0, "
        "total_earned INTEGER NOT NULL DEFAULT 0, "
        "referred_by INTEGER)"
    )
    # একটা টাস্ক একজন একবারই করতে পারবে (UNIQUE দিয়েই আটকানো).
    conn.execute(
        "CREATE TABLE IF NOT EXISTS tasks_done ("
        "id INTEGER PRIMARY KEY AUTOINCREMENT, "
        "user_id INTEGER, "
        "task_key TEXT, "
        "reward INTEGER, "
        "created_at TEXT DEFAULT CURRENT_TIMESTAMP, "
        "UNIQUE(user_id, task_key))"
    )
    # রেফারেল: বন্ধু প্রথম টাস্ক শেষ করলে বোনাস দেওয়া হয়।
    conn.execute(
        "CREATE TABLE IF NOT EXISTS referrals ("
        "id INTEGER PRIMARY KEY AUTOINCREMENT, "
        "referrer_id INTEGER, "
        "referred_id INTEGER, "
        "bonus INTEGER NOT NULL DEFAULT 0, "
        "status TEXT NOT NULL DEFAULT 'pending', "
        "created_at TEXT DEFAULT CURRENT_TIMESTAMP, "
        "UNIQUE(referrer_id, referred_id))"
    )
    conn.execute(
        "CREATE TABLE IF NOT EXISTS withdrawals ("
        "id INTEGER PRIMARY KEY AUTOINCREMENT, "
        "user_id INTEGER, "
        "amount INTEGER, "
        "method TEXT, "
        "number TEXT, "
        "status TEXT NOT NULL DEFAULT 'pending', "
        "created_at TEXT DEFAULT CURRENT_TIMESTAMP)"
    )
    conn.commit()
    conn.close()


def ensure_user(user):
    conn = get_conn()
    conn.execute(
        "INSERT OR IGNORE INTO users "
        "(user_id, username, first_name, balance, total_earned)"
        " VALUES (?, ?, ?, 0, 0)",
        (user.id, user.username or "", user.full_name),
    )
    conn.execute(
        "UPDATE users SET username = ?, first_name = ? WHERE user_id = ?",
        (user.username or "", user.full_name, user.id),
    )
    conn.commit()
    conn.close()


def get_balance(user_id):
    conn = get_conn()
    row = conn.execute(
        "SELECT balance FROM users WHERE user_id = ?", (user_id,)
    ).fetchone()
    conn.close()
    return row[0] if row else 0


def get_total_earned(user_id):
    conn = get_conn()
    row = conn.execute(
        "SELECT total_earned FROM users WHERE user_id = ?", (user_id,)
    ).fetchone()
    conn.close()
    return row[0] if row else 0


def add_balance(user_id, amount):
    """Balance-এ amount যোগ করুন (negative হলে কাটবে, 0-এর নিচে যাবে না)."""
    conn = get_conn()
    conn.execute(
        "INSERT OR IGNORE INTO users (user_id, balance, total_earned)"
        " VALUES (?, 0, 0)",
        (user_id,),
    )
    conn.execute(
        "UPDATE users SET balance = MAX(balance + ?, 0) WHERE user_id = ?",
        (amount, user_id),
    )
    if amount > 0:
        conn.execute(
            "UPDATE users SET total_earned = total_earned + ? WHERE user_id = ?",
            (amount, user_id),
        )
    row = conn.execute(
        "SELECT balance FROM users WHERE user_id = ?", (user_id,)
    ).fetchone()
    conn.commit()
    conn.close()
    return row[0] if row else 0


def set_referrer(user_id, referrer_id):
    """রেফারেল লিংক দিয়ে আসলে, শুধু প্রথমবার referrer সেট করুন."""
    try:
        referrer_id = int(referrer_id)
    except (TypeError, ValueError):
        return
    if referrer_id == user_id:
        return
    conn = get_conn()
    conn.execute(
        "INSERT OR IGNORE INTO users (user_id, balance, total_earned)"
        " VALUES (?, 0, 0)",
        (referrer_id,),
    )
    conn.execute(
        "UPDATE users SET referred_by = ? WHERE user_id = ? AND referred_by IS NULL",
        (referrer_id, user_id),
    )
    conn.execute(
        "INSERT OR IGNORE INTO referrals (referrer_id, referred_id)"
        " VALUES (?, ?)",
        (referrer_id, user_id),
    )
    conn.commit()
    conn.close()


def get_referral_stats(user_id):
    conn = get_conn()
    row = conn.execute(
        "SELECT COUNT(*) FROM referrals WHERE referrer_id = ?", (user_id,)
    ).fetchone()
    referred_count = row[0] if row else 0
    row = conn.execute(
        "SELECT COUNT(*), COALESCE(SUM(bonus), 0) FROM referrals"
        " WHERE referrer_id = ? AND status = 'paid'",
        (user_id,),
    ).fetchone()
    conn.close()
    return referred_count, row[0] if row else 0, row[1] if row else 0


def get_task_status(user_id):
    """{task_key: True} — কোন টাস্কগুলো শেষ হয়েছে."""
    conn = get_conn()
    rows = conn.execute(
        "SELECT task_key FROM tasks_done WHERE user_id = ?", (user_id,)
    ).fetchall()
    conn.close()
    return {row[0] for row in rows}


def complete_task(user_id, task_key):
    """টাস্ক শেষ করুন: পুরস্কার দিন, রেফারেল বোনাস থাকলে দিন.
    Returns (reward, referrer_bonus_paid_bool) বা None (আগেই শেষ)."""
    reward = TASK_REWARD.get(task_key)
    if reward is None:
        return None
    conn = get_conn()
    try:
        cur = conn.execute(
            "INSERT OR IGNORE INTO tasks_done (user_id, task_key, reward)"
            " VALUES (?, ?, ?)",
            (user_id, task_key, reward),
        )
        if cur.rowcount == 0:
            return None  # আগেই শেষ করা টাস্ক
        conn.execute(
            "UPDATE users SET balance = balance + ?, total_earned = total_earned + ?"
            " WHERE user_id = ?",
            (reward, reward, user_id),
        )
        # প্রথম টাস্ক শেষ হলে রেফারার বোনাস পায় (একবারই)।
        count = conn.execute(
            "SELECT COUNT(*) FROM tasks_done WHERE user_id = ?", (user_id,)
        ).fetchone()[0]
        bonus_paid = False
        if count == 1:
            row = conn.execute(
                "SELECT referrer_id FROM referrals"
                " WHERE referred_id = ? AND status = 'pending'",
                (user_id,),
            ).fetchone()
            if row:
                referrer_id = row[0]
                conn.execute(
                    "UPDATE referrals SET bonus = ?, status = 'paid'"
                    " WHERE referred_id = ?",
                    (REFERRAL_BONUS, user_id),
                )
                conn.execute(
                    "INSERT OR IGNORE INTO users (user_id, balance, total_earned)"
                    " VALUES (?, 0, 0)",
                    (referrer_id,),
                )
                conn.execute(
                    "UPDATE users SET balance = balance + ?,"
                    " total_earned = total_earned + ? WHERE user_id = ?",
                    (REFERRAL_BONUS, REFERRAL_BONUS, referrer_id),
                )
                bonus_paid = True
        conn.commit()
        return (reward, bonus_paid)
    finally:
        conn.close()


def get_referrer_id(user_id):
    conn = get_conn()
    row = conn.execute(
        "SELECT referred_by FROM users WHERE user_id = ?", (user_id,)
    ).fetchone()
    conn.close()
    return row[0] if row and row[0] else None


def create_withdrawal(user_id, amount, method, number):
    conn = get_conn()
    cur = conn.execute(
        "INSERT INTO withdrawals (user_id, amount, method, number, status)"
        " VALUES (?, ?, ?, ?, 'pending')",
        (user_id, amount, method, number),
    )
    wd_id = cur.lastrowid
    conn.commit()
    conn.close()
    return wd_id


def get_withdrawal(wd_id):
    conn = get_conn()
    row = conn.execute(
        "SELECT user_id, amount, method, number, status FROM withdrawals"
        " WHERE id = ?",
        (wd_id,),
    ).fetchone()
    conn.close()
    return row


def get_latest_pending_withdrawal(user_id, amount=None):
    conn = get_conn()
    if amount is not None:
        row = conn.execute(
            "SELECT id, amount, method, number FROM withdrawals"
            " WHERE user_id = ? AND amount = ? AND status = 'pending'"
            " ORDER BY id DESC LIMIT 1",
            (user_id, amount),
        ).fetchone()
    else:
        row = conn.execute(
            "SELECT id, amount, method, number FROM withdrawals"
            " WHERE user_id = ? AND status = 'pending'"
            " ORDER BY id DESC LIMIT 1",
            (user_id,),
        ).fetchone()
    conn.close()
    return row


def approve_withdrawal(wd_id):
    """Approve করলে তবেই ব্যালান্স কাটবে। Returns (ok, reason)."""
    conn = get_conn()
    row = conn.execute(
        "SELECT user_id, amount, status FROM withdrawals WHERE id = ?",
        (wd_id,),
    ).fetchone()
    if not row:
        conn.close()
        return (False, "not_found")
    user_id, amount, status = row
    if status != "pending":
        conn.close()
        return (False, f"already_{status}")
    bal = conn.execute(
        "SELECT balance FROM users WHERE user_id = ?", (user_id,)
    ).fetchone()
    if not bal or bal[0] < amount:
        conn.close()
        return (False, "insufficient")
    conn.execute(
        "UPDATE withdrawals SET status = 'approved' WHERE id = ?", (wd_id,)
    )
    conn.execute(
        "UPDATE users SET balance = balance - ? WHERE user_id = ?",
        (amount, user_id),
    )
    conn.commit()
    conn.close()
    return (True, "")


def reject_withdrawal(wd_id):
    conn = get_conn()
    row = conn.execute(
        "SELECT user_id, amount, status FROM withdrawals WHERE id = ?",
        (wd_id,),
    ).fetchone()
    if not row:
        conn.close()
        return (False, "not_found")
    user_id, amount, status = row
    if status != "pending":
        conn.close()
        return (False, f"already_{status}")
    conn.execute(
        "UPDATE withdrawals SET status = 'rejected' WHERE id = ?", (wd_id,)
    )
    conn.commit()
    conn.close()
    return (True, "")


def get_all_user_ids():
    conn = get_conn()
    rows = conn.execute("SELECT user_id FROM users").fetchall()
    conn.close()
    return [row[0] for row in rows]


def get_stats():
    conn = get_conn()
    users = conn.execute("SELECT COUNT(*) FROM users").fetchone()[0]
    total_balance = conn.execute(
        "SELECT COALESCE(SUM(balance), 0) FROM users"
    ).fetchone()[0]
    total_earned = conn.execute(
        "SELECT COALESCE(SUM(total_earned), 0) FROM users"
    ).fetchone()[0]
    tasks_done = conn.execute(
        "SELECT COUNT(*) FROM tasks_done"
    ).fetchone()[0]
    pending_wd = conn.execute(
        "SELECT COUNT(*) FROM withdrawals WHERE status = 'pending'"
    ).fetchone()[0]
    referrals_paid = conn.execute(
        "SELECT COUNT(*) FROM referrals WHERE status = 'paid'"
    ).fetchone()[0]
    conn.close()
    return users, total_balance, total_earned, tasks_done, pending_wd, referrals_paid


def get_recent_users(limit=20):
    conn = get_conn()
    rows = conn.execute(
        "SELECT user_id, first_name, username, balance FROM users"
        " ORDER BY user_id DESC LIMIT ?",
        (limit,),
    ).fetchall()
    conn.close()
    return rows


# ---------------- Health server (Render free) ----------------

def start_health_server():
    """Render free Web Service-এর health check-এর জন্য $PORT-এ server খুলুন."""
    port = int(os.environ.get("PORT", "10000"))
    app = Flask(__name__)

    @app.route("/", methods=["GET"])
    def health():
        return f"{BOT_NAME} is running", 200

    thread = threading.Thread(
        target=lambda: app.run(host="0.0.0.0", port=port, use_reloader=False),
        daemon=True,
    )
    thread.start()
    logger.info("Health server cholche, port: %s", port)


# ---------------- Menu / start ----------------

def welcome_text():
    return (
        f"👋 স্বাগতম! {BOT_NAME}-এ।\n\n"
        "এখানে SM SHADIN শপের প্রচারের কাজ করে টাকা আয় করুন:\n"
        "📋 টাস্ক শেষ করুন → ব্যালান্সে ৳ জমা হবে\n"
        "🎁 বন্ধুকে রেফার করুন → বোনাস পাবেন\n"
        "💸 ৳50 হলেই বিকাশ/নগদে উইথড্র করুন\n\n"
        "নিচের মেনু থেকে অপশন বেছে নিন।"
    )


def referral_link(user_id):
    if not BOT_USERNAME:
        return ""
    return f"https://t.me/{BOT_USERNAME}?start={user_id}"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    ensure_user(update.message.from_user)
    if context.args and context.args[0].isdigit():
        set_referrer(update.message.from_user.id, context.args[0])
    context.user_data.clear()
    await update.message.reply_text(welcome_text(), reply_markup=MAIN_MENU)


async def menu_new(update: Update, context: ContextTypes.DEFAULT_TYPE):
    ensure_user(update.message.from_user)
    context.user_data.clear()
    await update.message.reply_text(
        "🆕 আমি নতুন — কীভাবে কাজ করবেন:\n\n"
        "1️⃣ 📋 টাস্ক চাপুন — ৩টা কাজ দেখবেন।\n"
        "2️⃣ চ্যানেলে জয়েন করুন (জয়েন যাচাই করা হবে) বা শপের লিংক শেয়ার করুন।\n"
        "3️⃣ কাজ শেষ হলে ব্যালান্সে ৳ জমা হবে — 💰 ব্যালান্স চাপলে দেখতে পাবেন।\n"
        "4️⃣ 🎁 আমার রেফারেল থেকে নিজের লিংক বন্ধুদের পাঠান — বন্ধু প্রথম টাস্ক "
        f"শেষ করলে আপনি ৳{REFERRAL_BONUS} বোনাস পাবেন।\n"
        f"5️⃣ ব্যালান্স ৳{MIN_WITHDRAW} হলে 💸 উইথড্র চাপুন — বিকাশ/নগদ নম্বর দিন, "
        "অ্যাডমিন Approve করলে টাকা পাঠানো হবে।\n\n"
        "❓ সমস্যা হলে 🛟 সাপোর্টে লিখে পাঠান।",
        reply_markup=MAIN_MENU,
    )


# ---------------- Tasks ----------------

def tasks_keyboard(user_id):
    done = get_task_status(user_id)
    buttons = []
    for key, name, reward, _ch, _link in TASKS:
        mark = "✅" if key in done else "⬜"
        buttons.append([
            InlineKeyboardButton(
                f"{mark} {name} — ৳{reward}", callback_data=f"task:{key}"
            )
        ])
    return InlineKeyboardMarkup(buttons)


async def menu_tasks(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    ensure_user(user)
    context.user_data.clear()
    done = get_task_status(user.id)
    await update.message.reply_text(
        "📋 টাস্কসমূহ (প্রতিটা একবার করে করা যায়):\n\n"
        "• চ্যানেল জয়েন — জয়েন যাচাই করা হবে\n"
        "• শপের লিংক শেয়ার — শেয়ার বাটন দিয়ে শেয়ার করুন\n\n"
        f"শেষ করেছেন: {len(done)}/{len(TASKS)} টা",
        reply_markup=tasks_keyboard(user.id),
    )


async def is_channel_member(bot, channel, user_id):
    """True = জয়েন করেছে, False = করেনি, None = যাচাই করা যায়নি (বট অ্যাডমিন না)।"""
    try:
        member = await bot.get_chat_member(chat_id=channel, user_id=user_id)
        return member.status in ("member", "administrator", "creator", "restricted")
    except Exception as exc:
        logger.warning("Join check failed %s %s: %s", channel, user_id, exc)
        return None


async def task_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user = query.from_user
    ensure_user(user)
    key = query.data.split(":")[1]
    task = next((t for t in TASKS if t[0] == key), None)
    if not task:
        return
    _key, name, reward, channel, link = task
    done = get_task_status(user.id)
    if key in done:
        await query.answer("এই টাস্কটি আপনি আগেই শেষ করেছেন।", show_alert=True)
        return

    if key == "share_shop":
        # শেয়ার: Telegram শেয়ার বাটন + নিশ্চিতকরণ বাটন।
        # শেয়ার যাচাই করা যায় না, তাই শুধু একবারের কনফার্মেই পুরস্কার।
        share_url = (
            "https://t.me/share/url?url="
            + urllib.parse.quote(SHOP_LINK, safe="")
            + "&text="
            + urllib.parse.quote("SM SHADIN — সস্তায় VPN ও Proxy!", safe="")
        )
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("🔗 শেয়ার করুন", url=share_url)],
            [InlineKeyboardButton("✅ শেয়ার করেছি", callback_data="task_share_done")],
            [InlineKeyboardButton("⬅️ টাস্ক লিস্টে ফিরুন", callback_data="task_back")],
        ])
        await query.edit_message_text(
            "🔗 শপের লিংক শেয়ার করুন:\n\n"
            f"শপ: {SHOP_LINK}\n"
            f"পুরস্কার: ৳{reward} (একবার)\n\n"
            "নিচের শেয়ার বাটনে চাপ দিয়ে লিংকটা শেয়ার করুন, "
            "তারপর \"✅ শেয়ার করেছি\" চাপুন।",
            reply_markup=keyboard,
        )
        return

    # জয়েন টাস্ক: যাচাই করুন।
    member = await is_channel_member(context.bot, channel, user.id)
    if member is True:
        result = complete_task(user.id, key)
        if result:
            _reward, bonus_paid = result
            text = (
                f"✅ টাস্ক শেষ! {name}\n"
                f"💰 আপনার ব্যালান্সে ৳{_reward} যোগ হয়েছে।\n"
                f"💳 বর্তমান ব্যালান্স: ৳{get_balance(user.id)}"
            )
            if bonus_paid:
                referrer_id = get_referrer_id(user.id)
                if referrer_id:
                    try:
                        await context.bot.send_message(
                            chat_id=referrer_id,
                            text="🎁 রেফারেল বোনাস! আপনার রেফার করা বন্ধু প্রথম টাস্ক "
                            f"শেষ করেছে, তাই আপনার ব্যালান্সে ৳{REFERRAL_BONUS} যোগ হয়েছে।",
                        )
                    except Exception as exc:
                        logger.warning("Referral bonus janate parini: %s", exc)
            await query.edit_message_text(text, reply_markup=tasks_keyboard(user.id))
        else:
            await query.answer("এই টাস্কটি আগেই শেষ করা হয়েছে।", show_alert=True)
    elif member is None:
        await query.edit_message_text(
            "⚠️ জয়েন যাচাই করা যাচ্ছে না।\n"
            "বটকে চ্যানেলে অ্যাডমিন করা আছে কিনা অ্যাডমিনকে জানান।\n"
            f"চ্যানেল: {link}",
            reply_markup=tasks_keyboard(user.id),
        )
    else:
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("📢 চ্যানেলে জয়েন করুন", url=link)],
            [InlineKeyboardButton("✅ জয়েন করেছি, যাচাই করুন", callback_data=f"task:{key}")],
            [InlineKeyboardButton("⬅️ টাস্ক লিস্টে ফিরুন", callback_data="task_back")],
        ])
        await query.edit_message_text(
            f"❌ আপনি এখনো {channel} চ্যানেলে জয়েন করেননি।\n"
            "প্রথমে জয়েন করুন, তারপর যাচাই বাটন চাপুন।\n"
            f"পুরস্কার: ৳{reward}",
            reply_markup=keyboard,
        )


async def task_share_done(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user = query.from_user
    ensure_user(user)
    result = complete_task(user.id, "share_shop")
    if result:
        reward, bonus_paid = result
        text = (
            "✅ টাস্ক শেষ! শপের লিংক শেয়ার\n"
            f"💰 আপনার ব্যালান্সে ৳{reward} যোগ হয়েছে।\n"
            f"💳 বর্তমান ব্যালান্স: ৳{get_balance(user.id)}"
        )
        if bonus_paid:
            referrer_id = get_referrer_id(user.id)
            if referrer_id:
                try:
                    await context.bot.send_message(
                        chat_id=referrer_id,
                        text="🎁 রেফারেল বোনাস! আপনার রেফার করা বন্ধু প্রথম টাস্ক "
                        f"শেষ করেছে, তাই আপনার ব্যালান্সে ৳{REFERRAL_BONUS} যোগ হয়েছে।",
                    )
                except Exception as exc:
                    logger.warning("Referral bonus janate parini: %s", exc)
        await query.edit_message_text(text, reply_markup=tasks_keyboard(user.id))
    else:
        await query.answer("এই টাস্কটি আগেই শেষ করা হয়েছে।", show_alert=True)


async def task_back(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    ensure_user(query.from_user)
    done = get_task_status(query.from_user.id)
    await query.edit_message_text(
        "📋 টাস্কসমূহ (প্রতিটা একবার করে করা যায়):\n\n"
        f"শেষ করেছেন: {len(done)}/{len(TASKS)} টা",
        reply_markup=tasks_keyboard(query.from_user.id),
    )


# ---------------- Balance / Referral ----------------

async def menu_balance(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    ensure_user(user)
    context.user_data.clear()
    balance = get_balance(user.id)
    total = get_total_earned(user.id)
    await update.message.reply_text(
        f"💰 ব্যালান্স\n\n"
        f"💳 বর্তমান ব্যালান্স: ৳{balance}\n"
        f"📈 মোট আয়: ৳{total}\n\n"
        f"💸 উইথড্র করতে কমপক্ষে ৳{MIN_WITHDRAW} লাগবে।",
        reply_markup=MAIN_MENU,
    )


async def menu_referral(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    ensure_user(user)
    context.user_data.clear()
    link = referral_link(user.id)
    referred_count, paid_count, bonus_total = get_referral_stats(user.id)
    if not link:
        await update.message.reply_text(
            "🎁 আমার রেফারেল\n\n"
            "রেফারেল লিংক এখনো তৈরি হয়নি — বটের username সেট করা নেই।\n"
            "অ্যাডমিনকে BOT_USERNAME সেট করতে বলুন।",
            reply_markup=MAIN_MENU,
        )
        return
    await update.message.reply_text(
        "🎁 আমার রেফারেল\n\n"
        "আপনার রেফারেল লিংক:\n"
        f"{code(link)}\n\n"
        f"👥 আপনি রেফার করেছেন: {referred_count} জন\n"
        f"✅ তাদের মধ্যে প্রথম টাস্ক শেষ করেছে: {paid_count} জন\n"
        f"💰 রেফারেল বোনাস পেয়েছেন: ৳{bonus_total}\n\n"
        "নিয়ম: আপনার লিংক দিয়ে আসা বন্ধু প্রথম টাস্ক শেষ করলেই "
        f"আপনি ৳{REFERRAL_BONUS} বোনাস পাবেন।",
        reply_markup=MAIN_MENU,
        parse_mode="HTML",
    )


# ---------------- Withdraw ----------------

async def menu_withdraw(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    ensure_user(user)
    balance = get_balance(user.id)
    if balance < MIN_WITHDRAW:
        await update.message.reply_text(
            f"💸 উইথড্র\n\n"
            f"💳 আপনার ব্যালান্স: ৳{balance}\n"
            f"কমপক্ষে ৳{MIN_WITHDRAW} হলে উইথড্র করা যাবে।\n"
            "📋 টাস্ক শেষ করে ব্যালান্স বাড়ান।",
            reply_markup=MAIN_MENU,
        )
        return
    context.user_data["state"] = WAITING_WITHDRAW_AMOUNT
    context.user_data.pop("withdraw_amount", None)
    context.user_data.pop("withdraw_number", None)
    await update.message.reply_text(
        f"💸 উইথড্র\n\n"
        f"💳 আপনার ব্যালান্স: ৳{balance}\n"
        f"কমপক্ষে ৳{MIN_WITHDRAW} উইথড্র করা যাবে।\n\n"
        "কত টাকা উইথড্র করতে চান, শুধু সংখ্যাটা লিখুন।",
        reply_markup=MAIN_MENU,
    )


def withdraw_method_keyboard():
    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton("📱 বিকাশ", callback_data="wd_method:bKash"),
            InlineKeyboardButton("📱 নগদ", callback_data="wd_method:Nagad"),
        ],
    ])


async def handle_withdraw_amount(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    text = (update.message.text or "").strip().replace(",", "")
    try:
        amount = int(text)
    except ValueError:
        await update.message.reply_text(
            "❌ শুধু সংখ্যায় লিখুন, যেমন: 100", reply_markup=MAIN_MENU
        )
        return
    balance = get_balance(user.id)
    if amount < MIN_WITHDRAW:
        await update.message.reply_text(
            f"❌ কমপক্ষে ৳{MIN_WITHDRAW} উইথড্র করা যাবে। আবার লিখুন।",
            reply_markup=MAIN_MENU,
        )
        return
    if amount > balance:
        await update.message.reply_text(
            f"❌ আপনার ব্যালান্স ৳{balance}, এর বেশি উইথড্র করা যাবে না। আবার লিখুন।",
            reply_markup=MAIN_MENU,
        )
        return
    context.user_data["withdraw_amount"] = amount
    context.user_data["state"] = WAITING_WITHDRAW_NUMBER
    await update.message.reply_text(
        f"💸 উইথড্র: ৳{amount}\n\n"
        "টাকা পাঠানোর জন্য আপনার বিকাশ/নগদ নম্বরটি লিখুন "
        "(যেমন: 01XXXXXXXXX)।",
        reply_markup=MAIN_MENU,
    )


async def handle_withdraw_number(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (update.message.text or "").strip()
    number = text.replace(" ", "").replace("-", "")
    if not (number.isdigit() and len(number) == 11 and number.startswith("01")):
        await update.message.reply_text(
            "❌ নম্বরটি ঠিক মনে হচ্ছে না। ১১ সংখ্যার মোবাইল নম্বর লিখুন "
            "(যেমন: 01XXXXXXXXX)।",
            reply_markup=MAIN_MENU,
        )
        return
    context.user_data["withdraw_number"] = number
    context.user_data["state"] = None
    await update.message.reply_text(
        f"💸 উইথড্র: ৳{context.user_data.get('withdraw_amount')}\n"
        f"📱 নম্বর: {number}\n\n"
        "কোন মাধ্যমে টাকা নিতে চান, বেছে নিন:",
        reply_markup=withdraw_method_keyboard(),
    )


async def withdraw_method_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user = query.from_user
    method = query.data.split(":")[1]
    amount = context.user_data.get("withdraw_amount")
    number = context.user_data.get("withdraw_number")
    if not amount or not number:
        await query.edit_message_text(
            "❌ উইথড্র-এর তথ্য পাওয়া যায়নি। আবার 💸 উইথড্র চাপুন।"
        )
        context.user_data.clear()
        return
    if get_balance(user.id) < amount:
        await query.edit_message_text(
            "❌ ব্যালান্স কমে গেছে, এই উইথড্র করা যাবে না। আবার চেষ্টা করুন।"
        )
        context.user_data.clear()
        return
    wd_id = create_withdrawal(user.id, int(amount), method, number)
    context.user_data.clear()
    await query.edit_message_text(
        f"✅ উইথড্র রিকোয়েস্ট পাঠানো হয়েছে!\n\n"
        f"💰 পরিমাণ: ৳{amount}\n"
        f"📱 {method}: {number}\n\n"
        "অ্যাডমিন Approve করলে টাকা পাঠানো হবে। Approve হলেই ব্যালান্স কাটবে।"
    )
    admin = admin_id_int()
    if admin:
        keyboard = InlineKeyboardMarkup([
            [
                InlineKeyboardButton("✅ Approve", callback_data=f"wd_ok:{wd_id}"),
                InlineKeyboardButton("❌ Reject", callback_data=f"wd_no:{wd_id}"),
            ],
        ])
        try:
            await context.bot.send_message(
                chat_id=admin,
                text=(
                    "💸 নতুন উইথড্র রিকোয়েস্ট!\n"
                    f"👤 ইউজার: {esc(customer_label(user))}\n"
                    f"🆔 User ID: {code(user.id)}\n"
                    f"💰 পরিমাণ: ৳{amount}\n"
                    f"📱 {method}: {code(number)}\n"
                    f"🆔 Request ID: {wd_id}"
                ),
                reply_markup=keyboard,
                parse_mode="HTML",
            )
        except Exception as exc:
            logger.warning("Admin-ke withdraw janate parini: %s", exc)


async def withdraw_decision_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    if not is_admin(query.from_user.id):
        await query.answer("শুধু অ্যাডমিন Approve/Reject করতে পারবে।", show_alert=True)
        return
    await query.answer()
    wd_id_str = query.data.split(":")[1]
    try:
        wd_id = int(wd_id_str)
    except ValueError:
        return
    wd = get_withdrawal(wd_id)
    if not wd:
        await query.edit_message_text("❌ এই রিকোয়েস্টটি পাওয়া যায়নি।")
        return
    user_id, amount, method, number, status = wd
    if status != "pending":
        await query.edit_message_text(
            f"ℹ️ এই রিকোয়েস্টটি আগেই {status} করা হয়েছে।"
        )
        return
    if query.data.startswith("wd_ok:"):
        ok, reason = approve_withdrawal(wd_id)
        if ok:
            await query.edit_message_text(
                f"✅ উইথড্র Approved! User ID: {user_id}, ৳{amount} ({method}: {number})"
            )
            try:
                await context.bot.send_message(
                    chat_id=user_id,
                    text=f"✅ আপনার ৳{amount} উইথড্র Approve হয়েছে! {method} ({number}) নম্বরে টাকা পাঠানো হচ্ছে।",
                )
            except Exception as exc:
                logger.warning("User-ke withdraw janate parini: %s", exc)
        elif reason == "insufficient":
            await query.edit_message_text(
                f"⚠️ Approve করা যায়নি — ইউজারের ব্যালান্স ৳{amount}-এর কম। "
                "ইউজারকে জানান।"
            )
        else:
            await query.edit_message_text(f"⚠️ Approve করা যায়নি ({reason})।")
    else:
        ok, reason = reject_withdrawal(wd_id)
        if ok:
            await query.edit_message_text(
                f"❌ উইথড্র Rejected! User ID: {user_id}, ৳{amount}"
            )
            try:
                await context.bot.send_message(
                    chat_id=user_id,
                    text=f"❌ আপনার ৳{amount} উইথড্র রিকোয়েস্ট Reject হয়েছে। ব্যালান্স আগের মতোই আছে। সমস্যা হলে 🛟 সাপোর্টে লিখুন।",
                )
            except Exception as exc:
                logger.warning("User-ke withdraw janate parini: %s", exc)
        else:
            await query.edit_message_text(f"⚠️ Reject করা যায়নি ({reason})।")


# ---------------- Support ----------------

async def menu_support(update: Update, context: ContextTypes.DEFAULT_TYPE):
    ensure_user(update.message.from_user)
    context.user_data["state"] = WAITING_SUPPORT
    await update.message.reply_text(
        "🛟 সাপোর্ট: আপনার সমস্যা বা প্রশ্ন এখানে লিখে পাঠান, "
        "অ্যাডমিন বট থেকেই উত্তর দেবে।\n\n"
        f"সরাসরি যোগাযোগ: https://t.me/BestservicSM\n"
        f"📢 Community Channel: {CHANNEL_COMMUNITY_LINK}",
        reply_markup=MAIN_MENU,
    )


async def handle_support_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    text = update.message.text or ""
    context.user_data["state"] = None
    admin = admin_id_int()
    if admin:
        try:
            await context.bot.send_message(
                chat_id=admin,
                text=(
                    "🛟 নতুন সাপোর্ট মেসেজ!\n"
                    f"👤 {esc(customer_label(user))}\n"
                    f"🆔 User ID: {code(user.id)}\n\n"
                    f"{esc(text)}"
                ),
                parse_mode="HTML",
            )
        except Exception as exc:
            logger.warning("Admin-ke support janate parini: %s", exc)
    await update.message.reply_text(
        "✅ আপনার মেসেজ অ্যাডমিনের কাছে পাঠানো হয়েছে। উত্তর পেলে জানানো হবে।",
        reply_markup=MAIN_MENU,
    )


# ---------------- Admin commands ----------------

async def cmd_stats(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not is_admin(update.message.from_user.id):
        await update.message.reply_text("❌ শুধু অ্যাডমিন এই কমান্ড ব্যবহার করতে পারবে।")
        return
    users, total_balance, total_earned, tasks_done, pending_wd, referrals_paid = get_stats()
    await update.message.reply_text(
        f"📊 {BOT_NAME} — Stats\n\n"
        f"👥 মোট ইউজার: {users}\n"
        f"💰 সব ইউজারের মোট ব্যালান্স: ৳{total_balance}\n"
        f"📈 মোট আয় (সব ইউজার): ৳{total_earned}\n"
        f"📋 শেষ হওয়া টাস্ক: {tasks_done}\n"
        f"💸 Pending উইথড্র: {pending_wd}\n"
        f"🎁 রেফারেল বোনাস দেওয়া হয়েছে: {referrals_paid} জনকে"
    )


async def cmd_users(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not is_admin(update.message.from_user.id):
        await update.message.reply_text("❌ শুধু অ্যাডমিন এই কমান্ড ব্যবহার করতে পারবে।")
        return
    rows = get_recent_users(20)
    if not rows:
        await update.message.reply_text("👥 এখনো কোনো ইউজার নেই।")
        return
    lines = [f"👥 ইউজার (সর্বশেষ {len(rows)} জন):"]
    for user_id, first_name, username, balance in rows:
        tag = f"@{username}" if username else ""
        lines.append(f"• {first_name} {tag} — ID: {user_id} — ৳{balance}")
    await update.message.reply_text("\n".join(lines))


async def cmd_addbalance(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not is_admin(update.message.from_user.id):
        await update.message.reply_text("❌ শুধু অ্যাডমিন এই কমান্ড ব্যবহার করতে পারবে।")
        return
    if len(context.args) < 2:
        await update.message.reply_text("ব্যবহার: /addbalance <user_id> <টাকা>")
        return
    try:
        user_id = int(context.args[0])
        amount = int(context.args[1])
    except ValueError:
        await update.message.reply_text("❌ user_id আর টাকা সংখ্যায় লিখুন।")
        return
    new_balance = add_balance(user_id, amount)
    await update.message.reply_text(
        f"✅ User ID {user_id}-এর ব্যালান্সে ৳{amount} যোগ করা হয়েছে। "
        f"বর্তমান ব্যালান্স: ৳{new_balance}"
    )
    try:
        await context.bot.send_message(
            chat_id=user_id,
            text=f"🎁 অ্যাডমিন আপনার ব্যালান্সে ৳{amount} যোগ করেছে। বর্তমান ব্যালান্স: ৳{new_balance}",
        )
    except Exception as exc:
        logger.warning("User-ke addbalance janate parini: %s", exc)


async def cmd_broadcast(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not is_admin(update.message.from_user.id):
        await update.message.reply_text("❌ শুধু অ্যাডমিন এই কমান্ড ব্যবহার করতে পারবে।")
        return
    text = raw_command_text(update, 1)
    if not text:
        await update.message.reply_text("ব্যবহার: /broadcast <মেসেজ>")
        return
    user_ids = get_all_user_ids()
    sent = 0
    for uid in user_ids:
        try:
            await context.bot.send_message(chat_id=uid, text=text)
            sent += 1
        except Exception as exc:
            logger.warning("Broadcast %s: %s", uid, exc)
    await update.message.reply_text(
        f"📢 Broadcast শেষ! {sent}/{len(user_ids)} জনের কাছে পাঠানো হয়েছে।"
    )


async def cmd_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not is_admin(update.message.from_user.id):
        await update.message.reply_text("❌ শুধু অ্যাডমিন এই কমান্ড ব্যবহার করতে পারবে।")
        return
    if len(context.args) < 2:
        await update.message.reply_text("ব্যবহার: /reply <user_id> <মেসেজ>")
        return
    try:
        user_id = int(context.args[0])
    except ValueError:
        await update.message.reply_text("❌ user_id সংখ্যায় লিখুন।")
        return
    text = raw_command_text(update, 2)
    if not text:
        await update.message.reply_text("ব্যবহার: /reply <user_id> <মেসেজ>")
        return
    try:
        await context.bot.send_message(
            chat_id=user_id,
            text=f"🛟 সাপোর্টের উত্তর:\n\n{text}",
        )
        await update.message.reply_text(f"✅ User ID {user_id}-কে উত্তর পাঠানো হয়েছে।")
    except Exception as exc:
        await update.message.reply_text(f"❌ পাঠানো যায়নি: {exc}")


async def cmd_approve_withdraw(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not is_admin(update.message.from_user.id):
        await update.message.reply_text("❌ শুধু অ্যাডমিন এই কমান্ড ব্যবহার করতে পারবে।")
        return
    if len(context.args) < 2:
        await update.message.reply_text(
            "ব্যবহার: /approve_withdraw <user_id> <টাকা>"
        )
        return
    try:
        user_id = int(context.args[0])
        amount = int(context.args[1])
    except ValueError:
        await update.message.reply_text("❌ user_id আর টাকা সংখ্যায় লিখুন।")
        return
    row = get_latest_pending_withdrawal(user_id, amount)
    if not row:
        await update.message.reply_text(
            "❌ এই ইউজারের ৳{0} টাকার কোনো pending উইথড্র পাওয়া যায়নি।".format(amount)
        )
        return
    wd_id = row[0]
    ok, reason = approve_withdrawal(wd_id)
    if ok:
        await update.message.reply_text(
            f"✅ উইথড্র Approved! User ID: {user_id}, ৳{amount}"
        )
        try:
            await context.bot.send_message(
                chat_id=user_id,
                text=f"✅ আপনার ৳{amount} উইথড্র Approve হয়েছে! টাকা পাঠানো হচ্ছে।",
            )
        except Exception as exc:
            logger.warning("User-ke withdraw janate parini: %s", exc)
    elif reason == "insufficient":
        await update.message.reply_text("⚠️ ইউজারের ব্যালান্স কম, Approve করা যায়নি।")
    else:
        await update.message.reply_text(f"⚠️ Approve করা যায়নি ({reason})।")


async def cmd_reject_withdraw(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not is_admin(update.message.from_user.id):
        await update.message.reply_text("❌ শুধু অ্যাডমিন এই কমান্ড ব্যবহার করতে পারবে।")
        return
    if len(context.args) < 1:
        await update.message.reply_text("ব্যবহার: /reject_withdraw <user_id>")
        return
    try:
        user_id = int(context.args[0])
    except ValueError:
        await update.message.reply_text("❌ user_id সংখ্যায় লিখুন।")
        return
    row = get_latest_pending_withdrawal(user_id)
    if not row:
        await update.message.reply_text("❌ এই ইউজারের কোনো pending উইথড্র পাওয়া যায়নি।")
        return
    wd_id, amount = row[0], row[1]
    ok, reason = reject_withdrawal(wd_id)
    if ok:
        await update.message.reply_text(
            f"❌ উইথড্র Rejected! User ID: {user_id}, ৳{amount} (ব্যালান্স কাটা হয়নি)"
        )
        try:
            await context.bot.send_message(
                chat_id=user_id,
                text=f"❌ আপনার ৳{amount} উইথড্র রিকোয়েস্ট Reject হয়েছে। ব্যালান্স আগের মতোই আছে।",
            )
        except Exception as exc:
            logger.warning("User-ke withdraw janate parini: %s", exc)
    else:
        await update.message.reply_text(f"⚠️ Reject করা যায়নি ({reason})।")


# ---------------- Text router ----------------

async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    ensure_user(user)
    text = (update.message.text or "").strip()
    state = context.user_data.get("state")

    # মেনু বাটন চাপলে state যাই থাকুক, মেনুতেই যান (আটকে থাকবে না)।
    menu_buttons = {
        "📋 টাস্ক", "💰 ব্যালান্স", "💸 উইথড্র",
        "🎁 আমার রেফারেল", "🛟 সাপোর্ট", "🆕 আমি নতুন",
    }
    if text in menu_buttons:
        context.user_data["state"] = None
        context.user_data.pop("withdraw_amount", None)
        context.user_data.pop("withdraw_number", None)

    if state == WAITING_WITHDRAW_AMOUNT and text not in menu_buttons:
        await handle_withdraw_amount(update, context)
        return
    if state == WAITING_WITHDRAW_NUMBER and text not in menu_buttons:
        await handle_withdraw_number(update, context)
        return
    if state == WAITING_SUPPORT and text not in menu_buttons:
        await handle_support_message(update, context)
        return

    if text == "📋 টাস্ক":
        await menu_tasks(update, context)
    elif text == "💰 ব্যালান্স":
        await menu_balance(update, context)
    elif text == "💸 উইথড্র":
        await menu_withdraw(update, context)
    elif text == "🎁 আমার রেফারেল":
        await menu_referral(update, context)
    elif text == "🛟 সাপোর্ট":
        await menu_support(update, context)
    elif text == "🆕 আমি নতুন":
        await menu_new(update, context)
    else:
        await update.message.reply_text(
            "নিচের মেনু থেকে অপশন বেছে নিন।", reply_markup=MAIN_MENU
        )


# ---------------- Main ----------------

async def post_init(application):
    """Bot চালুর সময় আসল username বের করে নিন (রেফারেল লিংকের জন্য)."""
    global BOT_USERNAME
    if BOT_USERNAME:
        return
    try:
        me = await application.bot.get_me()
        if me.username:
            BOT_USERNAME = me.username
            logger.info("Bot username: @%s", BOT_USERNAME)
    except Exception as exc:
        logger.warning("Bot username ber kora jayni: %s", exc)


def main():
    if not BOT_TOKEN:
        logger.error("BOT_TOKEN সেট করা নেই! Render env-এ BOT_TOKEN দিন।")
        raise SystemExit(1)
    init_db()
    start_health_server()
    application = ApplicationBuilder().token(BOT_TOKEN).post_init(post_init).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("stats", cmd_stats))
    application.add_handler(CommandHandler("users", cmd_users))
    application.add_handler(CommandHandler("addbalance", cmd_addbalance))
    application.add_handler(CommandHandler("broadcast", cmd_broadcast))
    application.add_handler(CommandHandler("reply", cmd_reply))
    application.add_handler(CommandHandler("approve_withdraw", cmd_approve_withdraw))
    application.add_handler(CommandHandler("reject_withdraw", cmd_reject_withdraw))
    application.add_handler(CallbackQueryHandler(task_callback, pattern=r"^task:(join_proxy|join_community|share_shop)$"))
    application.add_handler(CallbackQueryHandler(task_share_done, pattern=r"^task_share_done$"))
    application.add_handler(CallbackQueryHandler(task_back, pattern=r"^task_back$"))
    application.add_handler(CallbackQueryHandler(withdraw_method_callback, pattern=r"^wd_method:(bKash|Nagad)$"))
    application.add_handler(CallbackQueryHandler(withdraw_decision_callback, pattern=r"^wd_(ok|no):\d+$"))
    application.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text)
    )
    logger.info("%s cholche...", BOT_NAME)
    application.run_polling()


if __name__ == "__main__":
    main()
