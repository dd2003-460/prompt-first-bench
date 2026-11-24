# T53b 异常观察清单（04-verify 待核验）
> origin: ai | 2026-11-20 14:40 | 13/62 早期 run 分布核验

## 异常 run（62 跑完后统一判）
| run | 异常 | 04-verify 动作 |
|---|---|---|
| gpu_formula_r3 | depth=0.0 (cov 正常 0.133) | 查 depth 计算是否挂，决定是否重算 |
| gpu_formula_r6 | cov=0 + n_nodes 字段缺失 | 查是否早退/数据不全，决定作废或补跑 |
| gpu_formula_r8 | cov=0 (nodes=114 正常) | 查 coverage 计算是否挂 |

## 字段信号
- n_verified/n_degraded 仅 gpu r01-r05,r07 有值，r08 后全 0/0 → 疑似 pipeline 在 r07 后停止填充该字段（judge.overall 仍正常）。04-verify 确认该字段是否已废弃，废弃则从统计口径剔除。

## webllm 混淆变量（04-verify 必须处理，2026-11-20 14:48）
- **25/30 run 日志带 WEBLLM-BROKEN**（Perplexity/ChatGPT 未登录，webllm 交叉验证全跳过），只有 5 个 run webllm 正常：
  - webllm 正常（离群，与其余不可直接比）：gpu_formula_r08 / gpu_text_r01 / gpu_text_r04 / gpu_text_r05 / gpu_text_r06（11-19 02:42~11-20 02:26 窗口）
  - 其中 gpu_text_r04/r05 崩在 checkpoint FileNotFoundError，实际有效 webllm run 只有 3 个
- **臂间可比性**：nat/soc/gpu 三臂的 formula 臂几乎全降级（25 个里 20+ 个），降级在各臂间大致均匀 → 臂间对比仍有效（混淆变量同水平），但"测的是无 webllm 的 S5"，结论只能限定为"webllm 缺席条件下的消融"
- **webllm 效应不可识别（14:50 实测）**：OK 组 n=2（cov mean 0.034 / depth 0.351）vs BROKEN 组 n=14（cov 0.252 / depth 0.448），无配对、臂构成不同 → 现有数据分离不出 webllm 效应，之前"倾向 (a) 因降级均匀"的理由作废
- **推论**：登录窗口已超时 → 剩余 ~50 run 全部降级，5 个 webllm-OK run（11-19 早期窗口）是各臂离群点；nat_text/soc_text 臂尚未开跑，将与 gpu_text 同水平降级 → 臂间对比仍有效（混淆同水平）
- **处置选项（需 D 定，不阻塞当前 run）**：
  - (a) 接受降级数据：62 跑完后出"webllm 缺席"口径的消融结论，5 个 OK run 标离群剔除或单列；webllm 效应另立 goal 补
  - (b) 登录后重跑：当前 12/62 有数据作废，重跑 4-5h（需 D 重新发起登录）
  - 我倾向 (a)——新理由：webllm 效应从现有数据不可识别，(b) 重跑只能补测一个正交维度、代价 4-5h；(a) 的臂间结论不受影响，webllm 维度留待登录后小规模配对实验（同 qid+arm 同 round 跑 with/without 各 2-3 个，可识别效应）
- **处置决定（T3，11-21 自主落盘，可逆）**：采纳 (a)。理由：(i) 降级在各臂间大致均匀 → 臂间 Δ 口径不受混淆影响（同水平偏移相消）；(ii) webllm 效应从现有数据不可识别（OK n=2 vs BROKEN n=14，无配对），(b) 重跑 4-5h 只补一个正交维度，产投比低；(iii) 5 个 OK run 标离群单列（gpu_formula_r08/gpu_text_r01/r04/r05/r06，其中 r04/r05 崩在 checkpoint 实际无效 → 有效离群 3 个），主统计剔除；webllm 效应 = E2 配对实验（登录后小规模，可识别）。**结论口径限定**：T53b 消融结论 = "webllm 缺席条件下的 S5 消融"，05-accept 对标 DESIGN.md 假设时须带此限定。

