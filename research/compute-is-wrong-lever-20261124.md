# origin: ai
# 方向判断：算力是错的杠杆（对 D autoresearch 目标的方向含义）
# 来源: pfb 三域数据 (GPU/Q6/Q7) · 2026-11-24 · 回应 D "没思考更大方向和 general 工作"

## 一句话判断（12:18 域范围修正后）

**修复回路是跨域瓶颈，不随算力 scaling；监控轴（gap 检测）是域特异的。** 想提升"知道自己不知道"，加预算修不好修复回路（跨域低产 1.6–5.2%），监控轴的 gap 检测则域特异：GPU 域预算买不到（平），Q6/Q7 域低水平且 50 档后微升（预算有弱效应）。

**12:18 修正**：初版把"算力买不到自我认知"说成跨域普适，错。Q6 数据（gap 率 0.073/0.003/0.016/0.026 @ 50/100/150/300）直接证伪了初版 P1（"预算 300→719 gap 率不应显著升"）——Q6 的 gap 率就是随预算升的。普适的只有"修复回路低产"，监控轴不变性只在 GPU 域成立。

## 从数据怎么推出来（证据强度分层，12:16 矛盾修正后）

**12:16 修正**：初版把三域都说成"强化不变性"，错。draft 自己写了 Q6 监控轴 invariance **does not transfer**（"the invariance is thus currently a GPU-domain result"）。三域实际不一致：

1. **元认知预算不变量 = GPU 域结果，不是三域结果**：GPU 域监控轴（claim-field gap rate）跨预算档 0.105/0.106/0.114 平（ANOVA F(2,12)=0.036, p≫0.05）。underpowered null（21.5% power），只能读"没检测到"。
2. **Q6 是反例（低水平 + 50 档后非平）**：claim-field gap rate 0.073/0.003/0.016/0.026 @ 50/100/150/300（n=3/档，draft 原文），719 档 0.000/0.029/0.005（rep 间大 spread）。与 GPU 的 flat 0.105/0.106/0.114 不同形——**Q6 水平低一个量级且 50 档后非平**。draft 定性："the invariance is thus currently a GPU-domain result, which is exactly the cross-domain validation this scan was designed to test"。
3. **修复回路低产是唯一跨域复现的**：GPU 域 flagged 节点只回头修 1.6–3.7%（node-level era-scoped / global），Q6 复现 5.2%（32/621，同量级，draft 明确 "does transfer"）。树是"绕着 52.5% 未验证节点往前长"（5630/10730）。**这条是测出来的、有牙齿的、跨域复现的——是下面方向判断的真正承重证据，比 #1 的域内 null 强。**
4. **Q7 第三域初步**（n=7，12:10 口径修正后）：gap 字段 50 档 0.000×3 / 100 档 0.000/0.020/0.010 / 150 档 r1 0.0133。形状与 Q6 同（低水平、50 档后微升）而非与 GPU 同（高水平、平）——**若 15/15 确认，"不变性"进一步降级为 GPU 域特异，"低产修复回路"仍是跨域机制**。

## 对 D 目标意味着什么（预言力，可证伪）

D 的终极目标：在 4×V100 硬件上建 research 的 AGI——能自主做研究、知道自己缺什么的系统（防御性语言=调研入口）。

这条判断给出一个**硬边界条件 + 可检验预言**（12:18 重写，初版 P1 已被 Q6 证伪）：

- **边界（跨域普适）**：autoresearch 系统里"修复回路低产"是跨域机制（GPU 1.6–3.7% / Q6 5.2%），不随算力 scaling——加预算不提高 flagged 节点的回修率。这是算力修不好的部分。
- **边界（域特异）**：监控轴 gap 检测的预算效应域特异——GPU 域平（预算买不到），Q6/Q7 域低水平且 50 档后微升（预算有弱效应）。**不能笼统说"算力买不到自我认知"。**
- **预言 P1（可证伪，12:18 重写，12:22 已直接检验）**：跨域修复回路——把预算从 300 提到 719，flagged 节点回修率（rework_count>0 且 end verified）不应显著上升。**12:22 检验结果：支持非证伪**。Q6 原批按档分解（fixed/reworked，draft 5.2% 同口径）：50 档 4.0% / 100 档 4.5% / 150 档 5.3% / 300 档 6.6% / 719 档 4.5%——高预算档不升反降；Q7 storage 0–2% 更平。Q6 50→300 的 2.6pp 微升在 n=3/档噪声内（b=300 三 rep spread 大），不当预算效应。
- **预言 P2（可证伪）**：改修复回路（把 rework 触发从"低产尾"改成"强制回修"）对回修率的影响，应比加预算更敏感。若加预算比改回路更有效 → 本判断错。
- **设计含义**：D 的 autoresearch 系统，算力预算花在"覆盖宽度"（多域、多节点，cov 随 realized 节点升三域一致）；"自我认知"分两层——修复回路（跨域瓶颈）靠架构改（回修触发机制），监控轴 gap 检测靠模型选择（域特异，GPU 域预算无效、Q6/Q7 域预算弱有效）。**不是"算力一律无效"，是"算力修不好修复回路"。**

