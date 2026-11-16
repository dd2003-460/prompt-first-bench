# SOC pending77 节点分类 — method-reviewer 独立分类

**origin: ai** · 分类人: method-reviewer (Hermes subagent) · 2026-11-16
**数据文件**: `experiments/stage-ablation/checkpoints/sm-soc-r1.json`（只读，未改动）
**范围**: pending 77（N1-N5, N35-N106）+ degraded 31，逐条分类 A/B/C 与 D/E
**checkpoint 状态基线**: verified=174, pending=77, degraded=31, failed=1, total=283, cov=0.615

## 方法说明（分类依据全部来自节点字段，不凭 claim 文字感觉）

**字段事实（脚本统计，可复现）**：
- pending 77 全部 `evidence=""`、`retrieval_sources=[]`（77/77 零证据零来源）
- pending 按 source 分布：knowledge=45, search=27, given=5
- pending 中 search_query 非空 34 条，空 43 条
- degraded 31 中 30 条 evidence 非空（N250 为空），26 条 search_query 非空，17 条 retrieval_sources 非空
- 全部 77 条 pending 均为 L1(5)/L3(72)；31 条 degraded 为 L2(5)/L3(1)/L4(25)
- checkpoint `network_degraded=false`；rework_events 显示 N28/N29 曾出现「检索失败: no sources from any channel (all 5 failed)」——即检索通道曾整体挂掉，这是 B 类判定的背景事实

**分类规则（机械可判，逐条引用字段）**：

pending 77：
- **A-可翻**：`source=given` 且 claim 含可直接核验的事实断言（明确数值/日期/定义/标准公式），evidence 缺失但可补。
- **B-需检索**：`source=search`（或 claim 明确「需检索/需从平台日志/需 A/B 测试/需爬虫」）且断言有明确外部来源存在（费率表/年报/公开研究/行业基准），来源存在但通道挂（retrieval_sources=[] 且 evidence=""）。
- **C-难核**：claim 本身模糊/复合/依赖主观判断/是推导框架或自设参数，公开来源基本不存在；或 source=knowledge 的纯推导/建模断言（无外部来源可补）。

degraded 31：
- **D-可救**：evidence 部分存在（rework 已记录「逻辑自洽」或来源存在但不对题），只差补强（换检索词/补直接来源）。
- **E-弃**：claim 本身站不住（公式量纲错/参数无出处且不可补/纯自设假设无验证路径）。

---

## 一、pending 77 逐条分类

格式：`节点id | 分类 | 一句话理由（引用字段）`

### given 5 条

- N1 | C-难核 | source=given 但 claim 是「构建演化-行为因果链」的框架性任务描述（L1），非事实断言，无可核验数值/日期/定义
- N2 | C-难核 | source=given，claim 是「解释两现象内在一致性」的分析任务（L1），非事实断言，无明确数值
- N3 | C-难核 | source=given，claim 是「识别核心驱动方」的归因任务（L1），依赖主观判断，无公开来源
- N4 | C-难核 | source=given，claim 是「设计最小干预+评估外部性」的设计任务（L1），非事实断言
- N5 | C-难核 | source=given，claim 是「置信度分级标注」的元任务（L1），非事实断言

### search 27 条

