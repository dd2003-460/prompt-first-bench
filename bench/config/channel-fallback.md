# origin: ai
# channel-fallback.md — round4 通道状态与 fallback 决策（2026-10-23）

## arena 状态：未解封 ❌

- `https://arena.ai/text/direct`（Direct 模式）：Cloudflare IP 级整站封禁，标题 `Attention Required! | Cloudflare`，`Sorry, you have been blocked`，Ray ID `a4ec11b18cff0507`。
- `https://arena.ai/agent`（agent mode）：同样封禁，Ray ID `a4ec16467e7f0507`。
- 与 round3 结论一致，封禁未解除。证据：`bench/evidence/round4-channel/arena.png`、`lmarena.png`。

## 备用网页 LLM 站点可用性（ego-browser v2.1.0，ego-lite 已登录会话）

测试 prompt：「回复 OK 两个词」。完整数据：`bench/evidence/round4-channel/probe-results.json`。

| 站点 | 状态 | 登录态 | 可用模型 | 限制 | 响应质量 |
|---|---|---|---|---|---|
| ChatGPT (chatgpt.com) | ❌ 不可达 | — | — | `ERR_CONNECTION_RESET`（2 次重试），OpenAI 封大陆 IP | — |
| DeepSeek (chat.deepseek.com) | ✅ 可用 | 已登录（D·declaim（囯內）） | 网页版默认模型（无模型选择器） | 单默认档；深度思考/智能搜索开关 | ✅ 正常（回复「OK OK」，3s 思考） |
| GLM (chatglm.cn) | ✅ 可用（受限） | 未登录，访客可对话（访客_141a24） | GLM-5.3 极致（页面标注） | 访客模式回答中途被登录弹窗打断 | ⚠️ 部分可见（推理正常，最终答案未完整捕获） |
| Google AI Studio (aistudio.google.com) | ❌ 不可达 | — | — | `ERR_CONNECTION_RESET`（2 次重试），Google 封大陆 IP | — |
| Gemini (gemini.google.com) | ❌ 不可达 | — | — | 同上 | — |
| Perplexity (perplexity.ai) | ❌ 不可达 | — | — | `ERR_CONNECTION_RESET`，需海外网络 | — |
| LMArena (arena.ai) | ❌ Cloudflare 封禁 | — | — | IP 级整站封禁 | — |

## round5 起各档 run 的通道决策

优先级规则：**arena 解封 > 网页 LLM 对应模型 > N/A（本地降级时）**。

| 档（模型） | round5 通道 | degraded | 依据 |
|---|---|---|---|
| claude（opus 等） | **N/A** | true（N/A） | arena 封禁；网页无 claude 对应通道（ChatGPT 不可达）→ 记 N/A + 原因，不硬跑 |
| gemini | **N/A** | true（N/A） | arena 封禁；aistudio/gemini 均 ERR_CONNECTION_RESET → 记 N/A + 原因 |
| qwen | **本地 vllm/qwen3.8-27b-w8a16** | true（标注实际模型） | 按 round3 既定本地降级策略；本地可跑 |
| gpt | **本地 qwen 代跑 + degraded 标注**，或 N/A | true | 无网页 gpt 通道（ChatGPT 不可达）；若 round5 要求 gpt 档对比则 N/A，若允许代跑则本地 qwen 代（degraded:true + 实际模型） |

**交叉验证 ≥2 LLM 档（V3）round5 可行性**：当前仅 DeepSeek（完整）+ GLM（访客受限）两个网页 LLM 可用，勉强满足「≥2 个不同 LLM」但均为国内模型且无海外模型交叉；建议 round5 起交叉验证组合 = DeepSeek + GLM（国内双源），并标注「无海外模型交叉」限制。

**下一轮复检点**：round5 开跑前重查一次 arena（ego-browser 开 /text/direct 看是否解封）；若解封则 claude/gemini 档立即切回 arena Direct。
