# idea53 推广方向调研 + 撞车分层判定（2026-11-25）

> 任务：对 idea53 新稿（加性树+微扰+级数信息增益）做推广方向调研，回答 D 四问（G1 拓扑 / G2 公式 / G3 对应 / G4 judge 加速）+ G5 分层撞车判定。
> 方法：arXiv export API 四轮共 84 组查询（33+20+21+10）+ 42 个 abs 页验证（文中引用 39 个全部覆盖）+ OpenReview 4 组搜索 + 概念最近 4 篇全文 grep（抽取完整性已对照验证）。
> 来源标注：①本轮工具输出 ②工作区文件 ③凭记忆（标 [待核验]）。所有 arXiv ID 均经 abs 页或 export API 验证。

## 1. 调研对象锚点（新稿数学骨架，5 行摘要）

- 判断写成可分解加性树：GPU 延迟 T=Σt_i，t_i=f_i/rate_i^α（叶=组件贡献，父=求和）。
- 取对数后微扰线性展开：log t_i=log f_i−α·log rate_i，弹性矩阵纯对角 ∂log t_i/∂log rate_k=−α·1[i=k]。
- P1 翻转概率闭式：P(flip)=Φ(−m/(ασ√2))，m=两最大叶对数间距（高斯扰动下 argmax 翻转）。
- P3 软判断 softmax(β·log t_i) 下信息增益二阶闭式：I₂=½(αβσ)²(1−EΣp_i²)（Fisher 形式），有效域 αβσ≤0.4。
- P2 "深层主导"拆三口径（翻转率/信息量/修正）互不一致；flat（σ=0）精确归零负控制。

## 2. G1 拓扑：树之外的节点打分理论

**结论：有先例。** 树之外的"节点/边重要性打分"在三个成熟体系里有现成理论，但都没有"可分解加性 + 对数线性微扰 + 闭式翻转"这套组合。

| 发现 | ID/年份 | 机制 | 与新稿重叠判定 | conf |
|---|---|---|---|---|
| 串并联系统可靠性精确优化 | 2107.13333 (Barrera, 2021)；1203.3307 (2012) | 串(AND/乘)并(OR)递归分解算系统可靠性 | **同机制不同包装**：都是"组合结构递归分解→聚合分数"，但代数=可靠性(乘/补)非加性延迟，无微扰翻转闭式 | 0.8 |
| 电网络/有效电阻(Kirchhoff) | 2202.12560 (Kron 约化, 2022)；1310.5163 (有向图有效电阻, 2013) | 一般图上节点/边重要性=拉普拉斯伪逆 R_ij=(L⁺)_ii+(L⁺)_jj−2(L⁺)_ij | **相邻不同机制**：都是给节点打分，但有效电阻=全局谱量(非局部可分解加性)，无翻转 | 0.75 |
| 小树宽图的精确网络可靠性 | 1712.09692 (2017)；2209.09711 (并行 BAT, 2022) | 一般图→树分解(tree decomposition)→DP 精确算可靠性 | **相邻不同机制**：树分解=把"树"推广到一般图的装置(树=特例)，但算可靠性非微扰翻转 | 0.75 |
| 超图节点打分 | — (all:hypergraph AND "node scoring" n=0) | — | 未找到 | — |
| 决策树分裂对扰动的敏感性 | 2407.03194 (Kedziora, 2024, 集成预测不稳定性) | 度量集成预测在采样扰动下的不稳定 | **相邻不同机制**：测"预测输出"不稳定，非"瓶颈叶 argmax 翻转"闭式 | 0.6 |

**G1 定位建议**：可站在可靠性理论的"递归分解组合结构"之上——串并联可靠性=加性树在可靠性代数下的同构特例，可作为"加性树是更一般组合打分的一个实例"的背书；但翻转闭式是新稿独有的增量。

## 3. G2 公式：更复杂结构的解析公式从哪来

按代数层分三段（D 2026-11-25 扩展：乘性层 + 场论层必须单独判）。

### 3a 加性/对数加性层（新稿所在层）

