# T37-B · Related Work 调研 — 阶段 02 资料搜集（research.md）

> 创建：2026-11-05 · 阶段：02（信息调研）· 上游：`loop-artifacts/stages/01/T37-01-goal-decomposition.md`（G1–G6 / R1–R8 / 冻结域①–⑥）
> 执行通道：arena agent mode @ `dd2003-460/prompt-first-bench` / `arena/t37-related-work`
> 全部观察时间戳为 UTC，来自本会话 `fetch_page` / `web_search` 工具的真实回执（非记忆）。
> 本阶段**不写最终 §2 定稿**、不写推荐；只给证据、暂定收录集与未解决空缺。

---

## 0. 通道实测回执（含失败，失败也入档）

| # | 通道 | 调用 | 结果 | 观察时间 | 处置 |
|---|------|------|------|----------|------|
| C1 | `ego-browser` + `ego-verify`（阶段 02 规则要求的网页 LLM 交叉询问） | — | **不可用**：arena agent mode 未挂载 ego-browser/ralph runtime（本仓库 `ralph` 命令在本沙箱不存在） | 2026-11-05T18:52Z | 记录后改用公开一手源；按规则"通道快速失败即记录、不等待不重试" |
| C2 | 沙箱 bash `curl` → export.arxiv.org / dblp.org / aclanthology.org / api.semanticscholar.org | 4 次 | 全部 **HTTP 000**（出口仅放通 github/npm/pypi 域） | 18:52Z | 改走平台 `fetch_page`（下方 C4–C7） |
| C3 | Semantic Scholar Graph API | 1 次 | **429 Too Many Requests** | 18:53Z | 不作主通道（重试上限内不再试） |
| C4 | arXiv API `export.arxiv.org/api/query`（`id_list` 批量） | 5 次 | **200，Atom 全文可读**（title/authors/submitted/comment） | 18:53:13Z–18:55:09Z | **主源 A** |
| C5 | DBLP publication API (`dblp.org/search/publ/api?format=json`) | 19 次 | **200，JSON 可读**（venue/year/type/key/doi/ee） | 18:53Z–18:56Z | **主源 B** |
| C6 | ACL Anthology（`aclanthology.org/2026.acl-long.448/`） | 1 次 | **200 可读**（作者/venue/DOI/bibkey 全取到） | 18:55Z | 第三源，用于 DREAM 复核 + G5 结论 |
| C7 | `web_search`（平台检索） | 1 次（τ-bench 裁决） | 命中 3 条独立页面（sophon.at / GitHub README / modelspec） | 18:56Z | 第三源，用于勘误裁决 |
| C8 | arXiv API 关键词检索 `all:"ablation study" AND all:"methodology"`（域⑥找专文） | 1 次 | 200，但 top-8 全为"应用论文里做了消融"（桥梁运维、医学分割、算法设计等），**无方法学专文** | 18:54:56Z | 触发 G4 降级方案（见 §5） |

**独立性声明**：源 A（arXiv）与源 B（DBLP）为**不同机构、不同数据库**，互不转引；`arxiv.org/abs/*` 页面与 arXiv API 同后端，**不互为独立源**，故本文件未把两者当双源。

---

## 1. 新增文献（域①–⑥，共 21 篇，全部过双源；19 篇于 18:54Z 首次落盘，N20/N21 于 02.5 对抗核验后补入 18:56Z）

格式：`[ID]` 标题 — 作者（前 3 + et al.）— venue/year — arXiv 或 URL — **与本文的相关性（1 句）** — 所属域 — 双源回执号。

### 域① LLM agent benchmarks（4 篇）

