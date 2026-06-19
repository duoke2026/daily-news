# 🌍 Daily Global Tech News

每天自动收集全球科技进展，每次发布20条最新科技新闻。

## 📰 功能特性

- ⏰ **每日定时更新** - 每天自动运行
- 🔍 **20条新闻** - 精选全球科技新闻
- 🌐 **多语言支持** - 覆盖全球主流技术媒体
- 📊 **话题分类** - AI、云计算、区块链、安全等
- 💾 **自动备份** - 所有新闻存档保存

## 📂 目录结构

```
daily-news/
├── .github/
│   └── workflows/
│       └── daily-news.yml      # 每日更新工作流
├── news/
│   └── 2026/
│       └── 06/                # 日期分类目录
│           └── 19.md          # 每日新闻文件
├── scripts/
│   └── fetch_news.py          # 新闻收集脚本
├── README.md                  # 项目说明
└── config.json               # 配置文件
```

## 🚀 快速开始

### 自动运行

工作流已配置为每天 UTC 时间 8:00 运行。

### 手动触发

```bash
# 通过 GitHub Actions 手动运行工作流
```

## 📚 新闻来源

该系统从以下权威科技媒体收集新闻：

- 🔴 Hacker News
- 🔵 TechCrunch
- 🟢 The Verge
- 🟡 ArXiv (AI/ML)
- 🟣 GitHub Trending
- 🟠 Product Hunt
- ⚫ Medium (Tech)

## 📝 新闻格式

每条新闻包括：
- 标题
- 描述
- 来源与链接
- 发布时间
- 相关标签

## 🔧 配置

编辑 `config.json` 自定义：
- 更新时间
- 新闻数量
- 话题分类
- 来源列表

## 📖 使用说明

1. 查看 `news/` 目录下的最新新闻
2. 按日期浏览所有历史新闻
3. 使用 GitHub Discussions 讨论相关话题

## 🤝 贡献

欢迎提交 Issue 或 PR 来改进新闻收集系统！

## 📄 License

MIT License

---

**最后更新**: 2026-06-19
