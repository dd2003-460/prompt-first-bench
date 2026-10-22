# RALPH Loop 团队配置（操作手册）

> 来源：原 AGENTS.md「RALPH Loop 团队配置」节，2026-10-21 移入（m00172 批准）。AGENTS.md 留指针。

## 全局 Team 定义

```
~/.claude/teams/ralph/
├── config.json              # Team 定义（成员、模型、工作目录）
├── commander-prompt.md      # Commander（指挥官）系统提示
└── README.md                # 文档
```

这是一个通用的 Team 配置，可以应用于 workspace 中的任意研究项目。
Commander 是团队的指挥层，通过 Agent 工具动态创建子代理执行任务。

## 启动方式

```bash
# 方式一：使用启动脚本（推荐）
ralph-start <project-dir>

# 方式二：手动启动
cd <project-dir> && claude -p "启动 RALPH Loop 团队。读取 .claude/ralph-loop.local.md 确认 loop_phase。"
```

**前置条件**：项目目录下必须有 `CLAUDE.md`。如果没有，从模板创建：
```bash
cp /Users/a1-6/Desktop/workspace/agents-templates/RALPH-project/CLAUDE.md <project-dir>/CLAUDE.md
```

## 状态查看

```bash
ralph-status
```

扫描所有项目，显示迭代号、loop phase、上一轮动作和结果的摘要表。

## 新建项目支持 RALPH

1. 复制模板到项目目录（参考 `agents-templates/RALPH-project/CLAUDE.md`）
2. 创建 symlink 指向全局 agents：`mkdir -p .claude && ln -sf /Users/a1-6/Desktop/workspace/agents .claude/agents`
3. 只需 CLAUDE.md 引用全局 agents 和 loop 定义，其余配置通过 Commander 自动化管理

## 关键路径

| 文件/目录 | 用途 |
|-----------|------|
| `agents/*.md` | 全局 Agent 规格（12个） |
| `loop/prompt-first/` | 1-loop 阶段定义（01–06 + 02.5/04.5） |
| `loop/archived-20261016/` | 1-loop 完整归档（main-8.7-loop）+ 2-loop（per-step）+ 本文件 |
| `<project>/tasks/decomposition.md` | 规划记录（分解树 + 任务表；派发只执行表内条目） |
| `scripts/ralph-sync.sh` | 同步脚本（每轮结束时调用） |
| `projects/ACTIVE.md` | 活跃项目面板（自动聚合） |
| `<project>/.claude/ralph-loop.local.md` | 项目全局状态副本 |
| `<project>/loop-state.json` | 项目本地状态 |