| ID | 条目 |
|----|------|
| N1 | **WebArena: A Realistic Web Environment for Building Autonomous Agents** — Zhou, S., Xu, F.F., Zhu, H., et al. — **ICLR 2024** — arXiv:2307.13854 — 端到端 web 任务成功率是唯一读数（GPT-4 agent 14.41% vs 人类 78.24%），说明既有 benchmark 只测"是否做成"、不拆阶段贡献，正是本文 stage ablation 补的空白。— 域① — A(18:54:14Z)+B(`conf/iclr/ZhouX0ZLSCOBF0N24`) |
| N2 | **SWE-bench: Can Language Models Resolve Real-World GitHub Issues?** — Jimenez, C.E., Yang, J., Wettig, A., et al. — **ICLR 2024** — arXiv:2310.06770 — 以 2,294 个真实 issue 做通过率评测，同样把"能力"压成单一标量；本文的 M1–M7 多维 rubric 与之构成互补而非同类。— 域① — A+B(`conf/iclr/JimenezYWYPPN24`) |
| N3 | **MLE-bench: Evaluating Machine Learning Agents on Machine Learning Engineering** — Chan, J.S., Chowdhury, N., Jaffe, O., et al. — **ICLR 2025** — arXiv:2410.07095 — 75 个 Kaggle 竞赛 + 人类基线，代表"用专家级任务标定 agent 上限"的路线；本文问的是相反方向（固定模型、变动 prompt 结构）。— 域① — A+B(`conf/iclr/ChanCJASLMPMW25`，注：DBLP 记 `ChanCJASMSLMPMW25`) |
| N4 | **BrowseComp: A Simple Yet Challenging Benchmark for Browsing Agents** — Wei, J., Sun, Z., Papay, S., et al. — **arXiv preprint 2025**（DBLP 仅有 CoRR 记录，无同行评审版） — arXiv:2504.12516 — 1,266 道"难找信息"短答案题，把难点定位在持久检索而非推理；本文 no-tool 设定下该维度整体不可测（M6 结构为 0），用于界定我们结论的适用边界。— 域① — A+B(`journals/corr/abs-2504-12516`) |

### 域② Prompt engineering / structured prompting（4 篇）

| ID | 条目 |
|----|------|
| N5 | **Self-Consistency Improves Chain of Thought Reasoning in Language Models** — Wang, X., Wei, J., Schuurmans, D., et al. — **ICLR 2023** — arXiv:2203.11171 — 多路径采样 + 边际化替代贪心解码，是"结构有用"的第一条强证据；与我们 S6/S7 的"风格 vs 结构"分离相对：self-consistency 变的是采样，我们变的是 prompt。— 域② — A+B(`conf/iclr/0002WSLCNCZ23`) |
| N6 | **Least-to-Most Prompting Enables Complex Reasoning in Large Language Models** — Zhou, D., Schärli, N., Hou, L., et al. — **ICLR 2023** — arXiv:2205.10625 — "先拆子问题再顺序求解"，是 S1（goal decomposition）最直接的文献祖先；SCAN length-split 99% vs CoT 16% 给出分解的效应量级。— 域② — A+B(`conf/iclr/ZhouSHWS0SCBLC23`) |
| N7 | **Plan-and-Solve Prompting: Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models** — Wang, L., Xu, W., Lan, Y., et al. — **ACL 2023**（pp. 2609–2634） — arXiv:2305.04091 — 明确指出 zero-shot CoT 的三类失败（算错、漏步、语义误解）并以"先列计划再执行"修复；与我们 M1 随结构变化而波动、M4 随显式清单上升的模式同源。— 域② — A+B(`conf/acl/WangXLHLLL23`) |
| N8 | **The Prompt Report: A Systematic Survey of Prompting Techniques** — Schulhoff, S., Ilie, M., Balepur, N., et al. — **arXiv preprint 2024**（DBLP 仅 CoRR；标题在 DBLP 记作 "…Survey of Prompting Techniques"，arXiv 记作 "…Survey of Prompt Engineering Techniques"，见 §3 矛盾 M6） — arXiv:2406.06608 — 58 种提示技术的分类法，为"结构类 vs 风格类"的划分提供外部术语坐标，避免我们把 S6/S7 的差异说成原创二分。— 域② — A+B(`journals/corr/abs-2406-06608`) |

