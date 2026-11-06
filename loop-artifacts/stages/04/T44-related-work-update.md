# T44: Related Work Update (Nov 2026) — `paper-draft.md` §2 增量文献、建议修改段落与矛盾清单

> **生成时间**：2026-11-06 UTC · **执行通道**：Arena Agent Mode（`web_search` + `fetch_page` 直连 arXiv Atom API / DBLP API / ACL Anthology）
> **目标底稿**：`experiments/stage-ablation/paper-draft.md`（§2 Related Work, L29–L61；§References, L344–L376）
> **全链路追溯工件**：`loop-artifacts/stages/01/T44-01-goal-decomposition.md` → `02/T44-02-research.md` → `02.5/T44-02.5-crosscheck.md` → `03/T44-03-actions.md`

---

## 0. 核心结论与前置边界声明（Upfront Scope & Limitations）

1. **核心统计**：共补入 **17 篇**经一手源（arXiv Atom API + DBLP / ACL Anthology / OpenReview / 官方仓）交叉核验的 **2026 H2 新文献**（编号 `Ref #32`–`#48`，与原稿既有 `Ref #1`–`#31` 零重复）。其中 **2026-09~11 最新文献 14 篇**（`2609.*` 5 篇、`2610.*` 7 篇、`2611.*` 1 篇、外加 `2608.18091v3` *EMNLP 2026 Findings* 10 月正式版），**2026-07~08 高相关文献 3 篇**（填补商业 Deep Research 横评与 no-tool 对照基准），在最严口径（仅计 09~11）与全 H2 口径下均远超 `≥8 篇` 门禁。
2. **底稿结构对齐说明**：任务书背景简述 §2 为三小节（2.1–2.3）且止于 2026-07；实查当前 `paper-draft.md`（经 T37 扩充后）已有 **六个小节（§2.1–§2.6）** 与 31 篇引用（含 3 篇 2026-09 文献，但 **2026-10~11 为 0 篇**，且 **LLM-as-judge 2026 可靠性/同族偏置方向几乎空白**）。下文表 1 同时标注「实盘 §2.1–§2.6 精确落点」与「任务书三大主块映射」，第 2 节给出的英文段落可直接替换/追加进 `paper-draft.md`。
3. **竞品稀缺性实证结论（好坏消息并列）**：
   - **利好（确立本文独特性）**：遍查 2026 H2 公开学术库，**严格同构竞品（固定开源权重模型 + 无外部工具 + 多阶段研究流水线逐阶段累积消融 + 多维科学问答 rubric）为 0 篇**——2026 H2 新发布的冠名智能体基准几乎全部默认绑定外部工具沙箱。
   - **限制与警示（前置披露）**：① 收录的 17 篇中包含 **5 篇 2026-10 中下旬最新 arXiv v1 预印本**（`2610.25954`, `2610.31639`, `2610.29073`, `2610.24320`, `2610.25846`），尚未经过同行评议且因发布仅 2–3 周尚未进入 DBLP 批处理索引；② 商业 Deep Research 宽深基准 **WANDR (`arXiv:2608.14747`)** 由 Perplexity AI 团队发布，测试中自家系统使用可编程生产级 API 而竞品（如 Gemini Deep Research）使用预览版产品界面，排名与中立学界基准（如 `DeepResearch Bench II`, `arXiv:2601.08536`）相反，引用时**只可引其跨系统共性瓶颈，不可盲引单一厂商胜率**；③ 2026 H2 关于裁判**格式/权威偏置**（Yin et al., `2610.24320`）与**口头置信度基率聚集假象**（Ghosh et al., `2610.25846`）的工作对本文 M2/M3/M6 解读构成实质约束（详见第 3 节张力清单 T1–T6）。

---

## 1. 新增引用总表（17 篇 · 2026 H2 核验完毕）

> **竞品分类口径**：
> - **方法论直接竞品（同处 `no-tool / parametric-only` 设定，共 4 篇）**：同样在不接入外部检索/执行工具的纯参数条件下，量化消融提示结构、任务分解或口头置信度机制（区别在于其任务为短答推理而非 6 阶段科学综述流水线）。
> - **相关但不同设定（共 13 篇）**：引入外部工具沙箱、端到端强化学习，或专门研究评测器（LLM-as-a-Judge）/ 检索后校准层。

