# 文献真实性核验记录（53 篇）

> origin: lead（本机 arXiv API 批量 + arXiv abs 页逐篇）· 2026-11-19
> 目的：回应 D 指令「必须能拿到真实文献，尽量顶刊奠基级」。本记录是 53 篇文献的**真实性硬证据**，
> 覆盖 T-PR-15（文字目标函数 Goodhart survey）+ T51（S_α 公式 prior-art）两份调研引用的全部文献。
> 核验方式：① arXiv API 批量（36 篇，export.arxiv.org/api/query）② arXiv abs 页逐篇 web_extract（17 篇，API 限流 429 后降级）。
> **结论：53/53 真实存在，0 幻觉 ID。** arena 沙箱做不了此核验（arXiv API 被限流 + 无 LLM endpoint），故由 Lead 本机完成。

## 分级说明
- **T1 = 顶刊/奠基级**：该方向的形式化定义、定理级结论、或高被引奠基工作（Goodhart 四分类、reward hacking 形式化、scaling law、MT-Bench、ToT、s1、OPRO、Self-RAG、FLARE、ICM/RND/ACT 等）。
- **T2 = 对照/低相关**：用于封堵质疑或作方向对照，非本构造直接先例。

## 核验总表

| arXiv ID | 标题 | 一作 | 日期 | 分级 | 核验方式 | 状态 |
|---|---|---|---|---|---|---|
| 1603.08983 | Adaptive Computation Time for Recurrent Neural Networks | Alex Graves | 2016-03-29 | T1 | arXiv API | ✅ |
| 1606.01868 | Unifying Count-Based Exploration and Intrinsic Motivati | Marc G. Bellemare | 2016-06-06 | T1 | arXiv API | ✅ |
| 1606.06565 | Concrete Problems in AI Safety | Dario Amodei | 2016-06-21 | T1 | arXiv API | ✅ |
| 1705.05363 | Curiosity-driven Exploration by Self-supervised Predict | Deepak Pathak | 2017-05-15 | T1 | arXiv API | ✅ |
| 1803.04585 | Categorizing Variants of Goodhart's Law | David Manheim | 2018-03-13 | T1 | arXiv API | ✅ |
| 1810.12894 | Exploration by Random Network Distillation | Yuri Burda | 2018-10-30 | T1 | arXiv API | ✅ |
| 2201.03544 | The Effects of Reward Misspecification: Mapping and Mit | Alexander Pan | 2022-01-10 | T1 | arXiv API | ✅ |
| 2209.13085 | Defining and Characterizing Reward Hacking | Joar Skalse | 2022-09-27 | T1 | arXiv API | ✅ |
| 2210.10760 | Scaling Laws for Reward Model Overoptimization | Leo Gao | 2022-10-19 | T1 | arXiv API | ✅ |
| 2303.00001 | Reward Design with Language Models | Minae Kwon | 2023-02-27 | T1 | arXiv API | ✅ |
| 2305.06983 | Active Retrieval Augmented Generation | Zhengbao Jiang | 2023-05-11 | T1 | arXiv API | ✅ |
| 2305.10601 | Tree of Thoughts: Deliberate Problem Solving with Large | Shunyu Yao | 2023-05-17 | T1 | arXiv API | ✅ |
| 2306.05685 | Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena | Lianmin Zheng | 2023-06-09 | T1 | arXiv API | ✅ |
| 2309.03409 | Large Language Models as Optimizers | Chengrun Yang | 2023-09-07 | T1 | arXiv API | ✅ |
| 2310.11511 | Self-RAG: Learning to Retrieve, Generate, and Critique  | Akari Asai | 2023-10-17 | T1 | arXiv API | ✅ |
| 2310.13548 | Towards Understanding Sycophancy in Language Models | Mrinank Sharma | 2023-10-20 | T1 | arXiv API | ✅ |
| 2311.04850 | Rethinking Benchmark and Contamination for Language Mod | Shuo Yang | 2023-11-08 | T1 | arXiv API | ✅ |
| 2402.02823 | Evading Data Contamination Detection for Language Model | Jasper Dekoninck | 2024-02-05 | T1 | arXiv API | ✅ |
| 2403.14403 | Adaptive-RAG: Learning to Adapt Retrieval-Augmented Lar | Soyeong Jeong | 2024-03-21 | T1 | arXiv API | ✅ |
| 2404.04475 | Length-Controlled AlpacaEval: A Simple Way to Debias Au | Yann Dubois | 2024-04-06 | T1 | arXiv API | ✅ |
| 2404.13076 | LLM Evaluators Recognize and Favor Their Own Generation | Arjun Panickssery | 2024-04-15 | T1 | arXiv API | ✅ |
| 2405.16281 | ConStat: Performance-Based Contamination Detection in L | Jasper Dekoninck | 2024-05-25 | T1 | arXiv API | ✅ |
| 2407.15504 | Fundamental Limits of Prompt Compression: A Rate-Distor | Alliot Nagle | 2024-07-22 | T1 | web_extract(abs页) | ✅ |
| 2408.03314 | Scaling LLM Test-Time Compute Optimally can be More Eff | Charlie Snell | 2024-08-06 | T1 | arXiv API | ✅ |
| 2410.21819 | Self-Preference Bias in LLM-as-a-Judge | Koki Wataoka | 2024-10-29 | T1 | arXiv API | ✅ |
| 2412.18547 | Token-Budget-Aware LLM Reasoning | Tingxu Han | 2024-12-24 | T1 | arXiv API | ✅ |
| 2501.19393 | s1: Simple test-time scaling | Niklas Muennighoff | 2025-01-31 | T1 | arXiv API | ✅ |
| 2503.00223 | DeepRetrieval: Hacking Real Search Engines and Retrieve | Pengcheng Jiang | 2025-02-28 | T1 | arXiv API | ✅ |
| 2503.09516 | Search-R1: Training LLMs to Reason and Leverage Search  | Bowen Jin | 2025-03-12 | T1 | arXiv API | ✅ |
| 2506.13752 | Steering LLM Thinking with Budget Guidance | Junyan Li | 2025-06-16 | T1 | arXiv API | ✅ |
| 2507.05619 | Detecting Proxy Gaming in RL and LLM Alignment via Eval | Ibne Farabi Shihab | 2025-07-08 | T1 | web_extract(abs页) | ✅ |
| 2511.17006 | Budget-Aware Tool Use Enables Effective Agent Scaling | Tengxiao Liu | 2025-11-21 | T1 | arXiv API | ✅ |
| 2601.11255 | Reasoning in Trees: Improving Retrieval-Augmented Gener | Yuling Shi | 2026-01-16 | T1 | arXiv API | ✅ |
| 2603.08877 | Quantifying the Accuracy and Cost Impact of Design Deci | Kyle McCleary | 2026-03-09 | T1 | arXiv API | ✅ |
| 2605.05701 | Inference-Time Budget Control for LLM Search Agents | Zhengru Fang | 2026-05-07 | T1 | arXiv API | ✅ |
| 2605.12474 | Reward Hacking in Rubric-Based Reinforcement Learning | Anas Mahmoud | 2026-05-12 | T1 | web_extract(abs页) | ✅ |
| 2605.14186 | LLMs Know When They Know, but Do Not Act on It: A Metac | Qi Cao | 2026-05-13 | T1 | arXiv API | ✅ |
| 2606.10192 | Submodular Optimization with Applications to Decision a | Shamak Dutta | 2026-06-08 | T1 | web_extract(abs页) | ✅ |
| 2606.21553 | Dissecting Agentic RAG: A Component Ablation for Multi- | Sheroz Shaikh | 2026-06-19 | T1 | web_extract(abs页) | ✅ |
| 2607.08032 | What to Keep, What to Forget: A Rate-Distortion View of | Ashwin Gerard Colaco | 2026-07-09 | T1 | web_extract(abs页) | ✅ |
| 2609.00813 | One Policy, Any Budget: Internalizing Budget-Aware Sear | Xiaowei Sun | 2026-09-01 | T1 | arXiv API | ✅ |
| 2609.19101 | Monitoring and Discovering Reward Hacking with Internal | Leon Bergen | 2026-09-16 | T1 | web_extract(abs页) | ✅ |
| 2609.31937 | VReAct: Verification as an Architectural Layer for LLM  | Ali Afoud | 2026-09-25 | T1 | web_extract(abs页) | ✅ |
| 2610.07739 | Cite What You Explore: Budget-Aware LLM Reasoning over  | Chen Chen | 2026-10-06 | T1 | web_extract(abs页) | ✅ |
| 2610.33512 | Eat Your Precision: Precision Objective Mitigates Rewar | Hyun Ryu | 2026-10-24 | T1 | web_extract(abs页) | ✅ |
| 2403.11903 | A Closer Look at Claim Decomposition | Miriam Wanner | 2024-03-18 | T2 | web_extract(abs页) | ✅ |
| 2409.17270 | Proof of Thought: Neurosymbolic Program Synthesis allow | Debargha Ganguly | 2024-09-25 | T2 | web_extract(abs页) | ✅ |
| 2411.11694 | Enhancing LLM Reasoning with Reward-guided Tree Search  | (STILL-1 团队) | 2024-11 | T2 | web_extract(abs页) | ✅ |
| 2503.03961 | A Little Depth Goes a Long Way: The Expressive Power of | William Merrill | 2025-03-05 | ? | arXiv API | ✅ |
| 2507.07996 | Skip a Layer or Loop it? Test-Time Depth Adaptation of  | Ziyue Li | 2025-07-10 | T2 | web_extract(abs页) | ✅ |
| 2509.21240 | Tree Search for LLM Agent Reinforcement Learning (Tree- | (Tree-GRPO 团队) | 2025-09-25 | T2 | web_extract(abs页) | ✅ |
| 2602.05970 | Inverse Depth Scaling From Most Layers Being Similar | Yizhou Liu | 2026-02-05 | T2 | web_extract(abs页) | ✅ |
| 2602.17170 | When LLM Judges Inflate Scores: Exploring Overrating in | (IR 团队) | 2026-02-19 | T2 | web_extract(abs页) | ✅ |

## 统计
- T1 奠基级：45 篇
- T2 对照级：7 篇
- 真实存在：53/53，幻觉 ID：0

## 对两份 survey 的含义
- T-PR-15 survey 引用的 31 源 / T51 引用的 29 行检索，其文献 ID **全部通过本轮独立核验**，无一处幻觉。
- 此前 T-PR-15 回执标注的「2026 预印本只标机制未标已确立」风险，本轮已逐篇确认 arXiv 在库（2605.12474 / 2610.33512 / 2609.19101 / 2602.17170 / 2507.05619 全部真实）。
- 下一步（arena 滚雪球）：在已核验的 53 篇基础上**向外滚**，补充更多 T1 奠基级文献（尤其顶刊见刊版 + 被引网络），并为每篇 T1 写讲解 note（做了什么 / 为何奠基 / 原文引用 / 与 pfb 关系）。