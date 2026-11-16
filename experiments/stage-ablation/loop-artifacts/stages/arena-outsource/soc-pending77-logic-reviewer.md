# soc-pending77-logic-reviewer — pending 77 / degraded 31 独立分类

**origin: ai** · logic-reviewer（与 method-reviewer 独立，未读其结果）· 2026-11-16
数据文件：`experiments/stage-ablation/checkpoints/sm-soc-r1.bak-verifyonly.json`（283 节点，verified=174 / pending=77 / degraded=31 / failed=1，与任务书口径一致；主 checkpoint `sm-soc-r1.json` 已被后续 verify-only 轮更新为 221-verified，本任务按任务书口径只读 bak 文件，未改动任何 checkpoint）

## 分类规则（逐字执行任务书定义）

- **A-可翻**：source=given 且 claim 是可直接核验的事实断言（有明确数值/日期/定义，evidence 缺失但可补）
- **B-需检索**：需要外部来源（search_query 非空或 retrieval_sources 为空的事实断言），来源存在但通道挂
- **C-难核**：claim 本身模糊/复合/依赖主观判断，公开来源基本不存在
- **D-可救**（degraded）：evidence 部分存在、只差补强
- **E-弃**（degraded）：claim 本身站不住

字段口径说明：pending 77 全部 evidence 为空、retrieval_sources 全部为空（程序核验：`sum(evidence)=0, sum(rs)=0`）；search_query 非空 34 条（source=search 27 条全部非空，source=knowledge 7 条非空）。degraded 31 中 evidence 非空 30 条（N250 为空），retrieval_sources 非空 17 条。

## 一、pending 77 逐条分类

### source=given（5 条，全部 L1 任务描述）

| 节点 | 分类 | 理由（引用字段） |
|------|------|------------------|
| N1 | C | source=given, L1, search_query 空；claim 是「构建…因果链…作为统一假设基础」的任务描述，非事实断言，无可核验数值/日期/定义，不满足 A 类条件 |
| N2 | C | source=given, L1, search_query 空；claim 是「具体解释…内在一致性」的分析任务，依赖 N1 假设链，非独立事实断言 |
| N3 | C | source=given, L1, search_query 空；claim 是「识别…核心驱动力」的归因任务，答案依赖平台数据（私有），公开来源不存在 |
| N4 | C | source=given, L1, search_query 空；claim 是「设计…干预措施」的设计任务，主观判断，无公开可核事实 |
| N5 | C | source=given, L1, search_query 空；claim 是「置信度分级标注」的方法任务，无明确数值/定义可核 |

### source=search（27 条）

