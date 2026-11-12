# origin: ai · 2026-11-11
# deepresearch 对照组框架选型（benchmark 用）

## 一句话结论

**Top-1 推荐：GPT-Researcher**（`assafelovic/gpt-researcher`）。它是唯一同时满足「pip 即可跑 + 原生多步检索+综合 + 能指向本地 OpenAI-compatible LLM」的现成 deepresearch 框架，部署最轻、与 bench 题（H200 TDP / LLaMA2 参数量这类需搜索验证的事实题）场景最对口。代价：它对模型指令遵循能力要求高，27B 本地模型可能偏弱——这是所有候选共同的结构性风险，不是 GPT-Researcher 独有。

---

## 为什么先拆后查（decomp）

任务 = 选一个「本地 Qwen3-27B 驱动 + 可插拔 search + 近 3 月活跃 + pip 可装」的开源 deepresearch 框架做 benchmark 对照组。正交子项：

| 子项 | 缺口 | 状态 |
|------|------|------|
| A. GitHub star / 最近 commit | 必须实查，凭记忆一律 [待核验] | ✅ 已实查（GitHub API） |
| B. 是否支持 OpenAI-compatible 本地 LLM (localhost:8787) | 看官方文档而非猜 | ✅ 已核文档 |
| C. 内置 web search / 自定义 search tool 可插拔性 | 看 README/配置 | ✅ 已核 |
| D. 部署复杂度（pip vs docker/db） | — | ✅ 已核 |
| E. deepresearch 场景适配度（多步检索+综合） | — | ✅ 已核 |

来源标注约定：① = 本轮 GitHub API / 文档实查；② = 工作区历史文件；③ = 纯记忆未验证 → 标 `[待核验]`。下文 star/commit 全部为 ① 类（2026-11-11 实查）。

---

## 候选对比（5 个）

> 注：候选里 `open_deep_research`(hf.co 官方示例) 实际仓库在 `langchain-ai/open_deep_research`，**已 archived**（见下），不符合「近 3 月活跃」约束，故降级为参考项而非正式候选。`AutoGPT/agpt-co` 中 agpt.co 是闭源 SaaS，其开源本体是 `Significant-Gravitas/AutoGPT`，下表按开源本体计。

| 框架 | repo | Stars ① | 最近 push ① | 本地 OpenAI-compat LLM | Web search / 自定义 search | 部署复杂度 | deepresearch 适配 |
|------|------|--------|------------|----------------------|--------------------------|-----------|------------------|
| **GPT-Researcher** ⭐top-1 | `assafelovic/gpt-researcher` | 30,628 | 2026-11-09 | ✅ 官方 docs 明确支持任意 LLM provider（含自定义 base_url） | ✅ 内置 DuckDuckGo/Bing/Tavily 等，search engine 可换 | **pip install gpt-researcher** 即可 | ★★★★★ 原生就是「多步检索+综合」deepresearch agent |
| OpenHands | `OpenHands/OpenHands`（原 All-Hands-AI，已改名） | 93,225 | 2026-11-11（当日） | ✅ 专门有 "Run Local LLMs" 文档页 | ✅ 内置 browser/web tools，可加自定义 tool | 偏重：默认 docker sandbox + runtime，pip 也能起但功能打折 | ★★★★ 通用 coding agent，能做检索但非 deepresearch 专用 |
| CrewAI | `crewAIInc/crewAI` | 60,768 | 2026-11-11（当日） | ✅ 走 LiteLLM，可指任意 base_url | 无内置，靠 task/tool 自接（可挂 research tool） | pip install crewai 即可 | ★★★ 多 agent 编排强，但 deepresearch 流程要自己搭 |
| LangGraph | `langchain-ai/langgraph` | 44,795 | 2026-11-11（当日） | ✅ 底层 langchain 可指任意 provider | 无内置，纯图节点自接 search node | pip install langgraph 即可 | ★★★ 灵活但要自己写检索循环，工程量大 |
| AutoGPT(开源本体) | `Significant-Gravitas/AutoGPT` | 187,991 | 2026-11-11（当日） | ⚠️ 走自己的 LLM 抽象，本地模型支持不如前几个直接 | ✅ 有 web search block | 偏重：自带平台/UI，docker 友好 | ★★★ 通用 agent 平台，deepresearch 非主打 |
| ~~open_deep_research~~（参考） | `langchain-ai/open_deep_research` | 12,677 | 2026-08-10 · **archived=True** | ✅ 基于 LangGraph，可指本地 LLM | ✅ 内置 search + 报告生成 | pip 即可 | ★★★★★ 设计就是 deepresearch，但**已归档停更**，不满足活跃度约束 |

### 关键判读