## 置信度 + 什么证据会推翻

- **conf 0.6**（方向判断；12:22 P1 直接检验支持后从 0.55 回升——初版 0.6 建立在"三域一致"误判上降到 0.55，现 P1 有 Q6 15 run + Q7 7 run 的按档分解实测支撑，"修复回路低产不随算力"这条承重证据从 2 域总量升级为 2 域按档分解）。
- 会推翻的：① P1 被证伪——某域高预算下 flagged 节点回修率显著升（>2× 量级）；② Q7 15/15 全量后 gap 出现与 Q6 相反的强预算趋势（如 GPU 式高水平平）；③ 换更强模型后修复回路回修率随预算升（说明是模型能力瓶颈而非架构）。
- 当前最弱一环：监控轴不变性只有 GPU 域一个 underpowered null（21.5% power），Q6/Q7 是反例——**"算力买不到自我认知"的普适版已被证伪，普适的只剩"修复回路低产"（这条有 GPU+Q6 两域实测，最硬）**。Q7 15/15 落地后 P1 的第三域验证自动出。

## 算力需求是域依赖的（12:30 方向判断）

**观察**（draft 已有测量，本条是方向含义）：
- GPU 域：cov 在 ~400 realized 节点饱和（断点 475，F(2,26)=2.88 p=0.074 marginal）
- Q6 域：cov 在 719 还在涨（拆墙批 n=3，Δ=+0.0289 > 1×sd，1.21× pooled se barely resolvable）
- 两域饱和点不同 → **cov 上限是域依赖的**（不是模型/harness 的固有属性，是领域分解复杂度决定的）

**方向含义**（对 D 的 research AGI 目标，actionable）：
- research AGI 的算力需求不是"一刀切给固定预算"，是**按领域复杂度分配**
- 简单领域（GPU serving，~400 节点饱和）少给算力
- 复杂领域（自然科学，719 还在涨）多给算力
- 比"固定预算"更省算力、更对齐 Pareto 边界（D 的目标就是"预算直接控制 AI 在 Pareto 边界上研究"）

**置信度**：初步信号（GPU marginal + Q6 n=3），域依赖方向成立但强度未确证。**Q7 第三域是关键验证**——若 Q7 饱和点也在 ~400，域依赖被削弱（说明是 GPU 特异）；若 Q7 饱和点 >719，域依赖强化（三域三档饱和点）。**12:50 初步信号（7/15 run, 未决）：Q7 在 100 realized 节点 cov 0.167 ≈ Q6 ~309 realized 水平，100→150 几乎平（n=1）——若 15/15 确认，Q7 饱和点 ~100-150，比 GPU（~400）还早 → 三域三档饱和点（100-150 / ~400 / >719），域依赖最强形态。注意 Q7 realized=budget 精确相等（hard cap），跨域比较统一在 realized 轴。**

**与"算力是错的杠杆"合起来 = 完整算力策略**：
1. 修复回路靠架构（算力修不好，跨域瓶颈）
2. 覆盖宽度靠算力，但按领域复杂度分配（域依赖上限）
→ D 的 research AGI：算力花在"按领域分配的覆盖宽度"，架构花在"修复回路"。

## 机制缺口：为什么修复回路低产（12:55 分解，D general 层要求）

**缺口**：上面说"修复回路靠架构改"，但没解释**为什么**低产——"改架构"是空处方，不知道改什么。不分解机制，P2（"改回路比加预算更有效"）就没法设计，因为不知道改哪个环节。

