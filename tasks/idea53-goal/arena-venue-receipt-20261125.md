# Arena 投稿策略审查回执（2026-11-25 第二轮）

## 派发事实

| 项 | 值 |
|---|---|
| taskSpace | 16060（pfb-idea53-venue-strategy） |
| 会话 URL | https://arena.ai/agent/01a212ae-2d6f-7f77-8427-b31d0d8b7ebc |
| 任务卡 | `arena-venue-brief-20261125.md`（收敛定位：前置工作/toy/不 solve/不 claim novelty） |
| SOP | `tasks/00-ops/sop-arena-review-light.md` |
| 开工确认 | orchestrating = true，新 taskSpace 无仓库绑定（纯策略，不误改仓库） |
| 耗时 | 9m51s，报告全文 `arena-venue-report-raw-20261125.md`（744 行） |

## 核心结论

**Q1 workshop 可发性**：够。最匹配三个（均在 ICLR 2027，2027-04-29/30 SF）：
- SciEval @ ICLR'27｜截稿 2027-02-01｜非存档｜接受 analysis/measurement/preregistration｜主场题材 conf 0.7
- Science and Society of Modern AI @ ICLR'27｜截稿 2027-01-30 AoE｜非存档 full≤8p / tiny≤3p｜主题含 "Measurement: the evaluations that decisions rest on"｜tiny 轨收"未发表想法 + 其评估"，与"前置评分基础"定位严丝合缝 conf 0.8
- Verifiable Agent Safety @ ICLR'27｜摘要 2027-01-25 / 全文 2027-02-01（日期 proposed）｜非存档 regular 5–9p / short 2–4p｜适配 spec-gaming + evaluation-with-guarantees，与 SCALR 切割叙事配套 conf 0.7
- 竞争力瓶颈不是"无 code 无实验"，是"结构过于 toy"——已有 40k workload toy 验证，措辞改"closed-form + simulation-free validation"。

**Q2 中稿概率路径**（workshop 与主会分列）：
- 路径1（推荐）：ICLR'27 workshop → NeurIPS 2027 E&D（原 D&B，2027-05 中旬估，未公布）。workshop 录用 50–65%（conf 0.55）；E&D 主会 15–25%（conf 0.45）。E&D 明文欢迎 evaluation practice 的 analysis/critique/redesign，"新评价指标定义"归入 E&D。
- 路径2（并行）：ICML 2027 主轨新设 "Datasets, Evaluations and Benchmarks"，摘要 2027-01-14 / 全文 2027-01-22（官方 blog 2026-11-24）。主会 8–15%（conf 0.5）。风险：两阶段评审对 toy-only 最不友好 + reciprocal reviewing 义务 + 仅 ~7 周备稿。
- 路径3：NeurIPS 2027 E&D 直投，12–20%（conf 0.4），无 workshop 反馈先行。
- MLSys 2027 主会已于 2026-10-30 截止（错过）；MLSys 2028（2027-10）作备份。

**Q3 费用**：投稿与发表全程 0 元。APC/版面费全 0（NeurIPS/ICML 无版面费，ICLR 出版 $0，OpenReview 免费）；arXiv 0 元（官方明示，conf 0.95）。只有注册/差旅花钱：NeurIPS 2026 巴黎 workshops-only 学生 €130 早 / €180 标准、学术 €170/€220、工业 €250/€300（conf 0.85）；ICLR 2027 费用未公布（2026-12-23 开放注册），参考 2026 学生 ~$425 起；ICML/NeurIPS 2027 未公布。Waiver 有：NeurIPS Financial Assistance（免费注册+酒店，学生作者优先）、ICLR Financial Assistance、EurIPS 学生注册豁免（conf 0.8）。

**Q4 加固**：
- 必做①（~1天）："分解树 + 增量信息 + 负控制"三合一结构图，画 H(D|S) 计算路径 + flat-rate→精确 0 图解。conf 0.75。
- 必做②（半天）：comparison table vs ID3/roofline/PID/SCALR，六列（输入/输出/闭式性/负控制/预注册/是否涉 spec 修订），前置封死"这不就是 ID3"。conf 0.7。
- 可选③：公开数据 spot-check 或 artifact 附录（脚本 + workload 生成器），对 E&D 加分。conf 0.6。

## 缺口（agent 自报，未验证，禁止当事实）

① SciEval 页数/存档性与 ICLR'27 workshop 统一政策未定（tentative）；② NeurIPS 2027 E&D CFP 与 ICML/NeurIPS 2027 注册费未公布；③ ICML 2026/2027 与 NeurIPS 2026 E&D 接收率无官方数字；④ E&D 对非数据类论文 artifact 要求待 2027 CFP。

## Lead 抽验

- 来源主机可达：neurips.cc=200、icml.cc=200、info.arxiv.org=301（重定向，正常）。
- 关键日期来自 agent 联网检索；2027 未公布项报告已明确标"未公布"，无编造数字迹象。
- 与上一轮 novelty 报告一致：都以"toy + 前置定位"为可守边界，未翻案。
