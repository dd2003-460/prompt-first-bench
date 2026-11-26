# 状态机机制 + 深层节点实证 + 未控变量清单（2026-11-26）

> origin: ai · 只读代码与 runs json，未跑任何实验/未调 LLM 端点。
> 数据源：`experiments/stage-ablation/s5_state_machine.py`（1870 行）、`s5_pipeline.py`（1380 行）、
> `ablation_harness.py`、`s8b_pilot.py`、`gates.py`、`runs-s5-sm-*.json`（13 个树 run）、
> `ablation-runs/gpu_formula_r*.json`（8 个 synth run）、`runs-qc-compare/*.json`、
> `loop/01..04.5-*.md`（六阶段文件）、`state-machine-status-20261126.md`、`T53-05-accept.md`、
> `modules/A-eval-infra/research/scoring-v3-gatefixed.md`。
> 注：`loop/prompt-first/` 目录现已不存在，六阶段文件实际位于 `pfb/loop/`（01/02/02.5/03/04/04.5），
> `ablation_harness.STAGE_FILES` 仍指向旧路径 `loop/prompt-first/`（`build_prompt('S5')` 当前会 FileNotFoundError）——
> 即 S5 六阶段注入的 harness 入口在 2026-11-26 时点已断链，历史 S5 分数（0.579）是断链前跑的。

## §1 机制对比：v18 状态机各阶段 prompt vs S5 六阶段注入

### 1.1 S5 臂的 prompt 构成（`ablation_harness.build_prompt`，DESIGN.md §2）

S5 = 单轮 one-shot LLM 调用（`s8b_pilot.run_one`，temperature=0，max_tokens=8000），
prompt = 六个阶段文件**全文按序拼接** + 题面 + 标注习惯句。实测各文件字符数：

| 阶段 | 文件 | 字符数 | 核心内容 |
|---|---|---|---|
| 01 | 01-goal-decomposition.md | 2542 | 递归分解到原子、空缺清单、候选集冻结、Reviewer 判定原则 |
| 02 | 02-information-research.md | 2366 | 网页 LLM 交叉询问（ego-browser）、≥2 独立来源、时效 7 天、WebFetch ≤4 URL |
| 02.5 | 02.5-cross-check.md | 683 | 矛盾解释、对抗核验（攻击核验方结论）、证据边界 |
| 03 | 03-action-decomposition.md | 904 | 可执行步骤 DAG、输入/动作/依赖/验收、替代路径 |
| 04 | 04-execution-verification.md | 989 | 执行记录、逐项对照验收、循环防护（≤2 重试） |
| 04.5 | 04.5-final-review.md | 842 | 反方检查、完整链条、不夸大结论、可交接 |
| 合计 | | **8326** | 再加题面与工具说明 ≈ 9-10K 字符，一次注入 |

S5 另有**三道闸**（`gates.py`，DESIGN.md D-a/D-b）：闸 1 无来源数字正则、闸 2 断言库矛盾比对、
闸 3 限制句位置 checklist——是**评分/审计层**的正则+LLM 后处理（M2/M3/M5 维度），
T22 结论：闸是隔离器不是验证器（post 无锚点率≈raw），价值在逐行 quarantine 审计链。

关键点：S5 的六阶段是**同一次 LLM 调用内的 prompt 规则**——模型"被告知"要按阶段做，
但没有任何机器环节强制执行阶段流转；检索在 S2+ 臂是 harness 层 research_hook 代查后注入
（DESIGN.md §5 公平性声明：S 臂联网深度与 D1 不完全等价）。

### 1.2 v18 状态机的阶段与 prompt（`s5_state_machine.py`）

状态集合 `{IDLE, DECOMPOSE, VERIFY, REWORK, STOP}`（line 402-407）。
主循环 `run()`（line 1200 起）：每轮 DECOMPOSE（拆 frontier 层）→ VERIFY（批核验）→
J_verify 判 rework → REWORK → J_stop 判停。各阶段 prompt（全部在 `s5_pipeline.py`，
SM 文件 line 493/545 import）：