**分解成 4 个可区分子假设**（每个对应一个不同的"架构改法"）：
- **H1 检测失败**：模型没 flag 出错的节点（监控轴失败）→ 改法=改检测。但 gap 检测已测（低水平非 0），部分排除——模型能 flag 一些，只是少。
- **H2 修复能力失败**：flag 了但修不好（rework 后 claim 没实质改变/仍错）→ 改法=改修复（更强模型/更多上下文）。
- **H3 触发过保守**：rework 只在极低置信时触发，大量"半错"节点不触发 → 改法=放宽触发阈值。
- **H4 回路断裂**：触发了但 rework 没真正回看原节点（改了别的/空转）→ 改法=修回路接线。

**哪个能用现有数据回答**（不用新跑）：
- H2/H4 可从树数据直接查：对每个 reworked 节点，比 rework 前后 claim 是否实质改变 + rework 次数分布 + rework 后 status 转移（verified/degraded/pending 各多少）。**这是 subagent 可做的本地文件分析。**
- H1/H3 需要触发日志（rework 触发时的置信度），现有树数据可能没有 → 待查。

**为什么这是 general 层**：P1 只说"低产不随算力"（现象），不分解机制就无法回答 D 真正的问题——"那我该怎么改"。H1-H4 把"改架构"从空话变成 4 个具体改法，每个有对应的可检验预测。这是从"测量结果"到"设计处方"的 general 跳跃。

**未决**：H2/H4 的树数据分析（派 subagent）；H1/H3 的触发日志是否存在（待查 s5_state_machine.py 是否记录 rework 触发置信度）。

**12:58 代码级机制核验（source ① 本轮读 s5_state_machine.py L728-788 + Q6 文件 rework_events）——H1-H4 被具体机制取代**：

读了触发逻辑，"为什么低产"有了具体答案，比 H1-H4 更可操作：

1. **触发是批级二值，非 per-node**（L728-734）：`_should_rework(batch)` = 批内 verified rate < `verify_threshold`(0.85) 才触发。→ **H3 以另一种形式成立**：批里 85% verified 时，剩下 15% 错的节点不触发 rework——粗粒度触发系统性漏掉"少数派错节点"。不是"置信度阈值保守"，是"触发粒度太粗"。
2. **三域全部 rework 是 angle 模式（盲换角度重搜），directed 模式全 0**（本轮全批核验：Q6 angle 621 / Q7 angle 121 / GPU angle 2298，directed 三域均 0）。**13:05 根因最终版（代码级证明，闭合）**：初版说"directed 死代码因为矛盾很少检出"——错，矛盾其实检得出（rounds_log 的 contradictions_found：Q7-100-r1 检出 2+2、Q6-300-r1 检出 1、GPU-719-r2 检出 1）。真正根因是**代码级结构性断链**：矛盾扫描只扫 verified 节点（L865）→ 矛盾事件节点集 ⊆ verified；rework 池 = 本轮 deduped 里 unverified 节点（L1450）；**verified 是主循环内的吸收态**——状态转移只有 pending→verified（L639/699/823/847）和 pending/degraded→degraded（L616/761/785/1231），主循环无 verified→unverified 降级路径（L1155 的 degraded→pending 重置只在 verify-only 模式，不重拆不 rework）→ 两集合结构性不相交 → directed 路径（要求节点同时在 rework 池且有矛盾事件，L764/776）**结构性不可达**，矛盾检得出也永不触发。
   - **证据等级标注**：这是代码级证明（逐行核状态转移），**非数据验证**——输出 JSON 不落盘 contradiction_events 字段（只有 rounds_log 计数），所以"矛盾节点∩rework 节点"的数据检验做不了（空字段求交=空，13:05 曾误当证据，已撤回）。经验事实 directed=0 与代码证明一致，但代码证明本身才是承重依据。
3. **max_rework=2**（L119）：每节点最多 rework 2 次，之后直接 degraded 放弃。

**机制结论（取代 H1-H4 的"空处方"）**：修复回路低产 = harness 设计问题，不是模型能力问题（三域全批核验一致）：
- 批级粗触发漏掉少数派错节点（触发粒度）
- directed 路径结构性不可达：矛盾扫描扫 verified、rework 只处理 unverified，两集合不相交（路径断链）
- 2 次即弃（预算过紧）

