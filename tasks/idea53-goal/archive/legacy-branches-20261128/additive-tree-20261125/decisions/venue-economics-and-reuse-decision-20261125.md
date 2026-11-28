# 顶会成本、前置工作复用与后续投稿路径决策（2026-11-25）

> 触发：用户质疑先前 arena 报告中「投稿发表全程 0 元、只花注册/差旅」的成本估计，
> 并追问「前置工作能否自引/继续」「有实验+verify/judge 后投什么」。
> 本文件只新增判断，不改 `submission/` 或任何投稿文件。
> 所有数字/政策均带来源；2027 未公布项明确标「未公布」，不编造。

---

## 一、会议 vs 期刊：你低估的是什么，没低估的是什么

### 1. 顶会不是「开会顺带收录」，在 AI/CS 它就是主出版渠道

CRA 2025 年《Unique Considerations for Evaluating Computing Researchers》原文：

> "Rigorously peer-reviewed conferences are the primary publication venue for computing research. Conference publication is prestigious, generally very competitive (e.g., acceptance rates less than 20%), and on par with or preferred to journals."

来源：https://cra.org/wp-content/uploads/2025/07/Unique-Considerations-for-Evaluating-Computing-Researchers.pdf

所以「顶会 = 组织会议 + 收录投稿」这句话只对了一半：它是**审稿 + proceedings 出版**，会议只是叠加在出版上的展示环节。在 AI/ML，主会（NeurIPS / ICML / ICLR）含金量不低于多数期刊；**workshop 则明显低一档**，不能混为一谈。

### 2. 「必须过来参加」分会议，差别很大

| 会议 | 论文被录用后是否必须到场 | 原文依据 |
|---|---|---|
| **NeurIPS** | **是**。至少一位作者主会注册并现场 present，virtual pass 不够；无人能去须找人代讲；否则保留撤稿权 | https://neurips.cc/FAQ/AuthorRegistration ; https://neurips.cc/Conferences/2026/PosterInstructions |
| **ICML** | **否（可只出虚拟票）**。presented 论文要线下注册；**accepted but not presented = proceedings-only，虚拟票即可** | https://icml.cc/FAQ/Author-Registration |
| **ICLR workshop** | workshop 本身线下办，但组织者必须为无法到场者提供内容访问（录像/网页/短稿）；存档状态由各 workshop 自定 | https://iclr.cc/Conferences/2026/WorkshopGuide |

**结论**：不是所有顶会都强制差旅。NeurIPS 强制；ICML 可走 proceedings-only 省掉差旅。

### 3. 费用：投稿/出版 0 元，但注册和差旅是两笔不同的钱

- 投稿、proceedings 收录、arXiv 均无 APC/版面费。
- **注册费真实存在**。NeurIPS 2026 官方价格页为动态渲染，第三方从官方计算器读出的美元数（标注为二手读取，2027 未公布）：
  - 学生主会 $285 早鸟 / $335 晚期；学术 $500 / $550；工业 $650 / $700。
  - 学生 workshop-only $230 / $280（Sydney），Atlanta $150 / $190；虚拟票学生 $50、学术 $200。
  - 来源：https://scientificfigure.com/zh/blog/neurips-poster-guidelines （官方页：https://neurips.cc/Conferences/2026/Pricing ）
- **waiver 只覆盖注册 + 住宿，明确不覆盖差旅**：
  - NeurIPS 2026 Financial Assistance 原文："Financial Assistance only covers registration and accommodation fees." / "Flights, trains, local transportation, meals, per diem... are not reimbursed." / 最多 7 晚预付酒店；覆盖所有 tracks，workshop 作者可申请，不保证获批。
  - ICML 2026 Financial Aid：注册 + 7 晚酒店，**"We are unable to provide travel support"**。
  - 来源：https://neurips.cc/Conferences/2026/FinancialAssistance ; https://icml.cc/Conferences/2026/FinancialAid

**修正先前判断**：「投稿发表 0 元」成立；「只花注册/差旅」也对，但**waiver 救不了差旅**。之前引用的 workshop-only €130–300 量级对 NeurIPS 2026 学生档大致成立，但主会学术档实际 $500–550，差旅另算。

### 4. 持久性：不是「会不会消失」，而是「以什么形态留下」

- 两者都永久存档可引用（NeurIPS proceedings / PMLR / OpenReview / JMLR-TMLR），不存在会议论文会消失的问题。
- 差别在形态：会议是**固定页数的时点快照**；期刊有卷期/ISSN、可变长度，TMLR 明文允许发表后加 "Post-Publication Changes" 小节并记录完整修订历史。
- J2C 特别提醒：期刊论文去顶会做 poster **不进会议 proceedings**，只是展示机会。
  - 来源：https://iclr.cc/public/JournalToConference

**会议相对期刊的真实劣势**不是含金量，而是：① 时间/页数刚性；② NeurIPS 强制到场；③ 后续扩展受 dual-submission 约束；④ 存档版不可再修订。
**期刊相对会议的真实劣势**：周期更长；TMLR 不在 AAAI 2027 journal track 名单里（官方名单只有 AIJ / JAIR / JMLR / AAMAS / MLJ / DMKD / CL / IJCV / IJRR / IEEE T-RO / ACM TEAC / Nature），且不在 CCF AI 列表（第三方整理，未核官方）；TMLR 去三大会只靠约 10% 的 certification 名额。
  - AAAI 2027 Journal Track：https://aaai.org/?p=96324 （截稿 2026-10-30，现已过）

---

## 二、前置工作能否自己引用、继续做：能，但分三种状态