### 域③ Calibration / confidence elicitation（5 篇：三路线 + 2026 两条新证据）

| ID | 条目 |
|----|------|
| N9 | **Teaching Models to Express Their Uncertainty in Words** — Lin, S., Hilton, J., Evans, O. — **TMLR 2022** — arXiv:2205.14334 — **verbalized 路线**奠基：不依赖 logits、模型直接用自然语言给置信度并可通过微调校准；本文 M2 的口径（解析输出里的置信度陈述）承自此线。— 域③ — A+B(`journals/tmlr/LinHE22`) |
| N10 | **Just Ask for Calibration: Strategies for Eliciting Calibrated Confidence Scores from LMs Fine-Tuned with Human Feedback** — Tian, K., Mitchell, E., Zhou, A., et al. — **EMNLP 2023**（pp. 5433–5442） — arXiv:2305.14975 — 在 RLHF 模型上 verbalized confidence 常优于条件概率（ECE 相对降约 50%），支持"提示语即可校准"的解释：本文 S6 的 M2=0.618 vs S0=0.037 与之同向。— 域③ — A+B(`conf/emnlp/TianMZSRYFM23`) |
| N11 | **Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation** — Kuhn, L., Gal, Y., Farquhar, S. — **ICLR 2023**（Spotlight） — arXiv:2302.09664 — **multi-sample 路线**：语义熵把"同义不同表述"归一后再测不确定性，比 token 级基线更能预测正确性；为我们只做 3 rep（temp=0/0.1）的统计弱点提供方法学出口。— 域③ — A(comment 明写 ICLR 2023 Spotlight)+B(`conf/iclr/KuhnGF23`) |
| N20 | **An Analysis of Training-Free Self-Reported Confidence in Language Models** — Meyer, L., Rossi, S., Chen, W., Laurent, T., Li, Y. — **arXiv preprint 2026**（arXiv comment 仅写 "workshop"，无具名会议；DBLP 仅 CoRR） — arXiv:2609.20541 — 在同一批 TriviaQA 上直接对比"verbalized / P(True) / 3-sample agreement"三信号：verbalized 最强（AUROC 0.956/0.937）、三样本一致性明显更弱（0.765/0.790），且 3 次采样会**放大共有的误解**——这直接解释本文 M2 在 S6（自然语言不确定性措辞）上跳到 0.618 而 S0 仅 0.037，并警示我们 3-rep 设计不能当"多源印证"。— 域③ — A(18:56:14Z)+B(`journals/corr/abs-2609-20541`) |
| N21 | **When Words Fall Short: Iterative Synergy Between Verbalized Reasoning and Hidden Features for LLM Confidence Estimation** — Xu, Y., Wang, A., Ren, J., et al. — **arXiv preprint 2026** — arXiv:2609.34454 — 反方证据：内置 confidence estimator 可显著优于 verbalized confidence（即"语言里的置信度"并非上界）；提醒我们 M2 的提升是**提示层效应**，不等于内部置信度被正确读出。— 域③ — A(18:56:14Z)+B(`journals/corr/abs-2609-34454`) |

### 域④ RAG evaluation & retrieval quality（3 篇，原为零覆盖）

| ID | 条目 |
|----|------|
| N12 | **RAGAs: Automated Evaluation of Retrieval Augmented Generation** — Es, S., James, J., Espinosa-Anke, L., Schockaert, S. — **EACL 2024 Demo**（pp. 150–158） — arXiv:2309.15217 — 无参考答案（reference-free）的 RAG 指标族：faithfulness / answer relevance / context relevance；我们的 M5（来源质量）与 M6（引用可验证）本质是它的手工化近似。— 域④ — A+B(`conf/eacl/ESJAS24`) |
| N13 | **ARES: An Automated Evaluation Framework for Retrieval-Augmented Generation Systems** — Saad-Falcon, J., Khattab, O., Potts, C., Zaharia, M. — **NAACL 2024**（pp. 338–354） — arXiv:2311.09476 — 用合成训练数据微调轻量 judge + PPI 校正，是"用 LLM 当评测器但要纠偏"的范式；本文 §3.5 的 judge 置信度上限 0.7 与 T26 异族复核是同一问题的简陋版，需在 §2 承认。— 域④ — A+B(`conf/naacl/Saad-FalconKPZ24`) |
| N14 | **RAGChecker: A Fine-grained Framework for Diagnosing Retrieval-Augmented Generation** — Ru, D., Qiu, L., Hu, X., et al. — **NeurIPS 2024**（Datasets & Benchmarks Track） — arXiv:2408.08067 — 把检索与生成分开诊断的细粒度指标（claim-level precision/recall）；与我们 S7V 的 claim-level 验证同构，可作为 §5.1 的对照坐标系。— 域④ — A+B(`conf/nips/RuQHZSCJWSLZWJ024`) |

