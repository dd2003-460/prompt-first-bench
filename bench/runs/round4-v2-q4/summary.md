# round4 路 C 汇总 — V2 × Q4 × 3 模型

> origin: ai · 2026-10-23 07:0x Asia/Shanghai · route C subagent（qwen3.8-27b-w8a16）
> 变体定义：V2 = V1b（01 目标分解：正交+完备+递归原子）+ 02 信息调研（来源+conf），出处 rubric/scoring.md 变体表。
> 通道状态：arena.ai 被 Cloudflare IP 级封禁（05:5x 起持续），本路由 06:5x 探针 1 次失败 → 按任务书降级（证据 bench/config/fault-evidence-20261023-round4-v2q4.md）。

## 3 格分数表（对照 V0 Q4：gemini 95 / claude 47 / qwen 40）

| 模型档 | 通道 | V0 Q4 | V2 Q4（本路由） | Δ | 备注 |
|---|---|---|---|---|---|
| claude-sonnet-5-high（强） | N/A（未执行） | 47（fail，Direct） | **N/A** | — | arena 封禁 + 本地无该模型；N/A 卷内留 prompt 全文与 H1/H2 待验证假设 |
| gemini-3.1-pro-preview（中） | N/A（未执行） | 95（success，**Agent Mode 通道**） | **N/A** | — | 同上；注意 V0 锚点 95 分是 agent 通道（有工具），与 Direct 不可直接平移 |
| qwen3.6-plus（弱） | local degraded（qwen3.8-27b-w8a16） | 40（fail，local） | **80（success 压线，n=1 单评）** | **+40** | 同通道同 prompt 族对照，增益可归因于 V2 流程 |

矩阵计入：1/3 格有分（qwen），2/3 格 N/A。

## 交叉验证对需检索题的增益初读数（n=1 探索性）

- **纯记忆通道下 V2 流程仍有实质增益（40→80）**：prompt 强制"给来源+conf+两源核对+无工具必须声明"后，模型把训练语料中的具体篇目/年份/统计量调出（LMSYS 博客 2023-05-03、arXiv:2403.04132、Agent Mode 发布 2026-06-04、Agent Arena 方法学、Help 系列），替代 V0 卷的纯结构推断。无通道变量（两卷均 local degraded）→ 增益归因 prompt 流程。
- **交叉验证环节的真实上限**：本地通道 7 条 claim 中 6 条"双源"同属官方文档族记忆，独立性弱；URL 级实时核对不可行。V2 的 02.5 条款在有网络通道（arena agent mode）预期增益更大——gemini 95 分卷的实证（自主 fetch 一手源）即该形态的上界参照。
- **退化路径封堵**：V0 裸 prompt 对"≥2 源交叉"这类隐含工具要求的题 → 模型自述无工具后退化为方法建议（claude 47 分主失分点）；V2 prompt 的显式条款（无工具→声明+用训练知识完成）在 qwen 卷实测堵住了该退化（产出 7 条带 conf claim 而非 0 事实）。

## claude 档失分原因判定

V0 Q4 × claude 47 分（Direct 通道）：**主因 = 裸 prompt 未声明工具缺失约束 → 模型"无可靠检索工具"认知下退化为"你该去哪查"的元方法输出，零可计分事实**；"没工具"是放大器而非唯一因（V2 同 prompt 在本地记忆通道即可 80 分，证明知识本身够、缺的是流程约束）。判定 conf 中：H2 的最终验证需 arena 解封后 claude Direct × V2 补跑（N/A 卷已留 prompt 全文）。

## 落盘清单

- bench/runs/round4-v2-q4/qwen3.6-plus/run1.md（prompt 全文 + 模型输出全文 + 交叉验证记录表 + 通道限制声明）
- bench/runs/round4-v2-q4/qwen3.6-plus/run1-score.md（D1-D4 逐项 + "D1 证据获取方式对比 V0" 单列）
- bench/runs/round4-v2-q4/claude-sonnet-5-high/run1.md（N/A + 原因 + prompt 全文 + 待验证假设）
- bench/runs/round4-v2-q4/gemini-3.1-pro-preview/run1.md（N/A + 原因 + prompt 全文 + 通道锚点备注）
- bench/config/fault-evidence-20261023-round4-v2q4.md（arena 封禁证据 + 降级决定）
- 截图：/Users/a1-6/Desktop/workspace/loop-artifacts/arena-launch/round4-v2-q4/probe-direct.png

## 限制

n=1/格；qwen 卷评审 = 执行者单评（同模型自评，探索性）；V2 定义按 scoring.md（01+02），未含 02.5 的"≥2 独立 LLM 服务"强条款（按 FINAL-VERIFY.md 该要求属 V3 臂）——本卷 02.5 节为 prompt 内的来源级交叉核对，强度低于 V3 的跨 LLM 核对，读增益时须注意。