| 发现 | ID/年份 | 机制 | 与新稿重叠判定 | conf |
|---|---|---|---|---|
| softmax↔Boltzmann 同构 | 教科书级（exponential family；R2 查询 n=1 仅 "Exponential families from a single KL identity"） | p_i∝exp(β·log t_i)=t_i^β，即叶贡献的幂律分布；β 角色=Boltzmann 温度倒数 | **宽主题层撞车（预期老）**：同构本身无新意；新稿增量=在同构上叠微扰展开得 I₂ 二阶闭式 | 0.85 |
| max-plus/tropical 代数 | 1202.6457 (Kobayashi, 2012, "Tropical geometry of PERT") | PERT 关键路径=max-plus 最长路径；串(max)并(sum)混合=tropical 多项式 | **相邻不同机制**：max-plus 管"瓶颈=max"代数，新稿管"求和=加性"代数；混合串并联恰是 tropical 的地盘，但 tropical 侧无微扰翻转闭式（全文 grep：tropical×38, max-plus×4, flip=0） | 0.75 |
| Jaynes 最大熵 + Fisher 信息 | 0708.2879 (Dimitrov, 2007)；0907.2732 (2009, maxent 原理↔Riemann 度量) | maxent 分布=指数族；Fisher 信息度量=maxent 推断的几何 | **宽主题层撞车（预期老）**：新稿 I₂ 的 Fisher 形式在此框架内是标准件 | 0.85 |
| Fisher 信息=静态响应/涨落 | R2-fisher-susceptibility n=8（top: fidelity susceptibility & QFI） | 统计力学教科书：Fisher 信息=参数响应的涨落形式（fluctuation-dissipation） | **宽主题层撞车（预期老）** | 0.85 |

### 3b 乘性层（D 扩展①：节点值相乘/级联/乘积形式）

| 发现 | ID/年份 | 机制 | 与新稿重叠判定 | conf |
|---|---|---|---|---|
| **Jackson 网络扰动论** | 0708.1718 (Zeitak & Melamed, 2007, "Dynamics of Jackson networks: perturbation theory") | 乘积形式（product-form）排队网络的参数微扰分析：性能指标（平均逗留时间）对参数的导数闭式；乘积形式⇒节点边际局部化 | **同机制不同包装（乘性层的对角弹性等价物）**：乘积形式的局部性=乘性世界的"对角弹性"；全文 grep：perturbation×32, diagonal×5, product form×2（抽取完整性已验证 len=53942）。**但无 argmax 翻转闭式** | 0.8 |
| product-form 稳态渐近 | 2304.01499 (Dai, 2023, GJN 渐近 product-form)；0905.3158 (Mairesse, 2009, 亏零 Petri 网 product-form) | 乘积形式=各节点边际之积的精确/渐近成立条件 | **相邻不同机制**：给"何时乘积形式成立"的判据，不是微扰翻转 | 0.7 |
| 乘法噪声下的翻转概率 | —（R4-flip-multiplicative n=8 全为无关物理/通信） | — | **未找到（空白确认）**：乘性结构下闭式翻转概率无先例 | 0.7 |

**G2b 关键问题回答**：乘性结构下"对角弹性"等价物**存在**（product-form 排队扰动论，0708.1718 为 arXiv 代表；经典基础=Whittle 1980 排队网络扰动分析专著，非 arXiv [待核验]）；闭式翻转概率**不存活**（未找到，空白）。

### 3c 场论/RG 层（D 扩展②：更现代的结构）

| 发现 | ID/年份 | 机制 | 与新稿重叠判定 | conf |
|---|---|---|---|---|
| **层级最大熵 via RG** | 2509.01424 (Asadi et al., 2025, "Hierarchical Maximum Entropy via the Renormalization Group") | RG 流定义尺度层级上的最大熵条件；粗粒化=逐层条件化 | **相邻不同机制（场论层最接近先例）**：同为"层级结构+逐层条件化+信息/熵"，但其层级=变量尺度层级（lattice/场），新稿层级=被判断量的分解树；全文 grep：renormalization×48, hierarchical×66, maximum entropy×27, coarse-graining×5, **tree×0**（抽取完整性已验证 len=80293）——它不做树 | 0.75 |
| 树张量网络 TTNS / MERA | 1302.2298 (Nakatani, 2013, TTNS 量子化学)；2110.08794 (Qian, 2021, "From Tree Tensor Network to MERA") | 张量网络建在树上(TTNS)；MERA=2D 推广；二者关系有显式构造 | **相邻不同机制**：回答了"树 vs 更一般层级结构"的方向（树=张量网络的特例，MERA 是其推广），但无"节点分数/翻转"语义 | 0.75 |
| RG↔深度学习层级 | 1301.3124 (Bény & Bauer, 2013)；2010.00029 (Hu, 2020, RG-Flow 层级流模型)；1710.02079 (Foreman, 2017, RG-inspired ML 格点场论) | NN 层≈RG 粗粒化块；层级流模型用 RG 可解释 | **相邻不同机制**：层级粗粒化=树的逐层条件化？部分同构（逐层条件化语义共享），但 RG 侧无判断/翻转语义 | 0.7 |
| 格点场上的"节点分数"理论 | —（R3-lattice-field-theory/lattice-spin-node 命中均为物理解算，无 per-site importance 理论） | — | **未找到（空白确认）**：连续场/格点场上的节点重要性打分无现成理论 | 0.65 |