### 域⑤ Deep research agents（有 paper 的，3 篇）

| ID | 条目 |
|----|------|
| N15 | **Assisting in Writing Wikipedia-like Articles From Scratch with Large Language Models**（STORM） — Shao, Y., Jiang, Y., Kanell, T.A., et al. — **NAACL 2024**（pp. 6252–6278） — arXiv:2402.14207 — 写作前阶段（多视角提问 → 大纲）的显式建模，其"organized +25% abs / coverage +10%"是唯一给出预写作阶段增益的同行评审数字；与我们 S1/S5 的"结构增益"可对照。— 域⑤ — A(comment: NAACL 2024 Main)+B(`conf/naacl/ShaoJK0KL24`) |
| N16 | **DeepResearch Bench: A Comprehensive Benchmark for Deep Research Agents** — Du, M., Xu, B., Zhu, C., et al. — **ICLR 2026** — arXiv:2506.11763 — 100 个博士级任务 + 22 领域，两套与人类判断对齐的评测法（reference-based 自适应标准 + 有效引用计数/引用准确率）；本文的 M5/M6 维度与其"citation accuracy"直接对话。— 域⑤ — A+B(`conf/iclr/DuXZZWM26`，作者数矛盾见 §3 M4) |
| N17 | **DeepResearcher: Scaling Deep Research via Reinforcement Learning in Real-world Environments** — Zheng, Y., Fu, D., Hu, X., et al. — **EMNLP 2025**（main, pp. 414–431） — arXiv:2504.03160 — 在真实 web 上端到端 RL 训练研究 agent（+28.9 于 prompt-engineering 基线），其"涌现的跨源交叉验证/自反思"正是本文用 prompt 想诱发却诱不出的能力（M7 失败）。— 域⑤ — A+B(`conf/emnlp/ZhengFHCYLL25`) |

### 域⑥ Ablation methodology in ML/NLP（2 篇，原为零覆盖）

| ID | 条目 |
|----|------|
| N18 | **Ablation Studies in Artificial Neural Networks** — Meyes, R., Lu, M., Waubert de Puiseau, C., Meisen, T. — **arXiv preprint 2019**（DBLP 仅 CoRR） — arXiv:1901.08644 — 唯一直接以"消融研究怎么做"为主题的方法学综述（源自神经科学 lesion 传统 → ANN 组件归因）；为我们的 S0–S5 累积臂设计提供方法学依据，同时暴露其局限（本文只做单向累积移除，未做 full 2^5 组合）。— 域⑥ — A+B(`journals/corr/abs-1901-08644`) |
| N19 | **Adding Error Bars to Evals: A Statistical Approach to Language Model Evaluations** — Miller, E. — **arXiv preprint 2024** — arXiv:2411.00640 — 把评测当实验：超总体抽样、差值方差、实验规划公式；直接作用于本文最弱处（3 rep、逐格 n=3、无 CI），§5.3 必须引用它以诚实标注统计效力。— 域⑥ — A+B(`journals/corr/abs-2411-00640`) |

