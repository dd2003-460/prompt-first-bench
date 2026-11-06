# T29 — 组合空白全面验证 + NoPUA 可应用性调研

> **目标仓库**：prompt-first-bench（pfb）· branch main
> **派发日期**：2026-11-07
> **前置**：T28（lit-survey/t28-criteria-implementation.md）、tasks/2026-11-07-nine-points.md
> **验收标准**（机器可查）：
> 1. `lit-survey/t29-blank-and-nopua.md` 落盘，≥8 个独立来源（arXiv ≥4 + GitHub ≥2 + 其他 ≥2），每条带 URL + conf
> 2. §1 空白验证：对"正交完备检查 + 失败回退 + 占位留空 + 调研后填充"的组合，**穷尽式搜索**（见下方搜索矩阵），每个搜到的近邻工作给"重叠度评估表"（四个组件逐一对比：有/部分/无 + 一句话理由）；最终结论 = "完全空白 / 部分空白（哪部分被谁占了）/ 非空白（最接近的工作是哪篇、差在哪）"，三选一，不许含糊
> 3. §2 NoPUA 应用：把 NoPUA（R6, arXiv 2603.14373）的方法论拆成**可迁移组件清单**（哪些是情绪词、哪些是结构），给出 pfb pipeline 里每个阶段（decomp/research/check/review）该注入哪个组件的具体建议，标 [可直接用] / [需改造] / [不适用]
> 4. §3 交叉验证独立性：回答"多源交叉验证时如何警惕伪独立"——找 ≥3 篇讨论 source independence / common origin / citation cartography 的工作（如 Common Crawl 溯源、媒体转载链检测、LLM 训练数据去重文献），总结可操作的独立性判据（不是"找两个不同网站"这种废话，要能执行的规则）
> 5. 找不到就说找不到，不编 DOI；conf 逐条标

## 背景

成璐 2026-11-07 两点反馈：
1. "NoPUA 看看能不能应用" + "2/3 总感觉不是空白，继续新建调研条目让 arena 全面一点多找"——即 T28 的"组合是空白"结论（基于成璐自己的搜索 + T28 agent 复核）可能太乐观，需要更穷尽的搜索来证实或证伪。
2. 对 decomp-01 反作弊规则的纠正："以事实为准，搜了很多都能交叉独立验证那漏了也不是模型问题（而是人类数据的问题）。当然交叉验证不知道有没有独立性警惕，比如很多媒体重复转载像人体蜈蚣。"——第 2 点已落盘修正（decomp-01 §2 规则③改为以事实为准），第 3 点（伪独立警惕）归入本任务 §3。

## 搜索矩阵（§1 必须覆盖，不许只搜一个引擎）

**关键词组**（每组 × 每个平台）：
- A: "completeness check" + "task decomposition" + LLM
- B: "redundancy detection" / "non-redundancy" + subtask + language model
- C: "placeholder" / "unknown slot" / "fill-in-later" + planning + LLM
- D: "adaptive re-decomposition" / "backtrack" / "retry decomposition" + failure + LLM agent
- E: "coverage" + "decomposition quality" + scaffold
- F: "element matching" / "requirement traceability" + subtask（这个方向在软件工程需求追溯里有大量工作，别漏）
- G: Chinese: 分解 完备性 检查 大模型 / 递归分解 回退 占位

**平台**（至少 4 个）：arXiv API（full-text search）、Google Scholar（ego-browser）、Semantic Scholar API、GitHub code search、Papers with Code、DBLP（按作者追踪 ADaPT/AOP/STaD 三篇的后续引用——**引用追踪是最容易挖到近邻工作的路径**：谁引了 ADaPT 又在它基础上加了东西？）

**特别要求**：T28 只做了浅层搜索就下了"空白"结论，这次要深一层——每篇找到的近邻工作必须读 abstract + method 节（不只标题），判断它到底覆盖了组合里的哪几个组件。宁可多花 token 读论文，不可凭标题下判断。

## NoPUA 拆解要求（§2）

NoPUA 原文（R6）是整套方法论 v2.0.0，不是单句 prompt。拆的时候区分三层：
- **情绪层**：信任语气词（"我相信你"类）——预期效果弱（T26 Q1-Q3：单轮激励≈0）
- **结构层**：明确边界、可验证检查点、进度可见——预期效果强（+59% hidden issues 的主因猜是这层）
- **流程层**：它的方法论整体怎么组织多步任务——这是最值得抄的

对 pfb 的每个阶段给具体注入建议，不要泛泛说"可以用信任语气"。

## 伪独立警惕（§3）

成璐的原话担忧："有很多媒体重复转载当人体蜈蚣一样"。要找的文献方向：
- 新闻事件中的信息溯源（event-level deduplication、story tracking）
- 学术领域的 citation cartography / 共同来源检测
- LLM 训练数据去重（DataComp、DCLM 等怎么处理 near-duplicate）
- 可操作判据示例（供参考，agent 自己找更好的）：两来源的原始 URL 域名是否同根、发布时间先后 + 内容包含关系、是否都引用了同一个上游源头

## 边界

- 不跑实验，纯调研
- 产出 ≤4 页正文 + 来源表
- 回执必须含 repo URL + branch + commit_sha