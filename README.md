# OpenClaw Skill 线上商店

社区驱动的 OpenClaw 技能市场 — 浏览、搜索、发现和分享 OpenClaw Skills。

## 功能

- 🔍 **技能搜索** — 按名称和描述关键字搜索
- 🏷️ **分类筛选** — 按开发/效率/安全/AI 等分类浏览
- 📋 **技能详情** — 查看完整信息、安装命令和项目主页
- ✨ **技能提交** — 社区成员可提交新 Skill

## 快速启动

```bash
# 1. 安装依赖
pip install flask

# 2. 初始化数据库（预置 8 个 Skill）
python seed_data.py

# 3. 启动服务
python app.py

# 4. 访问
open http://localhost:5050
```

## 运行测试

```bash
python -m pytest -v
```

## 技术栈

- **后端:** Python 3.11 + Flask 3.x
- **数据库:** SQLite（单文件，零配置）
- **前端:** Jinja2 模板 + 原生 CSS（GitHub 暗色主题）
- **测试:** pytest（20 个测试）

## 项目结构

```
openclaw-skill-store/
├── app.py              # Flask 应用 + 路由
├── models.py           # SQLite 数据模型
├── seed_data.py        # 种子数据（8 个 Skill）
├── templates/          # Jinja2 模板
│   ├── base.html       # 基础布局
│   ├── index.html      # 首页（列表+搜索）
│   ├── skill_detail.html  # 技能详情
│   ├── submit.html     # 提交表单
│   └── 404.html        # 404 页面
├── static/
│   └── style.css       # 暗色主题样式
├── tests/
│   ├── test_app.py     # 路由测试（16 个）
│   └── test_models.py  # 模型测试（4 个）
└── requirements.txt
```

## 由 AI 自主开发系统构建

本项目完全由 `autodev-pipeline` AI 自主开发系统构建：
1. 需求分析 → 方案设计
2. 任务拆分 → 并行开发（子 Agent）
3. 代码审查 → 测试验证
4. 部署上线

详见: `/Users/huymac/projects/ai-autodev-system/docs/architecture.md`
