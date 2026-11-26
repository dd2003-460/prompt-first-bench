# Q9 gold 骨架 A（主调研）— research-AGI 预算控制：150 节点内达"自我认识"的路径分解

> origin: arena agent · 2026-11-26 · 任务卡: `q9-gold-skeleton-arena-taskcard.md` 任务卡 A
> 题面基准: `q9-agi-question-v0.md`「## 题面 v1」（冻结 @ 8a9c45bfa；本文件建于 thinkmech-review HEAD 789e7735d，已核对）
> 独立性: 外部结论全部本轮独立调研（GitHub 开源实现 → arXiv abs 页逐个核验 → 与本仓 83-run 实测交叉对照 → 自推）；**未复用** gold-tree.md(Q1)/gold-Q6/gold-Q9 的数值与结构。
> 核验纪律: 凭记忆写下的 4 个 arXiv ID 被 abs 页证伪并弃用（见附 4）；论文自报数字未经复现标 [待交叉验证]；本沙箱无法核验的标「未验证」。
> 泄露边界（硬规则②）: 5 项因子已在题面清单内；本文件的骨架结构/阈值/数值不得进 prompt。
> 冻结（硬规则③）: 状态=待 Lead 与任务卡 B 对比 + D 确认后冻结，此后改动需 D 确认。

---

## 核心（排序键 + 分解树 · 46 行，≤50 达标）