**计数核对**：新增 21 篇（①4 ②4 ③5 ④3 ⑤3 ⑥2），每域 ≥1 ✅；双源 21/21 ✅；净新增 ≥10 ✅（21 ≥ 10）；与既有 10 篇去重后总数 31 篇 ≥ 20 ✅。
**时效**：2024–2026 者 15 篇（N1–N4, N8, N10, N12–N17, N19–N21），2019/2022/2023 者 6 篇（N5–N7, N9, N11, N18）——后者为"该路线第一篇/唯一方法学篇"，属稳定事实可用较早一手源（阶段 02 规则第 4 条）。

---

## 2. 既有 10 篇复核（R1 / G2）— 发现 5 处实质错误

| # | paper-draft §References 原记载 | 一手源复核结果 | 判定 |
|---|-------------------------------|----------------|------|
| E1 | Xiong, M. et al. (2023) … **ICLR 2024**, `arXiv:2305.14975` | arXiv API(2305.14975) = **Tian, K. et al. "Just Ask for Calibration"**（EMNLP 2023）；Xiong 真 ID = **2306.13063**（arXiv + DBLP `conf/iclr/XiongHLLFHH24`，ICLR 2024） | **ID 错**（指向他人论文）→ 必须改 |
| E2 | Kadavath, S. et al. (2022) … `arXiv:2107.03258` | arXiv API(2107.03258) = **"Lorentz-breaking Theory and Tunneling Radiation Correction to Vaidya-Banner de Sitter Black Hole"**（Bei Sha, Zhi-E Liu, 2021，物理）；真 ID = **2207.05221**（arXiv + DBLP `journals/corr/abs-2207-05221`） | **ID 错**（指向无关学科论文）→ 必须改 |
| E3 | τ-bench … "A Benchmark for Tool-Using AI Agents" · `arXiv:2410.02509` | arXiv API(2410.02509) = **"Bifurcations in the family of billiards associated with the curvature flow"**（数学）；真条目 = **2406.12045**，标题 **"τ-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains"**（arXiv + DBLP `journals/corr/abs-2406-12045` + web_search 三页面） | **ID 错 + 标题错** → 必须改 |
| E4 | LoCoMo, A. et al. (2024) … *NAACL 2024* | DBLP：**ACL 2024**（long, pp. 13851–13870，`conf/acl/MaharanaLTBBF24`）；arXiv:2402.17753 无 venue comment | **venue 错**（ACL 而非 NAACL）→ 必须改 |
| E5 | GAIA … "Huang, W., et al. (2023)" | arXiv API(2311.12983) 作者 = **Mialon, G., Fourrier, C., Swift, C., Wolf, T., LeCun, Y., Scialom, T.** | **作者错**（无 Huang W.）→ 必须改 |
| E6 | DREAM … "Deep Research Agent Evaluation and Measurement, ACL 2026 (In press)" | ACL Anthology `2026.acl-long.448`：真标题 **"DREAM: Deep Research Evaluation with Agentic Metrics"**，Avraham, E.B. et al.，ACL 2026, pp. 9879–9904, DOI 10.18653/v1/2026.acl-long.448 | **标题错**（副标题不同）→ 建议改 |
| E7 | ScientistTwo `arXiv:2609.19644` + §2.4 称其"proposes a *judge* architecture for evaluating scientific claims" | arXiv API(2609.19644)：Nam, J. et al., 2026-09-17，真实内容 = **全自主多智能体科学发现框架**（baseline→假设→实验→自动消融→模拟同行评审），**不是 judge 架构** | **内容误述**（定位句错）→ §2.4 需重写（见 §6 交接） |
| E8 | CoT `arXiv:2201.11903` / ToT `arXiv:2305.10601` / AgentBench `arXiv:2308.03688` + ICLR 2024 / Self-Consistency 等 | 全部与一手源一致（CoT 2201.11903 ✅；ToT "NeurIPS 2023 camera ready" ✅；AgentBench "Published in ICLR 2024" ✅） | **无误** |

**结论**：既有 10 篇中 7 篇需修订（E1–E5 为硬错误，E6/E7 为表述错误）；这不是 T37 的附带发现，而是"扩到 20 篇"之前必须先修的地基（阶段 01 I5 的假设已被证实）。