**G2c 关键问题回答**：D 的直觉"他们没涉及乘性和场论"**部分成立**——乘性层有排队扰动论（局部性/对角弹性等价物存在，翻转闭式不存在）；场论层有 2025 年的层级 maxent-via-RG 与 TTNS/MERA 框架（层级+条件化+信息语义存在），但"格点场上的节点分数"理论确属空白。**树不是已知的"场粗粒化极限"**——反向命题（树=场的 RG 极限）未找到先例，只有正向（树=张量网络特例）。

## 4. G3 拓扑↔公式对应：已知对应 + 哪端推导更快

**已知对应（均有文献，宽主题层）：**

| 对应 | 证据 | 机制 | conf |
|---|---|---|---|
| 有效电阻 ↔ commute time ↔ Laplacian 伪逆 | 2606.14895 (Rupchin, 2026)；1612.00731 (2016)；2109.14587 (Laplacian 伪逆性质, 2021) | commute time τ_ij=2m·R_ij；R_ij=(L⁺)_ii+(L⁺)_jj−2(L⁺)_ij；电阻距离=图不变量 | 0.85 |
| 电阻距离 ↔ 图不变量/Kirchhoff 指数 | 1905.09424 (2019)；2302.04114 (有向图电阻距离, 2023)；2603.04963 (2026) | 电阻距离谱表示↔spanning tree 计数（matrix-tree 定理） | 0.85 |
| RG 粗粒化 ↔ 层级条件化 | 2509.01424 (2025)；1301.3124 (2013) | 见 §3c | 0.75 |
| MDL/Occam ↔ 社区/模型复杂度 | 2409.10263 (MDL-Pool 图池化, 2024)；1806.07005 (MDL 热力学, 2018) | 描述长度=复杂度+拟合的分解 | 0.8 |

**"哪端推导更快"的证据：** 未找到直接对比研究（"从拓扑端推导公式 vs 从公式端推导拓扑，哪个快"的实验/理论对照）——**空白**（conf 0.7，基于 85 组查询零命中）。间接证据指向**拓扑端更快**：
- 树/串并联结构下可靠性与 PERT 关键路径的闭式都来自结构的递归分解（1202.6457：PERT 的 max-plus 闭式由图结构直接读出；2107.13333：串并联递归 DP），即"结构⇒公式"方向是构造性的。
- 反向（公式⇒结构）只有谱表示这类被动对应（电阻距离的谱公式不告诉你图长什么样）。
- 对新稿的含义：加性树的"结构⇒弹性对角+翻转闭式"正是拓扑端推导快的实例；推广时应保持"先定拓扑、再读公式"的方向。

## 5. G4 物理→judge 加速：闭式判据预言语境翻转→只审边界案例

**结论：部分先例。** "用便宜判据分流、只把边界案例送昂贵 judge"的工程范式非常成熟；但"用**闭式翻转概率**（而非学习到的置信度）做分流判据"无先例——这正是新稿 P1 的增量位。

