# V2 × Q4 × claude-sonnet-5-high — run1（round4 路 C）

> origin: ai
> 模型：claude-sonnet-5-high（强档）
> 时间：2026-10-23 07:0x Asia/Shanghai
> 通道：**N/A**（未执行）
> 题目出处：bench/tasks/fixed-questions.md Q4
> 变体：V2 = V1b（01 目标分解）+ 02 信息调研（来源+conf）【rubric/scoring.md 变体表】
> run：run1
> degraded: 不适用

## 状态：N/A（未执行）

**原因（任务书规则：本地降级只有 vllm/qwen3.8-27b-w8a16 可跑，claude/gemini 档本地跑不了→记 N/A + 原因）**：

1. arena.ai 通道不可用 — Cloudflare IP 级封禁持续（round3 05:5x 起，至本路由 06:5x 探针仍被拦截；证据：bench/config/fault-evidence-20261023-round4-v2q4.md + 截图 probe-direct.png）。
2. 本地仅 vllm/qwen3.8-27b-w8a16 一个模型可跑，无法代跑 claude-sonnet-5-high（不同厂商/系列，按 bench/config/models.md 档定义强档 = Anthropic claude-sonnet-5-high）。

**本卷应含的 prompt 全文**（与 qwen 档同 V2 变体，arena 解封后可直接补跑）：

```
调研任务：LMArena agent mode 与 browser mode 的执行层差异（≥2 来源交叉）。

请严格按以下流程执行并留痕（最终交付物必须包含流程过程记录）：
【01 目标分解】把任务分解为正交、完备（MECE）、递归到原子的子问题清单；子问题间不重叠、合起来覆盖全部题面要求。
【02 信息调研】逐个子问题检索来源：给出来源名称+URL/出处，并对每条关键 claim 标注置信度（conf：高/中/低）与依据。若你的环境没有联网/检索工具，必须明确声明，并用训练知识+明确标注的推断完成，不得假装检索。
【02.5 交叉验证】对每条关键 claim 用 ≥2 个独立来源/独立知识路径交叉核对：两源一致→conf 上调；矛盾→记录矛盾点并裁决（说明采信哪方及理由）；仅单源→标 conf 低。把核对过程写进交付物（来源A陈述 vs 来源B陈述 vs 结论）。
【交付格式】1) 子问题分解清单（标正交性说明）；2) 逐子问题的调研结果（含来源+conf）；3) 交叉验证记录表（来源A / 来源B / 是否一致 / 裁决）；4) 最终结论（agent mode vs browser mode 执行层差异，按维度组织）。
```

## 待验证假设（任务书重点观察项，留给补跑）

V0 Q4 × claude 47 分（round1-v0/claude-sonnet-5-high/q4-run1，Direct 通道）：模型自述"没有可靠的检索工具……无法真正完成 2 来源交叉验证"，退化为"你该去哪查"的方法建议，零可计分事实。
- 假设 H1：失分主因 = 无检索工具 + 裸 prompt 未声明工具缺失约束 → 退化为元方法输出；
- 假设 H2：V2 prompt 的"无工具必须声明 + 用训练知识完成 + 两源核对"条款能堵住退化路径 → claude 档 V2 分数应显著高于 47（方向性翻转，具体幅度待补跑）；
- 对照锚点：本路由 qwen 档同 prompt 同（本地记忆）通道实测 40→80（+40，fail→success），支持 H2 的机制可行性，但 claude 直连 run 才能定论。