| 新编号 | 调研方向 | 作者 (年份·月份) | 唯一标识符（arXiv ID / 正式 DOI）与 Venue | 竞品属性分类 | 一句话核心定位（含关键实证数字，源自一手摘要/正文） | 归入 `paper-draft.md` 小节（括号内对应三主块） |
|-------|---------|-----------------|----------------------------------------|------------|------------------------------------------------|------------------------------------------|
| **#32** | D1 Agent Bench | Park, C., Yoon, J., Han, S., Moon, H., & Lim, H. (2026-09 / v2 2026-11) | `arXiv:2609.34428` · *NeurIPS 2026 E&D Track* | 相关但不同设定（7 工具沙箱科学多跳 QA） | 提出 **AgentHop**（1,011 题），将单一准确率拆解为检索、综合、工具调用、资源管理四轴诊断 19 个模型，揭示跨家族行为指纹与同家族内部检索/综合权衡，印证多维诊断优于单标量总分。 | **§2.1** LLM Agent Evaluation *(2.1)* |
| **#33** | D1 Agent Bench | Yu, B., Zhang, Y., Su, Z., et al. (2026-10) | `arXiv:2610.25954` · arXiv preprint | 相关但不同设定（有工具监管工作流） | 提出 **CXBench**（120 任务 × 7 模型），用确定性规则卡 + LLM 裁判分离评估结果正确性与过程合规性，发现 **80.1%** 的结果通过运行实为过程违规「假通过」（双通过仅 13.8%）且纳入过程评分会改写模型排名。 | **§2.1** LLM Agent Evaluation *(2.1)* |
| **#34** | D1 Agent Bench | Zhao, R., & Raissi, M. (2026-07/08) | `arXiv:2608.11232` · *IJCAI 2026 FinLLM Workshop* | 相关但不同设定（**含显式 `no-tools` 对照组**） | **Backtrader-Bench** 同台对比 11 个无工具纯参数模型与 4 个带工具智能体：带工具前沿配置达 **90.0%**，超出最强无工具基线（**73.0%**）达 +17 pp，在去记忆挖掘题上半数无工具模型跌至 ~25% 随机水平，量化锚定纯参数天花板。 | **§2.1** LLM Agent Evaluation *(2.1)* |
| **#35** | D2 Prompt Ablation | Dominici, G., McMillan, T., Barez, F., Langheinrich, M., & Gjoreski, M. (2026-10) | `arXiv:2610.31639` · arXiv preprint | **★方法论直接竞品**（`no-tool` 推理期 DAG 分解 vs 单遍 CoT） | 提出 **CausalCoT**，指出标准单遍 CoT 因全局稠密注意力产生「注意力泄漏」与事后合理化，通过将问题拆成原子子问题 DAG 并在隔离上下文中求值，使中间步骤因果敏感度平均提升 **+12 pp（最高 +21 pp）**。 | **§2.2** Structured Prompting & CoT *(2.2)* |
| **#36** | D2 Prompt Ablation | Khan, I., Nguyen, T.V., Xia, Y., et al. (2026-10) | `arXiv:2610.29073` · arXiv preprint | **★方法论直接竞品**（`no-tool` 20 个开源模型提示风格/角色消融） | 横跨 20 个 LLM（含 2B–14B 开源模型）与 7 个基准量化对比零样本、零样本 CoT 与静态/动态专家角色 CoT（**RE-ZS-CoT**），对齐时最高提升 **+44 pp**，但错配角色显著拉低性能，印证提示框架须按题型自适应。 | **§2.2** Structured Prompting & CoT *(2.2)* |
| **#37** | D2 Prompt Ablation | Jia, R., & Mu, D. (2026-09) | `arXiv:2609.25366` · *TMLR* (Sep 2026) | **★方法论直接竞品**（`no-tool` 7B–9B 开源模型 CoT 因果消融） | 对 28,584 条续写轨迹做扰动截断消融，证明 **98.8%** 的 CoT 因果承重度偏差由模型相对任务难度解释：简单/熟悉题上模型静默绕过书面推理（装饰性），难题上错误传播飙升 **16 倍**，解释为何熟悉概念题 Q5 无需机械支架。 | **§2.2** Structured Prompting & CoT + **§2.6** *(2.2)* |
| **#38** | D3 LLM-as-Judge | Ayyagari, K.C. (2026-09) | `arXiv:2609.33044` · arXiv preprint (v2) | 相关但不同设定（云端前沿裁判稳定性审计） | 实测 4 个 `temp=0` 固定版本前沿裁判在三大榜单上的重跑翻转率均值 ~5%（临界题高达 **~40%**），跨模型家族裁判间 Kendall's $\tau$ 低至 **0.42–0.64**（15 条预期排序仅 8 条跨族存活），确立「多遍重跑 + 至少双家族裁判」准则。 | **§2.4** Eval & Judge Reliability + **§2.6** *(2.1/2.3)* |
| **#39** | D3 LLM-as-Judge | Chae, S., Kim, M., Jung, D., Choi, S., & Jung, S. (2026-10) | `arXiv:2608.18091` · `DOI: 10.18653/v1/2026.findings-emnlp.1571` (*EMNLP 2026 Findings*) | 相关但不同设定（10 模型自偏爱盲评机理拆解） | 剥离文本风格混杂后证明：**盲评下控制候选质量与裁判严厉度后，自偏爱基本消失甚至微弱反转**；仅在显式标注「自己/他人」标签时才出现双向虚高/压低，直接解释本文 §4.5 盲评同族裁判低打 ~0.15 源于严厉度基线而非反常自偏爱。 | **§2.4** Eval & Judge Reliability *(2.1/2.3)* |
| **#40** | D3 LLM-as-Judge | Kumar, V., Rathore, D., & Moitra, A. (2026-10) | `arXiv:2610.12083` · `DOI: 10.18653/v1/2026.aacl-long.207` (*AACL-IJCNLP 2026 Main*) | 相关但不同设定（6 前沿裁判多维可靠性审计） | 在 4 基准 × 5 格式 × 10 重复下发现最确定性的 `temp=0` 裁判虽 100% 自洽但真值一致率仅 **51%**，并证明**从成对胜率转向整体多维量表（holistic rubric）对可信判定率的提升超过任何单提示修补**。 | **§2.4** Eval & Judge Reliability *(2.1)* |
| **#41** | D3 LLM-as-Judge | Yin, Y., Wu, J., Kumar, A., Novotney, S., Liu, D., & Babinsky, E. (2026-10) | `arXiv:2610.24320` · arXiv preprint | 相关但不同设定（裁判权威/自信/格式偏置与自纠偏） | 首发权威偏置（伪造引用）、自信偏置（武断措辞）与**格式偏置（结构化排版）**基准，证明自纠偏提示在 20/21 组合上提升达 +15 pp（优于泛化退化的微调评论器），同时揭示结构化输出易获裁判格式加分的潜在混杂。 | **§2.4** Eval & Judge Reliability *(2.1)* |
| **#42** | D4 Deep Research | Polshkov, V., Pitera, M., Yang, J., et al. (2026-08) | `arXiv:2608.14747` · arXiv preprint | 相关但不同设定（商业 Deep Research 宽深动态核验） | 提出 **WANDR**（500 任务）重抓网页横评 Perplexity、OpenAI 与 Gemini Deep Research（最强仅 **0.363 Soft F1 / 0.133 Hard F1**），揭示忠实摘录虽 96.9%–99.4% 支持部分断言但仅 **55.6%–80.4%** 支持全部挂靠断言（部分支持陷阱）。 | **§2.1** & **§2.5** Deep Research Agents *(2.1)* |
| **#43** | D4 Deep Research | Zhu, P., Li, L., Yang, L., Su, S., & Shao, J. (2026-07) | `arXiv:2607.20891` · arXiv preprint (v2) | 相关但不同设定（Gemini DR 等抗误导评测） | **MisKnow-Agent** 在 DeepResearch Bench 任务上评测 Gemini Deep Research、DeerFlow 与 WebThinker：仅注入 **1 篇**权威伪装误导文档即令错误结论采纳率（FCAR）从 **0% 飙升至 54.7%**，且事后核验无法彻底消除采纳。 | **§2.5** Deep Research Agents *(2.1)* |
| **#44** | D4 Deep Research | Liu, H., Sun, Y., & Tan, Q. (2026-09) | `arXiv:2609.39154` · *NeurIPS 2026* | 相关但不同设定（有工具 + RL 动态图规划 DR） | 提出 **DAGent**，证明执行前一次性生成全任务图的静态分解（Plan-then-Patch）在证据最弱时做出最强承诺而脆弱，基于已完成节点置信度逐批生长的 **Evaluate-then-Grow** 在 BrowseComp-Plus / GAIA 上领先开源基线 **+5.3 / +5.8 分**。 | **§2.5** Deep Research Agents *(2.1/2.2)* |
| **#45** | D5 Calibration | Hsiao, Y.-C. (2026-09) | `arXiv:2609.10996` · arXiv preprint | 相关但不同设定（18 模型 verbalized vs logprob 跨代对比） | 横跨 18 个 LLM 对比口头置信度与 logprob（G-Eval），发现**代际兼容性转移**：2025 后旗舰闭源模型上口头置信度（含过度自信警示+自我辩论）全面优于 logprobs，但较早/较弱模型加载警示会付出平衡准确率代价。 | **§2.3** Self-Assessment & Calibration *(2.3)* |
| **#46** | D5 Calibration | Ghosh, D., Kumar, S., & Garg, A. (2026-10) | `arXiv:2610.25846` · arXiv preprint | **★方法论直接竞品/反方**（`no-tool` Qwen2.5 口头 vs 探针 vs 多样本审计） | 在 5 个 Qwen2.5 模型（0.5B–7B）上预注册对比口头置信度、隐状态线性探针与多样本一致性：证明**口头置信度跨微调模板几乎不相关，且低 ECE 源于向基率聚集的假性校准（区分分辨率仅为多样本一致性的约 1/2）**。 | **§2.3** Self-Assessment & Calibration *(2.3)* |
| **#47** | D5 Calibration | Xu, Y., Liang, Y., Cheng, J., et al. (2026-09/10) | `arXiv:2609.00935` · `DOI: 10.18653/v1/2026.emnlp-main.389` (*EMNLP 2026 Main*) | 相关但不同设定（Qwen2.5/Qwen3 深研双路径校准） | **DualStake** 在 8 个 QA 基准上研究 Deep Research 智能体校准，发现**检索末步诱导的证据置信度（E-Conf）比答案生成后口头置信度（A-Conf）提供更强的不确定性信号**，并提出双路径奖励对齐。 | **§2.3** Self-Assessment & Calibration *(2.3)* |
| **#48** | D5 Calibration | Schwager, N., Münker, S., Plum, A., & Rettinger, A. (2026-10/11) | `arXiv:2611.07735` · `DOI: 10.18653/2026.wnut-1.7` (*EMNLP 2026 W-NUT*) | 相关但不同设定（开源模型 token logprob 校准实证） | 测试开源权重模型（Ministral 3B/8B）的 **token probabilities（logprobs）**：仅靠上下文提示时严重过度自信且劣于统计基线，**从 3B 扩至 8B 提升准确率却恶化校准**，唯有 SFT 才将 ECE 从 **0.20 压至 0.006**。 | **§2.3** Self-Assessment & Calibration *(2.3)* |

