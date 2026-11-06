# T29 — 组合空白全面验证 + NoPUA 可应用性 + 伪独立判据

> 任务卡：`tasks/T29-blank-and-nopua.md`（派发 2026-11-07）｜不跑实验，纯调研
> 一句话结论：**部分空白**。四个组件各自都有占位者，但没有任何工作把它们串成"分解前质检门 → 失败回退 → 留占位 → 跨阶段回填 → 回填后复检"的闭环。最空的不是四个组件，而是**"占位"作为一等工件**与**回填后必须复检**这两条约束。

---

## 0. 先自我修正：T28 的"完全空白"作废

T28 的空白结论基于 10 条来源的浅层核对。本轮加了两条硬手段后，结论必须收窄：

1. **引用图**（OpenAlex `filter=cites:`）：ADaPT 有 **65** 篇引用者，AOP 有 **19** 篇，STaD **0** 篇。
2. **平台从 1 个扩到 5 个**（OpenAlex / DBLP / GitHub code search / web_search 聚合 / arXiv 直读；S2 失效）。

结果：**AOP 与 STaD 各自占掉了组合里的一整块**（完备性检查 / 重建覆盖率），因此"完全空白"不成立。成璐的直觉（"总感觉不是空白"）成立。本文件 §1.3 的重叠度表取代 T28 §1 的定性判断。

---

## 1. §1 空白验证

### 1.1 搜索覆盖（实际跑了什么、没跑成什么）

| 组 | 关键词 | 主用平台 | 结果 |
|---|---|---|---|
| A | "completeness check" + task decomposition + LLM | OpenAlex / web_search | 命中集中在中日工程博客与 AOP 线；学术侧无"分解后逐要素查漏"的独立方法名 |
| B | redundancy / non-redundancy + subtask | OpenAlex / web_search | AOP 的 non-redundancy 原则是唯一形式化入口；其余是去重工程实践 |
| C | placeholder / unknown slot / fill-in-later + planning | web_search / GitHub | **无学术命中**；命中的是 prompt 模板里的 `{placeholder}` 变量（同形不同义，见 §1.3 注） |
| D | adaptive re-decomposition / backtrack / retry + failure | OpenAlex（ADaPT 引用图） | 命中密集（ADaPT/WriteHERE/Magentic-One/RAO 候选），是四组件中最"拥挤"的一环 |
| E | coverage + decomposition quality + scaffold | OpenAlex | 命中 STaD（重建覆盖率）与工程侧"覆盖度评估"实践 |
| F | element matching / requirement traceability + subtask | web_search | **命中质量最高的一组**：需求追溯领域已有"要素×子任务一对多匹配"的实证口径 |
| G | 中文：分解 完备性 检查 大模型 / 递归分解 回退 占位 | web_search | 命中全部为博客/教材/公众号（CSDN、博客园、个人书稿），无同行评审工作 |

**平台实况（含失败）**

- **P1 OpenAlex**：主力。`search` + `filter=cites:` 双通道，引用图完整、可复现。
- **P2 DBLP**（`search/publ/api`）：标题级共现 `task decomposition completeness agent` = **0 命中**；`task decomposition agent` = 37；`decomposition completeness` = 12 且首位是数学论文（functional completeness）→ 说明**标题级检索对"组合"不敏感，只能当排除性证据**，不能当"不存在"的证明。
- **P3 GitHub code search**：`"coverage" "subtask" "placeholder" agent` = 28,224 个文件命中；`completeness check subtask decomposition LLM` = 11,856 → **不可判别**，噪声主导。代码层因此改用"方法名直读"：读 `archiki/ADaPT`、`sungeunan-ibm/task-scaffolding`、`wuji-labs/nopua` 三个仓的真实文件。
- **P4 arXiv 直读 + web_search 聚合**：覆盖 abs / HTML 全文 / ACL Anthology / CJR / 中文技术站。
- **P5 Semantic Scholar Graph API**：**失效**。先 429，等待 25s 后 `arXiv:2311.05772/citations` 返回 HTTP 500，未取得任何数据 → 引用追踪改由 OpenAlex 承担。
- **未覆盖**：Google Scholar（无 API，ego-browser 不可用）、Papers with Code（服务已下线）。

