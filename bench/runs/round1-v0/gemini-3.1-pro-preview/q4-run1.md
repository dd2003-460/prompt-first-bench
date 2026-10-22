# Q4 × gemini-3.1-pro-preview run1

- **题面**: 调研任务：LMArena 的 agent mode 与 browser mode 在执行层面上的差异（谁先、内容差异），给出来源。
- **V 等级**: V0（裸 prompt，无 loop 结构）
- **模型**: gemini-3.1-pro-preview（Agent Mode 会话，非 Direct）
- **run**: 1
- **会话 URL**: https://arena.ai/agent/01a164cb-92e2-71ae-9db4-b4440c309c57
- **抓取时间**: 2026-10-23 02:20 +08:00
- **抓取方式**: ego-browser v2 API, body.innerText, 完整报告 4934 字符
- **附加产物**: 模型自主写报告 bench/research/2026-10-22-q4-agent-vs-browser.md（commit e186401，+155 行）

## 答案（完整）

### 0. 先说第一发现：术语不对（conf 高）

Arena 官方不存在名为 "Browser Mode" 的模式。官方口径只有 Battle（默认）/ Direct / Side-by-Side / Agent Mode，发布博客与 Help 文档均如此列举。因此下文 "browser mode" 按本仓库两个有据可查的所指展开：(A) 产品层 = 浏览器聊天模式统称（Battle/Direct/Side-by-Side）；(B) 本仓库通道层 = ego-browser 自动化驱动 arena.ai Direct（round1-v0 全部 run 的通道）。A、B 模型侧执行路径相同，差别只在驱动 UI 的是真人还是脚本。

### 1. 谁先（历史先后，conf 高）

| 时间 | 事件 | 来源 |
|---|---|---|
| 2023-04 运行 / 2023-05-03 公开 | Chatbot Arena 上线：浏览器内两匿名模型并排聊天、投票后揭晓 | LMSYS 博客 2023-05-03 · arXiv:2403.04132 |
| 2023-05 | 开源实现 FastChat 支撑 Arena：controller 协调 + model worker 推理 + Gradio web server | lm-sys/FastChat |
| ≤2024-03-07 | 论文脚注自述站点已有 "direct chat"，故 Direct 先于 Agent（精确上线日官方未给，conf 中） | arXiv:2403.04132 |
| 2024-09-20 | "毕业"迁至 lmarena.ai（LMArena 之名定型） | LMSYS 新站点公告 |
| 2026-01-28 | LMArena 更名为 Arena（arena.ai） | LMArena is now Arena 博客 |
| 2026-06-04 | Agent Mode 官方发布（产品博客 + Agent Arena 方法学同日发）；发布时已有近 7 天 160,480 任务的运行数据，故实际开放早于公告数周（推断，conf 中） | Agent Mode 发布 2026-06-04 · Agent Arena 方法学 |
| 2026-08-24 | Agent Mode 的 GitHub 编程形态：OAuth 连仓库、沙箱 clone、diff 面板、commit/push/PR——即本仓库当前通道 | Coding in Agent Mode 2026-08-24 |

**一句话**：browser 先、agent 后，相差约 3 年。

会话内"谁先动"也不同（conf 高）：Battle 是用户先出题→系统采样 2 匿名模型→先投票后揭晓；Agent 是平台先备环境（随机分配 1 个 orchestrator + 仓库 clone 进沙箱）→用户一条 prompt→agent 自主规划连环动手，且 orchestrator 身份当前从不揭晓、仅在预判失败时可自动换模；仓库 browser 通道走的 Direct 则是先具名选模、后聊天。

### 2. 内容/执行差异（7 个正交维度）

| # | 维度 | Browser（Battle/Direct/Side-by-Side） | Agent Mode | 来源 |
|---|---|---|---|---|
| 1 | 谁拆任务/驱动循环 | 用户（或外置 ego-browser 脚本）逐轮索取；官方定性 "isolated, single-modality interactions"，复杂任务靠用户自行拆成多条 prompt | 内置 harness：orchestrator "autonomously builds a plan" 一口气跑完多步流；7 天实测会话平均 ~16.5 次结构化工具调用，长尾数百次 | Agent Mode 发布 · Agent Arena 方法学 |
| 2 | 工具与环境反馈 | 经典文本路径模型侧无工具：不跑代码、不触文件、环境不回话 | bash 沙箱/读写文件/web_search/fetch_page/生图/向用户提问；7 天 2,060,159 次调用（bash 93.6万、写文件 55万、搜索 27.6万）；退出码与工具错误即反馈 | Agent Arena 方法学 · Help: Agent Mode |
| 3 | 状态与持久化 | 无工作区；会话撞 token 上限即终结、上下文不可迁移到新会话 | 有状态长线程：工作区文件（可下载 zip）、内置上下文压缩（compaction）；连仓库时在沙箱副本+工作分支作业，每会话当前仅 1 个 PR，PR 关闭后不可再 push | Help: Agent Mode · Help: Coding · Help: Token Limits |
| 4 | 模型分配/披露 | Battle 随机 2 匿名、投票后揭晓；Direct/Side 用户具名选 | 每会话随机 1 orchestrator 且不披露；子组件（工具、生图模型、harness 等）亦随机化以做因果识别 | Agent Arena 方法学 · Help: Agent Mode |
| 5 | 产物形态 | 仅聊天文本（官方自比：以往是 "read-only / copy-paste" 体验） | 文件工件：仓库改动+diff、报告、可预览的站点、zip；连 GitHub 后交付 = 分支 + PR + checks | Coding in Agent Mode · Help: Coding |
| 6 | 评测信号/计分 | 匿名成对投票 → Bradley–Terry 回归（Elo 的统计化继任）；Direct 无票、Side 票不入榜 | 不设对战：单线程 trace 挖 5 信号（Confirmed Success、表扬vs投诉、可调向性、Bash 恢复、工具幻觉），组件随机化构成多干预 RCT，因果追踪估 "net improvement"（附 95% CI） | arXiv:2403.04132 · Agent Arena 方法学 |
| 7 | 权限与副作用 | 模型输出无现实副作用；风险面主要是对话数据被平台收集研究 | 可产生真实副作用（沙箱任意执行、经授权 commit/push/建 PR）；隔离靠一次性云沙箱+授权范围+用户 diff 审批 | Arena FAQ · Coding in Agent Mode |