- N35 | C-难核 | source=search，claim 的 CV≈5-10%/20-40% 是「感知方差」的自设参数，无公开来源可核（evidence=""，rs=[]）
- N45 | C-难核 | source=search，claim 要求「估算二手平台买家保留效用分布」——平台私有数据，公开来源基本不存在
- N47 | C-难核 | source=search，claim 要求「从平台日志中计算 Corr」——平台私有日志，公开来源不存在
- N48 | C-难核 | source=search，claim 要求「构建逻辑回归并验证 β1 显著性」——需平台私有数据跑回归，公开来源不存在
- N52 | B-需检索 | source=search，claim 是明确事实断言（闲鱼/eBay 佣金率 2.5%-5%），rq 非空（'used goods marketplace commission rate percentage eBay Xianyu 2023'），来源存在（平台公开费率页）但 rs=[]/evidence=""
- N69 | B-需检索 | source=search，rq 非空（'...buyer search time cost reduction price label experiment'），claim 中 T_search 基线有公开研究可查（眼动/比价时长实验），通道挂（rs=[]）
- N70 | B-需检索 | source=search，rq 非空（'price transparency label conversion rate uplift A/B test e-commerce'），电商 A/B 测试公开文献存在，rs=[]
- N73 | C-难核 | source=search，claim 是「需基于 N27 的分布计算占比」的推导任务，依赖 N27 本身（N27 在 degraded，未 verified），无独立公开来源
- N79 | B-需检索 | source=search，rq 非空（'NPS net promoter score revenue retention correlation e-commerce benchmark'），NPS-留存行业基准有公开咨询报告（Bain 等），rs=[]
- N82 | C-难核 | source=search，claim 要求「估计 δ_quality」——需平台商品质量标注数据，公开来源不存在
- N84 | B-需检索 | source=search，rq 非空（'e-commerce platform click to inquiry conversion rate baseline statistics'），claim 断言点击-咨询转化率 5-15% 有行业基准可查，rs=[]
- N86 | B-需检索 | source=search，rq 非空（'...platform annual report commission optimization strategy'），claim 本身就是「检索平台年报/招股书/高管演讲」的任务，来源明确存在（eBay 10-K 等），rs=[]
- N87 | B-需检索 | source=search，rq 非空（'eBay Mercari Xianyu commission rate structure...'），eBay/Mercari 公开费率结构可查（eBay FVF 页），rs=[]
- N88 | C-难核 | source=search，claim 要求「爬虫获取平台首页高溢价商品占比」——需实时爬取平台私有数据，非静态公开来源
- N92 | C-难核 | source=search，claim 要求「通过平台日志计算独立买家咨询率比值 ρ」——平台私有日志
- N93 | C-难核 | source=search，claim 断言闲鱼/Depop 挂价偏度>1.5、99th/Median>4.0——平台私有分布统计，公开来源基本不存在
- N94 | C-难核 | source=search，claim 断言品类偏离度 8-12%/20-30% 并「需建立品类-偏离度映射表」——平台私有数据
- N95 | C-难核 | source=search，claim 要求「回归分析（挂价 vs 新品原价）」——需平台成交数据跑回归
- N98 | C-难核 | source=search，claim 断言竞争密度弹性 ε_T,D≈-0.5——自设参数，无公开来源
- N99 | C-难核 | source=search，claim 断言零点击占比 30-40%——平台行为漏斗私有数据
- N100 | C-难核 | source=search，claim 断言 β≈-0.6 及「偏离度>20% 时咨询转化率降 50%」——平台私有数据
- N101 | C-难核 | source=search，claim 断言 Boost Factor≈1.2-1.5——平台算法私有参数
- N102 | C-难核 | source=search，rq 空，claim 断言「紧迫性指标提升、决策时间缩短 20-30%」——自设量化，无公开来源
- N103 | C-难核 | source=search，rq 空，claim 是噪声参数化模型（ε~N(0,σ²)）+「P(T<48h|P>1.15...)」推导，自设参数
- N104 | C-难核 | source=search，rq 空，claim 断言「信任折扣 10-15%」——自设参数，无公开来源
- N105 | C-难核 | source=search，rq 空，claim 断言「咨询延迟 2-3 倍」——自设参数，无公开来源
- N106 | C-难核 | source=search，rq 空，claim 是「统一假设框架的逻辑自洽性检验」——复合框架断言，非单一事实

### knowledge 45 条