| 节点 | 分类 | 理由（引用字段） |
|------|------|------------------|
| N35 | B | search_query 非空（"variance of buyer valuation standardized vs non-standardized goods…"）；claim 含明确数值（CV≈5-10% / 20-40%），属可检索经验事实，检索通道挂（retrieval_sources 空） |
| N36 | C | search_query 非空但 claim 是自设参数（「15-25% 时仍有 10-15% 买家右尾成交」为本模型假设），非公开可核事实 |
| N37 | C | search_query 非空但 claim 是需求函数基准形式 Q(P)=A*(Pm/P)^β、β≈1.2 的自设基准参数，非公开事实断言 |
| N38 | C | search_query 非空但 claim 是自设修正公式 Q'(P) 及 γ≈0.3 参数，推导框架非事实 |
| N39 | C | search_query 非空但 claim 是一阶条件推导 P*=C/(1-1/β_eff)，数学推导非可检索事实 |
| N40 | C | search_query 非空但 claim 是「维持高 P 的临界不等式」，自设决策规则非事实 |
| N41 | C | search_query 非空但 claim 是 T(D)=E[1/Q(P0(1+D))] 的数学表达，推导框架 |
| N42 | C | search_query 非空但 claim 是 R_consult(ΔP)=R_base*exp(-kΔP) 的数学表达，推导框架 |
| N43 | C | search_query 非空但 claim 是 λ_effective=λ_base+βσ² 的参数耦合假设，自设参数 |
| N44 | C | search_query 非空但 claim 是 Spence 模型 θ* 推导及「与观测 0.85 阈值偏差」，依赖私有观测值，复合推导 |
| N45 | B | search_query 非空（"buyer reservation utility distribution…empirical estimate"）；claim 核心是「估算买家保留效用分布」的经验数据，来源可能存在但通道挂 |
| N46 | C | search_query 非空但 claim 是混合策略均衡的函数关系 R_consult(q) 推导，数学推导 |
| N47 | C | search_query 非空但 claim 要求「从平台日志计算 Corr(D_initial, I_no_consult)」，数据私有（平台日志），公开来源不存在 |
| N48 | C | search_query 非空但 claim 要求逻辑回归验证 β1 显著性，依赖平台日志私有数据 |
| N49 | C | search_query 非空但 claim 是 P_market 的口径定义（加权中位数+异常值剔除规则），自设定义非事实 |
| N52 | B | search_query 非空（"used goods marketplace commission rate…eBay Xianyu 2023"）；claim 是佣金率 2.5%-5% 的行业基准，公开来源明确存在（eBay/闲鱼费率页），通道挂 |
| N53 | C | search_query 空；claim 是买家净效用公式 ΔCS+ΔT_b*C_t 的量化任务，依赖未定义参数，复合推导 |
| N54 | C | search_query 空；claim 是卖家净收益公式量化任务，依赖 N53 参数，复合推导 |
| N55 | C | search_query 空；claim 是平台净收益公式及 d(rPQ)/dr 符号判断，复合推导 |
| N56 | C | search_query 空；claim 含自设参数组（P=500元, Q=1, ΔT_s=2天, C_t=10元/天, ΔCS=50元）推得 r≈1.4%，自设参数非公开事实 |
| N57 | C | search_query 空；claim 是 GMV/留存率定义式及分解任务，自设定义 |
| N58 | C | search_query 空；claim 是损失率≤5% 约束的量化任务，依赖 N17 假设，复合 |
| N59 | C | search_query 空；claim 含自设断言「NPS 提升 5-10 分对应搜索成本降低 5-15%（基于行为经济学实证研究）」但无来源支撑，复合+未证实引用 |
| N60 | C | search_query 空；claim 是干预措施(1)的 GMV 增量假设（3%+8%）与 U/C=∞，自设参数 |
| N61 | C | search_query 空；claim 是干预措施(2)的假设链（15%×50%×(2%+4%)），自设参数 |
| N62 | C | search_query 空；claim 是干预措施(3)的假设链（30%×1.2），自设参数 |
| N63 | C | search_query 空；claim 是阈值敏感性假设（X=10%→25% 覆盖），自设参数 |
| N64 | C | search_query 空；claim 是数据依赖规则（n<5 不展示，覆盖 15%），自设规则 |
| N65 | C | search_query 空；claim 是反馈循环假设（咨询降 20%→48h 降价 5%），自设参数 |
| N66 | C | search_query 空；claim 含自设弹性值（-1.2/-0.4）与调整率假设，自设参数 |
| N67 | C | search_query 空；claim 是 15% 调整率构成拆解（5%+10%），自设参数 |
| N68 | C | search_query 空；claim 是利润非线性影响假设（约 10% 卖家反对），自设参数 |
| N69 | C | search_query 非空但 claim 是 S_cost 公式量化任务，依赖私有基线 T_search，复合 |
| N70 | C | search_query 非空但 claim 是「需通过 A/B 测试获取」的转化率基线，依赖未做的实验，私有数据 |
| N71 | C | search_query 空；claim 是锚定效应公式 ΔWTP=α*(P_label-P_market)，自设公式 |
| N72 | C | search_query 空；claim 是净效应阈值判定公式，复合推导 |
| N73 | C | search_query 非空但 claim 是 N_affected 公式计算任务，依赖 N27 分布假设，复合 |
| N74 | C | search_query 空；claim 是 V_original 加权计算任务，依赖子群划分，复合 |
| N75 | C | search_query 空；claim 是 Q_adjusted 模型及线性近似有效性验证，复合推导 |
| N76 | C | search_query 空；claim 是 ΔLoss 计算及 5% 阈值触发判断，复合推导 |
| N77 | C | search_query 空；claim 是 ΔGMV 两项分解量化任务，复合推导 |
| N78 | C | search_query 空；claim 是 S_time 量化任务，依赖 N30 差值，复合 |
| N79 | B | search_query 非空（"NPS net promoter score revenue retention correlation e-commerce benchmark"）；claim 核心是「查找行业基准系数」，公开基准可能存在但通道挂 |
| N80 | C | search_query 空；claim 是置信度公式及「n>1000 且 d>0.5 时置信度下限 80%」的自设规则，非公开事实 |
| N81 | C | search_query 空；claim 是数据源分级权重（1.0/0.7/0.4）自设标准，非公开事实 |
| N82 | C | search_query 非空但 claim 是 δ_quality 估计及「>0.1 则 20% 归因质量」的复合条件判断，依赖平台数据 |
| N83 | C | search_query 非空但 claim 是因果识别策略（DID/IV/Heckman）及置信度规则，方法论框架非事实 |
| N84 | B | search_query 非空（"e-commerce platform click to inquiry conversion rate baseline statistics"）；claim 核心是「检索平台日志中点击-咨询转化率基线 5-15%」，公开统计可能存在但通道挂 |
| N85 | C | search_query 空；claim 是数据噪音过滤规则（>10 次/日剔除）及置信度规则，自设规则 |
| N86 | C | search_query 非空但 claim 是「可获取性评估」任务（列出年报/招股书陈述，无则标[不可得]），元任务非事实断言 |
| N87 | B | search_query 非空（"eBay Mercari Xianyu commission rate structure seller pricing impact elasticity"）；claim 核心是对比同类平台公开费率结构，公开来源明确存在，通道挂 |
| N88 | C | search_query 非空但 claim 要求「通过爬虫获取平台首页/推荐流挂价偏离度>15% 占比」，私有数据+需爬虫，公开来源不存在 |
| N89 | C | search_query 空；claim 是 A/B 测试设计及预期区间（ΔC∈[8%,12%]），依赖未做实验 |
| N90 | C | search_query 空；claim 是信任度公式 T=1-举报率/浏览量 及边界条件，自设公式 |
| N91 | C | search_query 空；claim 是贝叶斯更新公式及 P(H|E) 数值推演（0.65→0.45），数学推导 |
| N92 | C | search_query 非空但 claim 是 ρ 比值计算任务（平台日志），私有数据 |
| N93 | B | search_query 非空（"second-hand marketplace listing price distribution skewness long tail statistics"）；claim 含明确统计断言（偏度>1.5、99th/Median>4.0），公开研究可能存在但通道挂 |
| N94 | B | search_query 非空（"category specific price deviation median listing vs sold price second hand platform"）；claim 是品类偏离度基准值（8-12% / 20-30%），公开数据可能存在但通道挂 |
| N95 | C | search_query 非空但 claim 是 90th 百分位构成分解及回归系数预测（0.3-0.5），依赖未做回归，复合 |
| N96 | C | search_query 空；claim 是 STR 指数衰减公式及 k∈[5,10] 的自设典型值，非公开事实 |
| N97 | C | search_query 空；claim 是筛选效应修正公式及「比值通常<0.7」的自设断言，复合推导 |
| N98 | C | search_query 非空但 claim 是竞争密度弹性 ε_T,D≈-0.5 的自设参数，非公开事实 |
| N99 | B | search_query 非空（"click through rate vs inquiry rate drop after price reduction e-commerce"）；claim 含明确占比断言（零点击 30-40% / 有点击无咨询 60-70%），公开漏斗数据可能存在但通道挂 |
| N100 | C | search_query 非空但 claim 是 β≈-0.6 的自设相关系数，非公开事实 |
| N101 | C | search_query 非空但 claim 是 Boost Factor≈1.2-1.5 的自设平台算法参数，平台私有，公开来源不存在 |
| N102 | C | source=search 但 search_query 空、retrieval_sources 空；claim 是稀缺性启发式+「决策时间缩短 20-30%」的复合心理机制断言，无检索通道且数值自设 |
| N103 | C | source=search 但 search_query 空；claim 是噪声参数化 ε~N(0,σ²) 及左尾变短断言，复合推导 |
| N104 | C | source=search 但 search_query 空；claim 是信号成本不对称+「信任折扣 10-15%」的复合断言，数值自设 |
| N105 | C | source=search 但 search_query 空；claim 是损失规避镜像效应+「咨询延迟 2-3 倍」的复合断言，数值自设 |
| N106 | C | source=search 但 search_query 空；claim 是统一框架逻辑自洽性检验+ Profit 函数平衡推导，复合推导 |

