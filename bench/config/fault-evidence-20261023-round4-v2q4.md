# arena.ai 故障证据 — 2026-10-23 路 C（V2×Q4）

> origin: ai
> 判定人：route C 执行 subagent（本地通道降级，model=qwen3.8-27b-w8a16）

## 判定

**arena.ai 仍不可用 — Cloudflare IP 级封禁**（round3 05:5x 起封禁，至 06:5x 未解封），按任务书规则该路由改本地降级通道。

## 尝试记录（Asia/Shanghai）

| # | 时间 | URL | 结果 |
|---|------|-----|------|
| 1 | 06:5x | https://arena.ai/text/direct（任务书要求的简单 run 探针） | "Attention Required! \| Cloudflare" → "Sorry, you have been blocked"，未及发送任何 prompt 即被拦截 |

## 证据

- 截图：`/Users/a1-6/Desktop/workspace/loop-artifacts/arena-launch/round4-v2-q4/probe-direct.png`（Cloudflare block 页）
- 前情：round3-v0 路由 05:54–05:57 三次尝试全被 Cloudflare IP 级硬拦截（`fault-evidence-20261023-round3-v0.md`）；round2 各路由 03:3x–04:1x 尚正常。推测短时间多路并发触发风控后封禁持续。

## 降级决定

3 格（V2 × Q4 × {claude-sonnet-5-high, gemini-3.1-pro-preview, qwen3.6-plus}）：
- **qwen3.6-plus 档**：本地降级通道执行（实际模型 = qwen3.8-27b-w8a16，channel=local，degraded:true）。
- **claude-sonnet-5-high / gemini-3.1-pro-preview 两档**：记 N/A（原因：本地仅 vllm/qwen3.8-27b-w8a16 可跑，无对应厂商模型；arena 通道不可用）。