| 发现 | ID/年份 | 机制 | 与新稿重叠判定 | conf |
|---|---|---|---|---|
| 级联分类器（cost-aware） | 1008.3742 (2010, 最优训练级联)；2110.14256 (2021, Pareto 精度-成本)；1710.03368 (2017, 摊销推理) | 便宜模型先判，不确定才升级到贵模型 | **相邻不同机制（工程范式撞车，预期老）**：分流框架相同；但判据=学习到的置信度/阈值，非闭式翻转概率 | 0.85 |
| selective prediction / abstention | 2603.21172 (2026, "Entropy Alone is Insufficient for Safe Selective Prediction in LLMs")；2605.01346 (CHASE, 2026) | 按不确定性弃权/分流 | **相邻不同机制**：同上；2603.21172 明确指出单一不确定性信号不够——支持"需要结构性判据"的论点 | 0.8 |
| LLM-judge 成本路由 | 2605.10805 (Zhang, 2026, "Reasoning Is Not Free: Robust Adaptive Cost-Efficient Routing for LLM-as-a-Judge")；2502.11021 (2025, 不确定性估计做 LLM 路由)；2510.20369 (2025, reward model 不确定时问强 LLM judge) | 按置信度/成本在 judge 间路由 | **相邻不同机制（最接近的应用先例）**：接口形态完全一致（边界案例→强 judge）；判据仍是学习置信度 | 0.8 |
| 鲁棒性证书（闭式判据分流） | 1902.01235 (Singla, 2019, ReLU 网络对抗鲁棒性证书)；2611.08035 (2026, margin 代理证书) | **闭式/可验证判据**：在证书半径内预测不变→免查；半径外才细审 | **同机制不同包装（判据哲学撞车）**：这是"闭式判据预言哪些输入在扰动下翻转→只审边界"的最直接先例！区别：它保护的是单个预测对输入扰动的不变性（安全验证），新稿保护的是瓶颈判断对参数扰动的不变性（judge 省钱）；机制同构（margin/间距↔m），领域不同 | 0.8 |
| 物理 spin flip / Kramers / Arrhenius | G4-kramers-escape n=10（Kramers 逃逸率等）；R2-escape-rate-decision n=0 | 亚稳态翻转率=Arrhenius/Kramers 公式 exp(−ΔE/kT) | **相邻不同机制**：物理"哪些态会翻转"的闭式判据存在（逃逸率），但作用于热力学态而非判断；无 judge 接口 | 0.7 |
| 决策树稳定性 | 2407.03194 (2024)；OpenReview h0vC0fm1q7 (ICLR 2025, "Sensitivity Verification for Additive Decision Tree Ensembles") | 树集成对输入扰动的敏感性**验证**（exact/approximate） | **相邻不同机制（撞车重点核查结果）**：它做"加性树集成的敏感性验证"，但方向相反——给定扰动界验证输出变化，而非给定扰动分布算翻转概率闭式；且对象是 GBDT/RF 而非瓶颈分解树 | 0.7 |

**接口可行性（一段）**：新稿 P1 的 P(flip)=Φ(−m/(ασ√2)) 可直接充当级联路由的**解析分流判据**：m 大（两最大叶间距大）→翻转概率可忽略→机械预言，免 LLM judge；m 小→边界案例→送 judge。与 1902.01235 类证书的区别在于：证书给的是**确定性不变性保证**（扰动界内必不翻），新稿给的是**概率性翻转率**（可设阈值 ε，P(flip)<ε 即免审），后者更贴近 judge 省钱的工程目标（允许小概率漏判换大比例免审）。落地需标定 σ（参数扰动的真实幅度）——这是从理论到接口的唯一额外测量项。风险：若 judge 的判断不满足"叶贡献独立高斯扰动"假设，闭式失效，需经验校准（flat 归零负控制恰好可用于此校验）。

## 6. G5 分层撞车 verdict 表

| 层 | 判据 | verdict | conf | 证据 |
|---|---|---|---|---|
| 宽主题层：扰动论/信息增益/softmax 同构/Fisher 度量 | 这些**单独**是否早有 | **有（预期老，不构成撞车）** | 0.9 | §3a 全部条目；教科书级 |
| 理论层（加性）：加性树上"翻转闭式 P1 + 级数信息增益 P3 + 对角弹性 + flat 归零负控制"的组合 | 该**组合**是否已有 | **未找到先例（空白）** | 0.75 | 84 组 arXiv 查询 + 4 组 OpenReview 零命中"组合"；最近邻 2407.03194/h0vC0fm1q7 方向相反（验证型非闭式型）；概念最近 4 篇全文 grep 无 flip/additive tree 组合 |
| 理论层（乘性，D 扩展①）：乘积形式结构上的微扰弹性/局部性 | 是否已有 | **有（局部性/对角弹性等价物）** | 0.8 | 0708.1718（Jackson 网络扰动论，product-form 微扰分析）；经典基础 Whittle 1980 [待核验] |
| 理论层（乘性）：乘性结构上的闭式翻转概率 | 是否已有 | **未找到（空白）** | 0.7 | R4-flip-multiplicative n=8 全无关；乘性噪声稳定性查询无翻转闭式 |
| 理论层（场论，D 扩展②）：层级结构+逐层条件化+信息/熵语义 | 是否已有 | **有（2025 年起活跃）** | 0.75 | 2509.01424（层级 maxent via RG）；TTNS/MERA（1302.2298/2110.08794）；RG↔ML（1301.3124/2010.00029） |
| 理论层（场论）：格点/连续场上的"节点分数"理论；树=场粗粒化极限 | 是否已有 | **未找到（空白）** | 0.65 | R3 两组查询零命中；仅正向"树=张量网络特例" |
| 经验交集层：GPU 瓶颈分解树评分 + 精确零负控制 + 预注册实验 | 是否已有 | **未找到先例（空白）** | 0.8 | 查询组 G5-dirichlet-latency/G5-elasticity-diagonal/G5-logspace-linear 全 n=0；roofline 系（R2-roofline）无微扰/翻转语义 |

