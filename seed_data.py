# seed_data.py — 预置 8 个真实的 OpenClaw Skill 种子数据
from models import get_db, init_db

SEED_SKILLS = [
    {
        'name': 'blogwatcher',
        'description': '监控博客和 RSS 订阅源，自动获取最新文章更新',
        'category': '效率',
        'author': 'OpenClaw',
        'install_cmd': 'openclaw install blogwatcher',
        'homepage': 'https://openclaw.ai/skills/blogwatcher',
        'emoji': '📰',
    },
    {
        'name': '1password',
        'description': '安全访问和管理 1Password 凭据，保护你的账号信息安全',
        'category': '安全',
        'author': 'OpenClaw',
        'install_cmd': 'openclaw install 1password',
        'homepage': 'https://openclaw.ai/skills/1password',
        'emoji': '🔐',
    },
    {
        'name': 'discord',
        'description': '管理 Discord 消息、频道和服务器交互',
        'category': '社交',
        'author': 'OpenClaw',
        'install_cmd': 'openclaw install discord',
        'homepage': 'https://openclaw.ai/skills/discord',
        'emoji': '💬',
    },
    {
        'name': 'canvas',
        'description': '生成和编辑 Canvas 图形，支持丰富的视觉创作',
        'category': '创作',
        'author': 'OpenClaw',
        'install_cmd': 'openclaw install canvas',
        'homepage': 'https://openclaw.ai/skills/canvas',
        'emoji': '🎨',
    },
    {
        'name': 'coding-agent',
        'description': 'AI 编程助手，帮你编写、审查和优化代码',
        'category': '开发',
        'author': 'OpenClaw',
        'install_cmd': 'openclaw install coding-agent',
        'homepage': 'https://openclaw.ai/skills/coding-agent',
        'emoji': '💻',
    },
    {
        'name': 'diagram-maker',
        'description': '一键生成架构图、流程图和各类技术图表',
        'category': '开发',
        'author': 'OpenClaw',
        'install_cmd': 'openclaw install diagram-maker',
        'homepage': 'https://openclaw.ai/skills/diagram-maker',
        'emoji': '📊',
    },
    {
        'name': 'apple-notes',
        'description': '管理 Apple Notes 笔记，同步和搜索你的备忘录',
        'category': '效率',
        'author': 'OpenClaw',
        'install_cmd': 'openclaw install apple-notes',
        'homepage': 'https://openclaw.ai/skills/apple-notes',
        'emoji': '📝',
    },
    {
        'name': 'gemini',
        'description': '接入 Google Gemini 模型，解锁多模态 AI 能力',
        'category': 'AI',
        'author': 'OpenClaw',
        'install_cmd': 'openclaw install gemini',
        'homepage': 'https://openclaw.ai/skills/gemini',
        'emoji': '🤖',
    },
]


def seed(conn=None):
    """向数据库插入 8 个预置 Skill（幂等：如已存在则跳过）"""
    if conn is None:
        conn = get_db()
        own_conn = True
    else:
        own_conn = False

    try:
        init_db(conn)

        for skill in SEED_SKILLS:
            existing = conn.execute(
                "SELECT id FROM skills WHERE name = ?", (skill['name'],)
            ).fetchone()
            if existing is None:
                conn.execute(
                    """INSERT INTO skills (name, description, category, author, install_cmd, homepage, emoji)
                       VALUES (?, ?, ?, ?, ?, ?, ?)""",
                    (skill['name'], skill['description'], skill['category'],
                     skill['author'], skill['install_cmd'], skill['homepage'], skill['emoji'])
                )
        conn.commit()
    finally:
        if own_conn:
            conn.close()


if __name__ == '__main__':
    seed()
    print("Seed data inserted successfully.")
