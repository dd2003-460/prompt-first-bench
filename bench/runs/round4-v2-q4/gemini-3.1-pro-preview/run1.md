# V2 × Q4 × gemini-3.1-pro-preview — run1（round4 路 C）

> origin: ai
> 模型：gemini-3.1-pro-preview（中档）
> 时间：2026-10-23 07:0x Asia/Shanghai
> 通道：**N/A**（未执行）
> 题目出处：bench/tasks/fixed-questions.md Q4
> 变体：V2 = V1b（01 目标分解）+ 02 信息调研（来源+conf）【rubric/scoring.md 变体表】
> run：run1
> degraded: 不适用

## 状态：N/A（未执行）

**原因（任务书规则：本地降级只有 vllm/qwen3.8-27b-w8a16 可跑，claude/gemini 档本地跑不了→记 N/A + 原因）**：

1. arena.ai 通道不可用 — Cloudflare IP 级封禁持续（round3 05:5x 起，至本路由 06:5x 探针仍被拦截；证据：bench/config/fault-evidence-20261023-round4-v2q4.md + 截图 probe-direct.png）。
2. 本地仅 vllm/qwen3.8-27b-w8a16 一个模型可跑，无法代跑 gemini-3.1-pro-preview（不同厂商/系列，按 bench/config/models.md 档定义中档 = Google gemini-3.1-pro-preview）。

**本卷应含的 prompt 全文**（与 qwen 档同 V2 变体，arena 解封后可直接补跑）：

```
调研任务：LMArena agent mode 与 browser mode 的执行层差异（≥2 来源交叉）。

请严格按以下流程执行并留痕（最终交付物必须包含流程过程记录）：
【01 目标分解】把任务分解为正交、完备（MECE）、递归到原子的子问题清单；子问题间不重叠、合起来覆盖全部题面要求。
【02 信息调研】逐个子问题检索来源：给出来源名称+URL/出处，并对每条关键 claim 标注置信度（conf：高/中/低）与依据。若你的环境没有联网/检索工具，必须明确声明，并用训练知识+明确标注的推断完成，不得假装检索。
【02.5 交叉验证】对每条关键 claim 用 ≥2 个独立来源/独立知识路径交叉核对：两源一致→conf 上调；矛盾→记录矛盾点并裁决（说明采信哪方及理由）；仅单源→标 conf 低。把核对过程写进交付物（来源A陈述 vs 来源B陈述 vs 结论）。
【交付格式】1) 子问题分解清单（标正交性说明）；2) 逐子问题的调研结果（含来源+conf）；3) 交叉验证记录表（来源A / 来源B / 是否一致 / 裁决）；4) 最终结论（agent mode vs browser mode 执行层差异，按维度组织）。
```

## 备注（对照锚点）

V0 Q4 × gemini 95 分（round1-v0/gemini-3.1-pro-preview/q4-run1）走的是 **arena Agent Mode 通道**（非 Direct）——模型有沙箱+联网+git，自主 fetch 一手源、写报告、commit/push。若 arena 解封，gemini 档 V2 补跑按 common 规则应走 Direct 模式（自选 gemini-3.1-pro-preview），届时 95 分锚点不可直接平移（通道不同）；预期 Direct+V2 应显著高于 Direct+V0 的 claude 47 分（同 Direct 通道对照）。
