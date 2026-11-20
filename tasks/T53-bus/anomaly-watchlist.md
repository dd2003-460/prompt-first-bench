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

**假阳性来源**：T53b 有 ~19% 节点（sm-gpu 80/429）level 字段与实际树深度不一致——一批 L2/L3/L4 的具体 claim 节点（N30-N34/N150-N154/N470-N473）**parent_ids 为空**，depth 计算走 parent_ids 链，它们掉到 depth 1 被误判成"L1 混入具体 claim"。

**真正的 T53b bug = parent_ids 持久化丢失**（数据完整性问题，非分解质量问题）：
- 代码创建时 fallback 是挂整批父节点（`pids = [p.id for p in parents]`），不该为空
- 但 N30（L2）在 r1 轮 checkpoint 里已是根目录（`7/` 而非 `3/1/`），丢失发生在首轮写入之前
- 机制未完全定位（TODO：trace 创建→首轮 checkpoint 之间的 parent_ids 赋值路径）
- **对 04-verify 的影响**：树结构/深度相关统计（S_alpha 层级贡献、depth 指标）在 parent_ids 丢失的节点上不可信；但 level 字段、claim 内容、judge 分、evidence 都安全

**历史版本 L1 污染的真正来源（prompt 定位）**：
| 时间 | commit | prompt | 效果 |
|---|---|---|---|
| 11-09 01:34 | 7152cec2b | v14：P1_DECOMPOSE 一次性拆整棵多层树 + "定量承诺"规则（每节点必须带具体数值/公式） | L1 污染 54-90%（claim 被顶到 L1） |
| 11-09 10:59 | 67176c6d4 | v15：阶段分离（P1 删敏感性规则，P4 加分析层） | nat 54%→38%（部分修复） |
| 11-11 22:17 | 35af322ef | T53：L1 骨架改纯目录层 P1_L1_SKELETON（3-7 维度，禁下钻） | **L1 污染 0%（已修复）** |

**结论**：历史 L1 污染 = v14 一次性 decompose + 定量承诺规则的产物，T53 的 P1_L1_SKELETON 已根治。T53b 不需要再修 decompose 层级放置——要修的是 parent_ids 持久化。
**对 D 之前决策的修正**："L1 污染作为负结果报告"这条作废——真实负结果是"parent_ids 丢失破坏 19% 节点的树结构"，不是分解质量问题。05-accept 对标 DESIGN.md 时，"judge gate 保证分解质量"假设**未被证伪**（L1 实际干净），需改口径。
