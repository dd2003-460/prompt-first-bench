# GOAL: idea53-cross-gradient（#53 独立短文）

> stage-gate goal_id: idea53-cross-gradient · 2026-11-24 D 指令"定 idea53 这个目标"
> 定位：从 #10 模块升格为**独立 goal**（D 判断：最快最小可发表）。#10 主线论文不受影响，#53 若成立可反哺 #10 analysis 章节。

## 0. 完整逻辑链（motivation，D 2026-11-24 给出）

**为什么是这个结构+这个量**（审稿人第一问 why tree / why MI 的答案）：
1. **非线性**：瓶颈判定 f(微架构因子)→瓶颈类型 是组合函数（因子交互：精度算力比×workload 构成×标量占比×带宽）。实证=T5000：FP16 占 workload 30% 但交互后占 78% 时间 → 占比小≠贡献小（非线性放大）。
2. **所以用信息论量非占比/ablation**：线性归因系统性低估交互项；互信息抓非线性依赖，无线性假设。
3. **所以用树**：①可展开（分解路径显式）②支持正交完备性**核对**（逐对检查；树是载体，正交完备由分解流程核对，非树自动判定）③逐层条件化 I(L_k|L_<k) 语义明确=增量信息。
4. **所以算深层节点信息增益**：树+条件化=逐层增量的天然载体，交叉梯度在此结构上算。
5. **落地**：树+逐层信息增益格式反过来当 LLM 推理模板；具体接 research-agi-budget 预算控制——预算小→压缩低信息增益节点，保留高增益深层判断节点。#53 信息增益=预算分配理论依据。

**投稿前待补（薄弱点）**：
- P1 非线性目前仅 T5000 单实例，需可算的非线性度定义（候选：交互项条件互信息），否则"非线性放大"是修辞非论证 [待核验]
- "判定正交完备"措辞→"支持正交完备性核对"（见 3②）

## 1. 本地背景扫描（4 项，有证据）

| 项 | 证据 |
|---|---|
| 项目 research/ | pfb/research/gpu-hardware-candidates-20261124.md（硬件候选集+V_fine 构造样例）；pfb/modules/F-theory/research/idea53-info-theoretic-contribution.py+.json（节点级 MI 已有） |
| 项目 memory/ | pfb/modules/IDEA-INDEX.md #53 行（四轮 arena 核验全记录，commits 70dca8efa/81be67cb9/82a67df96） |
| 全局 lit-survey | pfb/tasks/IDEA-review/result.md（arena 四轮撞车核验：DDx 三阶段/信息增益消歧/步类型分类学三线占位，未见=树×类型×深度×信息贡献测量+两级判定交叉梯度） |
| 历史结论 | 第三轮"浅层主导"=误读（词表偏向枚举型）；重释后=claim 的另一半（coarse 级浅层主导已实测成立） |

## 2. 调研对象全集

- **纳入**：三份 GPU run 树（rep-scan n=3849 / t53b n=5497 / stage-ablation GPU域 n=18243）——已有数据，纯离线
- **纳入**：V_fine 构造样例（5090 发射砍半→慢40% 方向修正 / T5000 高精度→瓶颈80%+ 粒度细化）——纯 spec+计算
- **排除**：跑新实验（D 明确不想跑，数据已有）
- **排除**：进 gold 树（D 2026-11-24 决策：保 gold 正交性，硬件=领域知识不混入方法论骨架）
- **排除**：embedding 类测量（macOS sentence_transformers regex 坑，27b subagent 两次撞 repetition loop）——用纯数学闭式 MI

## 3. 正交维度拆解

- **V_coarse**（资源类标签："带宽受限/算力受限"）：词表可测，已有 is_bottleneck 词表
- **V_fine**（机制级判断："容量 vs 带宽"/"issue rate vs decode width"）：27b judge 打标（127.0.0.1:8787），降级判据=机制级词正则（容量/带宽/issue rate/decode width/发射/occupancy）
- **正交性**：V_fine 条件化 V_coarse（I(L;V_fine|V_coarse)），粗/细两级不混算
- **完备性**：两级覆盖"枚举→判断"全链（arena 第四轮确认词表只够 coarse 级）

## 4. 量化定义（公式，无模糊词）

- I(L_k; V_coarse) = Σ p(l,v) log p(l,v)/p(l)p(v)，各层 k 分别算
- I(L_k; V_fine | V_coarse) = Σ p(l,vf,vc) log p(l,vf|vc)/p(l,vf|vc)
- **生死线**：I(L_k; V_fine|V_coarse) 随 k 单调不降（L4 > L1）→ claim 成立；不升 → claim 死
- **对照臂**：①深度置换（层标签随机打乱，MI 应→0）②fake-run 占位（无瓶颈节点，MI 应→0）③浅深节点数配平 ④层内类型对照（同层内判断型 vs 枚举型 fine-MI 比较，解 type×depth 混淆）
- **HARKing 防御**：判据+公式预注册（本文件即预注册），held-out=stage-ablation 域（前三轮未用其做 claim 推导）

## 5. 任务书（已派发，含失败降级）

| 任务 | 通道 | 状态 | 失败降级 |
|---|---|---|---|
| 交叉梯度计算（V_coarse 词表 + V_fine 27b judge） | subagent deleg_53e3a082 | running | 27b 打标失败→机制级词正则降级判据（标"降级"） |
| 投稿策略（对标/免费 venue/接受概率/最快路径） | arena 第五轮 session 01a20b11 | running | arena 超时→ego-browser 直接问 ChatGPT/Perplexity 交叉 |