**D 直觉核验结果**："信息/公式/物理里早有相关设想"——**宽主题层全中，理论层组合未中，乘性/场论层部分中**。D 的第二轮直觉"他们没涉及乘性和场论"=**部分成立**（乘性有排队扰动论、场论有层级 maxent-RG，但翻转/节点分数语义空白）。

**定位建议（撞车≠死亡）**：
1. 理论层：把 P1/P3 定位为"组合结构的扰动理论"在**加性代数**上的第一个完整闭式包（弹性+翻转+信息增益+负控制），与乘性层的排队扰动论（0708.1718）互为代数对偶——这是可站上去的叙事，不是被覆盖。
2. G4：与鲁棒性证书（1902.01235 系）明确划界——确定性不变性保证 vs 概率性翻转率分流，后者是 judge 经济学的新机制。
3. 场论层：2509.01424 是最近邻，related work 必须引它并说明层级语义差异（尺度层级 vs 分解树）。

## 7. 查询日志（全部 query 组 + 命中数 + 筛选决定）

数据文件：`/Users/a1-6/.hermes/cache/scratch/idea53-arxiv-results.json`（84 组完整条目）、`idea53-abs-verified.json`（42 ID 验证）、`idea53-fulltext-grep.json`（4 篇全文 grep）。

**R1（33 组，广撒网）：**