---

## 3. 矛盾登记表（D4，逐条含双源与处置）

| # | 争议点 | 源 A | 源 B | 可否解释 | 处置 |
|---|--------|------|------|----------|------|
| M1 | Xiong 2023 的 arXiv ID | arXiv API：2305.14975 → Tian et al. | DBLP：`conf/iclr/XiongHLLFHH24` + CoRR abs/2306.13063 | 可解释：draft 把 Tian 的 ID 误挂到 Xiong | 采用 2306.13063；2305.14975 归 N10（Tian） |
| M2 | Kadavath 2022 的 arXiv ID | arXiv API：2107.03258 → 黑洞物理论文 | DBLP：CoRR abs/2207.05221 = "Language Models (Mostly) Know What They Know" | 可解释：ID 手误（22→21，0705 顺序错） | 采用 2207.05221 |
| M3 | τ-bench 的 ID 与标题 | arXiv API：2410.02509 → billiards 数学论文 | DBLP `abs-2406-12045`；web_search 3 个独立页面（sophon.at、GitHub sierra-research/README、modelspec）均为 2406.12045 | 可解释：ID + 标题双错 | 采用 2406.12045 + 真标题 |
| M4 | DeepResearch Bench 作者数 | arXiv v1：5 作者（Du, Xu, Zhu, Wang, Mao） | DBLP ICLR 2026：6 作者（增 Licheng Zhang，排名第 4） | 可解释：arXiv v1 早于投稿版/相机版 | 引用用 5 作者 + et al.（以 arXiv 一手为准），并在 §2 采用 et al. 形式规避 |
| M5 | LoCoMo venue | draft：NAACL 2024 | DBLP：ACL 2024 (long) | 不可解释（非版本差异，属记载错误） | 采用 ACL 2024 |
| M6 | Prompt Report 标题 | arXiv： "…Survey of Prompt **Engineering** Techniques" | DBLP： "…Survey of **Prompting** Techniques" | 部分可解释：v6 改题 | 引用以 arXiv 现题为准，标注 DBLP 别名 |
| M7 | Semantic Uncertainty venue | arXiv comment：ICLR 2023 Spotlight | DBLP：`conf/iclr/KuhnGF23`（2023） | **两源一致**（非矛盾） | 采用 ICLR 2023；记录此条是为排除"该文常被误引为 ICLR 2024"的外部说法（agent 记忆偏差） |
| M8 | ScientistTwo 定位 | draft §2.4：judge 架构 | arXiv 摘要：自主科学发现多智能体框架 | 不可解释（内容误述） | 不改任务范围外的正文；在阶段 04 交接里标为"§2.4 需重写"，并给出一句更正稿（见 04 工件） |
| M9 | DREAM 副标题 | draft：Agent Evaluation and Measurement | ACL Anthology：Evaluation with Agentic Metrics | 不可解释 | 采用 Anthology 现题 |

**未解决/不强行收敛**：M4 的作者列表差异**不做仲裁**（无法判断相机版是否真加作者）；M6 的标题差异保留两种写法并注明来源。

---

## 4. 候选集变更登记（相对阶段 01 冻结域①–⑥，规则见 01 §6）