```
N-0  单位预算闭环成功率  J = post_acc × (150 / n_realized)                     SHARE 1.00  split
│    post_acc = n_search_verified / (n_search_verified + n_contradicted)   ← metacog_axis v1.1 口径, unverifiable/ambiguous 不进分母
│    n_realized = len(nodes) @ max_nodes=150 硬钳制后（s5_state_machine.py:1394-1405）——不取"计划节点数"
│    作用面: 能力轴=J 的上界 | 预算轴=J 的分母 | 检索质量轴=J 的分子 | 记忆轴=分母折扣 | 闭环=分子转化闸
│
├─ N-1 模型能力轴（元认知增益 vs 规模）· 5 判定叶
│  ├─ [能力] 自我认识信号载体在权重不在 prompt：事实层自我认识以线性特征存在于 residual stream、训练早期即涌现、中间层峰值、对格式扰动稳健 → prompt/harness 只能"读出+外置监控"，不新增监控能力 | 口径: 同题面同预算下 gap_rate 与 healthy_gap_rate 跨提示模板变体的方差（方差小=格式非主因） | https://arxiv.org/abs/2505.21399 | conf 0.6（特征存在性 0.8；"prompt 不能新增"为外推=未验证）
│  ├─ [能力] "校准随规模变好"是有条件的：较大模型仅在 MC/TF 且格式正确时 well-calibrated → gold 不以"换更大模型"为默认解，以"固定自评问法模板"为前置 | 口径: 置信度模板定值后，比 AUROC(gap 标记 ↔ 该节点是否 verified) | https://arxiv.org/abs/2207.05221 | conf 0.7
│  ├─ [能力] 规模不自动带来自验证：无外部反馈的内在 self-correction 不涨甚至退化；本仓 83-run rework 修复率实测仅 1.6–2.1%，两路证据同向 → 能力轴不是 150 节点预算内的第一杠杆 | 口径: 无外部反馈臂 vs 有证据反馈臂的 verified 转化率差 | https://arxiv.org/abs/2310.01798 + 本分支 metacog-loop-design-20261122.md | conf 0.75
│  ├─ [能力] 元认知监控+控制不在 scaling law 承诺范围内（无 ground-truth loss 可优化）→ 题面"能力增益曲线"文献层无单调上升证据，gold 给"平/域特异"锚点，不给"越大越好" | 口径: 跨域 gap_rate 域序（本仓 nat<soc<gpu, p<0.001）vs 跨模型档（阻塞） | https://arxiv.org/abs/2408.05568 + 本分支 plan-layered-20261122.md L2-1 | conf 0.6
│  └─ [能力] 量化档位不是排序键的系统性偏置源：4-bit 在 procedural reasoning 维度 ≈ FP16，且"量化比剪枝更抗能力退化" | 口径: 同模型双臂（formula vs text）post_acc 差 vs rep sd | https://arxiv.org/abs/2610.27913 + 本分支 verification-sop-literature-20261121.md | conf 0.55（ACE 测 INT4 非 NVFP4；V100 cc7.0 无 FP4 硬件路径，题面该组合=未验证）
│
├─ N-2 预算轴（节点/token → 覆盖/深度 Pareto）· 6 判定叶
│  ├─ [预算] 分母必须用硬钳制后的 realized 节点数：pre-clamp 批次 realized 271–462 与 150 档重叠，跨档比较一律按 realized 轴重算 | 口径: 每 run 输出 n_realized=len(nodes)；n_realized<0.8×150 单列"早停臂"不参与 Pareto 拟合 | 本分支 plan-layered L2-4「预算口径勘误」（47a8543cd） · https://github.com/dd2003-460/prompt-first-bench/blob/789e7735d/modules/B-pipeline-ablation/research/plan-layered-20261122.md | conf 0.9
│  ├─ [预算] 覆盖对预算的边际收益域依赖：GPU 域 cov ~300 节点进平台（719 不高于 300）、Q6 到 719 仍涨、Q7 ~100–150 即平 → 150 档是"拐点附近"而非通用饱和点，gold 不宣称"150 已够" | 口径: cov(bge-m3 cos≥0.70 命中 gold 单元比例) vs n_realized 分域曲线 | 本分支 k7-pareto-newjudge-20261124.md · https://github.com/dd2003-460/prompt-first-bench/blob/789e7735d/modules/B-pipeline-ablation/data/t53b/k7-pareto-newjudge-20261124.md | conf 0.7（两口径一致判"缓坡"，非跳升）
│  ├─ [预算] "预算-质量非单调"降级为旧口径伪影：池化后 total 单调升（50:0.463→719:0.643），故 J 的分母惩罚真实存在，不可指望"少花节点反而更好" | 口径: 5 档 n≥3 的 total/post_acc 表复算后再判 | 同上 · https://github.com/dd2003-460/prompt-first-bench/blob/789e7735d/modules/B-pipeline-ablation/data/t53b/k7-pareto-newjudge-20261124.md | conf 0.65
│  ├─ [预算] 预算的价值是条件性的：compute-optimal 分配较 best-of-N 提效 >4×，且仅在"小模型已有非平凡成功率"的题上测试时算力才可打赢 14× 大模型 → 150 节点按边际增益分配，不均摊到每层 | 口径: marginal_gain(J_decomp) 排序分配 vs 均摊，同预算比 J | https://arxiv.org/abs/2408.03314 | conf 0.7（FLOPs-matched 结论迁移到 research 分解树=未验证）
│  ├─ [预算] 多花节点 ≠ 多质量：overthinking 普遍（大量 token 不提准确率）→ 树内重复展开/近重复议论是同型浪费，按 n_verified/n_nodes 斜率而非绝对节点数计分 | 口径: 每 run 回归斜率 β(post_acc ~ n_nodes) 跨 5 档 | https://arxiv.org/abs/2504.13367 | conf 0.6（token 域证据，节点域类比）
│  └─ [预算] "何时停"是一等变量：结构化 STOP 只省 3.70% 检索调用却掉 0.625pp EM → 不接受"自动早停无损"假设 | 口径: max_rework/stop 阈值三臂（附 A#9）比 J 与 cov | https://arxiv.org/abs/2608.13237 | conf 0.6
│
├─ N-3 检索质量轴（retrieval → verify 成功率）· 6 判定叶
│  ├─ [检索] J 的瓶颈不是排序质量而是"来源含不含该数值"：本仓 degraded 中 84% unverifiable / 6% contradicted → 提 recall 不必然提 J，应改定向数值检索（查询词带具体参数） | 口径: classify_degraded 三态占比 + 定向 vs 泛化查询臂 verified 差 | 本分支 metacog-loop-design-20261122.md + https://arxiv.org/abs/2401.15884 | conf 0.8
│  ├─ [检索] "越相关越好"被证伪：非直接相关文档拉低表现，而加入随机文档曾使准确率最高 +35% → top-k 非单调杠杆，k 须定值或按模型自选值重算 | 口径: k∈{1,3,5} 三臂同预算比 J | https://arxiv.org/abs/2401.14887 | conf 0.7（+35% 属 RAG-QA 域；开放 web 检索仅方向性 conf 0.5）
│  ├─ [检索] 检索前过"相关性评估器"是最省节点的实现：对每篇结果打 correct/incorrect/ambiguous + decompose-recompose 过滤，plug-and-play 不改权重——与题面"只用 prompt+外部工具"同构 | 口径: 有 evaluator 臂 vs 无臂的 n_search/n_total 与 post_acc | https://arxiv.org/abs/2401.15884 （代码 https://github.com/HuskyInSalt/CRAG ，477★） | conf 0.75
│  ├─ [检索] 按需检索优于每节点必检：Self-RAG 以 reflection token 自适应决定检索并提升事实性/引用准确率；FLARE 低置信时前瞻检索；Adaptive-RAG 按题复杂度路由 retriever 档位 → 检索触发率是旋钮不是"越高越好" | 口径: 触发阈值 τ 模型自选 → gold 按其实际 n_search/n_flagged 重算 | https://arxiv.org/abs/2310.11511 （https://github.com/AkariAsai/self-rag ，2452★）; https://arxiv.org/abs/2305.06983 ; https://arxiv.org/abs/2403.14403 | conf 0.7（三者原法需微调，prompt-only 只能规则近似=未验证）
│  ├─ [检索] 注入顺序/长度是隐藏成本轴：长上下文呈 U 形位置效应；Chain-of-Note 用阅读笔记提升对无关文档的鲁棒性 → 证据注入按相关性降序 + 长度上限定值 | 口径: 同证据集不同顺序的 post_acc 差 | https://arxiv.org/abs/2307.03172 ; https://arxiv.org/abs/2311.09210 | conf 0.6（262K 窗口下 27b 是否仍 U 形=未验证）
│  └─ [检索] 核验粒度决定 J 可判定性：FActScore 主张原子事实级 precision，SAFE 用搜索 agent 核长文事实；本仓按"节点"计 → 粒度不一致会系统性偏移 J | 口径: 节点级 vs claim 级两种 post_acc 并报，差 >0.05 则强制 claim 级 | https://arxiv.org/abs/2305.14251 ; https://arxiv.org/abs/2403.18802 | conf 0.6
│
├─ N-4 记忆轴（跨 session 状态保持）· 6 判定叶
│  ├─ [记忆] 跨 run 复用有机制同构的先例：Voyager 持续增长技能库（检索复用）、ExpeL（跨任务提炼自然语言 insight，性能随经验累积上升）、Reflexion（情景记忆，不改权重）→ "跨 session 状态保持"可落成 claim 库而非泛化 RAG | 口径: 库命中节点的 verify 通过率 vs 未命中节点 | https://arxiv.org/abs/2305.16291 ; https://arxiv.org/abs/2308.10144 （https://github.com/LeapLabTHU/ExpeL ，252★）; https://arxiv.org/abs/2303.11366 | conf 0.7（各家自报数字 [待交叉验证]）
│  ├─ [记忆] 库的"压缩+文档化"半边不可省：LILO=综合→STITCH 压缩→AutoDoc 文档化；STITCH 自顶向下压缩较演绎式库学习快 3–4 个数量级、省 2 个数量级内存且对早停鲁棒 → 适配 150 节点短 run | 口径: cos≥0.85 近重复合并后的库大小 vs 注入质量（下游 post_acc） | https://arxiv.org/abs/2310.19791 ; https://arxiv.org/abs/2211.16605 （POPL 2023）; https://arxiv.org/abs/2006.08381 | conf 0.7
│  ├─ [记忆] 本仓已量化库要攻击的浪费：rep 间 claim 重叠（cos≥0.85）仅 4.7% = 每 run 95.3% claim 独立重新发现 → 可省节点上限 = 重发现节点占比（不是全部检索节点） | 口径: 库臂 vs 无库臂的 n_search/n_total 差 + cov 差（150 档双臂各 ≥3 rep） | 本分支 research/q9-memory-axis-design-20261124.md（P1 阈值梯度实测） · https://github.com/dd2003-460/prompt-first-bench/blob/789e7735d/research/q9-memory-axis-design-20261124.md | conf 0.65（重叠率 0.8；"可省节点"推导 0.5 [待实验]）
│  ├─ [记忆] 锚点文档的 gap 独立核验后保留为 gap：DreamCoder/LILO/STITCH 均有固定基语言 + 可执行程序验证器；research 域"claim 等价性"无 ground-truth 验证器，只能借 judge/embedding 近似 → 记忆轴 conf 上限锁 0.7，不因先例充分而上调 | 口径: 库条目 verified 判定与 judge 一致率（人工复核 ≥30 条） | 本分支 research/dreamcoder-lilo-stitch-collision-20261123.md §4 + https://arxiv.org/abs/2310.19791 | conf 0.6
│  ├─ [记忆] 库的头号风险是污染传播而非命中率不足：持久记忆会把单轮错误固化成跨 run 系统性偏差 → "只收 status=verified 且 evidence 非空 + 每条带适用条件 docstring"定为门禁级判据 | 口径: 误用率 = 注入后判 contradicted 的节点 / 注入节点（阈值 ≤5%） | https://arxiv.org/abs/2603.20357 ; AutoDoc 依据 https://arxiv.org/abs/2310.19791 | conf 0.7
│  └─ [记忆] 缓存 ≠ 记忆：收益记"省节点"不记"省时间"——本仓 checkpoint-as-cache 前缀 122/122 逐字一致（内容层成立）但 cov↓/gap↑，wall time 省 17.4% 在 n=3 下不显著 → 以省时为卖点的记忆方案不加分 | 口径: A(从头)/B(resume) 同预算的 J 与 cov 对照 | 本分支 modules/B-pipeline-ablation/research/idea2-ab-paired-20261124.md · https://github.com/dd2003-460/prompt-first-bench/blob/789e7735d/modules/B-pipeline-ablation/research/idea2-ab-paired-20261124.md | conf 0.7
│
└─ N-5 自我认识闭环（gap 标记 → 触发重查 → 查后正确率）· 6 判定叶
   ├─ [闭环] 三环缺一不成立，且断点位置已知：monitoring 健康（healthy_gap_rate 0.938、gap 难度梯度三题 Mann-Whitney 全 p<0.001），断在 control 之后（对 unverifiable 重搜 fix rate≈0）→ "unverifiable 不触发重查"判为最优闭环设计 | 口径: gap_rate → n_search/n_flagged → post_acc 三段漏斗逐项给分 | 本分支 metacog-loop-design-20261122.md + https://arxiv.org/abs/2408.05568 | conf 0.8
   ├─ [闭环] 闭环必须外接证据而非自问自答：工具交互批评才能可靠修正，仅靠自我修订常使结果更差 → "rework 只改措辞不改证据来源"的树不加分 | 口径: 修复后 status=verified 且 retrieval_sources 非空的节点占比 | https://arxiv.org/abs/2305.11738 ; https://arxiv.org/abs/2310.01798 | conf 0.75
   ├─ [闭环] 最便宜的一步是"允许查不到"：按不确定度弃权在近零额外算力下提升正确性 2–8%、避免 50% 幻觉、安全类 +70–99% → 与题面"unverifiable 不进分母"一致，unverifiable 记为健康产出（不重查） | 口径: 三态 vs 二态质询臂的 J 与 Δn（省出节点数） | https://arxiv.org/abs/2404.10960 [数字待交叉验证] | conf 0.7
   ├─ [闭环] gap 标记可被措辞刷分：弃权率部分是 prompt 工件 → 判据须锁词表与模板定值（本仓 DEFENSIVE_PATTERNS 8 条），跨措辞扰动不稳则整项判"未测通" | 口径: 3 组同义措辞模板下 gap_rate 极差 ≤0.03 | https://arxiv.org/abs/2507.16199 + 本分支 metacog_axis.py | conf 0.75
   ├─ [闭环] "闭环变好了"须过统计闸：贪心 gate 的 FER₀ 45.59% → 统计 gate 2.78%，即单次分数上涨近半概率是噪声 → gold 只接受 ≥3 rep + 显著性的闭环改进（ε≈judge 噪声 0.1） | 口径: 前后臂 Welch t（p<0.05）+ rep 数下限 | https://arxiv.org/abs/2611.10787（数字取本分支 trust-2611.10787-note.md 对原文 L18-38 逐行核实） | conf 0.75
   └─ [闭环] 150 节点内测不出"闭环随能力/预算涌现"：该命题无 ground-truth loss，需换模型档 + 跨域重复（本仓 capability 轴 C 项阻塞）→ 列为能力边界，不据文献外推给分 | 口径: 模型标"无法验证"并给出所需实验规模即得该项分 | 本分支 GENERAL-METHODOLOGY-PATH-20261123.md C 项 · https://github.com/dd2003-460/prompt-first-bench/blob/789e7735d/modules/B-pipeline-ablation/research/GENERAL-METHODOLOGY-PATH-20261123.md | conf 0.85
```