| tag | query | n | 筛选决定 |
|---|---|---|---|
| G1-reliability-seriesparallel | all:"series-parallel" AND all:reliability | 10 | 取 2107.13333/1203.3307（精确串并联优化）；余为分配/估计类 |
| G1-effective-resistance-graph | all:"effective resistance" AND all:graph | 10 | 取 2202.12560/1310.5163（定义+Kron）；余为应用 |
| G1-node-importance-dag | all:"node importance" AND all:"directed acyclic" | ERR | SSL EOF；未重跑（DAG 打分已由树分解条目覆盖，缺口标 §8） |
| G1-decision-tree-stability | all:"decision tree" AND all:stability AND all:perturbation | 6 | 弱命中；转向 G1-random-forest-instability |
| G1-random-forest-instability | all:"random forests" AND all:instability | 10 | 取 2407.03194（集成不稳定度量）；余为领域应用 |
| G1-bottleneck-decomposition | all:"bottleneck" AND all:"performance model" AND all:decomposition | 5 | 无对口（并行仿真/量化）；roofline 转 R2 |
| G1-hypergraph-scoring | all:hypergraph AND all:"node scoring" | 0 | 零命中→§8 缺口 |
| G1-network-reliability-exact | all:"network reliability" AND all:"exact" | 10 | 取 1712.09692（tree-width DP）/2209.09711（BAT） |
| G2-partition-softmax | all:"partition function" AND all:softmax | ERR | SSL EOF；教科书级同构，缺口标 §8 |
| G2-tropical-maxplus | all:"max-plus" AND all:algebra | 10 | 取 1202.6457（PERT tropical，R2 确认）；余为代数结构 |
| G2-maxent-jaynes | all:"maximum entropy" AND all:inference AND all:Jaynes | 10 | 取 0708.2879/0907.2732；余为应用 |
| G2-fisher-static-response | all:"Fisher information" AND all:"static response" | 0 | 零命中→改 R2-fisher-susceptibility（n=8，教科书级） |
| G2-boltzmann-freeenergy | all:"Boltzmann distribution" AND all:"free energy" AND all:"Feynman-Kac" | 0 | 零命中；Feynman-Kac 表述过窄，教科书级不追 |
| G2-closedform-flip | all:"flip probability" AND all:"closed form" | 4 | 全无关（教育/通信/解码）→支持空白 |
| G2-info-gain-perturbation | all:"information gain" AND all:perturbation AND all:"closed form" | 1 | 无关（Bayesian OED）→支持空白 |
| G3-resistance-commute | all:"effective resistance" AND all:"commute time" | 10 | 取 2606.14895/1612.00731 |
| G3-resistance-distance-laplacian | all:"resistance distance" AND all:Laplacian | 10 | 取 1905.09424/2302.04114/2603.04963 |
| G3-rg-coarsegraining | all:"renormalization group" AND all:"coarse graining" AND all:hierarchical | 10 | 弱命中；RG 层转 R3 |
| G3-mdl-occams | all:"minimum description length" AND all:Occam | 10 | 取 2409.10263/1806.07005 |
| G4-selective-prediction | all:"selective prediction" AND all:abstention | 10 | 取 2603.21172/2605.01346 |
| G4-cascade-classifier | all:"cascade" AND all:classifiers AND all:cost | 10 | 取 1008.3742/2110.14256/1710.03368 |
| G4-kramers-escape | all:"Kramers" AND all:"escape rate" | 10 | 物理侧确认存在（无 judge 接口），不深入 |
| G4-arrhenius-activation | all:"Arrhenius" AND all:"thermal activation" AND all:barrier | 10 | 同上 |
| G4-margin-routing | all:"margin" AND all:confidence AND all:routing AND all:classifier | 4 | 弱命中；LLM 路由转 R2 |
| G4-two-stage-screening | all:"two-stage" AND all:classifier AND all:screening | 10 | 领域应用为主，不取 |
| G4-llm-judge-efficient | all:"LLM-as-a-judge" AND all:efficient | 10 | 取 2605.10805/2510.20369/2502.11021（R2 补充） |
| G4-perturbation-boundary | all:"decision boundary" AND all:perturbation AND all:"closed form" | 3 | 取 1902.01235（证书系入口） |
| G5-additive-tree | all:"additive tree" | 10 | 全为图算法/回归树（含 2006.11771 协方差、2508.03059 密度比）→无瓶颈分解语义 |
| G5-flip-closedform | all:"flip probability" AND all:"closed-form" | 4 | 同 G2-closedform-flip，无关 |
| G5-softmax-fisher-hessian | all:softmax AND all:"Fisher information" AND all:Hessian | 1 | 无关（谱病态）→支持空白 |
| G5-dirichlet-latency | all:Dirichlet AND all:latency AND all:bottleneck | 0 | 零命中→经验层空白证据 |
| G5-elasticity-diagonal | all:elasticity AND all:"diagonal" AND all:perturbation AND all:scoring | 0 | 零命中→经验层空白证据 |
| G5-logspace-linear | all:"log space" AND all:"linear" AND all:"perturbation" AND all:"decision" | 0 | 零命中→经验层空白证据 |

**R2（20 组，定向）：** R2-reliability-polynomial n=8（几何性质，不取）；R2-critical-path-maxplus n=1（**1202.6457 确认**）；R2-fisher-susceptibility n=8（教科书级确认）；R2-fisher-thermo-response n=8（同上）；R2-decision-tree-noisy-labels n=0（缺口）；R2-additive-tree-boosting n=8（GBDT 系，无瓶颈语义）；R2-roofline n=8（经验层：roofline 无微扰/翻转语义）；R2-jackson-network n=4；R2-conformal-selective n=8（保形选择性预测，机制=覆盖保证，不取为最近邻）；R2-relu-certificates n=8（取 1902.01235/2611.08035）；R2-order-stats-gaussian-max n=8（弱）；R2-softmax-boltzmann n=1（指数族恒等式）；R2-kirchhoff-spanning n=8（matrix-tree，G3 佐证）；R2-instability-measure n=8（取 2407.03194 佐证）；R2-margin-flip n=6（取 2611.08035）；R2-escape-rate-decision n=0（物理↔决策接口空白证据）；R2-hierarchical-model-conditional n=8（弱）；R2-queueing-series-parallel n=0（缺口）；R2-performance-model-closed n=1（无关）；R2-judge-routing-margin n=8（取 2605.10805/2510.20369/2502.11021）。

