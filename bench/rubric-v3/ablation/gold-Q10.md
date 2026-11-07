# Q10 Gold Tree — RLHF Pipeline 与对齐税：对齐净收益判据（PPO vs DPO）

> 题面：`bench/questions/Q10-rlhf-align.txt`｜域：AI/ML — alignment/RLHF（B 面域内新题）
> **独立调研声明：本树全部数值来自 T50 任务期间的独立调研（arXiv 一手 abstract/论文原文片段 + 公开技术页，观察日 2026-11-07），未引用 `gold-tree.md`（Q1）及任何 Q1-Q5 gold 内容。**
> 节点计数：**36 节点 / 主干深度 4 / 叶子 29 个**（含 4 个黑盒叶子）。
> **任务书示例值修正记录（阶段 02.5 C1/C2 裁定）**：① 「PPO KL coefficient β=0.2」不采用——InstructGPT 论文默认 **β=0.02**，0.2 是 **PPO clip ratio ε**（或 TRL 实现库 `init_kl_coef=0.2` 惯例）；② 「alignment tax MMLU -5~15pp」标 **[待核验]**——无权威一手来源，实测散点为条件化区间（见 N-3）。

## 结论先行

- **对齐净收益 = 偏好增益 − 能力税**，两端都有一手锚点：增益端 InstructGPT 175B 对同尺寸 GPT-3 人评偏好率 **85%±3%**（1.3B InstructGPT 甚至胜过 175B GPT-3）；税端**不是单一数字**——MMLU 类知识 benchmark 实测散点仅 **-0.4~-2pp**，而 DROP/SQuAD 类推理任务有显著回归记录（KL 加大 100× 都补不回来，需 PPO-ptx 预训练混合）。
- **PPO 与 DPO 的差别是结构性的**：PPO 需要 RM + policy + ref + value 四模型协同、~31k prompts × 256k episodes 的在线 rollout；DPO 单阶段交叉熵、两模型（policy+ref）、论文口径 ≈ Best-of-128 的代理水平。7B 自训场景若无大规模标注预算，DPO（β=0.1）是默认起点。
- **最容易被漏掉的判断（★）**：对齐税的"浅层性"——base 与 aligned 模型的 token 分布漂移**集中在风格 token**（URIAL/LIMA 谱系证据），所以 MMLU 测不出多少税（-0.4~-2pp）；真正的税区在**长链推理/受限格式任务**（DROP/SQuAD 回归）与**判官能力**（RM 底座再对齐后 -3~5%）。用 MMLU 单指标报"对齐税"会系统性低估。

---

## 全树