**定量锚点**：2026-06 近 7 天，Agent 侧 160,480 任务/128,244 会话、75.6% 会话用过工具、写文件约 4,030 万行；browser 侧的对应量是"票数"（论文期 24 万票）。一个在计票、一个在计工具动作——这就是执行层差异的实质：循环归谁、环境是否回话、产物是否落盘。

### 3. 本仓库双通道实证（同一道 Q4 的两次作答）

- **browser 通道旧卷**（bench/runs/round1-v0/claude-sonnet-5-high/q4-run1.md，ego-browser→Direct 裸 prompt）：模型自述"没有可靠的检索工具"、核心全标"推测"，47/100 fail。其三处推测现已可纠正：① "Browser = DOM 单步操作"系误判——官方无此形态；② "Agent = 封装浏览器的循环"——循环属实，但官方工具量表无交互式 DOM 工具；③ "agent mode 不是公开文档化功能"——今有一手博客+方法学+Help 全集。
- **agent 通道本次**：模型直接在沙箱中读仓库、联网抓取上表全部一手源、写报告并 commit/push——即以自身执行演示两者差异。须注意：本会话 orchestrator 官方不披露，故该工件不能直接当具名模型的消融格，能否计入矩阵待 Lead 裁决。
- **对旧卷评分备注的校准**：若指仓库的外置流水线（脚本选模→抓取→Lead 落盘）则成立；若指模型侧则与一手源冲突。分水岭是循环的所有者（外置的人/脚本 vs 内置的 harness）。

### 4. 消歧与限制

- **Search Arena ≠ browser mode**：它是独立页签（2025-03-18 上线），搜索增强模型仍两两成对靠投票、无 bash/落盘，属 browser 家族的"会搜变体"。
- **browser-use/DOM 操作类 agent ≠ 两者的任何一方**（如学术界 BrowserArena 与 LMArena 无隶属）；若题面指这类，正确答案第一行应是"LMArena 没有这个模式"。
- **未公开项如实标未知**：2026 年 browser 端生产栈（FastChat 仅确证 2023–24 公开实现）、Agent 的 system prompt 与子 agent 细节，官方均未披露；NYT 同日报道因 403 未能抓取全文、仅作线索，未承担任何关键 claim。

### 来源清单

1. LMSYS 博客 2023-05-03
2. Chatbot Arena 论文 arXiv:2403.04132
3. lm-sys/FastChat
4. LMSYS 新站点公告 2024-09-20
5. LMArena is now Arena 2026-01-28
6. Agent Mode 发布 2026-06-04
7. Agent Arena 方法学 2026-06-04
8. Help: Agent Mode
9. Help: Battle Mode
10. Arena FAQ
11. Coding in Agent Mode 2026-08-24
12. Help: Coding
13. Help: Token Limits
14. Search Arena arXiv:2506.05334

## 评分

| 维度 | 满分 | 得分 | 说明 |
|------|------|------|------|
| D1 正确性 | 40 | 38 | 术语纠正精准（官方无 Browser Mode），时间线 7 节点全对（2023-04 上线/2024-09 毕业/2026-01 更名/2026-06 Agent 发布），7 维度差异表准确，定量锚点精确（160,480 任务/2,060,159 次工具调用/75.6% 会话用过工具）。扣分：Direct 精确上线日标"conf 中"合理但未给具体推断值。 |
| D2 完备性 | 25 | 24 | 覆盖题面三要素（谁先+内容差异+来源）且超额：7 正交维度、会话内"谁先动"对比、双通道实证、消歧与限制。扣分：未显式回答"browser mode 是否指 browser-use/DOM 操作类 agent"这一可能的第三种解读（仅在消歧节提及）。 |
| D3 结构正交 | 20 | 19 | 4 节结构清晰（术语纠正/谁先/差异/消歧），表格为主便于扫描，7 维度正交不重叠。扣分：第 3 节"双通道实证"混入了仓库内部信息（旧卷 47 分、orchestrator 不披露），与"调研 LMArena 本身"的题面略有偏移。 |
| D4 来源 conf | 15 | 14 | 14 条来源全列（博客/论文/GitHub/Help 文档），每条 claim 有编号引用，conf 显式标注（高/中/未知）。扣分：arXiv:2506.05334（Search Arena）未在正文中展开说明其"会搜变体"定位的具体证据。 |
| **总分** | **100** | **95** | **success** |

## 与 Q4 × claude 对比

- Q4 × claude (47)：Direct 模式裸 prompt，模型自述"没有可靠的检索工具"，核心全标"推测"，三处推测被本次答案纠正。
- Q4 × gemini (95)：Agent Mode 会话，模型自主 fetch 多个一手源、写报告并 commit/push，以自身执行演示 agent mode 与 browser mode 的差异。

**结论**：通道差异（Direct vs Agent Mode）对 Q4 这类需要检索的题影响巨大（47 vs 95）。gemini 在 Agent Mode 下展现了完整的调研能力（联网+写文件+commit/push），远超 Direct 模式下的裸 prompt 表现。