## 补跑项（62 跑完后手动补，不碰在跑实验）
| run | 状态 | 原因 | 动作 |
|---|---|---|---|
| gpu_formula_r06 | 已回滚重跑（2026-11-20 14:58 Lead, commit 0e2716bf3） | 空 done 回滚为 done=False，自愈链自然重跑（新进程带 faulthandler） | 无需手动，跑完对账 |
| gpu_formula_r09/r10 | 未标 done（results 有 11-19 残留） | 自愈链会自然补 | 等自愈链，跑完对账 |

## 真实进度口径（§8 对账，2026-11-20 14:45）
- cc-state done=13，但有数据工件的只有 **12**（r06 空 done）
- 汇报用"有数据 12/62"，不用"done 13/62"

## 统计口径（04-verify 必须遵守）
- **cc-state.json 的 done 列表是权威账本**（13/62）；ablation-results.json 有 16 条，其中 gpu_formula_r09/r10 是 11-19 的作废残留（cc-state 未标 done），直接数 results 会多算 2 条。
- 聚合时：以 cc-state done 为准，逐条 join results 记录；results 有而 cc-state 无的 = 残留，剔除。
- gpu r01-r05 是今天回退重跑的新数据（11-20 05:25-11:32），旧作废数据已被覆盖，不用管。

## 臂对比初判（13/62，非结论）
- nat/soc 臂数值干净（cov 0.17-0.86, depth 0.46-0.74）
- gpu 臂早期有 3 异常，占比 3/10，若 62 跑完仍 >30% 异常则该臂数据可信度存疑

## 2026-11-20 节点内容质量观察 (18:4x, 19/62 done 时抽查)
- nat (缓存公式): degraded=公式真数字缺 (judge 区分"推导自洽"vs"经验数值无据"), arxiv 源被正确采信, 知乎/CSDN 弱源未被带偏
- soc (二手平台均衡): degraded=公式假硬凑 (w_s/w_b/w_p 权重无出处, 阈值 2.0 无实证), 检索源含头条/百度
- NN119 evidence 空但已标状态 (小瑕疵, 质询未跑)
- **04-verify 统计注意**: degraded 标签混了两种成因 (公式自洽性 vs 数值有据性), 跨题 Δ 要拆两维度, 否则 soc 假公式和 nat 真公式混同, Δ 信号污染

## 2026-11-20 19:10 · checkpoint 清场销毁原始数据（已修）
- 现象：driver 每 run 启动 rm -rf checkpoint 目录 + 终盘文件，逐节点原始数据（claim/evidence/judge 质询）销毁，只留聚合统计
- D 指令：checkpoint 是原始数据，不许删
- 修复：clean 改 mv 归档到 checkpoints/archive/sm-{qid}-<ts>/（commit 446fb0494），防 resume 污染效果不变
- 损失：已完成 23 run 的节点级数据不可恢复；judge 分 + 最终 answer 安全（ablation-runs/ 持久化）
- 04-verify 影响：节点级细查只能覆盖归档后的 run；跨 run 节点质量对比样本不全，结论需标注

## 2026-11-20 19:55 · 占位符 evidence 57% + verified 膨胀（04-verify 必须处理）
- 现象：154 节点抽查，57% evidence = "先验知识/题面给定，逻辑校验通过"（占位符），其中 71/88 标 verified
- 因果链：DDG fast-fail 生效 → 检索通道缩水 → judge 退化为自洽性检查 → formula 臂公式"自推自"过 verified
- Δ 污染：formula 臂 verified 率高可能源于"公式更易自洽"而非"公式更好"；text 臂经验断言无法自洽只能 degraded
- 04-verify 处置：统计维度加第三个——evidence 来源（外部检索 vs 先验占位）；Δ 只在"有外部 evidence"的子集上算主口径，全量口径单列
- 对照缺口：已完成 23 run 的节点级数据已丢失（checkpoint 事故），占位符率的历史基线无法回查——本条是首个可测点
- 附带观察：nat text 臂也在生成公式（H_effective 全概率分解），两臂区分度可能小于预期