### 1.2 引用追踪（必做项：谁引了 ADaPT / AOP / STaD，又加了什么）

| 被引 | 引用数 | 引用者里真正"加了东西"的 | 加了什么 |
|---|---|---|---|
| ADaPT 2311.05772 | 65 | **WriteHERE**（2503.08275, EMNLP 2025） | 把"执行失败才继续分解"换成"按任务类型决定是否继续分解"，并引入 retrieval/reasoning/composition 异构任务类型 → **直接冲击我们"失败触发回退"的假设**：分解终止条件可以不是失败 |
| AOP 2410.02189 | 19 | **无** | 19 篇全是应用型（销售、岩土设计、教育、MCP 检索），**没有一篇改进 detector 本身** → AOP 的"完备性检查"是孤儿贡献：对我方是空位，但"没人跟"本身是警告（可能不够有用，或实现成本过高） |
| STaD 2604.18177 | 0 | — | "reconstruction coverage" 尚未被任何工作复用（2026-04 预印本，属正常） |

### 1.3 重叠度评估表（每篇均已读 abstract + method 节，不凭标题判断）

组件：① 正交完备检查 ② 失败回退 ③ 占位留空 ④ 调研后填充

| # | 工作 | ① | ② | ③ | ④ | 一句话理由 |
|---|---|---|---|---|---|---|
| 1 | **ADaPT** 2311.05772（NAACL 2024 Findings） | 无 | **有** | 无 | 无 | 执行器自报失败 → planner 递归再分解，深度上限单调升；但 planner 从不检查切分是否完备/重叠，失败信号只有模型自写的 `task completed/failed` |
| 2 | **AOP** 2410.02189（ICLR 2025） | **有（强）** | 部分 | 无 | 无 | detector 抽要素→逐条匹配→查未预见依赖，0.822→0.969；配 reward model + replan 反馈环。但 replan 只重拆"被判不完备的子任务"，不回退到上一层；且 detector 结尾"若无需修改即返回通过"是默认通过偏置 |
| 3 | **STaD** 2604.18177 | **有（离线）** | 无 | 无 | 无 | coverage = 遮住原题只给中间步骤能否复现最终答案（ToT 99.09% / GSM8K 87.52%），判等为 LLM 0/1；这是**评估指标**，不在生成回路里，且 0 引用 |
| 4 | **WriteHERE** 2503.08275（EMNLP 2025） | 无 | 部分 | 无 | 部分 | 异构递归规划 + DAG 状态调度 = 计划级"动态重规划"；终止靠任务类型不靠失败；无切分质量检查，无占位工件（pending 只是调度状态） |
| 5 | **WebWeaver** 2509.13312 | 无 | 无 | **有（隐式）** | **有（强）** | outline 节点内嵌 citation ID、writer 逐节从 memory bank 取证据回填——**这是"占位→调研→填充"最接近的实现**；但占位不是一等对象（是 outline 的副产物），且不回查完备性 |
| 6 | **需求追溯** 2506.16440 | **有（口径）** | 无 | 无 | 无 | 给的是"要素×子任务"匹配的口径与实证：一对多 framing 决定 recall，naive many-to-many 仅 ~5% F1（枚举偏置）→ 直接决定我们"承接表"该怎么问 |
| 7 | **Magentic-One**（AutoGen） | 无 | **有（计划级）** | 部分 | 无 | Task Ledger / Progress Ledger 双账本 + stall 计数触发 outer-loop 重规划；"educated guesses" 承认未知但**不阻断**，不是"留空待回填" |
| 8 | **中文工程实践**（书稿第10章 Planning 模式 / CSDN MECE 校验） | 部分 | 无 | 无 | 部分 | 已有"覆盖度评估→补查询→再综合"循环与 MECE 校验 prompt（互斥/完备/原子三问）；非同行评审，工程直觉与我们的组合高度重合 → **说明想法在实践层已经在空中** |