**对 D autoresearch 目标的设计含义（具体改法，不再是空话）**：
1. 触发粒度 batch → node（per-node verified 失败即触发）
2. **接通 directed 路径**（核心修复）：让矛盾扫描覆盖 unverified 节点，或让 verified 节点可被 rework 回退（打破两集合不相交）
3. max_rework 2 → 更高（或按节点重要性分配）
**这三条全是 harness 改动，零算力/零模型改动**——与 note 核心判断"修复回路靠架构"一致，且现在"架构"有了具体指代。

**P2 实验设计（2026-11-24 13:30 具体化，13:40 修正——初版"1 行改动"被主循环结构推翻）**：
- **初版错误**：以为把 L865 矛盾扫描过滤从 `verified` 扩到 `pending` 就能接通 directed。错——rework 池（L1450）= 本轮 `deduped` 的 unverified，而 `deduped` 只含**本轮 decompose 的新节点**（L1198 `new_nodes=[]` 每轮重置，L1368-1375 从 new_nodes 构建，L1407 extend）。上一轮遗留的 pending 节点**不进入**下一轮 rework 池。所以矛盾事件即使引用 pending 节点，这些节点也不在 rework 池里，`contra_idx.get(node.id)` 仍全空。
- **精确根因（第二层）**：directed 不可达是**双集合不相交**——(a) 矛盾事件节点集 ⊆ verified（L865 只扫 verified）；(b) rework 池 = 本轮新节点（L1450 + L1198）；(c) verified 是吸收态。新节点创建时是 pending，不可能同时是 verified；旧 pending 节点不进 rework 池。两个条件（在 rework 池 ∩ 有矛盾事件）结构性永不满足。
- **真修复方向（架构级，非 1 行）**：三选一——① rework 池改为"全部 unverified 节点"（含历史轮 pending）+ 矛盾扫描扩到 pending；② 矛盾事件触发时对冲突双方节点做**定向重验**（新路径，不依赖 rework 池）；③ 矛盾事件引用 verified 节点时，把该 verified 节点**降级回 pending** 并加入下轮 rework 池（破坏吸收态，需同步改状态机）。方案 ② 最干净（不动状态机不变量），③ 最激进。
- **假设 H**：接通 directed（任一方案）后，value_mismatch 类节点回修率 > 2.4%（blind-re-search baseline，80-run corpus 实测）。
- **控制臂**：A = 当前 harness（baseline）；B = 接通 directed（选定方案）。同预算/同题/同 rep（3 rep），max_rework=2 不变。
- **度量**：value_mismatch 类节点回修率（fixed/reworked，同 draft 331/8,870 口径）。
- **内部对照（关键）**：no_source 类节点 directed 不触发（无矛盾事件），两臂都应 ≈4.0%（纯 angle）。B 臂 no_source ≈ A 臂而 value_mismatch 升 → 升的是 directed 功劳。
- **判读**：B 臂 value_mismatch > 2.4% → 瓶颈在 harness（架构），方向判断成立；B 臂也不升 → 瓶颈在模型能力（H2）。
- **执行时机**：等 Q7 落地后（改 s5_state_machine.py 污染在飞 Q7）。方案选择需再读 `_rework_directed` 实现确认输入契约（矛盾事件结构 vs 节点状态）。

**H2/H4 机制分解数据（2026-11-24 13:50，subagent deleg_35078f46 salvage，Q6 完整 / GPU·Q7 被 token 截断）**：
- **rework_count 恒=1 跨域核验（14:10，独立复算）**：GPU 2298 / Q6 621 / Q6-rerun 460 / Q7(9 文件) 139——四批全恒=1，单尝试瓶颈是跨域机制非 Q6 特有。已进 draft §4.1/§5（commit 3eac3a1fe）。
- **Q6 原批 15 run（2727 节点 / 621 reworked）**：
  - **rework_count 恒=1（100%）**：621 个 reworked 节点无一 rework_count≥2——max_rework=2 从未用满。根因非预算紧，而是 **L750 rework 目标集只含当轮批**（节点 rework 一次后不在下轮池里，见上"精确根因"）。
  - **73% 实质改变**（454/621）：模型**修得动**——corrected_claim 与 claim 有实质差异（difflib 相似度 < 0.7）。H2"修不动"被数据削弱。
  - **27% 无实质变化**（167/621）：空转——rework 后 claim 几乎没变（相似度 ≥ 0.7）。例：N6 claim "RTX 4090 显存带宽 1008 GB/s，均价 $1600-$2000 [时效待核]" → corrected "…均价随时间波动，需查询实时市场数据"（把具体数字换成"待查"，实质信息量下降）。
  - **85% reworked 节点最终 degraded**（530/621）：修了但**没被验证接受**。最终 status 分布：degraded 530 (85%) / pending 59 (10%) / verified 32 (5%)。实质改变节点同样 87% degraded（395/454）。