## 2026-11-20 20:15 · 本地 KB 通道形同虚设（62 跑完后改进项）
- 实测：118 节点 retrieval_sources 中 104 空、14 全网络（amd 2/zhihu 6/csdn 4/sohu 2），本地文件命中 0
- 覆盖：_LOCAL_CORPUS_DIRS 只有 GPU 域（hardware KB 18 文件 + D1-gpu 120 文件）；域门控 qid≠gpu 直接返回空 → nat/soc 零覆盖
- gpu 不命中根因：grep 关键词匹配（5 词 → grep -rilE），query 措辞与 KB 文件措辞不匹配；KB 粒度=卡规格表，节点 query 粒度=运维/成本计算，粒度错配
- 改进（62 run 后，同质性约束内不动）：
  1. gpu：query→KB 文件映射表（比 grep 稳）或 gpu 题模板加规格表引用
  2. nat/soc：无本地语料（确认"真没有"）；D1-knowledge-base 项目语料接入 hook 是独立任务
- 04-verify 关联：本地命中 0 意味着所有 evidence 都来自"网络 or 先验占位"二分，占位符率归因不受本地通道干扰（简化）

## ~~L1 层级放置污染~~（2026-11-20 23:20 诊断反转，原 71% 是假阳性）

**原诊断作废**：之前报的"L1 污染率 71%（145/204）"是测量假象，不是 decompose 层级放置错误。

**真相（用 level 字段重算，代码赋值可信）**：T53b 全部 14 个归档 run 的真实 L1（level=='L1'）污染率 = **0%**。每个 run 的 L1 只有 4-6 个节点，全是干净的维度描述（可行性约束/精度权衡/TCO/性价比/不确定性），P1_L1_SKELETON 骨架 prompt 工作正常。

**假阳性来源（双口径，2026-11-21 01:5x 连通性分析修正）**：parent_ids 丢失有两个不同指标，都是真的：
- **字段丢失率 3-12%**（L2+ 空 parent_ids，~14 个/run）= 直接断掉的链接数
- **骨架脱离率 13-46%（全量均值 25%，1340/5305）**= 断链簇根 + 其下内部链接完好的子孙。每个 run 有 6-15 个孤儿簇根（level=L2/L3/L4 但 parent_ids 为空），每簇挂 3-6 个完好子孙。之前报的 19%（80/429）是 sm-gpu-r1 的脱离率，**不是错误口径**（我 00:3x 的"修正"修错了方向，已回滚该说法）。
- 结构形态：**干净 L1 骨架（4-6 正交维度）+ 深层 L3/L4 主体（L4 占 40-66%）+ 25% 漂浮孤儿簇**。level 字段（意图深度）与计算深度（损坏后）的分叉恰好=孤儿簇：d1 比 L1 多 14 个、d2 比 L2 多 ~19 个，全是簇内节点。

**"非正交"观察同属此损坏（2026-11-20 23:5x 补验）**：之前"L1 非正交/正交检验放行"与"污染 71%"是同一数据损坏的两个视角，不是独立问题。level 字段的逻辑证明：创建代码 `next_lv = max(parent_levels)+1`，空 parents 只产 L1 → level=L2 的节点逻辑上必有创建时父链接，parent_ids 为空=链接后损，level 是创建时真相的证书。加验：更敏感启发式（公式符号/具体数值）抓出 16/72 个 L1，人工全检=全是"维度名：覆盖范围"式描述（含领域词如 BF16/αβ），无具体 claim，真实 L1 污染率仍 0%。抽 3 run 真 L1 维度名人工判正交：gpu（约束/精度/成本/性能/综合）、nat（分布/LRU/LFU/更新/溯源）、soc（假设链/逐利/归因/干预/置信度）——正交，无冗余。

**真正的 T53b bug = parent_ids 持久化丢失**（数据完整性问题，非分解质量问题）：
- 代码创建时 fallback 是挂整批父节点（`pids = [p.id for p in parents]`），不该为空
- 但 N30（L2）在 r1 轮 checkpoint 里已是根目录（`7/` 而非 `3/1/`），丢失发生在首轮写入之前
- 机制未完全定位（TODO：trace 创建→首轮 checkpoint 之间的 parent_ids 赋值路径）
- **恢复源核查（2026-11-21 00:2x）**：目录结构**不是**独立 ground truth——`_save_checkpoint`（line 1026-1034）的目录树是从内存 parent_ids 现场构建的，目录和 node.json 是同一份数据的两个编码，丢失节点在目录里同样被放根层。sm.log 只记父 ID（"fanout cap: parent N4 kept 8/12"）不记子 ID，也恢复不了。**结论：已丢失的 3-12% 链接无任何独立记录源可恢复**。修复方向（62 run 后）：(a) 修持久化 bug 本体；(b) expand 事件日志加子节点 ID 列表，给未来数据留独立恢复源
- **对 04-verify 的影响**：树结构/深度相关统计（S_alpha 层级贡献、depth 指标）在 parent_ids 丢失的节点上不可信；但 level 字段、claim 内容、judge 分、evidence 都安全