- **活跃度（近 3 月）**：GPT-Researcher(11-09)、OpenHands/CrewAI/LangGraph/AutoGPT(均 11-11 当日) 全过线；open_deep_research 最后 commit 停在 2026-08-10 且 archived，**出局**。
- **本地 LLM 直连 localhost:8787**：5 个都能指 OpenAI-compatible endpoint，但 GPT-Researcher 和 CrewAI(LiteLLM) 的「改个 base_url 就完事」最干净；OpenHands 需要配 local-llms 文档里的 runtime 参数。
- **search 可插拔**：GPT-Researcher 内置多个 search engine 且可替换，正好能换成我们的 `research_hook v2`（arXiv+ego-browser+Wikipedia+DDG-lite）当自定义 search tool；其余框架要么无内置要么要自己写节点。
- **deepresearch 场景对口**：GPT-Researcher 从第一天就是「给定问题→多轮检索→综合成报告」，与 bench 题形态一致；OpenHands/CrewAI/LangGraph 是通用 agent，得额外搭检索-综合循环。

### 共同风险（必须标注，不可回避）

deepresearch 类框架对模型的**指令遵循 + 长程规划**能力要求高。本地 Qwen3-27B 相对前沿闭源模型偏弱，可能出现：检索轮次失控、引用漂移、综合深度不够。**这不是某个框架的缺陷，是「27B 本地模型驱动 deepresearch」的结构性上限**——无论选哪个框架都要带这个预期。对照组若用同一本地模型，则此风险在实验组/对照组间对称，不影响相对比较的有效性。

---

## Top-1 推荐：GPT-Researcher

**理由（对应 4 条硬约束逐条命中）**
1. 本地 LLM：✅ 官方 docs（`docs/docs/gpt-researcher/llms/llms.md`）明确支持任意 LLM provider，可设 OpenAI-compatible `base_url` 指向 `http://127.0.0.1:8787/v1`。
2. 可插拔 search：✅ 内置多引擎（DuckDuckGo/Bing/Tavily…），search engine 是可换组件，能挂自定义 search tool（如 `research_hook v2`）。
3. 近 3 月活跃：✅ 2026-11-09 仍有 push（① 实查）。
4. pip 可装 + 低部署复杂度：✅ `pip install gpt-researcher`，无需 docker/数据库。
5. 附加：deepresearch 场景原生对口（多步检索+综合），bench 题直接喂进去就能跑。

**备选**：若后续想要更强多 agent 编排能力，CrewAI（LiteLLM 接本地模型最顺）是第二选择；若只要「deepresearch 范式」不在乎活跃度，archived 的 open_deep_research 设计最纯粹，但停更风险高，不建议做主对照。

### 安装命令草案

```bash
# 1) 独立 venv（避免污染全局）
cd /Users/a1-6/Desktop/workspace/pfb
python3.13 -m venv .venv-gptr   # 或 uv venv .venv-gptr && source .venv-gptr/bin/activate
source .venv-gptr/bin/activate

# 2) 装框架
pip install gpt-researcher

# 3) 指向本地 Qwen3-27B（OpenAI-compatible @ localhost:8787）
export OPENAI_API_KEY="local-not-needed"          # 占位，本地服务不收 key
export OPENAI_API_BASE="http://127.0.0.1:8787/v1"  # 旧变量名；新版见下
# 新版 gpt-researcher 用 settings：
export LLM_MODEL="qwen3.8-27b"
# 或在代码里 ResearchConfig(llm_model="qwen3.8-27b", llm_base_url="http://127.0.0.1:8787/v1")

# 4) 冒烟测试：跑一道 bench 题，验证能出报告 + 引用
python - <<'PY'
import asyncio, gpt_researcher as gr
async def main():
    r = gr.GPTResearcher(query="NVIDIA H200 GPU TDP in watts")
    await r.conduct_research()
    print(await r.write_report())
asyncio.run(main())
PY
```

> 注意：gpt-researcher 的 LLM 配置入口随版本在 env var 与 `ResearchConfig` 之间变过，装完后以 `pip show gpt-researcher` 的版本对应文档为准；上面两条路径都给了，落地时二选一即可。

---

## 数据来源与置信

- 所有 star / pushed_at / archived 字段：① 类，2026-11-11 经 GitHub REST API（`api.github.com/repos/<repo>`）实查，可复现。
- OpenHands 原名 `All-Hands-AI/OpenHands` 返回 Moved Permanently，跟随重定向到 `OpenHands/OpenHands`。
- `open_deep_research` 真实 repo 为 `langchain-ai/open_deep_research`（非 huggingface 名下），web 检索确认 + API 实查 archived=True。
- 本地 LLM / search 支持：依据各框架官方文档页（GPT-Researcher llms.md、OpenHands local-llms、CrewAI llm-connections），属 ① 类文档查证。
- 无任何编造数字；若某字段当时查不到会标 `[待核验]`——本次 5 个候选全部查到，无空缺。