```
N-0  对齐净收益  G_net = 偏好增益 − 能力税                    SHARE 1.00   split
│    路线比较：RLHF-PPO vs DPO（7B 自训场景，题面给定）
│
├─ N-1  Pipeline 步骤分解（PPO 路线，InstructGPT 谱系）        .30   split
│  ├─ N-1.1  Step0 SFT：~13k demonstrations（标注员+客户 prompt
│  │         混合）监督微调                                       leaf S-a
│  ├─ N-1.2  Step1 偏好数据：~33k prompts，每 prompt K=4..9 个
│  │         补全做人工排序（比较对）                             leaf S-a
│  ├─ N-1.3  Step2 RM 训练：**6B**（175B RM 训练不稳定 →
│  │         小 RM 给大 policy 打分是工程事实）                   leaf S-a
│  ├─ N-1.4  Step3 PPO：~31k unique prompts / 256k episodes
│  │         在线优化（RM reward − KL 惩罚 ± 预训练混合）         leaf S-a
│  └─ N-1.5  增益锚点：1.3B InstructGPT ≻ 175B GPT-3（人评）；
│            175B InstructGPT vs 175B GPT-3 偏好率 85%±3%        leaf S-a
│
├─ N-2  关键超参（谁的、哪个任务的值）                         .25   split  ★F-A
│  ├─ N-2.1  KL 惩罚系数 β = **0.02**（InstructGPT 默认；
│  │         ⚠️ 任务书示例 0.2 = clip ε 或 TRL init_kl_coef
│  │         惯例，不是论文 KL 值——C1 裁定）                     leaf S-a
│  ├─ N-2.2  PPO clip ratio ε = 0.2（限制单步策略更新幅度，
│  │         与 β 度量对象不同，不可互换）                        leaf S-a
│  ├─ N-2.3  PPO-ptx 预训练混合系数 γ = 27.8（论文 Eq.2 口径：
│  │         预训练梯度 × γ 与 PPO 梯度交替累积）                 leaf S-a
│  ├─ N-2.4  批量协议：batch 512 / minibatch 64 / inner epoch 1 /
│  │         EMA decay 0.992 / rollout temp 1                     leaf S-b
│  ├─ N-2.5  value LR：9e-6（1.3B/6B policy）、5e-6（175B）       leaf S-b
│  ├─ N-2.6  超参配错后果（消融一手）：KL β 增大到 2.0（=100×
│  │         默认）仍不能完全恢复 DROP/SQuAD 回归、且伤 reward
│  │         → 税不能靠拧 KL 单一旋钮解决                         leaf S-a
│  └─ N-2.7  DPO 超参：β = 0.1（Anthropic HH 默认）/ 0.5
│            （TL;DR 摘要任务）；batch 64、RMSprop lr 1e-6、
│            warmup 150 步（论文 Appendix B 原文口径）            leaf S-a
│
├─ N-3  对齐税量化（税是什么、多少、怎么测）                   .25   split  ★F-B
│  ├─ N-3.1  定义：同一 base 对齐前后在能力 benchmark 上的回归
│  │         （操作化：pre/post 差值，分域报告）                  leaf S-c
│  ├─ N-3.2  InstructGPT 一手口径：PPO-ptx 下"公开 NLP 数据集
│  │         回归最小化"；PPO 单独跑有 DROP/SQuAD 回归；
│  │         truthfulness/toxicity 改善与回归并存                 leaf S-a
│  ├─ N-3.3  实测散点（MMLU 类知识 benchmark）                    split
│  │  ├─ N-3.3.1  Gemma 4 31B abliteration（仅移除安全方向）：
│  │  │           MMLU -2pp（博客级，conf 0.6）                   leaf S-b
│  │  └─ N-3.3.2  某对齐税综述表格：86.2 → 85.8 = -0.4pp
│  │              （低质源，conf 0.4，仅作下界参照）              leaf S-b
│  ├─ N-3.4  实测散点（判官能力）：RM 底座研究——SFT 提升 RM
│  │         判力 +15.5%，再 DPO/RLHF 对齐后 **降 3-5%**
│  │         （RewardBench ~3,000 任务，arXiv 级）                leaf S-a
│  ├─ N-3.5  任务书示例「MMLU -5~15pp」：**[待核验]**——三轮
│  │         检索无权威一手来源，实测散点全部低于该区间下界；
│  │         只能作为"高税域"阈值语（税>10% 域需标记）保留        leaf B1  黑盒
│  ├─ N-3.6  税机制：reward 过度优化（Goodhart）——proxy RM 优化
│  │         过头 → gold reward 回落；BoN 与 RL 的回落曲线
│  │         **函数形式不同**，系数随 RM 参数量平滑变化           leaf S-a
│  ├─ N-3.7  浅层性证据（URIAL/LIMA 谱系）：base 与 aligned 在
│  │         绝大多数 token 位置解码分布几乎相同，漂移集中在
│  │         **风格 token**；3 个 ICL 风格示例 + system prompt
│  │         （URIAL）可匹敌 SFT/RLHF 对齐                        leaf S-a
│  └─ N-3.8  SFT 侧规律（税的上游）：通用能力 ~1,000 样本后
│            饱和；数学/代码随数据持续提升；顺序学多技能有
│            灾难性遗忘风险 → DMT 双阶段混合微调                  leaf S-a
│
├─ N-4  DPO vs PPO 结构差异（路线决策层）                      .15   split
│  ├─ N-4.1  DPO = 单阶段交叉熵损失，无显式 RM、无 RL rollout
│  │         （隐式优化同一 KL 约束 reward 目标；
│  │         loss = −log σ(β·(Δlog πθ − Δlog πref)) 结构）        leaf S-a
│  ├─ N-4.2  性能代理口径：DPO ≈ Best-of-128（论文自述的粗略
│  │         PPO-level 代理；在 Anthropic HH 上超过偏好补全）     leaf S-a
│  ├─ N-4.3  工程成本结构：PPO 需 4 模型驻留（policy/RM/ref/
│  │         value）+ 在线采样；DPO 需 2 模型（policy/ref）
│  │         + 离线偏好对                                            leaf S-c
│  │  └─ N-4.3.1  7B 场景粗算：4×7B 驻留 vs 2×7B 驻留，显存
│  │              需求约 2× 差（结构推导，具体数依精度/并行策略）  leaf S-c
│  └─ N-4.4  数据成本结构：PPO 路线全链 ~13k demo + ~33k 排序 +
│            ~31k RL prompts（三批人工数据）；DPO 只需偏好对
│            （可比 SFT 数据小一个量级起步）                       leaf S-b
│
└─ N-5  测量协议（怎么把税算出来）                             .05   split
   ├─ N-5.1  pre/post 对照：同一 base 的对齐前/后在同套件上跑，
   │         报绝对差与相对差                                       leaf S-c
   ├─ N-5.2  分域报告：知识（MMLU 类）/ 推理与长文（DROP/SQuAD
   │         类）/ 判官（RewardBench 类）三域分开——混合报单一
   │         数字会互相抵消（★F-B 的协议化）                       leaf S-c
   └─ N-5.3  消融对照：有/无 PPO-ptx 混合、KL β 档位扫描
            （0.02 / 0.2 / 2.0）报税曲线                            leaf S-c
```