**历史版本 L1 污染的真正来源（prompt 定位）**：
| 时间 | commit | prompt | 效果 |
|---|---|---|---|
| 11-09 01:34 | 7152cec2b | v14：P1_DECOMPOSE 一次性拆整棵多层树 + "定量承诺"规则（每节点必须带具体数值/公式） | L1 污染 54-90%（claim 被顶到 L1） |
| 11-09 10:59 | 67176c6d4 | v15：阶段分离（P1 删敏感性规则，P4 加分析层） | nat 54%→38%（部分修复） |
| 11-11 22:17 | 35af322ef | T53：L1 骨架改纯目录层 P1_L1_SKELETON（3-7 维度，禁下钻） | **L1 污染 0%（已修复）** |

**结论**：历史 L1 污染 = v14 一次性 decompose + 定量承诺规则的产物，T53 的 P1_L1_SKELETON 已根治。T53b 不需要再修 decompose 层级放置——要修的是 parent_ids 持久化。

**深层结构实测（2026-11-21 01:5x，21 归档 run）**：
- **深度分布**：L4 占 40-66%（主体），L3 20-40%，L2 ~6%，L1 4-6 个。树是"窄骨架+深主干"形态，不是宽浅树。
- **深层内容质量（L3/L4 共 4751 节点）**：96% 含公式/数值（真推导，非空壳）；但 **66% 证据是占位/先验/逻辑校验**（无外部检索源）——深层节点"推导真、证据假"，与 57% 全局占位率×深度交互一致且更深。
- **正交验证**：sm.log 全量 551 通过 / 980 失败 = **36% 通过率**；失败原因分布：不完备 > 有冗余 > 非正交（非正交不是主因）。按 level 分层统计作废（sm.log 按 domain 模糊匹配，跨 run 节点 ID 撞号污染映射）——04-verify 需按 run 精确匹配重算。

**组合展开膨胀（2026-11-21 02:1x，gpu 域 4 归档 run）**：
- gpu 域 L3/L4 = 1302 节点 > 笛卡尔积上界 675（27 卡×5 精度×5 问题类型）——同一 (卡,精度) 组合被反复实例化（每组 5-34 节点，33% 节点跨多类型）。
- 问题类型分布：显存计算 39% / 吞吐估算 18% / 价格 TCO 15% / 质量损失 10% / 规格 8%——本质是同一套公式（KV Cache 公式、吞吐=带宽/权重字节数）对 27 张卡各实例化一遍。
- **04-verify 口径修正**：(1) 节点数指标（S_alpha、信息密度）被组合展开膨胀，gpu 域系统性低估；(2) Δ 对比需按 (卡,精度) 组合去重——节点数差异可能只是展开量差异非推理深度差异；(3) 正交 36% 通过率的"有冗余"主因=同组内组合冗余，非分解质量差。
- **微架构效率覆盖**：真微架构层（occupancy/warp/算术强度/roofline/cache 命中）仅 17 节点 vs 带宽吞吐层 406 节点（1:24）。有算术强度实算（GQA 头数折进 Ops/Byte）、Roofline 落地、带宽利用率修正因子 η、MoE 访问模式 30-50%——但 SM 占用率/warp 调度/寄存器压力/L1L2 命中率零覆盖。微架构效率停在 roofline 修正因子层，非独立分解维度（L1 六维度无此维度，骨架决定非 prompt 臂决定）。