**R3（21 组，D 扩展：乘性+场论）：** R3-jackson-product-form n=8（取 0905.3158）；R3-product-form-queueing ERR（SSL EOF，由 0708.1718 覆盖）；R3-jackson-network n=8（Perfect Sampling，不取）；R3-open-queueing-network n=0；R3-multiplicative-noise n=8（控制论稳定，无翻转）；R3-cascade-latency n=8（LLM 级联 RL，不取）；R3-series-composition-delay n=0（乘性延迟组合空白证据）；R3-product-moment-latency n=4（弱）；R3-multiplicative-perturbation n=8（矩阵分解界，无翻转）；R3-matrix-geometric-queues n=8（区块链排队，不取）；R3-wilson-rg-flow n=8（Wilson 流，场论层背景）；R3-lattice-field-theory n=8（可视化包，无节点分数）；R3-tensor-network-rg n=8；R3-MPS-rg n=8（MPS 重整化）；R3-MERA n=8（Kondo MERA）；R3-real-space-rg n=8（实空间 RG）；R3-hierarchical-coarse-graining n=5（Nystrom Markov 态模型，弱）；R3-conditional-hierarchy-markov n=0；R3-tree-tensor-network n=8（取 1302.2298/2110.08794）；R3-rg-machine-learning n=8（取 2010.00029/1710.02079）；R3-lattice-spin-node n=8（物理解算，无 per-site importance）；R3-effective-action-integrate-out n=8（HTL 有效作用量，背景）。

**R4（10 组，缺口补查）：** R4-flip-multiplicative n=8（全无关→乘性翻转空白）；R4-bottleneck-closedform n=3（信息瓶颈 RG，不取）；R4-sp-closedform n=8（串并联闭式成本，G1 佐证）；R4-minplus-bottleneck n=5（APSP 归约，不取）；R4-tropical-scheduling n=8（tropical 调度，G2 佐证）；R4-product-form-stationary n=8（亏零 Petri 网，0905.3158 佐证）；R4-tree-coarsegrained-limit n=6（代数粗粒化，弱）；R4-perturbation-analysis-queueing n=8（M/M/1 扩散环境扰动，0708.1718 佐证）；R4-influence-function n=8（影响函数=一阶扰动，机制佐证不取）；R4-leave-one-out-stability n=8（LOO CMI，不取）。

**OpenReview（4 组，api2.search）：** "flip probability" n=5（**"Flip Probability Scores" nuezWeGYKN 2025-08 投稿，无 venue/摘要→[待核验]**；tIUeexYnoX=ICLR 2027 withdrawn 医学影像，不取）；"additive tree" n=5（**h0vC0fm1q7=ICLR 2025 Poster "Sensitivity Verification for Additive Decision Tree Ensembles"**，已取）；"information gain perturbation closed form" n=5（全无关）；"bottleneck decomposition judge" n=5（LLM judge 评估类，无闭式判据分流）。

## 8. 缺口清单（搜不到的标 [待核验]，不编）

1. **[待核验] Whittle (1980) 排队网络扰动分析专著**——乘性层经典基础，非 arXiv，未及核验书目细节（作者全名/出版社）。
2. **[待核验] OpenReview "Flip Probability Scores"（nuezWeGYKN, 2025-08）**——标题命中但无 venue/摘要，403 无法拉详情；若其为"翻转概率作为评分"的方法论，可能触及 G4 判据层，需人工点开确认。
3. **DAG 上节点打分理论**——R1-node-importance-dag 查询 SSL 失败未重跑；现有证据（树分解/有效电阻）覆盖"一般图"但未专门覆盖 DAG 打分，conf 降档。
4. **partition function × softmax 的 arXiv 文献锚点**——R1 查询 SSL 失败；该同构为教科书级（exponential family），不阻塞结论但缺 arXiv 引用。
5. **乘性延迟系统的扰动理论**（端到端延迟=各跳延迟之积/级联）——R3-series-composition-delay n=0；排队侧有 0708.1718，但"网络延迟乘积"语义未找到专文。
6. **"哪端推导更快"的直接对比研究**——84 组查询零命中；§4 的"拓扑端更快"仅为间接证据（conf 0.7）。
7. **树=场粗粒化极限**——未找到先例；若 D 要主张此方向，属原创命题而非引用。
8. **G4 物理接口**（Kramers/Arrhenius 逃逸率→judge 翻转率的显式映射）——未找到；§5 接口段为本次调研的原创构造，非文献结论。