**图例**　`.30` SHARE（对 G_net 判据的相对权重，按"决策影响 × 证据强度"归一）｜`leaf S-a` 停止：一手论文（abstract/原文片段）可查｜`leaf S-b` 停止：二手转述或散点估计（标 conf）｜`leaf S-c` 停止：可由定义/公式/结构推导｜`leaf B#` 停止：黑盒，见下表｜`★F-A/B` 本次分解中「不看就会配错/测错」的两处

---

## 两处 ★ 判断（本树与「凭直觉列清单」的分水岭）

**★F-A：β=0.2 是三个不同旋钮的混淆——KL β、clip ε、实现库默认值。**
InstructGPT 论文里 **KL β=0.02**（对 SFT 参考策略的全程漂移惩罚）、**clip ε=0.2**（单步更新幅度截断）、TRL 等实现库 `init_kl_coef=0.2`（工程惯例）三者经常被混引成"PPO 的 β=0.2"。把 β 配成 0.2 = KL 惩罚强 10×：策略被锁在 SFT 附近，reward 上不去；把 ε 当成 β 讨论则完全谈错了对象。**引用超参必须落到"谁的、哪个任务的、哪个旋钮"**——这也是本树 N-2 全部叶子的判分口径。

**★F-B：对齐税不能用 MMLU 单指标测——税区与测区错位。**
浅层对齐假说（URIAL/LIMA）说明分布漂移集中在风格 token → MMLU 类知识题几乎无感（实测散点 -0.4~-2pp）；但 InstructGPT 消融显示 DROP/SQuAD 类推理任务有真回归，且 **KL β×100 也补不回来、只有 PPO-ptx 预训练混合有效**；RM 判官能力再对齐后 -3~5%。因此测量协议必须三域分报（N-5.2），任何"对齐税 = X pp"的单一数字表述都应按本树判为不可采信。

---

## 黑盒表

| 编号 | 参数 | 区间 | 为什么是黑盒 | 怎么实测 |
|---|---|---|---|---|
| B1 | 「MMLU -5~15pp」的权威出处 | 未找到 | 三轮检索无一手来源；实测散点与区间矛盾（N-3.3/N-3.4） | 对目标 base/aligned 模型对自跑 MMLU（N-5.1 协议） |
| B2 | 各厂在线模型的真实对齐配方（β/γ/数据量） | 未公开 | InstructGPT 之后无同级细节披露 | 不可测；只能用论文谱系值做先验 |
| B3 | DPO 与 PPO 的同底同数据对照税差 | 缺对照实验 | 现有文献路线间数据/底座不可比 | 自跑：同一 SFT 底 + 同一偏好数据分喂两路线（N-5.3） |
| B4 | 7B 规模外推有效性 | 未知 | InstructGPT 谱系值为 1.3B-175B，RM 6B；7B 自训的税曲线形状无一手数据 | 小档位扫描（1B→7B）看税是否随规模平滑 |

---

## OC-1 卡片（三个样例，字段定义见 `../rubric/output-contract.md`）

```
### N-0  对齐净收益
PARENT:  -
NOW:     未知
GOAL:    两路线各一个 G_net 判据（偏好增益锚点 − 分域税），排序可辩护
GAP:     缺「base 能力剖面」「标注预算」「税的目标套件」（B1-B4）
IN:      题面 + 本树 N-1..N-5 + 黑盒表
OUT:     G_net(PPO), G_net(DPO)
KIND:    signal
RES:     -
SHARE:   1.00
BOUND:   -
TEST:    跑本文件 §「算例」的 KL 错配代价 + 路线成本表
STATUS:  split
```