**K^t 口径实测（2026-11-21 03:0x，gpu 域 5 run 全量，runs-s5 json）**：
- 口径修正：之前"1302"是归档子集数，5 run 全量 L3/L4 = **1584**（L3 437 + L4 1147）。
- **粗 K^t（独立推理模式）= 11 种，压缩比 144x**：vram 417 / throughput 377 / cost 286 / quant_quality 143 / other 110 / filter 83 / spec 61 / scoring 48 / compat 43 / normalize 13 / microarch 3。11 种模式跨 5 run 稳定（每 run 8-11 种，重复出现的是同一批）。
- **中 K^t（模式×实体类）= 565，压缩比 2.8x**——565 贴着笛卡尔积上界 675，证实树 ≈ "11 模式 × ~50 实体实例"的枚举。
- **信息密度 = 11/1584 ≈ 0.7%**（粗口径）。K 下界再修正（D 11-21 S28）：解空间=推理结构⊗实例空间（直积），效率函数确定后实例化=确定性计算（脚本求值+排序，β≈0），LLM 产出边界收在效率函数——**推理产物 K ≈ 14 原子**（11 效率函数+3 微架构系数）；卡参数表=外部数据（K=0），实例求值=计算（K=0）。1584 节点里 LLM 真推理仅 ~14 原子，其余 1570 是数据实例化+计算展开。
- **04-verify 直接用**：gpu 域 Δ 对比主口径 = 独立推理模式数（11），不是裸节点数（1584）；formula/text 两臂比"模式覆盖数 + 每模式推导深度"，不比节点数。

**组合展开的 general 改法（2026-11-21 02:2x，一条规则导出）**：
- **核心规则**：分解树编码"推理结构"（正交维度+推理模式），不编码"实例空间"（实体×参数组合）。实例化是叶节点展开，不是树分支。——解释 L1 干净（维度）/L2+ 膨胀（实例当分支）。
- 导出 3 落点（同一规则，非并列；①③ 按 S28 直积+推理/计算分离收紧）：① decompose prompt 加"实例折叠"：LLM 只产出效率函数 f(H)（参数化节点），实例值不进树——脚本读卡参数表求值+排序（β≈0），不逐实体建节点；② 正交验证加"实例冗余"检测：claim 结构相同仅实体名不同=冗余非正交（治 36% 通过率的"有冗余"主因）；③ 信息密度按"独立推理模式数"（去重 公式×维度）算，不按裸节点数（治 gpu 域系统性低估）。
- **执行边界**：①②③ 中 ①② 改 SM 代码=62 run 后（同质性约束）；③ 是统计口径，04-verify 现在就能按"组合去重"算，现有 62 run 数据可用正确口径出结论，不必等改代码重跑。
**对 D 之前决策的修正**："L1 污染作为负结果报告"这条作废——真实负结果是"parent_ids 丢失使 25% 节点脱离 L1 骨架（字段丢失率 3-12%，脱离率 25% 双口径），树=干净骨架+25% 漂浮孤儿簇"，不是分解质量问题。05-accept 对标 DESIGN.md 时，"judge gate 保证分解质量"假设**未被证伪**（L1 实际干净），需改口径。

**matched 批跨批 judge 漂移（2026-11-24 22:4x，04-verify 必须处理；22:5x 修正窗口假说）**：
- 现象：同 qid+arm=gpu/formula，旧批（results.json，11-18~11-21，runs_matched）cov=0 2/10、depth 0.344、answer 均值 5554 字符；新批（results-sm-matched.json，11-21~11-22，runs_sm_matched）cov=0 **7/10**、depth 0.358、answer 均值 7843 字符。**depth 持平但 cov=0 翻倍** → 非 pipeline 崩溃（崩溃会 depth 一起掉），是评分口径/输入变化。
- **窗口放大假说=红鲱鱼（22:5x 实测推翻）**：judge 窗口 12k→40k→50k（commit 5d4eac6cb/1ce794ac6）看似是因子，但实测**新批 30 answer 全 ≤10986、旧批 30 全 ≤8084，无一触及 12k 窗口** → 窗口从未截断任何内容，对 cov=0 飙升贡献为零。此前把"窗口放大"列为因子是误判。
- **真实因子=pipeline/prompt 变更**：两批之间（11-21 13:37~11-22 06:50）SM prompt 大改——5d4eac6cb（synth FULL v2：prompt 结论→推导链、per-level token 按节点数缩放 250tok/节点）、1ce794ac6（synth FULL v3：解禁 prompt 覆盖 RL 简洁偏好、L4 3.5x 输出）。answer 从均值 5554→7843 字符（更长）但更长≠更对齐 gold → 配合 rubric 加严（cbc92a202 GPU_RUBRIC 补微架构要点 ★F-D，落在旧批中途）→ 新批更容易全 0。
- **judge 非零成本（修正）**：judge_v2_depth.score_run 走 `from ablation_harness import call_llm`（每 run 1 次 LLM call，max_tokens=2000）→ **重判需 vLLM，非零 LLM 成本**。vLLM 被 q7 占用期间无法重判。
- 结论：**两批 cov 不可直接比**（pipeline+prompt+rubric 三重不一致）。cov=0 飙升 = prompt 解禁致 answer 变长变散 + rubric 加严的叠加，现有数据分不开两因子各自贡献。
- 04-verify 动作：① matched 批 cov 对比**只在同批内**做（新批 30 runs 同 pipeline+judge 版本，批内可比）；② 跨批 cov 趋势（旧→新）标"pipeline/prompt/rubric 漂移污染"不作证据；③ 跨批可比需固定 pipeline+judge 版本重判（**需 vLLM，非零成本**，待 q7 释放后）；④ depth 是树结构量非 judge 量，跨批 depth 对比相对稳健但仍建议同批内做。
- 附带确认：matched 批记账完整（cc-state-sm-matched.json 11-24 03:23 核验 30/30 done，results 30 runs 对账一致，recover_sm_matched.py 已从 archive 恢复 driver bug 期间 19 轮）。