### pending 小计

**A=0, B=9, C=68**（77 条）

B 类 9 条：N35, N45, N52, N79, N84, N87, N93, N94, N99。共同特征：search_query 非空 + claim 核心是可检索的经验事实/行业基准（佣金率、转化率基线、分布统计），retrieval_sources 空（通道挂）。
C 类 68 条中：source=given 5 条全是 L1 任务描述；source=knowledge 45 条中 7 条有 search_query 但 claim 是自设参数/推导框架（N36-N44, N46, N49 等）；source=search 27 条中 18 条 claim 依赖私有平台数据（N47, N48, N70, N88, N92）或自设参数（N100, N101 等）或复合推导。
A=0 的依据：5 条 source=given 全部是 L1 任务描述（「构建/解释/识别/设计/标注」），无一条是「有明确数值/日期/定义的可直接核验事实断言」，不满足 A 类定义。

## 二、degraded 31 逐条分类

| 节点 | 分类 | 理由（引用字段） |
|------|------|------------------|
| N10 | D | evidence 存在（逻辑自洽+指出 0.85 阈值无来源）；source=knowledge, search_query 空；claim 主体是 Spence 模型定性机制（可核），仅 0.85 阈值缺来源，补强即可 |
| N11 | E | evidence 存在但明确指出来源[1][2]「未提供 60% 卖家或高挂价比例的具体数据支持」；retrieval_sources 2 条均为房产中介文章（toutiao），与二手平台卖家定价行为无关；claim 核心数值（60%、20%）无来源，站不住 |
| N27 | D | evidence 存在（指出来源缺具体统计参数）；retrieval_sources 2 条（smzdm 挂价指南+长尾分布概念）；claim 主体（右偏长尾分布结构）有定性来源支持，10-15%/2-3 倍数值待补强 |
| N28 | D | evidence="检索失败: no sources from any channel (all 5 failed)"——通道挂而非 claim 站不住；claim 是筛选效应的统计陷阱界定（方法论事实），逻辑自洽，通道恢复后可补 |
| N29 | D | evidence="检索失败: no sources from any channel (all 5 failed)"——通道挂；claim 是「零点击 vs 有点击无咨询」口径界定（方法论），逻辑自洽，通道恢复后可补 |
| N31 | E | evidence 存在但明确指出来源[1][2][3]「均与损失厌恶系数的具体统计参数无关」；retrieval_sources 为 Replication_crisis/Financial_economics 等无关条目；claim 核心 σ_λ≈0.4、15% 卖家为自设参数，无来源支撑 |
| N126 | E | evidence 存在但明确指出来源「均涉及宏观通胀、货币政策或股市波动，与该微观定价策略的具体阈值（20%）及参数（γ=0.6-0.8）完全无关」；retrieval_sources 为 Inflation/Monetary_policy 无关条目；claim 核心阈值无来源 |
| N153 | E | evidence 存在但明确指出来源「均与二手市场品类波动率无关」；retrieval_sources 为 Cryptocurrency/Economy_of_Russia 无关条目；claim 核心数值（20%/5%）无来源 |
| N155 | E | evidence 存在但明确指出来源「仅涉及 Redis Geo 技术实现及 LBS 概念，未提供…具体业务规则与统计参数的支持」；claim 核心（50km 半径、β≈0.5元/km）为自设业务规则，无来源 |
| N156 | D | evidence="经验事实，逻辑自洽但缺来源支持"；search_query 非空（"Xianyu Zhuanzhuan platform commission rate…"）；claim 是闲鱼/转转/Depop 佣金率 0%~6%，公开来源明确存在（平台费率页），补强即可 |
| N157 | E | evidence 存在但明确指出来源「仅定义弹性概念，未提供二手市场具体品类的实证数值」；retrieval_sources 为百度百科弹性定义条目；claim 核心 |ε| 分品类数值（2.0-2.5/1.2-1.8/3.0+）无来源 |
| N160 | E | evidence 存在但明确指出来源[1][2]「分别关于作家传记和城市定义，与该事实主题完全无关」；retrieval_sources 为 Robert_E._Howard/City 无关条目；claim 核心 δ=0.05/day 为自设参数 |
| N161 | D | evidence 存在（指出来源缺 eBay 费率数据）；search_query 非空（"eBay final value fee schedule 2024 percentage categories"）；claim 是 eBay FVF 13.25% 费率表，公开来源明确存在（eBay 官方费率页），补强即可 |
| N162 | D | evidence="经验事实，逻辑自洽但缺来源支持"；search_query 非空（"Xianyu…commission rate 2024 policy zero fee"）；claim 是闲鱼 0 佣金政策，公开来源存在（新闻报道/平台公告），补强即可 |
| N182 | E | evidence 存在但明确指出「NPS 与搜索成本的具体量化对应关系…无可用外部来源支持」；claim 核心（+5-10 分对应 5-15%）无来源，且引用的 Thaler 1980/Kahneman 2011 未核 |
| N190 | D | evidence 存在且做了实际逻辑校验（σ=0.2 时 P(X>10%)≈31.4%，与 25% 量级接近）；retrieval_sources 1 条（正态分布阈值原理，间接支持）；claim 主体（对数正态分布假设下的计算）成立，仅缺具体 σ 值，补强即可 |
| N194 | E | evidence 存在但明确指出来源（Asda、次贷危机、可持续采购）「与该具体电商业务指标完全无关，无外部证据支持具体数值（15%, 40%, 12%）」；claim 核心数值无来源 |
| N198 | E | evidence 存在但明确指出来源「仅涉及零售品类策略与结构优化，未包含 E=-1.2、标签感知价差修正或具体调整率推导」；claim 核心（15%→25% 调整率、70% 权重）无来源 |
| N222 | E | evidence="逻辑自洽，但属于经验事实且无可用外部来源支持"；claim 是工作点 A 的 ΔLoss_A≈0 假设，自设假设无来源 |
| N224 | E | evidence="逻辑自洽，但属于经验事实且无可用外部来源支持"；claim 是工作点 C 的 ΔLoss_C 计算假设，自设假设无来源 |
| N225 | E | evidence 存在但明确指出来源「均与二手平台价格敏感度弹性系数无关，无法提供外部支持」；claim 核心 E_price 系数无来源 |
| N227 | E | evidence 存在但明确指出来源「均与二手电商比价时长无关，无法提供 S_min 的具体数值支持」；claim 核心 S_min 中位数无来源 |
| N228 | E | evidence 存在但明确指出来源[1]「仅定义雇佣关系，[2]为沃尔玛简介，均与二手交易时间价值校准及目标用户时薪数据无关」；claim 核心时薪/紧迫性系数无来源 |
| N230 | E | evidence 存在但明确指出「属于经验事实且无可用外部来源支持」；claim 核心（NPS+10 分对应留存 5-10%）无来源 |
| N250 | D | evidence 为空（唯一一条）；但 claim 是纯数学计算（∂P*/∂r 公式代入 ε_d=-1.5, r=0.05 得 -13.33），可独立重算验证（(1/-1.5)*(1/0.95)≈-0.70，claim 数值本身存疑但属可核验的算术），补 evidence 即可，非 claim 站不住 |
| N261 | E | evidence 存在但明确指出「参考来源均为美剧剧集列表，与二手平台咨询行为完全无关」；retrieval_sources 为 Elementary/Equinox 剧集列表无关条目；claim 核心（重复咨询频次分布）无来源 |
| N273 | E | evidence 存在但明确指出「属于经验事实且检索无可用来源，无法验证具体数值 β≈-0.6」；claim 核心 β≈-0.6 无来源 |
| N276 | E | evidence 存在但明确指出「属于经验事实（平台算法参数），且无可用外部来源支持」；claim 核心 Boost 公式及 α=0.1-0.3 为平台私有参数，公开来源不存在 |
| N278 | E | evidence 存在但明确指出「属于经验事实（具体统计比例与画像特征），且本轮检索无可用来源支持」；claim 核心（60% 长尾卖家、曝光低 80%）无来源 |
| N279 | E | evidence 存在但明确指出「属于具体经验事实（特定脑区活动变化及 20-30% 决策时间缩短的具体数值），且本轮检索无可用来源支持」；claim 核心 fMRI 数值无来源 |
| N292 | E | evidence 存在但明确指出「参考来源均为通用市场营销概念，未提供该特定数学模型或实证数据支持」；claim 核心（β/γ 回归拟合）依赖平台历史数据，私有 |