- N36 | C-难核 | source=knowledge，claim 断言「10-15% 买家右尾概率」——自设参数（rq 非空但 source=knowledge 表明走的是知识推导而非检索通道）
- N37 | C-难核 | source=knowledge，claim 断言 β≈1.2——自设基准参数，无公开来源
- N38 | C-难核 | source=knowledge，claim 断言 γ≈0.3——自设参数
- N39 | C-难核 | source=knowledge，claim 是最优价格一阶条件推导（P*=C/(1-1/β_eff)）——数学推导框架，非事实断言
- N40 | C-难核 | source=knowledge，claim 是临界条件不等式推导——数学推导，无公开来源
- N41 | C-难核 | source=knowledge，claim 是 T(D) 函数形式 +「需分解为...」——建模任务
- N42 | C-难核 | source=knowledge，claim 是 R_consult(ΔP) 函数形式 +「需分解为...」——建模任务
- N43 | C-难核 | source=knowledge，claim 是 λ_effective=λ_base+β*σ² 参数耦合 +「需量化 β」——自设模型
- N44 | C-难核 | source=knowledge，claim 是 Spence 分离均衡推导 +「需计算 θ* 与 0.85 偏差」——推导任务，0.85 本身无来源（见 N10 degraded）
- N46 | C-难核 | source=knowledge，claim 是混合策略均衡分析 +「需计算 R_consult(q)」——推导任务
- N49 | C-难核 | source=knowledge，claim 是 P_market 口径定义（加权中位数+排除 2σ 异常值）——方法论定义，非可核验事实
- N50 | C-难核 | source=knowledge，rq 空，claim 是佣金下最优定价公式——数学推导
- N51 | C-难核 | source=knowledge，rq 空，claim 断言 P*_λ 比 P* 高 15-20%（「基于典型二手品类弹性估算」）——自设估算
- N53 | C-难核 | source=knowledge，rq 空，claim 是买家净效用公式 +「需计算正负」——推导任务
- N54 | C-难核 | source=knowledge，rq 空，claim 是卖家净收益公式 +「需比较差值」——推导任务
- N55 | C-难核 | source=knowledge，rq 空，claim 是平台净收益公式 +「需计算 d(r*P*Q)/dr」——推导任务
- N56 | C-难核 | source=knowledge，rq 空，claim 含自设参数组（P=500元, ΔT_s=2天, C_t=10元/天, ΔCS=50元）推得 r≈1.4%——自设参数推导，非事实
- N57 | C-难核 | source=knowledge，rq 空，claim 是 GMV/留存率定义式——定义，非可核验事实断言
- N58 | C-难核 | source=knowledge，rq 空，claim 是损失率约束 ≤5% +「需基于 N17 计算」——推导任务
- N59 | C-难核 | source=knowledge，rq 空，claim 是搜索成本约束 ≤10% + NPS 对应关系——自设约束
- N60 | C-难核 | source=knowledge，rq 空，claim 是干预措施(1)的 GMV 增量估算（3%+8%）——自设估算
- N61 | C-难核 | source=knowledge，rq 空，claim 是干预措施(2)的 GMV 增量估算（15%*50%*(2%+4%)）——自设估算
- N62 | C-难核 | source=knowledge，rq 空，claim 是干预措施(3)的 GMV 增量估算（0.7*1.2-1）——自设估算
- N63 | C-难核 | source=knowledge，rq 空，claim 是阈值敏感性估算（X=10%→25%, X=20%→10%）——自设估算
- N64 | C-难核 | source=knowledge，rq 空，claim 是数据依赖规则（n<5 不展示，覆盖 15%）——自设规则
- N65 | C-难核 | source=knowledge，rq 空，claim 是反馈循环估算（咨询降 20%→降价 5%）——自设估算
- N66 | C-难核 | source=knowledge，rq 空，claim 是弹性异质性断言（-1.2/-0.4, 15%→25%）——自设参数
- N67 | C-难核 | source=knowledge，rq 空，claim 是 15% 调整率拆解（5%+10%）——自设拆解
- N68 | C-难核 | source=knowledge，rq 空，claim 是利润非线性影响估算（约 10% 卖家反对）——自设估算
- N71 | C-难核 | source=knowledge，rq 空，claim 是锚定效应公式 + α>0.5 阈值——自设参数
- N72 | C-难核 | source=knowledge，rq 空，claim 是净效应阈值 +「需计算 X_critical」——推导任务
- N74 | C-难核 | source=knowledge，rq 空，claim 是 V_original 计算 + 子群加权——推导任务
- N75 | C-难核 | source=knowledge，rq 空，claim 是 Q_adjusted 模型 +「需验证线性近似」——建模任务
- N76 | C-难核 | source=knowledge，rq 空，claim 是 ΔLoss 计算 +「需计算占 GMV 比例」——推导任务
- N77 | C-难核 | source=knowledge，rq 空，claim 是 ΔGMV 分解 +「需分别量化」——推导任务
- N78 | C-难核 | source=knowledge，rq 空，claim 是 S_time 公式 +「需结合 N30 计算」——推导任务
- N80 | C-难核 | source=knowledge，rq 空，claim 是置信度公式 +「n>1000 且 d>0.5 时下限 80%」——自设标准
- N81 | C-难核 | source=knowledge，rq 空，claim 是数据源分级权重（1.0/0.7/0.4）——自设标准
- N83 | C-难核 | source=knowledge，rq 非空但 claim 是因果识别策略（DID/IV/Heckman）+「置信度维持 60-70%」——方法论选择，非事实断言
- N85 | C-难核 | source=knowledge，rq 空，claim 是噪音过滤规则（>10 次剔除，波动 [55%,65%]）——自设规则
- N89 | C-难核 | source=knowledge，rq 空，claim 是 A/B 测试设计 + 预期区间 ΔC∈[8%,12%]——实验设计，非事实
- N90 | C-难核 | source=knowledge，rq 空，claim 是信任度公式 T=1-(举报率/浏览量) + T<0.7 阈值——自设公式
- N91 | C-难核 | source=knowledge，rq 空，claim 是贝叶斯更新 +「P(H|E) 从 0.65 降至 0.45」——自设先验推导
- N96 | C-难核 | source=knowledge，rq 空，claim 是 STR 指数衰减 + k∈[5,10]——自设参数
- N97 | C-难核 | source=knowledge，rq 空，claim 是筛选效应修正 +「比值通常小于 0.7」——自设参数