**节点计数**: 1 根 + 5 因子分支 + 29 判定叶 = 35 节点 / 主干深度 3。**排序键 J 为唯一计分键**，其余四轴均通过 J 的分子/分母传导。

---

## 附 1 · 因子间依赖与交互（题面"另附"项）

| 耦合对 | 机制/方向 | 对 J 的净效应 | gold 处置 |
|---|---|---|---|
| 预算轴 × 检索质量轴 | 每次检索消耗 1 节点；触发率↑同抬分子分母。省检索的实测交换比：−3.70% 调用 ↔ −0.625pp EM [2608.13237] | 非线性，两轴不可各自申报 | 两轴共用同一 `n_search` 计数；τ 由模型自选则 gold 按实值重算 |
| 预算轴 × 记忆轴 | 库命中省掉"重发现"节点（本仓上限=95.3% 重叠补集），把 150 档推向 300 档覆盖 | **唯一同时降分母、保分子的正向杠杆** | 记忆轴单独计分，并要求 cov–nodes 曲线（150+库 vs 300 无库） |
| 检索质量轴 × 记忆轴 | 注入条目绕过检索 = 绕过验证 | post_acc 虚高（可靠性未证）+ 污染传播 | 注入条目必须重过质询才计入 verified |
| 能力轴 × 闭环 | 自评校准随规模且依赖格式 [2207.05221]；监控信号在权重里 [2505.21399] | 决定 gap 标记质量上限（J 的入口） | 模板/词表定值；gold 不给能力轴"越大越好"锚点 |
| 能力轴 × 预算轴 | compute-optimal 仅在"小模型已有非平凡成功率"的题上划算 [2408.03314] | 题易→预算收益高；题难→换模型优先（本题域外） | J 按难度分档报（本仓证据：gap_rate 域序 nat<soc<gpu） |
| 闭环 × 预算轴 | unverifiable 不触发重查 → 直接释放节点（本仓 46 次重拆全浪费在"查不到"） | 分母↓、cov↑ | 列为首要干预；须验证省出节点确实转成深度/覆盖 |
| 记忆轴 × 闭环（rep 方差） | 库是**故意耦合 rep 的共享先验**，与 rep 独立性实验方向相反 | rep 方差↓ ≠ 质量↑ | 库臂独立于 rep-scan；须过统计闸 [2611.10787] |
| 检索质量轴 × 闭环（分母粒度） | 节点级 vs 原子 claim 级核验改变 post_acc 分母口径 | 系统性偏移，跨模型不可比 | 粒度在 rubric（D3）前定值；本骨架建议 claim 级 |

