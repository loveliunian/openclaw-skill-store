# tests/test_models.py — 数据模型测试
import os
import pytest
import sqlite3

# Force test database before importing models
os.environ['DATABASE'] = os.path.join(os.path.dirname(__file__), 'test_skills.db')


@pytest.fixture(autouse=True)
def clean_test_db():
    """每个测试前清理测试数据库"""
    db_path = os.environ['DATABASE']
    if os.path.exists(db_path):
        os.remove(db_path)
    yield
    if os.path.exists(db_path):
        os.remove(db_path)


def test_init_db_creates_skills_table():
    """init_db 应创建 skills 表"""
    from models import init_db, get_db

    conn = get_db()
    init_db(conn)

    cursor = conn.execute(
        "SELECT name FROM sqlite_master WHERE type='table' AND name='skills'"
    )
    result = cursor.fetchone()
    assert result is not None
    assert result['name'] == 'skills'
    conn.close()


def test_skills_table_has_correct_columns():
    """skills 表应有所有必需的列"""
    from models import init_db, get_db

    conn = get_db()
    init_db(conn)

    cursor = conn.execute("PRAGMA table_info(skills)")
    columns = {row['name'] for row in cursor.fetchall()}

    expected_columns = {
        'id', 'name', 'description', 'category', 'author',
        'install_cmd', 'homepage', 'emoji', 'downloads', 'created_at'
    }

    assert expected_columns.issubset(columns), f"Missing columns: {expected_columns - columns}"
    conn.close()


def test_add_and_get_skill():
    """插入和查询 Skill 记录应正常工作"""
    from models import init_db, get_db

    conn = get_db()
    init_db(conn)

    conn.execute(
        """INSERT INTO skills (name, description, category, author, install_cmd, homepage, emoji)
           VALUES (?, ?, ?, ?, ?, ?, ?)""",
        ('test-skill', 'A test skill', 'testing', 'tester',
         'pip install test-skill', 'https://example.com', '🧪')
    )
    conn.commit()

    row = conn.execute("SELECT * FROM skills WHERE name = ?", ('test-skill',)).fetchone()
    assert row is not None
    assert row['name'] == 'test-skill'
    assert row['description'] == 'A test skill'
    assert row['category'] == 'testing'
    assert row['author'] == 'tester'
    assert row['install_cmd'] == 'pip install test-skill'
    assert row['homepage'] == 'https://example.com'
    assert row['emoji'] == '🧪'
    assert row['downloads'] == 0
    conn.close()


def test_seed_data():
    """运行 seed_data 后应有 8 个预置 Skill"""
    from models import init_db, get_db
    import seed_data

    conn = get_db()
    init_db(conn)

    seed_data.seed(conn)

    count = conn.execute("SELECT COUNT(*) as cnt FROM skills").fetchone()['cnt']
    assert count == 8, f"Expected 8 skills, got {count}"

    # 验证几个关键 Skill 存在
    row = conn.execute("SELECT * FROM skills WHERE name = ?", ('blogwatcher',)).fetchone()
    assert row is not None
    assert row['emoji'] == '📰'

    row = conn.execute("SELECT * FROM skills WHERE name = ?", ('coding-agent',)).fetchone()
    assert row is not None
    assert row['category'] == '开发'

    row = conn.execute("SELECT * FROM skills WHERE name = ?", ('gemini',)).fetchone()
    assert row is not None
    assert row['emoji'] == '🤖'

    conn.close()