- **三域矛盾信号 100% 浪费**：contradictions_found 总计 **35**（GPU 24 / Q6 4 / Q7 7），对应 directed rework = **0**——检出的矛盾信号全部因 directed 路径结构性不可达而浪费。
- **机制分解更新（H2 vs H4）**：H4（回路断裂）证据更强且是结构性的——(a) rework_count 恒=1（节点只修一次就出局）；(b) 73% 修得动但 85% 不被接受（修了白修）；(c) 35 个矛盾信号 0 转化（directed 死路径）。瓶颈不是"模型修不动"（H2 弱），而是"修了不被接受 + 只修一次 + 矛盾信号浪费"（H4 强）。
- **对 P2 的含义**：接通 directed 只是三处断裂之一。完整修复需同时：① rework 池含历史轮 pending（让节点能修多次）；② directed 路径可达（让矛盾信号转化为定向修复）；③ 修后验证接受率提升（73% 修得动但 85% degraded → 验证标准或修复质量有问题）。P2 实验应测这三处各自的边际贡献，不只测 directed。

## 与 draft 的关系

workshop draft 的 headline "budget buys breadth, not metacognition" 目前只当测量结果报。本 note 把它升级为**方向判断**，但 12:18 修正后范围收窄：draft 的 headline 本身是域内（GPU）结果，draft §4.3 已诚实标注 Q6 监控轴 invariance does not transfer。本 note 的贡献是把"修复回路低产"从 draft 的一个测量数字，升级为**跨域机制 + 对 D autoresearch 目标的设计约束**（带 P1/P2 预言）——这是 general 的那一层。**升级状态（2026-11-24 14:15）**：
- **已进 draft**（commit 3eac3a1fe）：机制（H4 回路断裂 > H2 修不动：72.6% 修得动但 85.3% degraded + rework_count 恒=1 跨 4 批）进 §4.1；P2 可执行改动（(a) directed reachable + (b) re-entry + 正交预言）进 §5。这直接挡住审稿人"是不是 27b 太弱"——数据答"72.6% 修得动，是 harness 只给一次机会 + 修了不被接受"。
- **等 Q7**：P1 跨域声明（修复回路回修率不随预算升）现在是"两域完整（GPU/Q6）+ 一域初步（Q7 9/15，低档平）"，等 Q7 落地后升级"三域完整"。draft 现在报 fix rate 数字（1.6-2.1% / 3.7% / 5.2%）但没明确写"不随预算升"的跨域趋势声明——这条等 Q7 第三域完整后补。
- **不进 draft**：P2 实验本身（改 harness 跑两臂）是 future work，draft §5 只写"planned as the next experiments"，不展开实验设计。
- **headline 不能改成跨域普适版**：Q6 监控轴反例在 draft §4.3 已写，headline 保持域内（GPU）结果 + 跨域机制（修复回路）的区分。

## 13:10 投稿硬伤：draft 核心机制声明被代码级发现推翻（已修，13:15-13:25 收口）

**draft 现有声明（§4.1 L51/53 + §5 L183/189，承重）**：
- "Bottleneck: **27b directed-fix capability** (judging which side of a contradiction is credible and producing a corrected claim), not trigger targeting."
- "the missing piece is *fix capability* — the 27b model cannot reliably judge which side of a contradiction is credible"
- 提议修复："route **directed-fix** to a stronger model or human step where capability is the ceiling"
- 承重数字："value_mismatch fix rate 2.4% (22/932)"

**代码级发现（本 note 13:05 闭合，全 83 文件 archive corpus 核验）**：
- directed 模式在**全部 83 个 archive run**（draft 的 by-reason fix rate 的实际数据源）里**一次都没触发**——9,196 个节点级 rework 事件全是 angle 模式（盲换角度重搜），directed = 0。
- directed 路径结构性不可达（verified 是主循环吸收态，矛盾扫描只扫 verified、rework 只处理 unverified，两集合不相交）。
- **关键**：`repair-closure-dryrun.py` L76-84 的 fix rate 计算**按 `reason` 文本分类、不按 `mode` 过滤**——所以 "value_mismatch fix rate 2.4%" 测的是 **angle 模式（盲重搜）** 在矛盾类节点上的表现，**不是**模型"判断矛盾哪边可信"的能力。