## 6. 验收标准（逐项勾选）

- [ ] idea53-cross-gradient.json 落盘：I(L_k;V_coarse) 各层值 + I(L_k;V_fine|V_coarse) 各层值 + 三对照臂
- [ ] 生死线判定：fine-conditional 随深度升/不升，明确结论
- [ ] 预注册合规：判据在数据出来**之前**已落盘（本文件 commit 时间 < 数据产出时间）
- [ ] venue 决策：免费渠道排序 + 概率估计（arena 第五轮回执）
- [ ] 若成立：短文大纲（claim+方法+结果+对照臂）落盘；若不成立：负结果记录（排除什么错误解释）
- [ ] IDEA-INDEX #53 行更新最终状态

## 7. Arena 核验看法汇总（qqbot 接手必读，来源 pfb/tasks/IDEA-review/result.md）

**四轮结论链**（commits 70dca8efa→81be67cb9→82a67df96，第五轮投稿策略 running）：
- R1：强近邻 IGRPO(2607.06223)/Thought Anchors(2506.19143)/2411.11984，剩空白=深度梯度实证+瓶颈定位，conf 0.45
- R2（信息论精化）：转发平凡性一击（深层>浅层对可枚举信息数学必然）→ 需条件化 I(L_k;Y|L_<k)
- R3：conf 0.7，workshop/短文级，独立顶会难；链式域已撞（2601.23163 NeurIPS'26 E&D / 2508.03346 / 2604.06695）
- R4（枚举vs判断精化，当前 claim）：conf 0.6 条件可发表；撞车三线占位（DDx 三阶段 2602.03340 / 信息增益消歧 2402.03271+2605.05386 / 步类型分类学 2512.14332+2512.00729）；**未见同构=树×类型×深度×信息贡献测量+两级判定交叉梯度**；最难一击=同义反复+HARKing+概念已占位三连击；守法=判据去深度化+层内类型对照+预注册 held-out+三控制臂（本 goal §4 已全落实）

**接受率对标（第五轮 7dae6431a 实核，5 个最接近）**：
- 2601.23163 Probing Trajectories → **NeurIPS'26 E&D 已录**（abs comments 实抓）——#53 链式版正面参照，赛道对口
- 2508.03346 Step Entropy → **ICLR 2026 正刊已录**——"零重跑信息贡献度量"类方法文可上正刊，#53 需硬切割（树×类型×交叉梯度）
- 2610.00571 SLIDER → ICLR'26 workshop 已录（PID 方法学最近邻）
- 2506.19143 Thought Anchors → ICLR'26 在审未录（在审状态参照）
- 2402.03271 UoT → NeurIPS'24 正刊（弱相关）

**venue 决策（0 元投稿，arena 第五轮概率估计=主观判断非事实）**：
- **主推双轨**：NeurIPS 2027 E&D（~2027-05 截稿，P 全守法 0.30 / 半守法 0.15；分析型免 code 是 2026 CFP 明文）+ ICML 2027 workshop（CFP ~2027-05/06，P 0.55/0.35，short 文先发）
- 备选：NeurIPS'27 workshop 0.55/0.35、MLSys'27 workshop 0.45/0.25（域最对口但方法异质减分）、ACL Findings 0.20/0.10（gpu 域边缘，ARR 2027-01-04 仓促不建议）
- ICML'27 main 0.08/0.04 → **窗口留给 #10 主线**，#53 不挤
- 兜底：arXiv 挂网（0 元锁时间戳）必做
- 残余风险：接收后注册费（数百-千美元级，未验证）；最便宜闭环=arXiv+workshop
- **最快路径 3-4 周**：W1 打标+MI 管线（=本 goal T1-T3）→ W2 预注册冻结（OpenReview/OSF 免费存档）+主结果+held-out → W3 4 页短文+arXiv
- 交叉梯度不成立情形：E&D<0.05，仅方法论短文 workshop P≈0.2，arXiv 兜底

**论文格式（短文路线）**：
- 长度：4-6 页（E&D/Findings 标准）或 workshop 5 页
- 结构：①claim（枚举vs判断的增量贡献）②方法（交叉梯度+PID 可选升级）③数据（三源 run 树 n=3849/5497/18243）④结果（两条梯度+四对照臂）⑤held-out 预注册检验 ⑥limitation（held-out 单域/词表 coarse 级/V_fine 27b 打标质量）
- 必含防御段：HARKing 声明（预注册 commit 20c029300 时间戳早于数据）+ 转发平凡性回应（条件化消解）+ 同义反复回应（层内类型对照解 type×depth 混淆）

## 8. qqbot 接手入口

- 状态机：stage-gate goal_id `idea53-cross-gradient`（全平台共享，~/.hermes/.stage-gate/idea53-cross-gradient.json）
- 分解树+任务表：本目录 decomposition.md（T1-T7，机器可查验收）
- 预注册：GOAL.md §4 @ 20c029300（16:18）
- 在跑：T1-T3 subagent deleg_53e3a082 / T5 arena 第五轮（session 01a20b11，分支 arena/f8477718-prompt-first-bench）
- 接手动作：等 T1-T3 回执 → T4 生死线判定 → T6 分支（短文大纲/负结果）→ T7 合规检查 → stage_advance

## 约束

- 纯离线计算，不跑新实验（D 指令）
- 免费渠道优先（D 没钱，venue 无版面费）
- 27b 打标 prompt <200 token，分小节增量写盘（防 token 上限）
- 结果不信汇报信 git（fetch → show → 独立复算数字）