| 状态机环节 | prompt 常量 | 字符数 | 内容 |
|---|---|---|---|
| L1 种子 | P1_L1_SKELETON | 1087 | 先写终点目标函数（要素可测+组合方式），再导 3-7 个正交顶层维度；禁止下钻 |
| 逐层分解 | P1H_INDEX | 2312 | 目录树 INDEX 隐喻；子节点必带数值/公式；复合概念 X=f(A,B) 必拆；深度判据（专家会说"还差一层"吗）；反 Goodhart 反参数展开；硬停门禁 3 条；source 三分类 |
| 广度审查 | P15A_DIMENSIONS + P15B_GAP_FILL | 270+574 | 列顶层维度 → 对照节点找缺失维度补 3-10 个节点 |
| 核验 | P3_VERIFY | 2284 | 单节点：逻辑自洽 + 对照来源包核验 → verified/degraded/failed（含反方质询步） |
| REWORK 定向 | _rework_directed 内联 prompt | ~400 | 两矛盾节点双方 evidence 裁决，产 corrected_claim + 新检索词，重搜重验 |
| REWORK 换角度 | _rework_angle 内联 prompt | ~300 | 给 2 个不同检索角度的改写 query（至少 1 个英文），逐个重试 |
| 矛盾扫描 | _scan_contradictions 内联 prompt | ~400 | 每轮对最近 30 个 verified 节点批量查互相矛盾的数值 |
| 正交审查 | line 1371 内联 | ~300 | 兄弟节点正交性审查，非正交丢弃 |
| 综合 | synthesize_answer（line 1580） | ~2000/层 | 按 L 层分段综合（temp=0.7）→ merge 成最终答案（temp=0.7, max_tokens=8000） |

机器判定（替代了 S5 的"prompt 内规则自觉"）：
- **J_decomp**（line 136-157）：n-gram Jaccard 边际增益 `1 - mean(max sim)`，threshold 0.50；
- **J_verify**（line 789-795）：批内 verified 率 < 0.85 → 强制 REWORK；
- **J_stop**（line 1545-1553）：stop_criterion="necessary"（judge_necessary_batch，LLM 判本轮无必要节点）
  或 "gain"（连续 stop_rounds=2 轮低增益），另有饱和停（本轮 0 新节点）；
- **硬顶**：max_nodes=150 / max_depth=4 / max_rework=2 / max_kids_per_parent=8（ObjectiveConfig line 107-131）；
- **S_α 修正得分**（line 380）：recall×precision 型（F_β, β=0.5）+ 冗余惩罚 β=3.0，防 Goodhart 刷分；
- **leak_check**（line 81）：每轮 decompose/rework 输出后查 gold 实体泄漏，命中 ABORT。

### 1.3 覆盖范围对照表

| 能力 | S5 六阶段注入 | v18 状态机 | 备注 |
|---|---|---|---|
| 目标分解（正交/完备/原子） | 01 全文 + decomp 模块（S1 臂） | P1_L1_SKELETON + P1H_INDEX + 硬停门禁 | SM 更细（逐父节点、层级 INDEX 隐喻） |
| 信息调研（真检索） | 02 全文（prompt 规则）+ harness research_hook 代查 | P2 search_node 真检索（每节点），source=search 才触发 | 两者都有真检索，SM 是逐节点粒度 |
| 交叉核验（≥2 独立来源/对抗核验） | 02.5 全文（prompt 规则） | P3_VERIFY 单节点 vs 来源包 + 矛盾扫描（机器触发） | SM 无"≥2 独立来源"硬要求；有全局矛盾扫描（S5 无对应机器环节） |
| 行动分解（DAG/验收） | 03 全文 | **无对应环节** | SM 的"行动"= 状态机流转本身，无 DAG 步骤规划 |
| 执行验证 | 04 全文（prompt 规则） | VERIFY 状态 + J_verify 阈值 + 矛盾扫描 | SM 是机器判定，S5 是 prompt 自觉 |
| 终审/反方检查 | 04.5 全文（反方检查原则） | **无对应环节**（synth prompt 有"矛盾取多数一致"，无独立反方终审） | SM 缺 04.5 等价物 |
| 三道闸（无来源数字/矛盾/限制句位置） | gates.py 后处理 | **无对应环节**（leak_check 只防泄漏，不审无来源数字/限制句位置） | SM 的 verified 状态部分覆盖闸 1 职能 |
| 停止判据 | 无（单轮，模型自己写完） | J_stop + 硬顶（机器） | SM 独有 |
| REWORK | 无（单轮内无返工机制） | J_verify 触发，定向/换角度两种 | SM 独有 |
| 防泄漏 | gold 不进 prompt（纪律） | gold 不进 prompt + leak_check 机器 ABORT | SM 多一层机器闸 |