---

## 2. 建议修改文本（直接可贴进 `experiments/stage-ablation/paper-draft.md`）

> **合入指南**：以下英文文本严格保持 `paper-draft.md` 现有学术语调与括号作者-年份引用规范。经机器模拟逐段合入实测：§2 正文主体净增 **628 词**（正文不含 References 与 Appendices 由 **6,085 词** 增至 **6,713 词**，严格落在 `arxiv-submission.md` 规定的 `4,000–8,000` 词正文区间内；含 References `#32`–`#48` 新增 **422 词** 与 Appendices 在内的全文件由 **7,091 词** 增至 **8,141 词**）。
> **重名消歧注意**：原稿已有 `Xu, Y., Wang, A., et al. (2026)` (`arXiv:2609.34454`, Ref #23)，本次新增 `Xu, Y., Liang, Y., et al. (2026)` (`arXiv:2609.00935`, Ref #47)，下文在 §2.3 与 §References 中显式用 **`Xu, Wang, et al. (2026)`** 与 **`Xu, Liang, et al. (2026)`** 区分。

### 2.1 贴入 `§2.1 LLM Agent Evaluation`（追加在现有第 2 段末尾，L37 之后）

```markdown
Late-2026 benchmarks begin decomposing aggregate agent accuracy along operational axes, yet still presuppose external tools. AgentHop (Park et al., 2026) dissects 1,011 multi-hop scientific QA tasks across retrieval, synthesis, tool-call, and resource-management axes in a seven-tool sandbox, exposing model-family signatures, while CXBench (Yu et al., 2026) separates outcome accuracy from process compliance via hybrid grading, finding 80.1% of outcome-passing runs violate workflow rules ("false-passes"). Backtrader-Bench (Zhao and Raissi, 2026) contrasts 11 parametric-only (`no-tools`) baselines against tool-augmented agents (+17 pp with tools, 90.0% vs. 73.0%, and ~25% no-tool collapse on contamination-filtered items), anchoring our §5.1–§5.3 parametric ceiling. In commercial deep research, WANDR (Polshkov et al., 2026) benchmarks Perplexity, OpenAI, and Gemini Deep Research across 500 wide-and-deep tasks via live page-refetch verification (peaking at 0.363 soft F1 / 0.133 hard F1 under vendor-logged tasks and asymmetric interfaces). Unlike these tool-coupled benchmarks, we isolate *per-stage prompt contributions* in a strict no-tool regime before re-introducing controlled retrieval (§5.1).
```

### 2.2 贴入 `§2.2 Structured Prompting and Chain-of-Thought`（替换现有第 2 段 L43，将本文 M7/S6/S7 与 2026 H2 三篇 no-tool 直接竞品深度咬合）

```markdown
Three late-2026 parametric-only studies clarify *when* and *why* explicit scaffolds help or hurt. Via continuation-patching ablations over 28,584 traces, Jia and Mu (2026) show task difficulty explains 98.8% of CoT causal load-bearingness: models silently bypass written CoT on familiar items ("decorative" CoT) while propagating errors 16× more strongly on hard items — matching why bare/fuzzy S6 excels on familiar conceptual Q5 whereas scaffolding is load-bearing on spec-dense or tension-heavy Q1/Q4. Dominici et al. (2026) show monolithic CoT suffers *attention leakage* (post-hoc lookup rationalization), whereas evaluating a sub-question DAG in isolated parent-only contexts (CausalCoT) boosts causal faithfulness by +12 to +21 pp — explaining why single-pass inline verification (S3, S8E) dilutes attention while two-pass separation (S7V) succeeds. Across 20 models (2B–14B+) and seven benchmarks, Khan et al. (2026) find Role-Enhanced Zero-Shot CoT gains up to +44 pp when role framing aligns with the task, but degrades when misaligned. Consistently, our M7 results show structure aids fact recall (M1) and gap listing (M4) yet degrades contradiction adjudication (M7: 0.306→0.256 from S0 to S1), as tree-template compliance crowds out implicit caveats.
```

### 2.3 贴入 `§2.3 Self-Assessment and Calibration`（替换现有第 2 段 L49，合并新旧校准证据并消歧 `Xu`）

```markdown
Across arms, M2 means span 0.037–0.618, reflecting absent uncertainty markers under mechanical prompts versus S6's fuzzy jump (0.618 vs. S0: 0.037; cf. Tian et al., 2023). Late-2026 work sharply bounds verbalized versus logprob calibration. Supporting verbalized elicitation, Meyer et al. (2026) find verbalized confidence beats 3-sample agreement on TriviaQA (AUROC 0.956/0.937 vs. 0.765/0.790, as 3-rep agreement amplifies shared misconceptions); Hsiao (2026) documents a *compatibility shift* across 18 LLMs where post-2025 frontier models yield better soft scores from verbalized confidence than logprobs (though pre-2025/weaker models pay a balanced-accuracy penalty); and Schwager et al. (2026) show open-weight token probabilities remain overconfident under prompting alone (3B→8B scaling raises accuracy while *degrading* calibration unless fine-tuned, ECE 0.20→0.006). Conversely, three studies caution against over-interpreting M2: Xu, Wang, et al. (2026) show hidden-feature estimators outperform verbalized self-reports; Ghosh et al. (2026) show across five Qwen2.5 models that verbalized confidence is template-brittle and achieves deceptively low ECE by clustering near the base rate with half the resolution of sampling agreement; and Xu, Liang, et al. (2026) show post-retrieval *evidence confidence* beats post-answer verbalized confidence in deep-research agents. We thus treat S6's M2 gain as prompt-layer elicitation rather than calibrated internal readout.
```

### 2.4 贴入 `§2.4`（建议将小节标题更新为 `### 2.4 RAG Evaluation, Retrieval Quality, and Judge Reliability`，在现有段末 L53 后追加第 2 段）

```markdown
Late-2026 LLM-as-a-judge audits motivate and bound our §3.5/§4.5 dual-judge design. Ayyagari (2026) shows pinned, temperature-0 frontier judges flip ~5% of item verdicts (~40% on close calls) and diverge across model families (Kendall's $\tau$ = 0.42–0.64 on Arena-Hard; only 8/15 head-to-head claims survive cross-family swaps), prescribing multi-run reporting and $\ge$2 judge families — matching our ±0.10 single-pass noise floor (§5.4). Kumar et al. (2026) show a temperature-0 judge can reach 100% repeat consistency at 51% ground-truth accuracy, yet find **holistic rubric scoring** improves trustworthiness more than any single-format prompt fix, supporting our 7-dimension rubric over pairwise win-rates. Crucially, Chae et al. (2026) explain why our same-family Qwen3.8-27B judge scores its own outputs ~0.15 *lower* than the frontier judge (§4.5): under *blind* evaluation without authorship labels, self-preference vanishes (and slightly reverses) once quality and baseline *judge severity* are controlled. Finally, Yin et al. (2026) document *formatting bias* (rewarding structured layouts) and *authority bias* (rewarding fabricated citations), a caveat for M3/M6 on S1–S5 mitigated on M1/M4 via format-stripped assertion matching.
```

### 2.5 贴入 `§2.5 Positioning vs. ScientistTwo and Deep Research Agents`（追加在现有段末 L57 之后）

```markdown
Recent 2026 deep-research evaluations expose two vulnerabilities mirroring §5.1. On planning, DAGent (Liu et al., 2026) shows static upfront decomposition ("Plan-then-Patch," analogous to S1) commits hardest when evidence is weakest, whereas confidence-conditioned incremental expansion ("Evaluate-then-Grow") gains +5.3/+5.8 points on BrowseComp-Plus and GAIA at lower cost. On retrieval grounding, WANDR (Polshkov et al., 2026) finds faithful excerpts support *some* claim 96.9%–99.4% of the time, but full support for *all* attached claims drops to 55.6%–80.4%, paralleling S7T's source-anchoring drop (M1: 0.771→0.480). More severely, MisKnow-Agent (Zhu et al., 2026) shows injecting one authority-cued misleading document into DeepResearch Bench tasks drives false-conclusion adoption from 0% to 54.7% (including Gemini Deep Research) despite post-hoc defenses — bounding S7V (two-pass verification neutralizes *benign incomplete* snippets, not *adversarially false* sources).
```

### 2.6 贴入 `§2.6 Ablation Methodology`（替换原稿 L61 中 `(b) no 2024–2026 paper...` 至段尾部分）

```markdown
(b) while recent work formalizes continuation-patching ablations for CoT traces (Jia and Mu, 2026) and cross-family stability protocols for LLM judges (Ayyagari, 2026), no 2024–2026 paper addresses *combinatorial stage-ablation methodology for agent prompt pipelines*, so we borrow from ANN lesion tradition plus evaluation statistics (Miller, 2024), cited in §5.4 to flag statistical power at $n=3$ per cell.
```

### 2.7 配套新增 `§References` 条目（直接追加在 `paper-draft.md` L376 `31. Miller...` 之后，外加 2 条原稿细微修正）

> **原稿既有条目细微勘误提示**：
> - `6.` 原稿副标题写为 *An Autonomous Multi-Agent Framework for Scientific Discovery*，arXiv 官方 v1 真实标题为：`Nam, J., Yoon, J., Pan, Y., et al. (2026). ScientistTwo: Pioneering the Human Knowledge Frontier with Autonomous AI. arXiv preprint 2026. arXiv:2609.19644.`
> - `23.` 正文引用处建议由 `Xu et al. (2026)` 改为 `Xu, Wang, et al. (2026)`，以与下方新增 `47. Xu, Liang, et al. (2026)` 明确区分。

```markdown
32. Park, C., Yoon, J., Han, S., Moon, H., Lim, H. (2026). AgentHop: A Diagnostic Benchmark for Agentic Multi-Hop Question Answering over Scientific Citation Graphs. *NeurIPS 2026* (Evaluations and Datasets Track). arXiv:2609.34428.
33. Yu, B., Zhang, Y., Su, Z., et al. (2026). CXBench: A Benchmark for Process-Compliant LLM Agents in Regulated Customer-Experience Workflows. arXiv preprint 2026. arXiv:2610.25954.
34. Zhao, R., Raissi, M. (2026). Backtrader-Bench: Benchmarking LLM Agents on Algorithmic Trading with Self-Generated MCQs. *IJCAI 2026 FinLLM Workshop*. arXiv:2608.11232.
35. Dominici, G., McMillan, T., Barez, F., Langheinrich, M., Gjoreski, M. (2026). Causal Chain of Thought: Mitigating Attention Leakage via Context Isolation. arXiv preprint 2026. arXiv:2610.31639.
36. Khan, I., Nguyen, T.V., Xia, Y., et al. (2026). A Large-Scale Evaluation of Role-Enhanced Zero-Shot Chain-of-Thought Prompting. arXiv preprint 2026. arXiv:2610.29073.
37. Jia, R., Mu, D. (2026). From Decorative to Load-Bearing: Task Difficulty Shapes the Causal Role of Chain-of-Thought. *TMLR 2026*. arXiv:2609.25366.
38. Ayyagari, K.C. (2026). Pinned and Still Unstable: Within-Judge Verdict Variance and the Noise Floor of LLM-as-Judge Leaderboards. arXiv preprint 2026. arXiv:2609.33044.
39. Chae, S., Kim, M., Jung, D., Choi, S., Jung, S. (2026). Self- and Other-Labels Induce Bidirectional Bias in LLM Judges. *Findings of EMNLP 2026*, pp. 33466–33482. DOI: 10.18653/v1/2026.findings-emnlp.1571. arXiv:2608.18091.
40. Kumar, V., Rathore, D., Moitra, A. (2026). All Verdicts are Not Equal: Rethinking LLM Judge Reliability. *AACL-IJCNLP 2026*, pp. 4581–4598. DOI: 10.18653/v1/2026.aacl-long.207. arXiv:2610.12083.
41. Yin, Y., Wu, J., Kumar, A., Novotney, S., Liu, D., Babinsky, E. (2026). The Judge Can Debias Itself: Awareness and Self-Debiasing for Reliable LLM-as-a-Judge. arXiv preprint 2026. arXiv:2610.24320.
42. Polshkov, V., Pitera, M., Yang, J., et al. (2026). WANDR: A Benchmark for Wide and Deep Research. arXiv preprint 2026. arXiv:2608.14747.
43. Zhu, P., Li, L., Yang, L., Su, S., Shao, J. (2026). Is Deep Research Reliable? Misleading Knowledge Induces False Conclusions. arXiv preprint 2026. arXiv:2607.20891.
44. Liu, H., Sun, Y., Tan, Q. (2026). DAGent: Evaluate-then-Grow Planning for Deep Research Agents. *NeurIPS 2026*. arXiv:2609.39154.
45. Hsiao, Y.-C. (2026). Rethinking Verbalized Confidence for LLM-as-a-Judge: A Compatibility Shift on Post-2025 Proprietary Models. arXiv preprint 2026. arXiv:2609.10996.
46. Ghosh, D., Kumar, S., Garg, A. (2026). Measurement Validity and Representation Dynamics of Confidence Signals in Large Language Models. arXiv preprint 2026. arXiv:2610.25846.
47. Xu, Y., Liang, Y., Cheng, J., et al. (2026). DualStake: Dual-Path Confidence Calibration in Deep Research Agents. *EMNLP 2026*, pp. 8924–8941. DOI: 10.18653/v1/2026.emnlp-main.389. arXiv:2609.00935.
48. Schwager, N., Münker, S., Plum, A., Rettinger, A. (2026). Evaluating Token Probabilities as Confidence Estimators in Human Behavior Simulations: A Case Study in Luxembourgish Next Like Prediction. *EMNLP 2026 W-NUT*, pp. 89–100. DOI: 10.18653/2026.wnut-1.7. arXiv:2611.07735.
```

---

## 3. 矛盾 / 张力清单与差异来源深度归因（Contradiction & Tension Analysis）

检索发现 **6 组与本文核心结论构成直接矛盾、方法学威胁或适用边界限定的 2026 H2 工作**（外加 1 组外部基准排名冲突），逐项拆解差异根源与论文应对策略如下：

### T1. 【方法学混杂威胁】LLM 裁判的「格式偏置」与「权威偏置」 vs 本文 S1–S5 结构化总分增益（+0.182）
- **矛盾文献**：Yin et al. (`arXiv:2610.24320`, Oct 2026) 证明前沿 LLM 裁判系统性存在 *formatting bias*（偏爱结构化排版）与 *authority bias*（偏爱伪造/形式化引用标签）。
- **与本文的冲突**：本文累积臂 S1–S5 强制模型输出 Markdown 树状标题与章节锚点，而基线 S0 与模糊臂 S6 为散文段落；审稿人极易质疑「S5 胜 S0 的 +0.182 是否只是裁判被排版与引用外壳哄骗？」
- **差异来源与实证拆解**：
  1. **在 M3（结构）与本地同源 M6（形式引用）上，偏置确实存在**：例如本地 27B 裁判在 S2–S5 给出 M6=1.000（仓库前序异族审计 T23-v2 已证实其中包含形式合规但实质不支持的假阳性）。
  2. **在核心事实与缺口维度（M1/M4）上，评估协议提供了去格式隔离**：本文 `score.py` 并非让裁判直接给全文印象分，而是先抽取去格式的原子事实断言（assertions）再与 gold 逐条匹配；更有力的反证是，轻结构混合臂 **S7** 在异族前沿裁判下取得全场最高 M1（**0.761**，且 Q2 达 1.000），高于重度模板化的 S5（0.521），说明事实召回提升并非纯排版假象。
- **建议应对**：已在 §2.4 建议段落中显式引用 Yin et al. (2026) 主动披露 M3/M6 的格式/权威偏置边界，并强调 M1/M4 的原子断言抽取设计。

### T2. 【表面方向相反 → 机理化解】传统「同族自偏爱虚高」 vs 本文 §4.5 同族 27B 裁判保守低估（−0.15）
- **矛盾文献**：传统文献及 Barbera et al. (`arXiv:2610.18108`, Oct 2026) 将同模型家族偏置建模为「对同族产出过度自信/虚高打分（inflation）」；而本文 §4.5 实测本地 Qwen3.8-27B 裁判对自身产出比异族前沿裁判平均**低打 ~0.15（保守偏置）**。
- **差异来源（由 Chae et al., `arXiv:2608.18091`, *EMNLP Findings 2026* 精确解开）**：
  - 既往测得同族虚高的实验大多在**成对偏好比较（pairwise preference）**或**含模型风格指纹/身份线索**下进行，把「质量启发式 + 裁判严厉度基线」与「自偏爱」混为一谈。
  - Chae et al. (2026) 控制文本风格后证明：**在无来源标签的盲评（blind evaluation）中，控制候选质量与裁判固有严厉度（evaluator severity）后，同族自偏爱完全消失，甚至在一个维度上微弱反转（对自己更严）**；唯有显式贴上「self/other」标签才会触发双向虚高/压低。
  - 本文采用无标签单文档盲评 + 逐条断言核对，因此 −0.15 本质上是 **Qwen3.8-27B 相对前沿模型在严格字面匹配上的基准严厉度差（severity offset）**，与 Chae et al. 完全自洽。

### T3. 【统计效力与跨族翻转】`temp=0` 裁判高重复一致性假象 vs 本文单裁判噪声底与 Q1 H1 跨族反向
- **矛盾文献**：Ayyagari (`arXiv:2609.33044`, Sep 2026) 与 Kumar et al. (`arXiv:2610.12083`, *AACL 2026*)（以及开源小裁判上的 Tiwari `arXiv:2609.13824`）。
- **冲突与张力**：① `temp=0` 并非确定性真值（临界题翻转率 ~40%，最稳定裁判靠重复错判仅达 51% 真值一致率），这意味着同模型双遍高 $\kappa$ 不能证明外部效度；② 跨家族裁判间中段排序一致性低至 $\tau=0.42\text{–}0.64$（15 条声明仅 8 条跨族存活），这直接解释了为何本文 §4.5 跨题扩展中 **Q1 的 H1（S1 vs S0）在同族 27B 裁判（+0.064）与异族前沿裁判（−0.187）间发生符号翻转**！
- **差异来源与正面支撑**：细微效应量（如单题 S1−S0）落在了跨族裁判分歧噪声带（±0.10）之内，而强效应（H2: S1→S2 信息调研段增益，以及 S7 > S6）超越噪声带故跨族稳健；同时 Kumar et al. 证明**整体多维量表（holistic rubric）比成对胜率可信度更高**，正面背书了本文 7 维量表设计。

### T4. 【指标效度反例】口头置信度「基率聚集假性校准」 vs 本文 §4.3「提示语校准自我评估（M2: 0.037→0.618）」
- **矛盾文献**：Ghosh et al. (`arXiv:2610.25846`, Oct 2026) 与 Xu, Liang, et al. (`arXiv:2609.00935`, *EMNLP 2026*)（对比支持方的 Hsiao `arXiv:2609.10996`）。
- **与本文的冲突**：本文 §4.3 与 §5.2 称「一句 'be honest about uncertainty' 即可将 M2 从 0.037 拉至 0.618，是廉价校准杠杆」。但 Ghosh et al. 在同属 Qwen 系的 Qwen2.5 模型上预注册审计发现：(1) 口头置信度对轻微提示词改写极不稳定；(2) **口头置信度的低 ECE 具有误导性——它通过把分数聚集在先验基率附近显得「校准良好」，但对正误的区分分辨率（resolution）只有多样本一致性的约一半**！此外 DualStake 证明答案后口头置信度（A-Conf，即本文 M2）弱于检索后证据置信度（E-Conf），且 Hsiao 指出较弱/前代模型加载校准警示可能折损准确率。
- **差异来源**：
  1. **测量口径不同**：本文 M2 是规则匹配「不确定性表述出现率与 M1 粗粒度一致性」；S0/S1 得分近零（0.037/0.093）是因为未提示时模型根本不输出不确定性词（零表达地板效应），而 S6 解锁了不确定性表达。
  2. **模型代际差**：Hsiao 的正向结果主要在 2025 后旗舰闭源模型上成立，而本文与 Ghosh et al. 均处于中小规模开源权重模型（Qwen 系）。
- **建议应对**：在 §2.3（见上方建议文本）与 §5.2 将「calibrates self-assessment」审慎收窄为「elicits explicit uncertainty markers at the prompt layer, without guaranteeing fine-grained instance-level discrimination」。

### T5. 【规划机制张力】前置静态分解（S1）非普适正收益 vs 动态生长分解与上下文隔离分解
- **矛盾文献**：DAGent (Liu et al., `arXiv:2609.39154`, *NeurIPS 2026*)、CausalCoT (Dominici et al., `arXiv:2610.31639`, Oct 2026)、Jia & Mu (`arXiv:2609.25366`, *TMLR 2026*)（辅以专利生成的 Jiang et al. `arXiv:2607.10480`）。
- **与本文的冲突与深层合流**：表面上经典文献（Least-to-Most）认为分解单调有益，而本文却观察到三个反常：① 异族裁判下 H1（S1>S0）跨题不显著（2 正 2 负）；② S1 使矛盾推理 M7 从 0.306 跌至 0.256；③ 单遍内嵌核验 S8E 与 S3 无增益。2026 H2 这组文献证明这不是实验噪声，而是三条机制的必然结果：
  1. **无证据过早承诺**（DAGent）：执行前一次性画死分解树（Plan-then-Patch，即 S1）在证据最弱时锁死结构，不如按置信度动态扩展（Evaluate-then-Grow）；
  2. **单上下文注意力泄漏**（CausalCoT）：在同一上下文窗口内既拆题又作答/自审（S1–S5, S8E）存在全局注意力串扰，唯有跨调用隔离上下文（对应本文双遍 S7V）才能强制局部因果约束；
  3. **口头化细节抽象与难度阈值**（Jia & Mu; Jiang et al.）：熟悉概念题（Q5）无需书面支架（S6 夺冠），而强行套用机械树模板会抹掉参数记忆中附带的隐式限定语（如 Q1 中 H100 PCIe vs SXM 的括号说明被树结构挤掉，导致 M7 下跌）。

### T6. 【安全边界矛盾】事后双遍核验恢复准确率（S7V M1=0.762） vs 误导性检索源下事后防御失效（FCAR=54.7%）
- **矛盾文献**：MisKnow-Agent (Zhu et al., `arXiv:2607.20891`, Jul 2026)。
- **与本文的冲突**：本文 §5.1 得出乐观结论：「两遍式『草稿→逐条核对原文删无据数字』（S7V）足以中和工具检索的源锚定降分（M1 从 0.480 恢复至 0.762）」。但 MisKnow-Agent 在 DeepResearch Bench 上证明：一旦检索结果中混入 **1 篇**带权威伪装但结论错误的文档，包括 Gemini Deep Research 在内的系统错误结论采纳率高达 **54.7%**，且**事后核验（post-research defense）无法消除错误采纳**。
- **差异来源（检索噪声性质的本质不同）**：
  - **本文 S7T/S7V 面对的是「良性不完整噪声（benign incompleteness）」**：`research_hook` 抓回的真实 arXiv 摘要与官网页面本身**没有造假**，只是缺少子问题所需的精确数字（例如只有通用架构描述而无 PCIe vs SXM 吞吐对比）；第一遍生成时模型受部分相关文本诱导脑补了数字，第二遍逐字比对源文本时因「源文本确实没写该数字」即可精准剔除。
  - **MisKnow-Agent 面对的是「对抗性/高权威错误源（adversarial / authoritative misinformation）」**：误导文档里**白纸黑字写着伪造数字与错误结论**，单靠「核对断言是否被源文本支持（faithfulness check）」会判定为「有源支持」而放行！
- **建议应对**：已在 §2.5 建议文本中明确切分这一边界——S7V 解决的是 *faithfulness to incomplete sources*（防模型越界脑补），解决 *source veracity*（防错误外部源投毒）则需多独立源交叉对质（即本文 `competitor-survey.md` §5.3 规划的下一代「双独立源印证升级 conf」机制）。

### 附：外部竞品基准内部矛盾备注（M-stake1 · 写作避坑提醒）
- 在商业 Deep Research 横评中，Perplexity 团队发布的 **WANDR (`arXiv:2608.14747`)**（及早先 **DRACO `arXiv:2602.11685`**）均测得 **Perplexity 第一 > Gemini / OpenAI**；而学界独立团队发布的 **DeepResearch Bench II (`arXiv:2601.08536`)** 与 **DeepResearch Bench (`arXiv:2506.11763`)** 则测得 **OpenAI-o3 DR / Gemini DR 领先 Perplexity**。根源在于任务分布（Perplexity 真实日志导出的多实体宽表搜集 vs 博士级长文分析）与被测接口不对等（Perplexity 生产级 Search-as-Code API vs 竞品网页预览端）。本文 §2.1/§2.5 建议文本已规避引用任何单一商业名次，仅引用跨系统一致成立的「低硬 F1 与部分证据支持瓶颈」。