### degraded 小计

**D=9, E=22**（31 条）

D 类 9 条：N10, N27, N28, N29, N156, N161, N162, N190, N250。共同特征：evidence 字段存在且指出「逻辑自洽/部分支持/通道挂」，claim 主体可核（定性机制、方法论界定、公开费率表、纯算术），只差补强来源或通道恢复。
E 类 22 条：evidence 字段明确记录「来源与主题无关/无可用来源/数值无支撑」，retrieval_sources 多为无关条目（Wikipedia 通胀/货币政策/作家传记/美剧列表等）或空，claim 核心数值为自设参数或依赖私有平台数据，公开来源基本不存在。

## 三、汇总

| 类别 | 计数 |
|------|------|
| A-可翻 | 0 |
| B-需检索 | 9 |
| C-难核 | 68 |
| D-可救 | 9 |
| E-弃 | 22 |

**现实上限**（任务书口径 (174 + A + D) / 283）：

- 保守（只算 A+D）：(174 + 0 + 9) / 283 = 183/283 = **0.647**
- 乐观（B 类 9 条检索通道修复后全补上）：(174 + 9 + 9) / 283 = 192/283 = **0.678**

**与 lead 估算 0.813 的差距**：保守 0.813 - 0.647 = **0.166**；乐观 0.813 - 0.678 = **0.135**。

主因：lead 估算「pending 77 中约 46 个 knowledge/given 类可翻 verified」，逐条核后 5 条 source=given 全是 L1 任务描述（非事实断言），45 条 source=knowledge 全是自设参数/推导框架/量化任务（无一条是「有明确数值/日期/定义且 evidence 缺失但可补」的可直接核验事实断言），A 类为 0。B 类 9 条是真正「来源存在但通道挂」的节点（佣金率、转化率基线、分布统计等公开可检索事实），若检索通道修复可补，但不计入保守口径。

## 备注

- 本分类只读 checkpoint（bak-verifyonly 文件），未改动任何 checkpoint，未把任何节点翻成 verified。
- 分类依据全部引用节点字段（source/level/search_query/retrieval_sources/evidence），未凭 claim 文字感觉拍。
- N250 的 claim 数值（-13.33）与公式代入结果（≈-0.70）不一致，但这属于「可核验的算术错误」而非「claim 站不住」，仍归 D（补 evidence+修正数值即可）；若 lead 认为算术错误=站不住，可改 E，影响上限 0.647→0.636。