**一句话机制差异**：S5 把六个阶段的方法论全文塞进单次调用的 prompt，靠模型自觉执行（机器只在评分端有三道闸）；
状态机把流程拆成机器强制流转的状态（DECOMPOSE→VERIFY→REWORK→STOP），prompt 只负责单步动作，
"注意力拉回"由状态机每轮重新注入 P1H_INDEX + 已确认事实块完成——代价是丢了 03 行动分解、04.5 终审、三道闸这三个 S5 环节。

### 1.4 注意力拉回机制的失效模式对比（②c 事实基础，不下结论，供 Lead 判 Q2）

"注意力拉回" = 长程任务中把模型注意力拉回每个环节、防漂移的机制。两臂实现与失效模式：

| | v18 状态机（机器判定强制流转） | S5 六阶段（prompt 内规则） |
|---|---|---|
| 拉回机制 | 每轮机器重新注入 P1H_INDEX + 已确认事实块（verified 节点）；DECOMPOSE→VERIFY→REWORK→STOP 强制流转，模型不能跳阶段 | 六阶段方法论全文一次注入单次调用，靠模型"被告知后自觉"按阶段推进；无机器环节强制阶段流转 |
| 失效模式 1 | rework 换角度救不回：机器判定触发返工 663 次但成功率仅 6.6%，失败节点沉 degraded——机器能"发现"问题但"修不好" | 单轮 one-shot 无返工机会：模型写错/漏掉某阶段，本次调用内无第二次机会纠正 |
| 失效模式 2 | max_depth=4 硬顶命中即 break（不经 J_stop 停止判据）：深层"拆够了吗"无判据，只有硬顶 | 无机器强制流转：模型可能跳过某些阶段（尤其 04.5 终审/反方检查），跳过后无机器环节补回 |
| 失效模式 3 | 双重 12K 截断：L4 深层内容（占树 39-64%）经 synthesize→judge 两道截断被削弱，拉回的深层注意力到判分端丢失 | 检索在 harness 层 research_hook 代查后注入：S 臂联网深度与 D1 不完全等价（DESIGN §5 公平性声明自标） |
| 失效模式 4 | directed 定向修正 0 次触发：_scan_contradictions 产出的 contradiction 从未送进 _rework_directed，机器矛盾检测的"修"路径实际未启用 | 三道闸是隔离器不是验证器（T22：post 无锚点率≈raw）：闸不能真正提升质量，价值在逐行 quarantine 审计链 |

事实小结（不下结论）：状态机失效集中在"机器能强制流转但修不好（rework 6.6%）+ 深层拉回被截断削弱"；
S5 失效集中在"靠自觉无强制（可跳阶段）+ 无返工 + 检索不等价 + 闸不验证"。
两者失效模式正交，不是同一维度的强弱——Q2"为何 prompt 堆叠更强"不能简单归因为"状态机拉回更弱"。

## §2 REWORK 实证（runs json 提取）

口径：13 个树 run json（`runs-s5-sm-*.json`）+ `ablation-runs/gpu_formula_r*.json`（synth 层，无 rework_events 字段）。
rework 事件两种形状：节点级 `{node_id, attempt, mode, reason}`（`_rework` line 813 落盘）和
父节点级 `{parent_id, issues, suggestions, round}`（`_verify_parent_nodes` 落盘）。
drb-2 与 drb-2-reverified 是同一棵树的重验版，去重后 **11 个独立树**。