**pending 小计：A=0, B=7, C=70**

---

## 二、degraded 31 逐条分类

格式：`节点id | 分类 | 一句话理由（引用字段）`

- N10 | E-弃 | evidence 明确「阈值 0.85 为经验参数，无来源支持且非第一性原理可推导」——参数无出处且不可补，rework 1 次已降级
- N11 | E-弃 | evidence 明确来源[1][2]「未提供 60% 卖家或高挂价比例的具体数据支持」——claim 的核心数字（60%、20%）无来源，rework 1 次
- N27 | E-弃 | evidence 明确来源[1][2]「未提供挂价分布的具体统计参数」——中位数高 10-15%、90th 为 2-3 倍无来源，rework 1 次
- N28 | D-可救 | evidence=「检索失败: no sources from any channel (all 5 failed)」——通道挂导致降级，claim 是方法论断言（区分全量/成交周期），逻辑自洽，换通道可补
- N29 | D-可救 | evidence=「检索失败: no sources from any channel (all 5 failed)」——同上，claim 是数据口径界定，逻辑自洽
- N31 | E-弃 | evidence 明确来源[1][2][3]「均与损失厌恶系数的具体统计参数无关」——σ_λ≈0.4 无来源
- N126 | E-弃 | evidence 明确来源[1][2][3]「均涉及宏观通胀、货币政策或股市波动，与该微观定价策略完全无关」——γ 跃升 0.6-0.8 无来源
- N153 | E-弃 | evidence 明确「参考来源均与二手市场品类波动率无关」——20%/5% 波动率无来源
- N155 | E-弃 | evidence 明确来源「仅涉及 Redis Geo 技术实现及 LBS 概念」——50km 半径、β≈0.5 元/km 无来源
- N156 | D-可救 | evidence=「经验事实，逻辑自洽但缺来源支持」——闲鱼/转转/Depop 费率 0%~6% 有公开来源（平台费率页），rs=[] 但 rq 非空，换检索词可补
- N157 | E-弃 | evidence 明确来源「仅定义弹性概念，未提供二手市场具体品类的实证数值」——ε≈2.0~2.5/1.2~1.8/3.0+ 无来源
- N160 | E-弃 | evidence 明确来源[1][2]「分别关于作家传记和城市定义，与该事实主题完全无关」——δ=0.05/day 无来源
- N161 | D-可救 | evidence=「参考来源[1][2][3]均未包含 eBay 具体费率数据」——eBay FVF 13.25% 有官方费率页（rq 非空 'eBay final value fee schedule 2024'），来源存在但检索未命中
- N162 | D-可救 | evidence=「经验事实，逻辑自洽但缺来源支持」——闲鱼 0 佣金政策有公开报道（rq 非空 'Xianyu Alibaba...commission rate 2024'），来源存在
- N182 | E-弃 | evidence 明确「NPS 与搜索成本的具体量化对应关系属于经验事实，且无可用外部来源支持」——+5-10 分对应 5-15% 无来源
- N190 | D-可救 | evidence=「逻辑校验通过：对数正态分布假设下，若 σ=0.2，P(X>10%)≈31.4%，与 25% 量级接近但非精确匹配，需具体 σ 值验证」——数学推导成立，只差 σ 值（rq 非空，可检索）
- N194 | E-弃 | evidence 明确参考来源（Asda、次贷危机、可持续采购）「与该具体电商业务指标完全无关」——15%/40%/12% 无来源
- N198 | E-弃 | evidence 明确来源[1][2]「仅涉及零售品类策略与结构优化，未包含 E=-1.2、标签感知价差修正」——25% 调整率无来源
- N222 | D-可救 | evidence=「逻辑自洽，但属于经验事实且无可用外部来源支持」——工作点 A 是场景假设（非事实断言），逻辑自洽，可保留为假设
- N224 | D-可救 | evidence=「逻辑自洽，但属于经验事实且无可用外部来源支持」——工作点 C 是场景假设，逻辑自洽
- N225 | D-可救 | evidence=「参考来源[1][2][3]均与二手平台价格敏感度弹性系数无关」——ΔConv 公式逻辑自洽，E_price 可检索（rq 非空）
- N227 | D-可救 | evidence=「参考来源均与二手电商比价时长无关」——T_saved 公式逻辑自洽，S_min 可检索（rq 非空 'average time spent comparing prices'）
- N228 | D-可救 | evidence=「参考来源[1]仅定义雇佣关系，[2]为沃尔玛简介」——V_time 公式逻辑自洽，目标用户时薪可检索（rq 非空）
- N230 | D-可救 | evidence=「属于经验事实且无可用外部来源支持」——NPS+10 分对应留存 5-10% 有公开咨询报告（Bain），rq 非空
- N250 | E-弃 | evidence=""（空），claim 断言 ∂P*/∂r≈-13.33——公式量纲可疑（佣金率每增 1 个百分点，P* 降 13.33% 不合直觉），无证据无来源
- N261 | E-弃 | evidence 明确「参考来源均为美剧剧集列表，与二手平台咨询行为完全无关」——重复咨询频次分布无来源
- N273 | D-可救 | evidence=「属于经验事实且检索无可用来源」——β≈-0.6 是负相关断言（逻辑自洽），rq 非空，可换检索词
- N276 | E-弃 | evidence=「属于经验事实（平台算法参数），且无可用外部来源支持」——Boost 公式 α∈[0.1,0.3] 是平台私有参数，不可补
- N278 | E-弃 | evidence=「属于经验事实（具体统计比例与画像特征），且本轮检索无可用来源支持」——60% 零点击卖家是长尾非专业、曝光低 80% 无来源
- N279 | E-弃 | evidence=「属于具体经验事实（特定脑区活动变化及 20-30% 决策时间缩短的具体数值），且本轮检索无可用来源支持」——fMRI 具体数值无来源
- N292 | E-弃 | evidence 明确「参考来源均为通用市场营销概念，未提供该特定数学模型或实证数据支持」——T 公式的 β/γ 无来源

