# models.py — SQLite 数据模型
import sqlite3
import os

DATABASE = os.environ.get('DATABASE', os.path.join(os.path.dirname(__file__), 'skills.db'))


def get_db() -> sqlite3.Connection:
    """获取数据库连接，row_factory 设为 Row 以便字典式访问"""
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


def init_db(conn=None):
    """初始化数据库，创建 skills 表（如不存在）"""
    if conn is None:
        conn = get_db()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS skills (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT NOT NULL,
            category TEXT DEFAULT 'other',
            author TEXT DEFAULT '',
            install_cmd TEXT DEFAULT '',
            homepage TEXT DEFAULT '',
            emoji TEXT DEFAULT '🔧',
            downloads INTEGER DEFAULT 0,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