## 附 2 · 参数定值表（硬规则①：定值 or "模型自选且 gold 按其值重算"）

| # | 参数 | 取值 | 出处/理由 |
|---|---|---|---|
| 1 | 研究预算 | 150 节点（定值，非下限） | 题面 v1（已冻结） |
| 2 | n_realized（J 分母） | `len(nodes)` @ 硬钳制后 | s5_state_machine.py:1394-1405（47a8543cd） |
| 3 | post_acc 分母 | verified + contradicted | metacog_axis.py:115-123（v1.1） |
| 4 | degraded 三态分类 | UNVERIFIABLE_RE / CONTRADICTED_RE 正则表 | metacog_axis.py:45-61（定值，不可改） |
| 5 | gap 词表 | DEFENSIVE_PATTERNS 8 条 | metacog_axis.py:26-36（定值） |
| 6 | 自评置信度问法模板 | 定值：单一 "该 claim 是否有可核验来源支持？(verified/contradicted/unverifiable)" | 由 N-1.2/N-5.4 决定；模板变体只进"扰动测试"不进正式批 |
| 7 | 检索 top-k | 默认 5（对齐 LILO/本仓锚点）；**模型自选 → gold 按其 k 重算 J** | N-3.2 非单调 |
| 8 | 库注入相似度阈值 | 默认 cos≥0.85；**模型自选 → gold 按其值重算命中率**（0.75/0.80/0.85/0.90/0.95 梯度已有实测） | 本仓 P1 阈值梯度 |
| 9 | max_rework | 默认 2（现状值）；**模型自选 → 按其值重算分母**（rework 节点计入 n_realized） | metacog-loop-design |
| 10 | 采样 | temp=0 + **串行单请求（并发数=1）** | 实测：并发×4 下同 prompt 输出全不同（verification-sop-literature-20261121.md）→ 并发不钉死则 J 不可复现 |
| 11 | 复现下限 | 每臂 ≥3 rep + Welch t p<0.05（ε≈0.1） | N-5.5 + TRUST |
| 12 | judge 口径 | cov = bge-m3 cosine≥0.70 命中 gold 单元；J 不做 judge 加权（避免与排序键混淆） | judge_v1 冻结口径 |
| 13 | J 有效性下限 | n_realized < 30 的 run 不计 J（防"极小树刷比率"退化）| **[待 D 定]**，本骨架给值不给权威 |