> 注：关键词 C 在 GitHub 上的大量命中是 `{placeholder}` 模板变量，与"留占位待回填"语义无关，按同形不同义排除。

### 1.4 结论（三选一）

**部分空白。**

**已被占（谁占了哪块）**

- ① 正交完备检查：**AOP**（分配前 detector，最强）、**STaD**（离线重建覆盖率）、**需求追溯**（要素×子任务一对多口径）；
- ② 失败回退：**ADaPT**（执行失败→递归再分解）、**Magentic-One**（stall→重规划）、WriteHERE（类型驱动重规划）；
- ④ 调研后填充：**WebWeaver**（citation-grounded outline→逐节回填）、STORM 线、WriteHERE。

**仍然空（精确位置，三条）**

- **(a) ③ 占位作为一等工件**：没有任何工作把"未知项"写成带三字段（未知什么 / 为什么未知 / 回填触发条件）的结构化对象。WebWeaver 最接近，但它的槽位是 outline 节点 + citation ID，未知性没有被显式承认。
- **(b) 回填后复检**：AOP 只在分配前查一次，STaD 只在评估时查一次，WebWeaver 根本不回查。**"填充完成后重跑同一个完备性检查"这个动作，一篇都没有。**
- **(c) 失败信号接到占位**：ADaPT 的失败→重试/再分解，T28 的"第 3 次降级占位"是唯一已知连接，而 ADaPT 没有占位概念。**"失败不是继续拆，而是承认这里是未知"这个转向，未见先例。**

**最接近整组合的一篇**：WebWeaver（2509.13312）——差在无质检门、无回退、无复检；次近 AOP——差在无占位、无回填、detector 默认通过。

→ 对 pfb 的含义：**不要宣称"首创组合"**，应宣称"把三个已有零件串成带复检的闭环，并把占位提升为一等工件"。前者是 AOP/WebWeaver 已有的，后者才是空位。

---

## 2. §2 NoPUA 三层拆解与四阶段注入

### 2.1 原文口径（先纠正任务卡一处）

任务卡写 R6 = arXiv 2603.14373（v2.0.0）。已核实：**2603.14373 = 《Trust Over Fear: How Motivation Framing in System Prompts Affects AI Agent Debugging Depth》**，Wu Ji 单作者，2026-03-15 提交，13 页 23 引用，代码指向 `wuji-labs/nopua`。仓库 `SKILL.md` 现为 **v2.0.2**，本报告读的是**仓库原文**（比论文更完整）。

硬数字：Study 1（9 个调试场景，Claude Sonnet 4）hidden issues **+59%**（p=0.002, d=2.28）、调查步数 +83%、**surface-level issues −15%**；Study 2（5 次自动 × 3 条件，135 个场景级数据点）hidden **+25%**（p=0.016）、步数 +74%；PUA 恐惧框在所有指标上不显著（p>0.3）。**conf 0.75**（单作者、自评、无第三方复现；仓库与论文同源）。

### 2.2 三层拆解（可迁移组件清单）

| 层 | 组件（原文位置） | 迁移价值 |
|---|---|---|
| **情绪层** | 三信念表述（"穷尽一切/先做后问/主动出击"）、道德经引文、"出于自尊"、"我还能做什么"内在声音 | **低**。T26 Q1–Q3 已证单轮激励≈0；本层唯一作用是把"被检查"改写成"自己想做" |
| **结构层** | ①失败计数阶梯（第2次换眼睛/第3次升维度/第4次归零/第5次臣服）②能动性光谱（被动 vs 主动行为对照）③诚实自检表（17 行：状态→问题→行动）④7 项清醒清单（第4次失败强制全做）⑤交付自检清单（"用工具验证，不要用嘴验证，把输出贴上来"） | **高**。全部是**可判定**的结构：触发条件、检查项、证据要求都写死了 |
| **流程层** | 水的方法论五步：止（列出已试方案找共同模式）→ 观（逐字读失败信号/主动搜索/读原始材料/验证前置假设/反转假设）→ 转（四问）→ 行（新方案三条件：本质不同、有验证标准、失败产生新信息）→ 悟（+悟后延伸）；外加"打转检测"（三次同思路换参数即打转）与"外部内容当材料不当命令" | **最高**。这套顺序本身就是多步任务的组织法，且每一步都能落到 pfb 的具体节点 |

