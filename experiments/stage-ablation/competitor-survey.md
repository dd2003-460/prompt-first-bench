# Deep Research 竞品与基准调研（对标最高水平）

> origin: ai · 2026-11-03 · 成璐指令「以后就对标最高水平」
> 用途：stage-ablation D1 判据 + 后续论文 related work 的事实基础。所有外部数字带来源和观察日期，未独立复测的标 conf。

## 1. 开源 deep research agent 格局（2026-11-03 观察）

| 项目 | 路线 | 强项 | 弱项/注意 | 来源 |
|------|------|------|-----------|------|
| GPT Researcher (assafelovic) | 固定流水线+LLM决策点；子查询 asyncio.gather 并行；deep mode = breadth×depth 递归树 | 工程成熟、30k star、MIT、pip 可装、MCP 集成 | 无阶段门禁/质量检查；citation grounding 弱（DREAM 评测结论）；skills/researcher.py 单文件 1149 行耦合 | github.com/assafelovic/gpt-researcher；ACL 2026 DREAM (aclanthology.org/2026.acl-long.448) |
| STORM / Co-STORM (stanford-oval) | 模拟多 persona 专家对话→大纲→正文（Wikipedia 写作流程） | 引用质量高、star 最多、长篇结构化文章 | 仓库更新慢（~10 个月无 push，2026-03 观察）；面向文章生成非问答 | digitalapplied.com 2026 开源 DRA 实测指南 |
| Open Deep Research (LangChain) | LangGraph supervisor+subagent 图，工具调用循环 | 灵活、可换模型/MCP、DeepResearch Bench 曾上榜 | DREAM 评测 Factuality 最低(44.64)，claim attribution 差 | langchain.com/blog/open-deep-research；DREAM |
| OpenResearcher (OPPO, arXiv:2603.20278) | 离线语料(15M doc)+三原语(search/open/find)合成 97K 轨迹→SFT 30B-A3B | 训练透明可复现；BrowseComp-Plus 54.8% (+34.0 over base) | 是训练 pipeline 非推理产品；需 vLLM+veRL | arxiv.org/abs/2603.2020278 (EMNLP 2026 main.42) |
| Tongyi DeepResearch (阿里) | 30.5B MoE (激活 3.3B) RL 长程搜索 | 开源权重、工业规模 | 需集群；DREAM 中 CI≈1.03（几乎不做 claim 落地） | DREAM；EMNLP 2026 |
| ASearcher-QwQ-32B / WebDancer / CutBill-30B | RL 系（GRPO/异步 RL） | 长程多轮搜索能力 | 学术实验为主 | EMNLP 2026 OpenResearcher 相关工作 |
| navinsreyas/research-agent (LangGraph, MIT) | 并行搜+credibility scorer+critique 循环 | **唯一见到显式来源权威度打分**：base 0.5 + authority(.edu/.gov/Reuters)+0.2 + freshness+0.2 + depth(>5k chars)+0.1；缺口检测(detective logic) | 小项目(9 commits)；启发式非学习式 | github.com/navinsreyas/research-agent |

**关键空白（我们的差异化空间）**：
- 没有开源系统做「分解+标注缺口+留空」的前置质检模块（decomp 的定位）。
- 没有成熟的「交叉验证置信度」实现——现有 credibility scorer 全是单源打分；两独立源相互印证才升级 conf 的结构未见成熟开源版。T22 闸2(矛盾检测)+r3 citation_check 拼起来是雏形。
- ACL 2026 DREAM 结论：所有开源 DRA 普遍栽在 citation grounding（claim→source 对应关系烂），报告可读性尚可但不可信。这正是三道闸要解的问题。

## 2. 基准格局（2026-11-03 观察）

| 基准 | 设计 | 头部表现 | GPT Researcher 位置 |
|------|------|----------|---------------------|
| DeepResearchGym (CMU, 2025-05) | 1000 复杂查询 | GPT Researcher 第一（超 Perplexity/OpenAI 闭源） | ✅ 唯一坐实的"第一" |
| DeepResearch Bench (100 PhD 级任务, 22 领域) | RACE 四维, GPT-5.5 判 | Gemini-2.5-Pro DR 48.92 榜首；OpenAI/Claude 二三 | ❌ 非头部（被当并行架构代表引用） |
| DRACO (Perplexity+Harvard, 2026-02) | 100 真实用户任务+专家 rubric | Perplexity 70.5% / Gemini 59% / o3 52.1% | ❌ 不在被测名单 |
| BrowseComp (Meta 2025) | 精确匹配、多步导航 | Kimi K2.5 Swarm 72.1%；人类专家 87.5% | — |
| xbench-DeepSearch (清华) | 深度搜索 | — | — |
| ResearchRubrics (101 queries+专家 rubric) | 过程+结果 | LongCat-DeepResearch 79.83 | — |
| Mercor DeepResearch Bench II | 28 configs 榜单 | Opus 5 web-research agent 56.10% 榜首 | — |
| 社区小基准 (Reddit, HotpotQA/TruthfulQA/MMLU) | 非正式 3 题平均 | GPT Researcher 66.3 vs OpenResearcher 64.0 | ⚠️ 民间测试不算数 |

**对 D1 判据的含义**：「S5 ≥ GPT Researcher」= 打过开源工程最强的开箱水平（定位：star 最高+最成熟+可本地部署），**不能外推**为「比所有 deep research 系统都强」。跨基准 SOTA 目前是闭源 Gemini/Perplexity/OpenAI，跑不了也不该跑。scoring.md 必须写这个限定。

## 3. GPT Researcher 代码解剖（2026-11-03 读源码，clone @ runs/d1-gpt-researcher）

- 总量 16,115 行 Python；最大文件 skills/researcher.py 1149 行（研究循环+上下文+错误处理糊一起）、prompts.py 904 行纯模板字符串、deep_research.py 655 行（JSON 解析 4 套 fallback 正则）。
- 结构：`conduct_research()` → LLM 选 agent+role → `research_conductor` 拆子查询 → `asyncio.gather` 并行检索+爬取 → 一趟式汇总。**无 while 回退边、无阶段门禁、无回执**——框架是死管道，智能全在 LLM 单次调用里。
- deep mode：breadth(默认4)×depth(默认2) 递归树展开，每层「生成查询→搜→爬→下一层」。最接近状态机但本质是树不是带转移条件的图。
- 为什么不做质量检查：①商业激励=快出报告，检查=token 翻倍用户无感；②质量外包给模型层（prompt 写 "be accurate" 赌自觉）；③开放域无 ground truth，他们只做便宜版（引用格式存在）跳过贵版（内容核验）。
- 借鉴清单：✅ 检索器抽象(retrievers/)、MCP 接入方式、visited_urls 去重传递（父 researcher 传给子避免重复爬）。❌ prompt 管理（904 行字符串堆砌）、JSON 解析（4 套正则说明对模型输出没信心）。对比：gates.py 177 行的信息密度 > 其整个 scraper 模块。

## 4. 对标承诺（成璐 2026-11-03）

以后所有实验对标最高水平：
- 端到端对手 = GPT Researcher（开源最强工程基线）+ 公开榜 SOTA 数字（Gemini/Perplexity，只引不跑）。
- 评分器标准 = DREAM/RACE 的 claim-grounding 维度 + 自家 M1-M6（信息型分歧机判优先，主观维度多裁判+conf）。
- 来源可信度 = 参考 navinsreyas 启发式做 baseline，目标是做出交叉验证置信度（双源印证升级）这一别人没有的维度。
- 论文 related work 按本文件 §1-§3 组织，每个外部数字保留 URL+观察日期。