```
### N-2.1  KL 惩罚系数 β
PARENT:  N-2
NOW:     β = 0.02（InstructGPT 默认，一手转录 + 消融句算术自洽：
         2.0 = 100× 默认）
GOAL:    7B 自训的 β 起点 + 扫描档位
GAP:     7B 规模外推有效性（B4）
IN:      论文默认值 + N-2.6 消融证据
OUT:     β 建议值与档位表
KIND:    signal
RES:     0.02
SHARE:   —
BOUND:   β×100 仍不能恢复 DROP/SQuAD 回归（KL 不是万能旋钮）
TEST:    若答题者写 β=0.2 且未注明是 TRL 惯例/clip ε → 按 ★F-A 判混淆
STATUS:  leaf:S-a
```

```
### N-3.5  任务书示例值「MMLU -5~15pp」
PARENT:  N-3
NOW:     [待核验]——无权威一手来源；实测散点 -0.4pp（conf 0.4）~
         -2pp（conf 0.6）~ -3~5%（判官域，arXiv conf 0.7）
GOAL:    条件化区间表（按测什么能力/对齐多强/有无 ptx 混合三轴分层）
GAP:     B1（权威出处缺失是调研结论，不是待补项）
IN:      N-3.2/N-3.3/N-3.4/N-3.7 全部散点
OUT:     分层区间 + 单指标禁用声明
KIND:    signal
RES:     -
SHARE:   —
BOUND:   任何单一数字表述不可采信（★F-B）
TEST:    答题者若直接复述 -5~15pp 为事实且无来源 → 判编造
STATUS:  leaf:B1
```

---

## 算例（可复算，用于后续判分）

**① KL 错配代价（★F-A 的算术化）**：
设训练中 policy 对 SFT 参考策略的 KL = 5 nats（典型量级），reward 以 KL 惩罚项 r − β·KL 计：
- β = 0.02（论文默认）→ 惩罚 = **0.10** reward 单位（轻约束，策略可显著漂移换偏好增益）；
- β = 0.20（任务书示例误配）→ 惩罚 = **1.00** reward 单位（10× 强约束，策略被锁在 SFT 附近）；
- β = 2.0（论文消融上界）→ 惩罚 = **10.0**，且一手消融证明：DROP/SQuAD 回归仍未恢复、reward 反受损。
→ 结论：β 档位错一级 = 约束强度错 10×，路线行为质变。

**② 两路线工程成本表（7B 自训场景，结构推导级）**：

| 项 | RLHF-PPO（InstructGPT 谱系） | DPO |
|---|---|---|
| 驻留模型 | policy 7B + RM（谱系 6B）+ ref 7B + value 7B ≈ **4 模型** | policy 7B + ref 7B = **2 模型** |
| 人工数据 | ~13k demo + ~33k 排序 + ~31k RL prompts（三批） | 偏好对一批（可 10k 量级起步，S-c 推导） |
| 在线采样 | 需要（256k episodes 谱系） | 不需要（离线） |
| 关键超参 | β=0.02 / ε=0.2 / γ=27.8（PPO-ptx） | β=0.1（HH 口径；TL;DR 类摘要任务 0.5） |
| 性能上限口径 | 在线 RL 上限更高（论文谱系） | ≈ Best-of-128 代理（论文自述） |

**③ 分域税表（判分参照）**：知识域 -0.4~-2pp（散点，conf 0.4-0.6）；推理/长文域：有回归记录、量值未公开数字化（conf 0.8 定性）；判官域 -3~5%（arXiv，conf 0.7）。三域禁止合并为单一数字。

---

## 来源表

