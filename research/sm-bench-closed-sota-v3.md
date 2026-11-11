# T53 基线升级：闭源 SOTA + DeepResearch Bench（2026-11-11）

## 决策背景
成璐指令："要不打闭源sota，拿真实几个research的bench"。原 v2 基线（本地 Qwen3-27B + GPT-Researcher + 自造 5 题）说服力不足，升级为：
- **题目**：DeepResearch Bench（arXiv 2506.11763，848 stars，MIT/Apache 2.0）——100 道 PhD 级真实研究任务（50 中 / 50 英），22 个领域，专家撰写 rubric（每题含 dimension_weight + criterions）。
- **SOTA 臂**：Claude Code CLI（本机已装 2.1.210，OAuth 登录态可用，`claude -p` 冒烟通过）。自带 WebSearch/WebFetch 工具 = 真实 deep-research agent，不是裸 LLM。
- **我方臂**：GPT-Researcher + 本地 Qwen3-27B@8787 + arxiv retriever（已部署，冒烟通过）。
- **打分**：DRB 官方 RACE 协议（target vs reference 相对评分 + 加权维度分）+ FACT（引用抽取核验）。judge 走 OpenRouter/OpenAI 的 GPT-5.x（DRB 默认），无 key 时降级方案见下。

## 与旧口径的关系
- `sm-bench-sota-criteria.md` v2 的"本地模型+开源框架"定位**保留为内部消融臂**（B1/B2/B3），不再是主对比。
- 本文件是新的主对比口径（v3）。旧 5 题（H200/Transformer/HotpotQA/LLaMA2/DeepSeek-V3）保留作快速 smoke，不再作为 AC4 依据。

## 子项分解（decomp）
| # | 子项 | 状态 | 缺口 |
|---|------|------|------|
| 1 | bench 选型 | ✅ DRB（备选 GAIA 450 题，答案型非报告型，不匹配 report 对比） | — |
| 2 | 题目子集 | 待选 | 建议 n=10（5 zh + 5 en，覆盖 ≥4 领域）；全量 100 题成本另算 |
| 3 | SOTA 臂执行 | claude -p 通道已通 | 单题耗时/成本未测；需确认 claude 的 web 搜索在 -p 模式可用 |
| 4 | 我方臂执行 | gptr_bench_run.py 已有（自造 5 题版） | 需改接 query.jsonl 的 prompt 字段；输出格式对齐 raw_data/<model>.jsonl |
| 5 | judge | DRB 默认 GPT-5.5/GPT-5.4-mini via OpenRouter | **本机无 OPENROUTER_API_KEY / OPENAI_API_KEY** → 需成璐提供 key，或降级用 qwen2.5-7b@1234 当 judge（半异族，下界估计） |
| 6 | 输出对齐 | — | DRB raw_data 格式：{"id","prompt","article"} jsonl；claude 输出需截断清洗（clean_article.py） |

## 成本估算（粗）
- claude -p 单题 deep research：预计 3-10 分钟、$0.5-3（取决于 web 检索轮数）。n=10 ≈ $5-30。
- GPT-Researcher 本地跑：免费（本地 27B），单题 ~90s-5min。
- judge（OpenRouter GPT-5.x）：RACE 每对 1 次长调用，n=10 ≈ $2-5。
→ **需要花钱的只有 SOTA 臂和 judge，总量级 $10-35。**

## 风险
1. claude -p 的 web 工具在非交互模式是否启用 [待核验] —— 下一回合先跑 1 题带 web 依赖的验证。
2. DRB 官方 judge 要 GPT-5.x key；没有则 judge 降级，结论标"judge 受限"。
3. 中文题占一半，Qwen 系有主场优势，解读时要分开报 zh/en 两组分数。

## 落盘索引
- bench 仓库 clone: `/tmp/drbench/`（正式跑前移入 pfb/third-party/）
- 本文件: `research/sm-bench-closed-sota-v3.md`