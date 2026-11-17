# 检索设施修复任务书

## 背景

pfb 的基础检索设施目前只有 arXiv API + 直访站点能用，DDG/Bing/Startpage 全废。需要修复检索设施，让 pfb 能从权威、官方、社区三个层面获取信息。

## 目标

修复 pfb 的检索设施，使其能从以下三个层面获取信息：

1. **权威来源**：arXiv API（已能用）+ 官网直访（已能用）
2. **官方来源**：GitHub API（免费，5000 次/小时）+ 官方文档站（直访）
3. **社区来源**：ego-browser（已登录会话）+ 论坛直访（Stack Overflow / Reddit / Hacker News）

## 验收标准

1. **arXiv API**：已能用，不需要修复
2. **GitHub API**：能搜索 GitHub 仓库、issues、PRs（免费，5000 次/小时）
3. **ego-browser**：能搜索 Stack Overflow / Reddit / Hacker News（已登录会话）
4. **官网直访**：能直访官方文档站（如 PyTorch / TensorFlow / HuggingFace 文档）

## 任务分解

### 1. GitHub API 集成

- **目标**：集成 GitHub API，能搜索 GitHub 仓库、issues、PRs
- **验收**：能搜索 "langgraph checkpoint" 并返回相关仓库/issues/PRs
- **实现**：
  - 使用 GitHub REST API（免费，5000 次/小时）
  - 搜索端点：`/search/repositories`、`/search/issues`、`/search/code`
  - 认证：使用 personal access token（免费）
  - 落盘：`research_hook.py` 加 `_github_search(query, max_results=5)` 函数

### 2. ego-browser 集成

- **目标**：集成 ego-browser，能搜索 Stack Overflow / Reddit / Hacker News
- **验收**：能搜索 "langgraph checkpoint crash recovery" 并返回相关帖子
- **实现**：
  - 使用 ego-browser CLI（已登录会话）
  - 搜索端点：Stack Overflow / Reddit / Hacker News
  - 落盘：`research_hook.py` 加 `_ego_browser_search(query, max_results=5)` 函数

### 3. 官网直访

- **目标**：能直访官方文档站（如 PyTorch / TensorFlow / HuggingFace 文档）
- **验收**：能直访 PyTorch 文档并提取相关内容
- **实现**：
  - 使用 `web_fetch` 或 `ego-browser` 直访官方文档站
  - 落盘：`research_hook.py` 加 `_official_docs_search(query, max_results=5)` 函数

## 边界

- 不修改 pfb 的核心逻辑（decompose/search/validate）
- 只修改 `research_hook.py`（检索层）
- 所有修改必须留痕（git commit）

## 派发

- **通道**：arena agent mode
- **仓库**：pfb（prompt-first-bench.git）
- **分支**：main
- **任务书**：本文件