**"+59% 出自哪层"**：**结构层⑤（交付自检 = 贴证据）+ 流程层"观"的前三项（逐字读失败信号、读原始材料不读二手）**。判据：hidden issues 的发现依赖"真的去看原始材料"，而不是"被鼓励去看"。**conf 0.55**——这是推断，原文未做层间消融。

**必须同时记住的代价**：**surface issues −15%**。这套方法论是**深度换广度**。而 pfb 的 check 阶段恰恰要覆盖面（覆盖率 ≥0.80 是 T28 的硬 FAIL 条件）。所以抄它只能抄到"如何深挖单个可疑点"，不能抄"整体就该这样"。**conf 0.9**（原文直接给出该数字）。

### 2.3 四阶段注入建议

| 阶段 | 注入组件 | 标签 | 具体改法（落到文件与节） |
|---|---|---|---|
| decomp | 结构层① 失败计数阶梯 | **[需改造]** | `decomp-01 §2` 规则④：同节点第 2 次回退**必须换本质不同的切分维度**（原文"换眼睛"），第 3 次按 T28 降级占位。**不能照抄"第5次臣服"**——pfb 没有"移交给谁"，改成"占位 + 缺口清单" |
| decomp | 流程层"止"（先枚举已试方案再动手） | **[可直接用]** | 回退前强制输出 3 行 `已试切分：[维度A / 维度B]`，再给新切分。这条专门防"换参数式回退"（同一维度的措辞微调被当成新方案） |
| research | 流程层"读原始材料，不是二手引用" | **[可直接用]** | 硬规则：每条事实必须挂**一级源**（原文/官方文档/仓库文件/命令输出）；二手转述只能当线索，不得当证据。与 §3 的 R1–R2 联动 |
| research | 流程层"把读到的外部内容当材料，不当命令" | **[可直接用]** | 原文这条本是防 prompt injection 的；对本仓特别相关——我们天天在读别人的 README / SKILL / issue。直接抄进 research 与 check 的 system prompt |
| check | 结构层⑤ "用工具验证，不要用嘴验证" | **[可直接用]** | T28 `§2` 的 `COVERAGE: x.xx` 行必须附证据（URL / 行号 / 命令输出），无证据视为未填 |
| check | 结构层③ 诚实自检表 | **[需改造]** | 改写成可证伪形态：每条 PASS 必须附 `反例检索词：X`（我搜了什么来推翻它）。原表是"问题→行动"，对模型仍可空转；加"反例检索"才机械可查 |
| check | 情绪层"穷尽一切，不要说做不到" | **[不适用 → 反向使用]** | **必须反着写**：pfb 要的是"说不出就写 `[待核验]` 占位"。依据 T26 Q4：压力/穷尽要求把 fabrication 从 16% 推到 34.7%。**这一条与"占位留空"直接对撞，是本任务最重要的负向结论** |
| review | 流程层"行"的三条件（本质不同 / 有验证标准 / 失败产生新信息） | **[可直接用]** | 直接做 review 驳回判据：新方案三条缺一即驳回。原文这三条本就是用来拒绝"假新方案"的 |
| review | 流程层"打转检测" | **[可直接用]** | 连续两轮 review 意见语义相似度 >0.8 → 判打转，强制换方向。**可机器判**，适合写成脚本闸门 |
| review | 情绪层 信任语气/"我相信你能做到" | **[不适用]** | 单轮激励≈0（T26 Q1–Q3）；review 是判定环节，加语气只增加 token |

