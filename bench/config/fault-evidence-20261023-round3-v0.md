# arena.ai 故障证据 — 2026-10-23 路 B（V0 补 run3）

> origin: ai
> 判定人：route B 执行 subagent（本地通道降级，model=qwen3.8-27b-w8a16）

## 判定

**arena.ai 不可用 — Cloudflare IP 级封禁**，连续 3 次尝试全部失败，按任务书规则该格改本地降级通道。

## 尝试记录（Asia/Shanghai）

| # | 时间 | URL | 结果 |
|---|------|-----|------|
| 1 | 05:54 | https://arena.ai/text/direct | "Attention Required! \| Cloudflare" → "Sorry, you have been blocked"（Ray ID a4ebbf9daa01a13e） |
| 2 | 05:56 | https://arena.ai/text/direct（retry） | 同上，Cloudflare block 页 |
| 3 | 05:57 | https://arena.ai/（根域） | 同上，Cloudflare block 页 |

## 证据

- 截图：`/Users/a1-6/Desktop/workspace/loop-artifacts/arena-launch/round3-v0-run3/fail1-cloudflare-block.png`
- 现象：ego-browser（ego-lite 已登录 profile，前几轮 arena 均正常）打开 arena.ai 任意路径均返回 Cloudflare "Sorry, you have been blocked" 硬拦截页；非 reCAPTCHA（可点过），非临时 429，为 IP 级安全封禁。
- 注：round2 各路由（v0-q1 / v1a-q2 / v1b-q2）今日凌晨 03:3x–04:1x 均正常跑通，05:5x 起被封，推测短时间内多路并发触发 Cloudflare 风控。

## 降级决定

12 格（Q2/Q3/Q4/Q5 × 3 模型 × run3）全部无法走 arena：
- **qwen3.6-plus 档 4 格**：本地降级通道执行（实际模型 = 执行者自身 qwen3.8-27b-w8a16，channel=local，degraded:true）。
- **claude-sonnet-5-high / gemini-3.1-pro-preview 共 8 格**：记 N/A（原因：本地通道无该模型，arena 不可用）。