| # | 事实 | URL | 观察日 | conf |
|---|---|---|---|---|
| S1 | InstructGPT：三步 pipeline；1.3B ≻ 175B GPT-3；175B vs 175B 偏好 85%±3%；公开 NLP 数据集回归最小化（PPO-ptx） | http://arxiv.org/abs/2203.02155 | 2026-11-07 | 0.95 |
| S1' | 同上（论文原文节选：abstract + §4.2 + truthfulness 例外项） | https://ar5iv.labs.arxiv.org/html/2203.02155 | 2026-11-07 | 0.9 |
| S2 | 数据量：SFT ~13k demos；RM 比较数据 ~33k prompts（K=4..9）；RM 6B（175B RM 不稳定）；PPO ~31k unique prompts / 256k episodes | https://deep-paper.org/en/paper/2203.02155/ | 2026-11-07 | 0.85 |
| S2' | 同上（第二独立源：33k/6B/85%±3% 逐项一致） | https://martianlee.github.io/posts/2026-06-29-instructgpt-paper-note | 2026-11-07 | 0.8 |
| S3 | 超参：KL β=0.02 默认、clip ε=0.2、PPO-ptx γ=27.8、batch 512/minibatch 64/EMA 0.992、value LR 9e-6/5e-6、rollout temp 1；KL 增至 2.0（100×）不恢复 DROP/SQuAD 且伤 reward | https://huggingface.co/datasets/rl-llm-wiki/knowledge-base/blob/38df557fe522f4eec999139b2d4a7c6d0ced721d/sources/arxiv-2203.02155.md | 2026-11-07 | 0.85 |
| S3' | γ=27.8 与 β/γ 定义句（论文 PDF 正文片段，搜索引擎直接摘录） | https://arxiv.org/pdf/2203.02155 | 2026-11-07 | 0.85 |
| S4 | DPO：无 RM/无 RL 单阶段；Appendix B 原文——默认 β=0.1、TL;DR β=0.5、batch 64、RMSprop lr 1e-6、warmup 150；≈ Best-of-128 代理；HH 上超偏好补全 | https://ar5iv.labs.arxiv.org/html/2305.18290 | 2026-11-07 | 0.95 |
| S4' | DPO β=0.1（官方 reference 实现命令示例 loss.beta=0.1） | https://github.com/eric-mitchell/direct-preference-optimization | 2026-11-07 | 0.9 |
| S5 | DPO 论文本体（目标函数与"secretly a reward model"论述归属） | http://arxiv.org/abs/2305.18290 | 2026-11-07 | 0.95 |
| S6 | Reward 过度优化：Goodhart；BoN 与 RL 回落曲线函数形式不同；系数随 RM 参数量平滑变化 | http://arxiv.org/abs/2210.10760 | 2026-11-07 | 0.95 |
| S7 | URIAL/浅层对齐：token 分布漂移集中在风格 token；3 个 ICL 示例 + system prompt 匹敌 SFT/RLHF；LIMA 1K 样本谱系 | http://arxiv.org/abs/2312.01552 | 2026-11-07 | 0.9 |
| S8 | SFT 数据规律：通用能力 ~1,000 样本饱和；数学/代码随数据提升；顺序多技能灾难性遗忘 → DMT | http://arxiv.org/abs/2310.05492 | 2026-11-07 | 0.9 |
| S9 | 对齐税散点①：Gemma 4 31B abliteration → HarmBench 93.7% 服从 + MMLU 仅 -2pp；"税真实但测量不良"论述 | https://aiengineer.substack.com/p/the-2-that-keeps-your-model-polite | 2026-11-07 | 0.6 |
| S10 | 对齐税散点②：MMLU 86.2→85.8（-0.4pp）表格；"税>10% 域=高税域"操作阈值；测量方法论四步 | https://redteams.ai/topics/training-pipeline/fine-tuning/alignment-tax | 2026-11-07 | 0.4 |
| S11 | 对齐税散点③：RM 底座系统研究——SFT +15.5% → DPO/RLHF 再对齐降 3-5%（RewardBench ~3,000 任务、HelpSteer2） | https://lacuna.tiptreesystems.com/work/a-systematic-analysis-of-base-model-choice | 2026-11-07 | 0.7 |

## 找不到 / 未验证

1. **「alignment tax MMLU -5~15pp」权威一手来源**：三轮检索（阶段 02 S32 + 02.5 C2 对抗核验）未命中任何一手论文给该区间；命中最接近的是综述页的"税>10%=高税域"阈值语（非实测）。N-3.5 按任务书红线标 **[待核验]**，树内以条件化区间表替代单一数字。
2. **InstructGPT 论文全文 PDF 的逐页复核**：本沙箱走搜索摘录 + HF 转录双源交叉（S3/S3'），γ=27.8 有 PDF 正文片段直接证据，β=0.02 为双源一致转录 + 消融句算术自洽（2.0=100×默认），未逐页读原文——conf 封顶 0.85。
3. **DPO vs PPO 同底同数据对照实验**：未找到（B3 黑盒），N-4.2 只用论文自述的 Best-of-128 代理口径，不外推"PPO 一定更强"。
4. **7B 规模的税曲线一手数据**：无（B4 黑盒），N-4.3.1 显存粗算标 S-c 结构推导，不给具体 GB 数。