### 2.1 次数与分布

| run（qid） | 节点数 | 节点级事件 | 父节点级事件 | mode | attempt 分布 |
|---|---|---|---|---|---|
| drb-1 | 169 | 149 | 0 | null（旧版格式，D34 前） | 全 1 |
| drb-2 | 62 | 55 | 0 | null（旧版） | 全 1 |
| gpu-formula-r2 | 53 | 32 | 0 | angle×32 | 全 1 |
| gpu-textarm-r2 | 124 | 72 | 0 | angle×72 | 全 1 |
| gpu-textarm-seed | 23 | 8 | 0 | angle×8 | 全 1 |
| l4-disambig | 300 | 97 | 37 | angle×97 | 全 1 |
| nat | 278 | 4 | 0 | angle×4 | 全 1 |
| q6-nev | 187 | 122 | 0 | angle×122 | 全 1 |
| q6 | 300 | 91 | 49 | angle×91 | 1×65, **2×26** |
| q7-rd | 51 | 28 | 0 | angle×28 | 全 1 |
| soc | 283 | 5 | 0 | angle×5 | 全 1 |
| **合计（去重）** | | **663** | **86** | | |

- **max_rework=2 生效证据**：q6 有 26 个节点 attempt=2（第二次 rework 仍失败 → degraded）；
  其余树全 attempt=1（第一轮 rework 后节点即 degraded，未触发第二次）。
- **定向修正 rework（directed）在落盘数据中 0 次**：mode 全为 angle 或 null，
  即 `_scan_contradictions` 产出的 contradiction_events 从未把节点送进 `_rework_directed`
  （rework_fix_rate 指标在落盘 json 中无样本，只有 angle 模式）。
- T53-accept AC5 记录（2026-11-16，gpu 163 节点树，与落盘 json 非同批）：gpu 40 次 rework，
  N29/N45/N31/N18 四个节点返工后终态 verified；nat 1 个（N28）；soc 5 次未翻回。

### 2.2 成功率

- 被 rework 过的唯一节点合计 **637 个**（drb-2 双版本去重后），其中终态 verified 的 **42 个 → rework 成功率 6.6%**。
- 逐树：drb-1 10/149=6.7%、gpu-formula-r2 5/32=15.6%、gpu-textarm-r2 18/72=25%、
  l4-disambig 2/97=2.1%、q6 2/65=3.1%、其余 0-25%。
- 失败去向：rework 未成功 → `status=degraded`（放弃，保留节点但标降级），
  这是各树 degraded 占比高的主因（如 q6-nev 121/187=65% degraded，q7-rd 28/51=55%）。
- 父节点级 rework（l4-disambig 37 + q6 49 = 86 次）：issues 为「不完备/有冗余」类，
  suggestions 是合并/补节点建议——**无落盘字段记录其执行结果**（只记事件不记 fix 与否），
  这部分成功率不可测。

**一句话**：REWORK 机制真实存在且高频触发（663 次节点级 + 86 次父节点级），但成功率仅 6.6%——
换角度重搜（angle 模式）绝大多数救不回核验失败的节点，失败节点沉为 degraded。

## §3 深层节点（L4）实证

### 3.1 层级分布（11 个独立树）

| run（qid） | L1 | L2 | L3 | L4 | 总计 | L4 占比 |
|---|---|---|---|---|---|---|
| nat | 5 | 23 | 71 | **179** | 278 | 64% |
| soc | 5 | 24 | 76 | **178** | 283 | 63% |
| q6 | 5 | 29 | 91 | **175** | 300 | 58% |
| l4-disambig | 4 | 29 | 94 | **173** | 300 | 58% |
| q6-nev | 4 | 20 | 54 | **109** | 187 | 58% |
| drb-1 | 5 | 19 | 47 | **98** | 169 | 58% |
| gpu-textarm-r2 | 6 | 13 | 34 | **71** | 124 | 57% |
| q7-rd | 4 | 11 | 12 | **24** | 51 | 47% |
| drb-2 | 6 | 9 | 23 | **24** | 62 | 39% |
| gpu-formula-r2 | 6 | 13 | 34 | 0 | 53 | 0%（2 轮内未到 L4） |
| gpu-textarm-seed | 6 | 17 | 0 | 0 | 23 | 0%（早期截断） |

