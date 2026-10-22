# arena.ai 故障证据 — 2026-10-23 路 B（V1a/V1b × Q1）

> origin: ai
> 判定人：route B 执行 subagent（本地通道降级，实际模型 vllm/qwen3.8-27b-w8a16）

## 判定

**arena.ai 不可用 — Cloudflare IP 级封禁**（与 05:54–05:57 路 B 补 run3 同一封禁窗口，未解封）。试跑 1 次简单 run（任务书允许 1 次）即失败，按任务书规则全部走本地降级通道。

## 尝试记录（Asia/Shanghai）

| # | 时间 | URL | 结果 |
|---|------|-----|------|
| 1 | 06:51 | https://arena.ai/text/direct | "Attention Required! \| Cloudflare" → "Sorry, you have been blocked"（Ray ID a4ec11a65fed0507） |
| 2 | 06:53 | https://arena.ai/（确认性复查，非新 run） | 同上，Cloudflare block 页 |

## 证据

- 截图：`/Users/a1-6/Desktop/workspace/loop-artifacts/arena-launch/round4-v1q1/fail1-cloudflare-block.png`
- 现象：ego-browser（ego-lite 已登录 profile）打开 arena.ai 任意路径均返回 Cloudflare "Sorry, you have been blocked" 硬拦截页；非 reCAPTCHA（可点过），非临时 429，为 IP 级安全封禁。
- 前情：round2 各路由今日 03:3x–04:1x 正常；05:5x 起被封（见 `fault-evidence-20261023-round3-v0.md`）；06:51 仍未解封。

## 降级决定

6 格（V1a/V1b × Q1 × 3 模型）全部无法走 arena：

- **qwen3.6-plus 档 2 格**（V1a×Q1、V1b×Q1）：本地降级通道执行（channel=local，degraded:true，实际模型 = 执行者自身 vllm/qwen3.8-27b-w8a16，按任务书"代 qwen 档 + 实际模型标注"）。
- **claude-sonnet-5-high / gemini-3.1-pro-preview 共 4 格**：记 N/A（原因：本地通道无该模型，arena 不可用）。