## 附 3 · 能力边界（题面要求显式声明"150 节点内无法验证"）

- **模型能力轴增益曲线**：需 7b/70b 换模重跑，本仓 C 项「阻塞」→ 未验证（N-1.1~1.5 只能给文献锚点，不能给数值锚点）。
- **NVFP4 在 V100(cc7.0) 上的实际数值行为**：V100 无 FP4 硬件加速路径，题面该组合本身待 D 核验；ACE 结论基于 INT4 → 未验证。
- **跨域外推**：+35%（RAG-QA）、91% pass@1（HumanEval）、15.3× 里程碑（Minecraft）、−90% token（LOCOMO）均为他域数字，方向性可用、幅度不可搬 → 全部标 [待交叉验证]。
- **"闭环随能力/预算涌现"**：无 ground-truth loss，150 节点内不可判 → N-5.6。

## 附 4 · 调研证伪记录（本轮 abs/API 逐个核验，供交叉验证门禁复用）

- `2407.20233` ≠ 自验证论文（实为 MentorAI 平台文）→ **弃用**；`2310.04530` ≠ "Just Ask for Calibration"（实为星系考古）→ 正确 ID **2305.14975**；`2305.14457` ≠ ActiveRAG（实为比较推理预训练）→ 正确 ID **2305.06983**；`2310.12148` ≠ Barzelay&Cohan（实为黑洞壳）→ 检索噪声结论改用已核验的 **2401.14887**。
- arXiv 检索未能命中 "AI Models Know They're Wrong"（Kapoor et al.）→ 该"自验证不随规模提升"结论**本轮不引用**，改由 2310.01798 + 本仓实测承担（N-1.3）。
- GitHub 实现层核验（api.github.com，本轮）：AkariAsai/self-rag 2452★、HuskyInSalt/CRAG 477★、LeapLabTHU/ExpeL 252★、stanford-oval/storm 31956★、PeterGriffinJin/Search-R1 5601★、mem0ai/mem0 69498★ —— 检索/记忆两轴**有可跑的开源实现**，能力轴与闭环两轴**无对口开源实现**（仅 prompt 组合）→ 该不对称写入 N-1/N-5 的 conf 上限。
- 与记忆轴锚点文档的差异（独立核验结论）：其 3 组件结构与 2 臂实验设计成立（N-4.1~4.5 覆盖），但**锚点漏了两条**——① 注入条目须重过质询（否则绕过验证，N-3/N-4 交互行）；② 记忆收益只可记"省节点"、不可记"省时间"（N-4.6，来自本仓 Idea2 配对统计）。

## 附 5 · 复算入口（本地实测，全部可机械重跑）

- `python3 modules/B-pipeline-ablation/metacog_axis.py --runs-dir <dir>`（J 的分子/漏斗）
- `modules/B-pipeline-ablation/research/gap-retrieval-coupling.py`（(a)→(b) 耦合 cor=+0.029/+0.064，n=15 不显著 → 支撑"N-5.1 断点在 control 之后"）
- `modules/B-pipeline-ablation/data/t53b/k7-pareto-newjudge-20261124.md`（预算曲线，N-2.2/2.3）
- `research/q9-memory-axis-design-20261124.md` + `research/dreamcoder-lilo-stitch-collision-20261123.md`（记忆轴锚点与撞车判决）
- 外部源全部为 `https://arxiv.org/abs/<id>`（本轮经 export API 核验标题/作者/摘要）与 `https://github.com/<org>/<repo>`（本轮经 api 核验存在性）。