**degraded 小计：D=10, E=21**

---

## 三、汇总

| 类别 | 计数 | 说明 |
|------|------|------|
| A-可翻 | 0 | pending 中 source=given 的 5 条全是 L1 框架/任务描述，非事实断言 |
| B-需检索 | 7 | N52, N69, N70, N79, N84, N86, N87 |
| C-难核 | 70 | 其余 pending（含 45 条 knowledge 推导/自设参数 + 20 条 search 平台私有数据/自设参数） |
| D-可救 | 13 | N28, N29, N156, N161, N162, N190, N222, N224, N225, N227, N228, N230, N273 |
| E-弃 | 18 | 其余 degraded |

D+E=31 ✓

**现实上限 = (174 + A + D) / 283 = (174 + 0 + 13) / 283 = 187/283 = 0.661**

**与 lead 估算 0.813 的差距**：
- lead 估算 A=46（「pending 77 中约 46 个是 knowledge/given 类可翻 verified」）+ D=10 → (174+46+10)/283 = 230/283 = 0.813
- 本分类 A=0（given 5 条全是框架任务，knowledge 45 条全是推导/自设参数，无一可翻）+ D=13 → 187/283 = 0.661
- **差距 0.152（0.813 - 0.661）**，主因是 lead 把 46 条 knowledge/given 当成「可翻 verified」，但逐条核后这些节点全是推导框架或自设参数，没有一条是「有明确数值/日期/定义且 evidence 缺失但可补」的事实断言。
- 若 B 类 7 条检索通道修复后能补上来源（乐观情形），上限可升至 (174+7+13)/283 = 194/283 = 0.686，仍远低于 gate 要求的 0.898。