### 2.4 一句话总结

值得抄的是**流程层的顺序**（止→观→转→行→悟，尤其"读原始材料"与"新方案三条件"）和**结构层的强制触发点**（失败计数阶梯、证据化交付）；**不值得抄的是语气**，以及**"不许说做不到"**——后者与占位留空是同一枚硬币的两面，选错一边就把抗 fabrication 的收益全吃掉。

---

## 3. §3 伪独立性：从"找两个不同网站"到可执行判据

成璐的原话担忧：很多媒体重复转载，像人体蜈蚣。三组文献说明这不是隐喻，而是**可测量**的现象。

### 3.1 三组文献（各给一条可迁移动作）

**A. 新闻转载链（媒体侧）**——Silverman 2015（Tow Center，2014-08~12，1,500+ 篇文章 / 100+ 谣言）：新闻站点把别家报道当证据，而别家又只引别家；**沿链接链追到源头，往往只是一条社交媒体帖或一个薄弱来源**。量化：仅约 36% 的媒体在谣言被证伪后回访更新；13 家报道某claim 的媒体里只有 1 家去查了真伪。可迁移动作：**追问 the original source，而不是追问"还有谁在说"**。conf 0.85（报告非同行评审，但数据与方法是公开的）

**B. 引用制图（学术侧）**——Fister/Fister/Perc 2016（Frontiers in Physics 4:49）：用社区检测找"互引密度显著高于同学科基线"的作者群；Kojaku/Livan/Masuda 2021（Sci Rep 11）：用"异常引用组"检测期刊级操纵。可迁移判据：**独立性不是看两篇是否不同，而是看它们的引用邻域是否异常重叠**。conf 0.8

**C. 训练数据去重（语料侧）**——Lee et al. 2022（2107.06499）：exact-substring + near-dup 去重显著降低记忆化；DCLM（2406.11794）：240T token 流水线里 dedup 是标准步骤；SimHash（Manku et al., WWW 2007）给的是 Web 规模的 near-duplicate 指纹法。可迁移判据：**相似度必须在固定阈值上机械判定，不能靠"看起来不一样"**。conf 0.85

### 3.2 可执行判据 R1–R7

| 编号 | 判据 | 怎么判（机械动作） | 命中后处置 |
|---|---|---|---|
| **R1** | 同源域 | 取两来源的最上层可注册域（eTLD+1）；相同即非独立。跨域但同一发布主体（同机构子域、同一 publisher 字段）→ 判"疑似" | 判非独立 / 疑似，降级计数 |
| **R2** | 上游收敛 | 各自抽"它说它从哪知道的"（attribution 字段：引用的推文/新闻稿/repo/论文）；交集非空 → 非独立。等价于 Silverman 的"沿链追到 first source" | 计 1 个证据，记 `同源(R2)` |
| **R3** | 内容包含 + 时序 | A 早于 B 且 B 正文近似包含 A 关键句（5-gram Jaccard ≥0.5 或 SimHash 汉明距 ≤3）→ B 依赖 A | B 不计入独立证据 |
| **R4** | 引用邻域密度 | 两来源共引/共被引集合 Jaccard 高于同领域基线 → 疑似同一引用共同体 | 标"疑似"，要求补一个圈外源 |
| **R5** | 数字指纹 | 两来源的关键数字/日期/单位完全一致，且**都无原始出处** → 典型转载指纹（这条最实用，成本最低） | 判非独立，标 `数字同源待溯` |
| **R6** | 独立复现门槛 | **来源数 ≠ 证据数**：R1–R5 全通过才计数 +1，否则不计数 | 报告必须分开写 `引用条数 5 / 独立证据数 2`；差额即蜈蚣长度 |
| **R7** | 冲突处置 | 独立来源互相矛盾时**禁止取多数**（多数可能是转载链） | 写 `[冲突: A 说 x / B 说 y / 缺裁断依据]` 并降级为占位 |

### 3.3 写进 prompt 的形态

