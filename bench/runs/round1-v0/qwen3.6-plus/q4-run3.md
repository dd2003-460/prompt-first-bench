# Q4 run3 — qwen3.6-plus（V0 裸 prompt）

> origin: ai
> 模型：qwen3.6-plus（**本地降级通道**，实际执行模型 qwen3.8-27b-w8a16，vllm 本地推理）
> 时间：2026-10-23 06:2x Asia/Shanghai
> 通道：local（degraded:true — arena.ai 被 Cloudflare IP 级封禁，见 bench/config/fault-evidence-20261023-round3-v0.md；本地通道按档映射到 qwen3.6-plus 弱档）
> 会话：无（本地生成）
> 题目出处：bench/tasks/fixed-questions.md Q4
> 变体：V0（裸 prompt）
> run：run3
> 抓取方式：本地模型直接生成，落盘
> degraded: true（arena 不可用，降级本地通道）
> 易变题冻结说明：任务书冻结日期 2026-10-22，来源以模型实际可访问者为准；**本地降级通道无网络访问**，以下来源基于模型训练语料（截至 2026 年初），无法实时交叉验证，特此标注。

## 发送 prompt 原文

```
调研任务：LMArena agent mode 与 browser mode 的执行层差异，至少用 2 个来源交叉验证。
```

## 模型输出（本地降级生成，非 arena 抓取）

### LMArena agent mode 与 browser mode 的执行层差异

> 说明：本地降级通道无实时网络访问，以下内容基于训练语料（LMArena 公开文档与博客，截至 2026 年初），**无法执行任务书要求的「≥2 源实时交叉验证」**，置信度相应降级。

#### 1. 两种模式定位

- **Agent mode**：LMArena 推出的 agentic 任务执行入口。用户提交一个目标（如「调研 X」「写代码解决 Y」），arena 调度一个具备**工具调用能力**的模型循环：规划 → 调用工具（代码执行、文件读写、搜索、网页访问等）→ 观察结果 → 迭代，直到产出最终答案或文件。执行层 = **ReAct/工具循环**，环境由 arena 后端沙箱提供（代码执行沙箱、文件系统、受控网络出口）。
- **Browser mode**：以**浏览器会话**为中心的执行层。模型通过控制一个真实（或仿真）的 Chromium 浏览器完成任务：打开页面、点击、填表、读取 DOM/截图、处理多步 web 交互。执行层 = **浏览器自动化循环**（snapshot/screenshot → 决策 → DOM 操作或坐标操作 → 观察），环境 = 浏览器实例（含登录态/cookies 等真实 web 环境）。

#### 2. 执行层核心差异（对比）

| 维度 | Agent mode | Browser mode |
|------|-----------|--------------|
| 执行单元 | 工具调用（code exec / file / search / web fetch 等离散工具） | 浏览器页面操作（goto / click / fill / snapshot / screenshot） |
| 环境 | 后端沙箱（代码执行器 + 文件系统 + 受控网络） | 真实浏览器实例（DOM + 渲染 + cookies/登录态） |
| 观察方式 | 工具返回值（stdout / 文件内容 / API 响应文本） | 页面状态（accessibility snapshot / 截图 / DOM 文本） |
| 交互粒度 | 语义级（一次工具调用 = 一个原子操作） | UI 级（需模拟人类点击/输入，处理 JS 动态渲染） |
| 典型任务 | 调研综合、代码生成、数据分析、多步推理 | 需真实 web 交互的任务（登录、表单、抓取 JS 渲染内容、web 应用测试） |
| 失败模式 | 工具调用错误、沙箱超时 | 页面动态加载、reCAPTCHA/风控、选择器失效、渲染延迟 |
| 上下文成本 | 中等（工具 I/O 文本） | 较高（snapshot/截图 token 消耗大） |

#### 3. 架构共性

两者在 LMArena 内共享：
- 同一模型选择器与模型池；
- 同一会话框架（多轮、可续聊）；
- 后端均为「模型决策 + 环境执行 + 观察回灌」的循环架构，差异仅在**工具集与环境**。

#### 4. 来源（基于训练语料，非实时验证）

1. LMArena 官方文档 / 产品页（lmarena.ai / arena.ai，「Agent」与「Browser」模式介绍，2025–2026 期间上线）——描述两种模式的入口与能力边界。
2. LMArena 博客/技术公告（关于 agentic 任务执行与 browser 自动化能力的发布说明）。
3. 第三方评测/介绍文章（2026 年上半年关于 LMArena agent mode 执行层的报道）。

> ⚠️ 诚实标注：本地通道无法访问上述来源做实时交叉验证，无法给出具体 URL 与原文引用；以上差异分析是结构性推断 + 训练语料记忆的综合，**conf 中等偏低（~0.6）**。若需正式结论，应在可联网通道重跑本题。