**matched 批旧批(clean 层)臂间消融（2026-11-24 22:5x，回答"gpu 弱是臂特异还是题面固有"）**：
- 干净层=旧批（runs_matched，60 runs）的 **POST-rubric 层（11-19 19:19 后，n=53）**：该层内 rubric 版本统一（新）、judge 窗口统一（12k，窗口变更 11-21 23:35 在旧批结束 11-21 13:37 之后）→ 层内 formula/text 两臂可比。PRE-rubric 层仅 7 runs 且全是 gpu/formula（无 text 臂）→ 不可做臂间比，弃用。
- 臂间 Δ（formula − text，同 qid，POST-rubric 层）：
  - **gpu: Δdepth=-0.025, Δcov=+0.005**（f cov 0.111 / t 0.107，f depth 0.360 / t 0.385）→ **两臂在 gpu 上同等弱** → gpu 弱是**题面固有**（storage/硬件题难），非 formula 臂特异。
  - **nat: Δdepth=+0.113**（f 0.650 / t 0.537）→ formula 臂在 nat 明显更强。
  - **soc: Δdepth=+0.003, Δcov=+0.186**（f 0.900 / t 0.714）→ depth 持平但 formula 覆盖率更高。
- **结论：formula 臂的优势是域依赖的**——在 nat（推理域）和 soc（覆盖域）有净增益，在 gpu（硬件/算力域）中性（两臂都弱）。这解释了为何 gpu 是"弱域"：不是某个臂在 gpu 上退化，而是 gpu 题面对两臂都难。
- 口径注意：gpu/formula 在 POST-rubric 层仅 n=3（另 7 个 gpu/formula 落在 PRE-rubric 层），Δ 的 n 偏薄；但"两臂在 gpu 同等弱"的定性结论对 n 稳健（cov 0.111 vs 0.107 本就接近）。
- **分数时效核验（22:5x，防"分数是后来重算的"伪分层）**：results.json 与 runs/ 内嵌分数对账——**coverage 60/60 完全一致**（judge 原始分，run 时算）；**depth 19/60 有小幅出入**（0.01-0.19，run 文件 mtime 晚 60-140h = 11-24 模块重组 c4455d61c 拷贝+重算）。⟹ **Δcov 结论完全有效**（原始分）；**Δdepth 是统一重算值的对比**（同一新 depth 公式作用于全部 60 runs，系统性偏移在臂间相消，相对差异仍可比，但绝对值非 run 时原值）。
- 与上一条（跨批 judge 漂移）的关系：跨批 cov 飙升（新批 gpu cov=0 7/10）= prompt 解禁 + rubric 加严的**测量口径**变化；本条（同批 clean 层）= **真实实验**信号（gpu 题面固有难 + formula 优势域依赖）。两者正交，04-verify 应分开处理：跨批 cov 不作证据，同批 clean 层 cov/depth 臂间 Δ 可作证据。
