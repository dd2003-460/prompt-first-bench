# T42 阶段 02：证据与未解决项
观察时间：2026-11-06 UTC。网页 LLM：`command -v ego-browser` 无输出、`ego-verify` skill 不存在；未登录/未配置，未能取得网页 AI 交叉询问回执。已向 Lead（本交付用户）报告；不是独立模型证据。web_search 可用；以下基于搜索工具页面/摘录，未独立直接抓取网页。每项置信度为证据适用性而非结果概率。

| ID | 标题、来源、日期 | 观察和范围 | conf |
|---|---|---|---|
| R1 | [OpenAI GPT-4o 模型卡](https://platform.openai.com/docs/models/gpt-4o)，2024-05-13 发布，现页标 Deprecated | 128,000 总窗口；标价输入 $2.50/M、输出 $10/M；实用部署须确认可用和实时价格 | 0.8 |
| R2 | [OpenAI embedding-3-small 模型卡](https://developers.openai.com/api/docs/models/text-embedding-3-small)，发布日期未给 | $0.02/M 输入 token；仅 embedding，不含解析、索引、运维 | 0.8 |
| R3 | [Leng et al., Long Context RAG Performance](https://arxiv.org/html/2411.03538v1), 2024-11 | 三数据集 823 查询；DocsQA 在 1/5/13/29 个 chunk 的召回 0.547/0.856/0.906/0.957；FinanceBench 为 0.097/0.287/0.493/0.603。特定检索器和语料，不是本企业正确率 | 0.9 原实验、0.2 迁移 |
| R4 | [Liu et al., Lost in the Middle](https://aclanthology.org/2024.tacl-1.9/), 2024 | 文档位置可影响特定模型多文档 QA/键值检索；不是所有模型必然如此 | 0.8 |
| R5 | [Lost in the Evidence?](https://arxiv.org/html/2605.27105), 2026-05 | 现代模型、不同协议下未复现清晰 U 形；不可对 Q4 强推位置曲线 | 0.7 |
| R6 | [LaRA benchmark](https://arxiv.org/html/2502.09977v2), 2025 | 128k 时部分开源模型 RAG 优于 LC；部分强闭源模型反之；任务和模型有关 | 0.8 |
| R7 | [Token Tax](https://arxiv.org/abs/2606.20898), 2026-06 | 972 答案、3 台设备、2 小模型；长上下文正确率 73.1%，语义 RAG 65.4%，token 成本 26 倍；非 Q4 生产成本 | 0.8 原实验、0.2 迁移 |
| R8 | [Ioannidis](https://en.wikisource.org/wiki/Page:Ioannidis_(2005)_Why_Most_Published_Research_Findings_Are_False.pdf/1), 2005 | PPV 由功效、α 和事前比率决定，采用简单二分模型 | 0.9 理论、0.2 迁移 |
| R9 | [Carlin, Power, prevalence, PPV](https://www.johancarlin.com/power-prevalence-and-the-positive-predictive-value.html), 2020 | 独立推导同类基率-功效关系；与 R8 概念对照 | 0.8 |
| R10 | [ASA p-value statement](https://www.amstat.org/asa/files/pdfs/P-ValueStatement.pdf), 2016 | p 值不是假设为真概率，也不是效应大小 | 0.9 |
| R11 | [FDA BSA 示范项目](https://www.fda.gov/about-fda/cder-center-clinical-trial-innovation-c3ti/bayesian-statistical-analysis-bsa-demonstration-project), 2026-04-08 | FDA 允许合条件项目的预先指定 Bayesian primary analysis；不等于普遍监管批准 | 0.9 |
| R12 | [Ji, FDA draft perspective](https://arxiv.org/html/2601.14701v1), 2026-01 | 提出 Bayesian 可以校准频率 type-I error；特定情况下与 FDA 同意后可用其他指标；是草案的二手解读，非最终法令 | 0.8 |
| R13 | [第三方 GPT-4o 定价](https://pecollective.com/blog/llm-pricing-comparison-2026/), 2026-09 | $2.50/M 输入、$10/M 输出，与 R1 一致，但可能引用厂商，非独立测量 | 0.6 |

关键空缺：Q4 企业 token 体量、查询分布、QPS、可用预算、实际正确/可引用率、p95、更新成本、权限和合同费均无；Q5 场景损失、基率、效应分布、制度与实测工作时间均无。均需实际数据。网页检索不能取代现场试验；没有两独立源支持的高影响量维持 GAP。
