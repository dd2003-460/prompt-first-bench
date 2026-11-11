# T-PR-15 阶段 02：信息调研（证据台账）

- 上游：`loop-artifacts/stages/01/T-PR-15-01-goal-decomposition.md`
- 通道：`fetch_page`（arxiv.org / ar5iv / deepmind blog，全部可用）+ `web_search`（可用，仅返回片段）
- 不可用：bash curl 出网（白名单）、任何本机 LLM endpoint
- 产出：`research/text-objective-goodhart-survey.md` §2-§6、`research/search-log-text-objective.json`

## 1. 证据台账（按子问题）

| 子问题 | 关键主张 | 一手证据 | 证据层级 | 反证/边界 |
|---|---|---|---|---|
| Q1 | Goodhart 有 4 类机制，是比另两者更宽的伞 | 1803.04585 §2-§3；2209.13085 §3 的伞式引用 | ① 全文 | 有文献把 spec gaming 当更一般项（ai-safety-atlas，③）；"最一般"无统一定义 |
| Q1 | spec gaming 无客观判据（依赖意图） | Krakovna 2020 原文 "no objective way to distinguish" | ① 全文 | — |
| Q1 | reward hacking 需 r_true/r_proxy 两函数，判据可形式化 | 2209.13085 hackability 定义 | ① 全文 | 只适用 MDP 内，不能直接套 prompt 场景 |
| Q2-a | 重复列表攻击可翻转 judge 判定 | 2306.05685 Table 3：91.3%/91.3%/8.7% | ① 全文（表格） | GPT-4 仅 8.7% → 强模型抗性存在 |
| Q2-a | 长度偏置可回归校正 | 2404.04475：Spearman 0.94→0.98 | ① 全文 | 校正的是长度一个中介，非全部偏置 |
| Q2-b | 关键词 stuffing 可骗相关性判定 | Alaofi 2024（SIGIR-AP）经 2602.17170 + 2503.19092 转述 | ③ 二手×2 | 一手原文未取 → `[待核验-原文]` |
| Q2-c | 自评 inflation 与 self-recognition 线性相关 | 2404.13076 §1：73.5%、>90%、线性相关 | ① 全文 | 任务是摘要，外推到"分解质量"有跳跃 |
| Q2-d | PM 偏好 sycophantic 回答 | 2310.13548 §1/§4 | ① 全文 | 同文亦报告部分 sycophancy 随优化下降 |
| Q2-d | 弱 verifier 的假阳性被定向搜出 | 2605.12474：FP 10.3%/19.8% → exploitation 39→65%/63→75% | ① 全文 | 预印本 |
| Q2-e | 改写可绕过 n-gram 并抬高分数 | 2311.04850：MMLU 45.3→88.5 | ① 片段 | 需训练侧污染，prompt 场景不直接适用 |
| Q3-A | 解释错位有机制无实验 | 2201.03544 的 incorrect ontology；1803.04585 的近似 | ① 全文 | 无对照实验 → 弱 |
| Q3-B | 省略约束导致排序反转（可证） | 2209.13085 清洁机器人反例 | ① 全文 | 是 MDP 结论，需类推 |
| Q3-B | 强 verifier 也救不了未写清的 rubric | 2605.12474 §4 | ① 全文 | 预印本；rubric 域为医疗/科学 |
| Q3-C | 代理优化到崩，有标度律 | 2210.10760 两条函数形式 | ① 全文 | 合成 gold RM，非人类真值 |
| Q3-C | recall-only 奖励导致变长/不必要内容 | 2610.33512 §1 | ① 全文 | 预印本 |
| Q4 | 6/9 手段可在 prompt/判据层实施 | 见 survey §5 表 | ① 为主 | 无一条能"消除"hack（Skalse 的结构性论证） |
| Q5 | pfb rubric 4/6 维是计数型 proxy | score.py/gates.py（② 层源码） | ② 本地 | 未做对抗实测 |

## 2. 来源分级统计

- 外部 31 条：`full` 15、`partial` 8、`abstract` 5、`secondary` 1、其余为二次引用计数（见 search-log）。
- 本地 ② 层 4 条：v17 诊断、self-judge survey、score.py+gates.py、rubric-v3.1 冻结文档。
- ③ 层（未取原文）：Alaofi 2024 原文。

## 3. 通道故障与处置（不得静默跳过）

| 通道 | 实测 | 处置 |
|---|---|---|
| `curl export.arxiv.org` | 返回空（白名单外） | 改用 `fetch_page` 逐条开 abs/html 页面确认标题作者 |
| 本机 LLM endpoint `127.0.0.1:8787` | `Errno 111 Connection refused` | AC8 记 `not_satisfied`，交付脚本+设计，交 Lead 本机补跑 |
| `web_search` 全文 | 只返回摘要+片段 | 标 `partial`，不当作 full 计数 |

## 4. 本阶段新增的、任务书没预设的发现

1. **recall-only 奖励的 hack 有名字也有解法**：2610.33512 把"rubric 覆盖度=recall"导致的变长/不必要内容直接称为 reward hacking，并用 F_β 精度项修复；这与 v17 的 S_α 数学同构，比任务书预期的"information-gain trap"更贴。
2. **pfb 自身 rubric 的 M3（hedge 词计数）是最脆弱的单点**：一个正则计数就能被"插入 hedge 词"抬高，且与判者噪声无关。
3. **"文字 vs 数值"这个二分本身可能设错**：C3/C4 两条反证把结论口径改成"可操纵接口数 × 优化压力"（见 02.5）。