**结论**：lead 的 0.813 上限不成立。现实上限 0.661（保守）~0.686（乐观，B 类全补上），距 gate 0.898 差 0.212~0.237。gate 在当前 checkpoint 结构下不可达，除非：(1) 重新生成 checkpoint 让 pending 节点走通检索通道，或 (2) 放宽 gate 阈值，或 (3) 接受 cov=0.661 作为该臂的真实水平。

---

## 四、分类依据可复现性

所有分类基于节点字段（source/evidence/search_query/retrieval_sources/claim 中的数字），可用以下脚本复现字段统计：

```python
import json
from collections import Counter
d = json.load(open('experiments/stage-ablation/checkpoints/sm-soc-r1.json'))
nodes = d['nodes']
pend = [n for n in nodes if n['status']=='pending']
deg = [n for n in nodes if n['status']=='degraded']
print('pending by source:', Counter(n['source'] for n in pend))
print('pending with rq:', sum(1 for n in pend if n['search_query']))
print('pending with rs:', sum(1 for n in pend if n['retrieval_sources']))
print('pending with ev:', sum(1 for n in pend if n['evidence']))
print('degraded by source:', Counter(n['source'] for n in deg))
print('degraded with ev:', sum(1 for n in deg if n['evidence']))
print('degraded with rq:', sum(1 for n in deg if n['search_query']))
print('degraded with rs:', sum(1 for n in deg if n['retrieval_sources']))
```