| # | 域 | 变更 | 条目 | 理由 | 时间 |
|---|----|------|------|------|------|
| 1 | ⑥ | 域内**补 1 篇统计方法学** | N19 Miller 2024 | 域⑥候选中 Meyes 2019 只讲"如何做消融"，不覆盖"消融结果如何判显著"；本文 3-rep/无 CI 是最大弱点，必须有方法学支撑 | 18:54Z |
| 2 | ② | 域内**补 1 篇 survey** | N8 Prompt Report | 为"结构 vs 风格"提供外部术语坐标，避免自造二分 | 18:54Z |
| 3 | ① | 域内**补 1 篇 2025 检索型 benchmark** | N4 BrowseComp | 任务卡要求"优先 2024–2026"，且它界定了我们 no-tool 结论的边界 | 18:54Z |
| 4 | ③ | 三路线各 1 篇（verbalized/multi-sample/logprob-adjacent）| N9/N10/N11 | 任务卡域③明确要求"verbalized confidence, logprob-based, multi-sample"三路线；N10 同时补 logprob（条件概率）对照 | 18:54Z |
| 6 | ③ | 域内**补 2 篇 2026 实证**（含 1 篇反方） | N20 Meyer 2026 / N21 Xu 2026 | 02.5 对抗核验发现域③原缺 2024–2026 覆盖（任务卡"优先 2024–2026"）；N20 同时给我们 3-rep 设计的反证，N21 是 verbalized 路线的反方证据，§2 必须写双面 | 18:56Z |
| 5 | 全域 | **无域增删** | — | 6 域冻结不变 | — |

**排除了什么**：① 未收 SWE-bench+ / SWE-ABS 等 2026 派生变体（DBLP 检索中出现，但属同一 benchmark 的派生，去重规则 F2.3 不收）；② 未收 Perplexity/OpenAI DR 产品页（任务卡域⑤要求"有 paper 的"，X2）；③ 未收"只在应用里做了消融"的 2026 论文（域⑥只收方法学）。

---

## 5. 空缺回收（对 01 §7 G1–G6）

| 空缺 | 状态 | 证据 |
|------|------|------|
| G1（6 域均可解析） | **已回收** | 21/21 篇双源可解析；每域 ≥1 |
| G2（既有 10 篇 ID 复核） | **已回收（负面）** | 7 篇需修订（§2 E1–E7）；3 篇无误（E8） |
| G3（venue/year 双写口径） | **已回收（规则）** | 口径 = `venue year + arXiv ID` 并列；预印本写 "arXiv preprint YYYY"；arXiv 年 ≠ 会议年不算矛盾（如 WebArena arXiv 2023 / ICLR 2024） |
| G4（域⑥是否有专文） | **部分回收** | 有 1 篇真方法学专文（N18, 2019）；2024–2026 **无**专门"LLM 消融方法学"论文（C8 检索 top-8 全为应用论文）→ 域⑥ = N18 + N19（统计口径）拼合，**在 §2 必须显式声明"LLM 领域缺消融方法学专文，我们借用 ANN 方法学 + 评测统计"** |
| G5（ACL Anthology/OpenReview 可达） | **已回收（正面）** | ACL Anthology 200 可读（C6）；OpenReview 未试（DBLP 已提供 ee 链接，无需） |
| G6（§2 接线形态） | **保留** | 默认按"新增子节 + References 增量"执行，owner=user 未答，阶段 04 记录为显式默认假设（不阻塞） |

---

## 6. 交给 02.5 / 03 的证据边界

**可计入已核验证据**：§1 的 21 篇（title/authors/venue/year/ID 双源）；§2 E1–E8 的勘误结论（每处 ≥2 源）。

**不得计入已核验证据**：
- N4/N8/N18/N19/N20/N21 的 "venue" —— 均为 arXiv 预印本，无同行评审版（DBLP 亦只有 CoRR），写作时不得写成会议论文。
- M4 的作者数仲裁（未收敛）。
- 任何"该论文证明了我们结论"的因果表述——本阶段只建立"主题相关 + 元数据为真"；强度分级与论证接法归 03/04。

**关键不确定性（须在 04 明示）**：
1. 域⑥ 无 2024–2026 专文，只能是"借用 + 声明"，属方法学弱点而非可补齐项。
2. §2.4 的 ScientistTwo 定位句（M8）是既有正文的**内容错误**，修它会改到 T27 拥有的正文段落 → 04 只给更正稿，不擅自改正文，除非 §2 增量小节内引用时按正确描述写。
3. 本轮未做"文献→我们数字"的效应量对齐（例如 STORM 的 +25% 与我们 S1 的 +0.129 不可直接比较），§2 措辞不得暗示可比。