**L4 节点共 1031 个**（去重后 9 个含 L4 的树），是各树最大单层（39-64%）。
v18 的 max_depth=4 硬顶意味着 L4 是最后一层：树在 L4 处被截断，"该不该继续拆"由
P1H_INDEX 的硬停门禁 3 条 + J_stop 判，但 max_depth=4 一旦命中直接 break（run() line 1230-1234），
不经过停止判据——深层是否"拆够了"没有判据，只有硬顶。

### 3.2 L4 节点实际内容样例（verified，claim 前 100 字）

| node id（run） | 内容 |
|---|---|
| N100（nat） | 基于 Web 边缘节点对象存储的经验分布，Pareto(α=1.1) 的最小截断值 x_min 通常设定为 4KB (4096 Bytes)，以对齐常见网络包/块粒度并覆盖绝大多数静态资源 |
| N101（nat） | 在引入截断上限 S_max=100MB 后，截断 Pareto 分布的期望值 E[S]_trunc 的计算公式修正为：E[S]=[x_min·α/(α-1)]·(1-(S_max… |
| N107（soc） | 阈值敏感性边界：当个体损失厌恶系数 λ<1.5（约占总卖家群体 15% 的左尾分布）时，降价带来的感知效用损失不足以抵消销量预期增加的收益，该群体不响应平台降价提示 |
| N108（soc） | 方差来源解构：λ 的个体间标准差 σ_λ≈0.4 主要源于风险偏好特质与过往交易经验频率的差异，而非单纯的认知偏差噪声 |
| N154（q6） | 核心区 P99 延迟基准值 P_core=35ms，基于国内一线及新一线城市用户到最近边缘节点的 RTT 均值加上边缘节点处理延迟 (5-10ms) 及抖动估计得出 |
| N55（q7-rd） | 三星电子 2023 财年半导体板块研发强度 = 18.46 万亿韩元/61.73 万亿韩元 ≈ 29.9%，显著高于集团整体研发强度 12.6%，该差值量化了… |
| N70（q7-rd） | 阿里巴巴 FY2023 的研发强度计算式为 11.16/250.2 = 4.46%，该数值显著低于三星电子 FY2023 的 6.47% |
| N193（l4-disambig） | N55 的工作点 A（算力主导型）：BF16 精度下 GPU 峰值算力 312 TFLOPS (A100 SXM) 且计算效率 η_compute=0.90，则理论最大解码吞吐… |
| N205（l4-disambig） | A100 SXM 多卡方案拥有 NVLink 4.0 (双向 ~600 GB/s)，其 Tensor Parallelism (TP) 效率 PE_TP ≈ 1/(1+(k-1)·…) |
| N277（l4-disambig） | RTX 3090 在 INT8 精度下 KV Cache 读取为顺序大块访问，此时 DRAM 行缓冲命中率 >95%，有效带宽效率… |

L4 的内容形态 = 具体公式代入/边界条件/敏感度系数/机制解释（正是 P1H_INDEX 反 Goodhart 条款
要求的"机制解释/交互效应/边界条件"类深度），不是参数表复读。

### 3.3 微架构类命中

- `grep 微架构|microarch`（11 个树 run 全部节点 claim + 8 个 synth run 的 answer 文本）：**0 命中**。
- `效率|efficiency`（节点 claim，11 个独立树去重口径，与 rework 统计一致）：合计 **39 处命中**
  （l4-disambig 18、nat 5、q6 5、gpu-textarm-r2 4、gpu-formula-r2 2、gpu-textarm-seed 2、drb-2 1、q6-nev 1、soc 1）；
  其中 **L4 层 21 处**（l4-disambig 9、nat 5、gpu-textarm-r2 2、q6 2、drb-2 1、q6-nev 1、soc 1；
  样例 PE_TP 并行效率、η_compute 计算效率、DRAM 行缓冲命中率/有效带宽效率、c_pass 估算等，见 §3.2 N193/N205/N277）。
  注：早期脚本误扫 13 文件（drb-2 双版本重复计入 + 混入 nat-verifyfix 5 节点诊断 run）得 41，
  此处按与 rework 一致的 11 树去重口径修正为 39；"L4 层 9 处"系误把 l4-disambig 单文件 L4 命中当总数，修正为 21。
- 结论：**"微架构效率"作为字面术语不存在，但同类深层内容（微架构级效率参数：并行效率/计算效率/
  访存效率）以具体公式形式存在于 L4 层**——L4 节点出现了，且内容确实是深层机制级。

### 3.4 L4 节点有没有参与判分

- **judge 输入是最终 answer，不是树节点**：`s8b_pilot.judge`（line 157）= GOLD 要点清单
  （gpu 15 点/nat 6/soc 7/q6-nev 10）× 候选回答前 **12000 字符**，逐条 0/1 → coverage；
  `judge_v2_depth.score_run` 同样只对 answer 打分（depth_score）。
- L4 节点参与判分是**间接的**，通路 = 节点树 → `synthesize_answer`（line 1580）按层分段综合
  （每层 seg **截断 12000 字符**，head 8000 + tail 4000）→ merge 成 answer（max_tokens=8000）→ judge
  （再截 answer 前 12000 字符）。
- **双重截断**：代码注释（line 1576-1579）自证——"L4 有 97 节点 24K chars，截断后丢失的恰是
  后半段的 roofline/故障损耗/利用率等关键公式节点"。即 L4 节点虽被生成和核验，
  但到 judge 的信息通路有两道截断（综合层 12K + judge 层 12K），深层内容对最终分数的贡献被结构性削弱。

## §4 未控变量清单（除 max_nodes=150 / max_depth=4 / max_rework=2 外）

| # | 变量 | 状态 | 证据 |
|---|---|---|---|
| 1 | 8787 长会话漂移（同会话后段 run 质量下降） | **未控** | T53-accept §4：nat 10-run 前 5 个 cov 0.833-0.667、后 5 个 0.333-0.167，hf 从 2-3 涨到 5-13，"不是随机噪声"；status 报告 §2 标 nat 0.517 FAIL 口径混杂。v18 各 run 与 S5 基线不在同一会话窗口跑，分数含基础设施噪声 |
| 2 | SM_SEED 只控树不控 LLM 采样 | **部分控** | s5_state_machine.py line 28-34：SM_SEED 只 seed Python `random` 单例（影响 _perturb 零宽字符、random.sample 等）；LLM 端 8787 后端采样可复现性 [待核验]（T53 AC7）。且 decompose/synth 调用 temperature=0.7/top_p=0.95（line 504/599/1614/1634），SM_SEED 管不到端点侧 |
| 3 | 温度设置不一致（跨环节/跨臂） | **未控** | 同一管线内：decompose temp=0.7、verify temp=0、rework-directed 0.0、rework-angle 0.3、synth 0.7、judge 0（s8b_pilot line 180）；S5 臂整体 temp=0（DESIGN.md §2 "同 temperature=0"）。v18 与 S5 的温度分布完全不同，分数不可直接比 |
| 4 | judge 同族偏差（qwen3.8-27b 评 qwen3.8-27b） | **未控** | s8b_pilot.judge docstring 自标"同族 27b, 仅相对有效"；scoring-v3-gatefixed.md 交叉判官表：同族 judge 说 S1-S0=+0.129，异族（arena GPT）=-0.187，方向相反。v18 与 S5 分数都由同族 judge 出，绝对值不可信 |
| 5 | 题集/gold 锚点数差异（gpu 15 点 vs nat 6 vs soc 7） | **部分控** | s8b_pilot.GOLD：gold 点数不同 → coverage 分母不同（6 点题拿 1 点=0.167 跳变，15 点题粒度更细）；status 报告 §2 已标"口径混杂"。跨题比分时锚点密度差异未归一 |
| 6 | 口径混杂（v18 与 S5 不同指标/不同批） | **未控** | status 报告 §2：v18 gpu 0.393≈v13 0.389 < S5 0.579 是不同批 run、部分不同指标（depth vs coverage）的直接并排；synth 注释（line 1573-1575）自证 gate 0.898 是 S0 的 judge.coverage 而 SM 产 depth，"两个指标不同没法比" |
| 7 | 综合层截断（L4 信息丢失） | **未控** | synthesize_answer line 1576-1579：每层 seg 截 12K（head 8K+tail 4K），L4 97 节点 24K chars 后半段（roofline/故障损耗/利用率公式）被丢；judge 再截 answer 前 12K。深层节点对分数贡献被截断，截断量随树大小变（nat 278 节点 vs q7-rd 51 节点截断损失不同） |
| 8 | 检索质量波动（ego-browser/arXiv 通道可用性） | **未控** | SM 有 _probe_network 降级（network_degraded 时检索退化），但落盘 json 无逐节点检索成功率字段；nat 树 70 节点 pending 是 8787 502 中断（T53 AC3），检索/推理通道噪声混入树质量 |
| 9 | n 太小（单 rep 或 n=2） | **未控** | DESIGN.md §4："n=2 只能出方向性结论（t17 已证 n=2 噪声 ≥ 域差）"；v18 各题多为单 rep（nat-synth-multi 10 rep 是例外，sd 0.263 本身说明方差大） |
| 10 | S5 六阶段文件路径断链（harness 指向已不存在的 loop/prompt-first/） | **未控（历史口径）** | ablation_harness.STAGE_FILES 指向 pfb/loop/prompt-first/（不存在），文件实际在 pfb/loop/；build_prompt('S5') 当前 FileNotFoundError。S5 0.579 是断链前跑出，复跑 S5 需先修路径，否则"S5 vs v18"对比的 S5 侧不可复现 |

Top3（对分数影响最大）：**#1 8787 漂移**（nat FAIL 的主因，直接翻转 gate 判定）、
**#4 judge 同族偏差**（方向都可能反）、**#6 口径混杂**（v18 0.393 vs S5 0.579 的并排本身不可比）。

## §5 对 D 三问的直接回答

- **②（状态机为何弱于 prompt 堆叠 / 有 rework 吗）**：事实基础——状态机有 rework（663 次节点级 + 86 次父节点级，max_rework=2 生效，q6 有 26 节点 attempt=2），但 rework 成功率仅 6.6%（42/637），失败节点沉为 degraded；机制上状态机丢了 S5 的 03 行动分解、04.5 终审、三道闸三个环节（§1.3 表），且综合→judge 通路有双重 12K 截断，L4 深层内容（占树 39-64%、共 1031 节点）对最终分数的贡献被结构性削弱；注意力拉回机制的失效模式对比见 §1.4（状态机失效=机器强制流转但修不好+深层被截断；S5 失效=靠自觉可跳阶段+无返工+检索不等价+闸不验证——两者正交，非同一维度强弱）；v18 与 S5 的温度分布（0.7 vs 0）、批、指标口径都不同（§4 #3/#6），0.393 vs 0.579 的差距目前无法归因到单一机制。
- **④（深层节点有出现和计算吗）**：有。L4 节点共 1031 个（9 个含 L4 的树，占各树 39-64%，是最大单层）；"微架构/microarch" 字面 0 命中，但"效率/efficiency"类深层内容命中 39 处（L4 层 21 处：PE_TP 并行效率、η_compute、DRAM 行缓冲命中率等，§3.2 样例）；判分对象是最终 answer 不是树节点，L4 只通过 synthesize_answer 间接进 judge，且被两道 12K 截断削弱。
- **⑤（未控变量）**：10 条清单见 §4——未控 8 条（#1 8787 漂移、#3 温度不一致、#4 judge 同族、#6 口径混杂、#7 综合截断、#8 检索波动、#9 n 太小、#10 S5 路径断链），部分控 2 条（#2 SM_SEED 只控树不控 LLM 采样、#5 gold 锚点数差异）。
