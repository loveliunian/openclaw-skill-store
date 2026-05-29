#!/bin/bash
# OpenClaw Skill 商店 — 一键启动脚本
set -e

cd "$(dirname "$0")"

echo "=== OpenClaw Skill 在线商店 ==="

# 检查 Python
if ! command -v python3 &> /dev/null; then
    echo "错误: 需要 Python 3.10+"
    exit 1
fi

# 安装依赖
echo ">>> 安装依赖..."
pip install flask -q 2>/dev/null || true

# 初始化数据库
echo ">>> 初始化数据库..."
python3 seed_data.py

# 启动服务
echo ">>> 启动服务 (http://localhost:5050)..."
python3 app.py
