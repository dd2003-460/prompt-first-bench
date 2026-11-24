# gpt-researcher 臂 0 结果根因诊断 + 修复（2026-11-25 04:20）

## 现象
`gptr-q2-r1.json`（11-24 03:05）：48s 空返回，"No sources were retrieved (searches may have returned nothing or been blocked)"。

## 根因（网络层，非包层）
- ddgs 包默认 backend = **mojeek**，本机 `curl https://www.mojeek.com/search` → **HTTP 000（7.4s 超时，网络层封死）**
- `DDGS(backend="duckduckgo")` → `DDGSException: No results found`（ddg 端点本机返回 202 但 ddgs 解析不出结果）
- `DDGS(backend="bing")` → **OK，3 results**（llm-stats.com / benchlm.ai，10s 内）
- 旁证：s5 的 `research_hook` 不走 ddgs 包（走 ego-browser + arXiv API + bing 纯 HTTP + DDG-lite 快失败降级），所以 s5 搜索正常而 gptr 臂全空

### 端点可达性快照（本机直连，2026-11-25 04:18）
| 端点 | 结果 |
|---|---|
| mojeek（ddgs 默认） | HTTP 000 ❌ |
| html/lite/api.duckduckgo | HTTP 202（ddgs 解析不出）❌ |
| bing intl | HTTP 200 ✅ |
| searx.be | HTTP 200（JSON API 关闭）⚠️ |
| arxiv export / en.wikipedia | HTTP 200 ✅ |

## 修复（已落，pilot 结束后生效）
`run_gptr_q2.py` 顶部对 `ddgs.DDGS.text` 注入 `backend=bing`（monkeypatch，10 行，含注释）。
- 命中路径确认：vendored `runs/d1-gpt-researcher/gpt_researcher/retrievers/duckduckgo/duckduckgo.py` L32 `from ddgs import DDGS`（vendored 树无 ddgs shadow）→ patch 命中同一类
- 搜索腿不碰 vLLM，已单独验证 `DDGS(backend="bing")` 出结果
- 全臂重跑仍需 vLLM（pilot PID 53387 占着 8787，~7h）

## 备选（未用）
gpt-researcher searx retriever 需 `SEARX_URL`，但 searx.be JSON API 关闭 + 该 venv 里 langchain/pydantic 版本冲突 → 不选。bing 后端零 key、已验证，最短路径。