**总原则：「引用」永远可以；「复用文字/图/结果」受政策约束。**

| 前置形态 | 能否引用 | 能否在新稿复用内容 | 政策依据 |
|---|---|---|---|
| **arXiv 预印本** | 可以，且**必须**当 prior work 引用 | 可以；TMLR 明文允许与 arXiv 重叠 | NeurIPS 2026："We do not distinguish arxiv papers and other published papers"；"nonanonymized preprint alone is not a violation"，但 "Any paper that influenced the submission... must be cited"；TMLR editorial policies |
| **明确 non-archival 的 workshop** | 可以 | 可以；TMLR 与 NeurIPS 都明文豁免 | TMLR："acceptable... if shared at venues... publicly declared, in writing, to be non-archival"；NeurIPS："dual submissions to nonarchival workshops are permitted"；ICML 双投指南："Virtually all workshop submissions are ICML-compatible" |
| **archival workshop（有 proceedings）** | 可以引用 | **TMLR 禁止**复用文字/图/结果；主会视为 prior work，需实质新增，否则增量过薄被拒 | TMLR editorial policies；NeurIPS 2026 Main Track Handbook；ICML 双投指南明确 "long running series with reviewed submission... archival status... considered a conference" |

双盲下的自引写法：ICLR 要求相关 arXiv 自引用**第三人称**；NeurIPS 旧指南同样要求匿名化（"Author et al." 而非 "our previous work"）。

**对 #53 的直接操作建议**：
1. 现有 GitHub hash 时间戳（eb1b0598c 早于 718394ece）只锁优先级，不等于学界认可的公开时间戳；补一个 arXiv 版本更稳。
2. 投 workshop **前必须查该 workshop 的 archival status**（ICLR workshop guide 要求组织者明示）；只投 non-archival 的，否则堵死后续 TMLR。
3. `manuscript-scoped/paper-zh.md` 是内部梳理稿，不外发、不挂公开仓库，不构成 prior art。

---

## 三、有实验 + 可靠 verify/judge 流程 + 完整结论后，投什么

### 首选：TMLR（Transactions on Machine Learning Research）

- **为什么匹配**：官方定位 "technical correctness over subjective significance"；验收标准明文写着 **"Papers should be accepted if they meet the criteria, even if the contribution or significance of the work is modest"**；同时拒绝 "bold statements unsupported by empirical or rigorous evidence" 和 "incorrectly claim novelty"。这与「前置工作 + 不 overclaim + 精确零负控制」的定位几乎逐字对齐。
- 成本：0 版面费、0 参会要求、rolling 投稿、无固定页数、双盲开放评审。
- 隐藏门槛：**不接受与作者此前 archival 工作的文字/图/结果复用**——所以 workshop 必须 non-archival。
- 上行路径：拿 J2C / Featured / Outstanding certification（TMLR 估计约 10% 的录用论文）后，可在 NeurIPS/ICML/ICLR 联合 J2C track 做 poster，**不再评审、不进会议 proceedings、容量 150/会、两年窗口**。ICLR 2027 申请截止 2026-12-18（已公布）；2028 未公布。
  - 来源：https://jmlr.org/tmlr/editorial-policies.html ; https://iclr.cc/public/JournalToConference ; https://blog.tmlr.org/2025/tmlr-joins-neurips-icml-iclr-journal-to-conference-track

### 次选：NeurIPS 2027 Evaluations & Datasets（原 D&B）

- 有 verify/judge 流程和完整实验后，形态更像 evaluation 贡献；2026 年该 track 已是正式 track（有独立 abstract/full paper 截止）。
- 代价：**至少一位作者必须线下到场**；通常要放 code/data artifact。
- 2027 CFP/截稿/费用**未公布**，不得编造；按 2026 节奏约 5 月初，只作规划参考。

### 第三：ICML 2027 主会

- 优势：可走 **proceedings-only，虚拟票即可**，省掉差旅——这是它相对 NeurIPS 的结构性优势。
- 2027 截稿约 1 月（arena 估计，未官方确认）；竞争强度高于 workshop 一档。

### 其他

- **ICLR 2028 主会**：实验足够强、能支撑比现在更硬的 claim 时再考虑；ICLR 2027 主会截稿（2026-09-24）已过。
- **JMLR**：理论完全成熟后的目标；J2C 资格不需 certification，但门槛与周期显著更高。
- **AAAI 2027 Journal Track**：TMLR 不在名单内；且 2026-10-30 已截止，本轮不可用。
- **workshop**：只作为拿反馈的入口，且只投 non-archival；不能当作「先发表再扩投」的跳板。

### 决策（按优先级）

1. 先补 arXiv 公开时间戳；中文版留内部。
2. workshop 只投明确 non-archival 的（ICLR 2027 窗口）。
3. 实验 + verify/judge + 完整结论齐备后，**主投 TMLR**；这是成本、门槛、定位三项同时最优的路径。
4. 需要会议曝光时走 TMLR 的 J2C certification 或 ICML proceedings-only；**不为 NeurIPS 主会预算差旅**，除非确实有人能到场。
5. 不要把 archival workshop 稿原样扩投 TMLR 或主会——这是唯一会真正堵死路径的操作。

---

## 未验证 / 待复核

- NeurIPS 2027、ICML 2027 的 CFP、截稿、注册费与 waiver：未公布。
- NeurIPS 2026 注册金额来自第三方读取官方计算器（官方页面动态渲染），以官方付款页为准。
- TMLR 不在 CCF AI 列表：第三方整理，未核 CCF 官方文件；如涉及单位考核须自行复核。