1. research 阶段每条事实尾部附 `独立性: 独立 / 同源(R编号) / 未知`；"未知"不计分。
2. check 阶段把 `独立证据数` 与 `引用条数` 分列输出，差额超过一半即触发"补圈外源"动作。
3. 与 T28 规则③（以事实为准）衔接：**若穷尽搜索后公开数据只有同源来源，这不是模型缺陷**——写 `[待核验: 公开数据仅同源]` 占位，不编第二来源。这与 decomp-01 §2 的修正一致。

---

## 4. 给下一张任务卡的落地清单

1. `decomp-01 §2`：回退时强制输出"已试切分清单"，且必须换维度（NoPUA 流程层"止"+ 结构层①）。
2. `decomp-01 §2` 规则④改写：第 3 次失败 → 产出**占位工件三字段**（未知什么 / 为什么未知 / 回填触发条件）——这是 §1.4(a) 的空位。
3. 新增 check 段动作：**回填后复检**（重跑覆盖图；覆盖图无变化不允许 PASS）——这是 §1.4(b) 的空位。
4. research 段加入 §3.2 的 R1/R2/R5 与"独立证据数"字段。
5. 明文禁止把 NoPUA 的"穷尽一切"语气带入 check（§2.3 最后一条）。

---

## 5. 来源表

| # | 类型 | 标题 | URL | conf | 读到层级 |
|---|---|---|---|---|---|
| S1 | arXiv | ADaPT: As-Needed Decomposition and Planning with Language Models（NAACL 2024 Findings） | https://arxiv.org/abs/2311.05772 | 0.95 | 全文 + 官方 prompt 文件 |
| S2 | arXiv | Agent-Oriented Planning in Multi-Agent Systems（AOP, ICLR 2025） | https://arxiv.org/abs/2410.02189 | 0.9 | abs + 方法（ICLR PDF） |
| S3 | 其他 | AOP ICLR 2025 会议全文 | https://proceedings.iclr.cc/paper_files/paper/2025/file/31610e68fe41a62e460e044216a10766-Paper-Conference.pdf | 0.9 | 方法 + 消融 |
| S4 | arXiv | STaD: Scaffolded Task Design for Identifying Compositional Skill Gaps in LLMs | https://arxiv.org/abs/2604.18177 | 0.85 | 方法 + 附录 H prompt |
| S5 | arXiv | Beyond Outlining: Heterogeneous Recursive Planning for Adaptive Long-form Writing（EMNLP 2025） | https://arxiv.org/abs/2503.08275 | 0.9 | 摘要 + 方法 4.1 |
| S6 | arXiv | WebWeaver: Structuring Web-Scale Evidence with Dynamic Outlines for Open-Ended Deep Research | https://arxiv.org/html/2509.13312v3 | 0.85 | 方法 3.1–3.2 |
| S7 | arXiv | Evaluating the Use of LLMs for Documentation to Code Traceability（要素匹配口径） | https://arxiv.org/pdf/2506.16440 | 0.8 | 结果 + 讨论（一对多 vs 多对多） |
| S8 | arXiv | Deduplicating Training Data Makes Language Models Better | https://arxiv.org/abs/2107.06499 | 0.85 | 摘要 + 去重方法 |
| S9 | arXiv | DataComp-LM (DCLM) | https://arxiv.org/abs/2406.11794 | 0.9 | abs（dedup 流水线定位） |
| S10 | arXiv | Trust Over Fear: How Motivation Framing in System Prompts Affects AI Agent Debugging Depth（= NoPUA 论文/R6） | https://arxiv.org/abs/2603.14373 | 0.85 | abs 全文数字 |
| S11 | GitHub | wuji-labs/nopua（★1404，SKILL.md v2.0.2 原文） | https://github.com/wuji-labs/nopua | 0.95 | SKILL.md 全文 + LINEAGE.md |
| S12 | GitHub | archiki/ADaPT（★95，官方实现） | https://github.com/archiki/ADaPT | 0.9 | prompts/ 目录实读 |
| S13 | GitHub | sungeunan-ibm/task-scaffolding（STaD 代码，★0） | https://github.com/sungeunan-ibm/task-scaffolding | 0.8 | 仓库树 |
| S14 | GitHub | microsoft/autogen（Magentic-One 实现所在） | https://github.com/microsoft/autogen | 0.8 | 文档描述 |
| S15 | 其他 | Silverman 2015, Lies, Damn Lies, and Viral Content（Tow Center, Columbia） | https://www.cjr.org/tow_center_reports/craig_silverman_lies_damn_lies_viral_content.php | 0.85 | 报告结论段 |
| S16 | 其他 | Fister, Fister & Perc 2016, Toward the Discovery of Citation Cartels in Citation Networks, Frontiers in Physics 4:49 | DOI 10.3389/fphy.2016.00049 | 0.85 | 二手引用（Retraction Watch 访谈 + 多篇引文一致） |
| S17 | 其他 | Kojaku, Livan & Masuda 2021, Detecting anomalous citation groups in journal networks, Sci Rep 11 | DOI 10.1038/s41598-021-93572-3 | 0.8 | 二手引用（多篇参考文献一致） |
| S18 | 其他 | Manku, Jain & Sarma 2007, Detecting Near-Duplicates for Web Crawling（WWW 2007, SimHash） | **DOI 未核，不编**；方法名可查 | 0.7 | 仅方法名 |
| S19 | 其他 | OpenAlex Graph API（引用追踪数据源：ADaPT W4401043434 / AOP W4403882551） | https://api.openalex.org/works?filter=cites:W4401043434 | 0.9 | 原始 JSON |
| S20 | 其他 | DBLP publication search API（标题级共现计数） | https://dblp.org/search/publ/api?q=task%20decomposition%20completeness%20agent&format=json | 0.9 | 原始 JSON |
| S21 | 其他 | 中文工程实践：第 10 章 Planning 模式（覆盖度评估→补查询→再综合） | https://waylandz.com/ai-agent-book/%E7%AC%AC10%E7%AB%A0-Planning%E6%A8%A1%E5%BC%8F/ | 0.6 | 书稿章节（非同行评审） |
| S22 | 其他 | 中文工程实践：Agent 任务分解与多级规划（MECE 校验 prompt） | https://blog.csdn.net/weixin_65162103/article/details/164617888 | 0.55 | 博客（非同行评审） |