**矛盾**：draft 把低回修率归因到一个**从未被执行的机制**（directed adjudication）。"27b 判断不了矛盾哪边可信"这个诊断，证据上不支持——因为判断矛盾哪边可信的代码路径（`_rework_directed`）根本没跑过。2.4% 是盲重搜碰巧修好矛盾类节点的比例，不是 adjudication 能力上限。

**对 draft 的影响（投稿硬伤级）**：
- **影响面（grep 全文核验）**：机制声明 "directed-fix capability / cannot reliably judge which side of a contradiction is credible" 出现在 **4 处**：L51（§4.1 finding 1 末句 "Bottleneck: 27b directed-fix capability"）、L53（§4.1 Claim "the missing piece is *fix capability* — the 27b model cannot reliably judge..."）、L183（§4.4 "Predicted failure mode: ...capability, not targeting: a stronger directed-fix model"）、L189（§5 implication 1 "route directed-fix to a stronger model or human step where capability is the ceiling"）。
- **不受影响**：L21（abstract）的 "capability bottleneck" 指的是 **bare-arm control**（breakage 是能力瓶颈非 prompt artifact）——那是另一个独立 claim（n=6 bare arm），与 directed 路径无关，不受本发现影响。
1. L51/L53 的 "Bottleneck: 27b directed-fix capability" 声明**站不住**——directed 没跑过（全 83 文件 0 次），无法声称是模型能力瓶颈。
2. L183/L189 的提议修复 "route directed-fix to a stronger model" **方向错**——真问题是 directed 路径不可达（harness 设计），换更强模型不会让一条死路径活过来。真修复是**接通 directed 路径**（harness 改动，零模型改动）。
3. "value_mismatch 2.4%" 数字本身没错（angle 模式实测），但**它的机制解释错了**——它测的是盲重搜，不是 adjudication。

**处置**：这是 draft 的承重机制声明（§4.1 finding 1 + §5 implications），不是边角数字。Q7 落地 + 压缩 pass 时必须一起修：把 "capability bottleneck" 重写成 "harness gap（directed path structurally unreachable）"，把 "route to stronger model" 改成 "make directed path reachable + then test whether a stronger fixer helps"。P2 预言（接通 directed 后回修率应升）正好是这个修复的可检验版本。

**修复执行记录（13:15-13:20，已落地 commit f101f8ba3 + 742427103）**：
- 4 处 patch 全部落地（L51/L53/L183/L189），旧声明 0 残留，grep 核验通过。
- L189 内部矛盾已修：初版 patch 让 (a)"stop reworking value_mismatch" 与 (b)"make directed reachable" 冲突（(a) 是旧框架下"2.4%=wasted"的结论，新框架下 2.4% 只是 blind-re-search baseline，stop reworking 应推迟到 directed 测过之后）。改为"2.4% 是 baseline 非 ceiling，stop reworking 推迟到 directed 路径测过之后，只有那时才 warranted"。
- abstract (L9) / L21 不受影响：L9 只报 "1.6–2.1%" 数字无机制归因；L21 的 "capability bottleneck" 指 bare-arm L4 breakage（0/6 到 conclusion layer），是独立 claim，与 directed 路径无关。

**遗留（已解决 13:25，commit 84064c874）**：draft 现有文本标 "80-run corpus"（10,702 event-level / 331/8,870 node-level），archive 全 `*` glob 是 83 文件。查清：`repair-closure-dryrun.py` 用 7 个 pattern（`sm-gpu-*/budget-*/sm-nat-*/sm-soc-*/idea2-*/repscan-*/rep-*`）= **80 文件**（排除 3 个 `sm-t53b-backup-*` 备份），所以 draft 的 "80-run corpus" 是对的。"83 runs"（L9/L20/L49）是**跨域 metacognition corpus**，与 repair-closure 的 80-run 是两个不同语料、两个不同分析，都是合法用法。本发现插入文本初版误用 "0/9,196 (83 runs)"，已统一改为 "0/8,870 node-level (80-run corpus)"（与 draft 的 331/8,870 同口径；8,870 = 80-run corpus 节点级 rework，全 angle、directed=0，独立复算吻合）。