统计：arXiv 10 条（S1–S10）、GitHub 4 条（S11–S14）、其他 8 条（S15–S22）→ 满足 ≥8 / arXiv≥4 / GitHub≥2 / 其他≥2。

---

## 6. 未找到 / 未验证（不编）

1. **Semantic Scholar 数据未取得**：429 → 等 25s → HTTP 500。引用追踪已由 OpenAlex 替代，但**未做跨库交叉核对**。
2. **Google Scholar 未覆盖**（无 API），**Papers with Code 已停服**。这两条是本轮搜索矩阵的真实缺口。
3. **以下 6 篇只到标题+摘要片段，method 未读 → 不入重叠度表**，列为候选供下轮读：TDAG（Neural Networks 185:107200）、Select-Then-Decompose（EMNLP 2025）、PlanGenLLMs（ACL 2025）、RAO（arXiv 2605.06639）、AutoSOTA（arXiv 2604.05550）、Auto-Eval Judge（arXiv 2508.05508）。
4. **STaD 的 coverage 由谁执行**（同模型/异族模型/人工）原文未明写 → 承 T28 标 `[未验证]`。
5. **NoPUA 的 +59% 无第三方复现**，且单作者自评、n=9 场景 → conf 0.75，不作为"已证实效应"使用。
6. **GitHub code search 无法判别"组合是否被实现"**：28,224 个文件的噪声说明该工具只能用于"按方法名找实现"，不能用于"证明无人实现"。**这一点应写进后续任务卡的方法说明，避免下一轮重复踩。**
