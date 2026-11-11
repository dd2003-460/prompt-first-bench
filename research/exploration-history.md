# PFB 探索路径全景（编号整理版 v2）

> origin: ai · 2026-11-11 · 成璐指令「s5又是什么，忘了，所以还能重新整理编号和过往探索路径吗」+「编号清楚吗，连续吗，历史探索路径这样可以看清楚吗」
> 本文件是唯一的"编号→含义"权威映射 + 完整探索叙事。旧文档里的裸编号（vN/SN/TN/rN）以本文件为准解读。
> 配套：`numbering-audit-2026-11-11.md`（5 套编号系统的混乱现状 + 迁移清单）。
> v2 修订（11-11 晚）：v3-v15 段从 git log 逐版本重建，runs-* 目录数据实测回填，runs-r293 等来历查清。

## 0. 四套编号体系速查

| 前缀 | 含义 | 命名空间 | 例子 |
|------|------|----------|------|
| **S** | 实验臂（ablation arm）——一种 prompt/管线策略 | S0–S8M，跨全部 bench 题共用 | S5 = 层级分解+核验管线臂 |
| **v** | S5 臂内部的 prompt/代码迭代版本 | v3–v17 → T53（连续线，不另起 v18） | v17 = 无限预算层级 INDEX 分解 |
| **T** | 任务 ID（goal 执行单元） | 全局递增，tasks/ 下唯一 | T53 = decomp 状态机重构 |
| **r** | 运行副本 / 工程迭代轮 | 两个不同命名空间（见 §4） | runs-s5-gpu-v13-r5.json 的 r5 = 第 5 个 rep |

**S5 定义**（最常被忘的一个）：pfb 消融实验里"带真实检索的多步研究管线"那一档。
S0 = 裸 CoT baseline；S1 = 单轮结构化；…；S5 = decompose→search→verify loop→synthesize 四阶段管道
（harness 层真调 research_hook 检索，每节点独立 LLM 校验，失败回炉 ≤K 轮）；S8/S8L/S8C = 质询循环变体。
代码入口 `experiments/stage-ablation/s5_pipeline.py`（P1–P4 线性管线），
层级化扩展 `s5_hierarchy.py`（v17），目标函数驱动重写 `s5_state_machine.py`（T53）。

**一句话主线**：S5 臂从"往 prompt 里堆规则"（v3-v15，失败）转向"目标函数驱动的状态机"（v16→v17→T53），
中间发现 v17 的爆炸本质是 Goodhart 刷分（目标函数只奖规模不罚冗余），T53 就是修这个的目标函数重写。

## 1. 时间线主线（逐版本连续叙事）

### Phase 0 · 建 bench + 四臂基线（11-06~07）

5 道事实题（nat/soc/gpu/hw/bio）+ gold 要点表 + judge 口径（rubric v2）。
四臂 n=30：**S0=0.5558, S1=0.5746, S5=0.7907**（B-face 跨族 judge 验证方向一致）。
C-face 判官 FAIL；E3 机制 = 生成时预防。
同期 r293 轮次（主仓全局迭代号）出了 scores-v2（改进 M1 judge + Q4 gold 修正）——
这就是 `runs-r293/` 目录的来历：11-06 那次打分快照，不是某个 run 配置。

### Phase 1 · S8 质询循环（11-07）

S8 = S5 + 矛盾质询 loop；O6（矛盾发现）均值 0.876。
self-judge vs B-face 对比暴露 self-judge 系统性偏高 ~0.14（S8: 0.783→0.642）。
S8L（长 prompt 发散前段）/ S8C（约束化模板）两轮 → #24 任务类型路由修正为"结构效应待确认"。
产出：`runs/s8-report.md`（完整四臂表）。旁支结论进了 paradigm-routing 仓（T-PR-13 persona 零效应等）。

### Phase 2 · S5 管线硬化（11-08~09，v3→v15）

北极星：S5 稳定超过 S0（nat cov≥0.634, gpu depth≥0.50）→ 可发表消融报告。
这段是"往 prompt 里堆规则"的实验期，每个版本对应一次 P1/P4 规则修改 + 一轮 smoke 验证。

**11-08 下午（v3 前后，基础设施日）**——一天内连改十几个 commit，把管线从"能跑"推到"能量化"：
- 深度连续打分 judge_v2_depth 上线（binary coverage 之外加 k·ln(k+1) 加权深度分）
- GPU 题 rubric 重建（31 节点 gold-tree 1:1 对齐）
- P1 迭代分解（3 层树，8→25 节点）、P1.5 两遍 gap check（A=独立维度/B=补洞）
- 来源标签（given/knowledge/search）强制进正文、内外校验链闭合
- **关键转折：引入分解目标函数**——先 Σn·ln(kₙ)，后对称化 S_α = Σ[n·ln kₙ + α·kₙ·ln n]（α=0.5），
  边际增益精确化为 Δ=ln((k_n+1)/k_n)，用它替代固定节点数 band 做停止判据
- 成璐指令：撤掉检索预算上限（21:58）

**11-08 晚~11-09 凌晨（v10 诊断 → v13 稳定性）**：
- v10 诊断：排除性结果不该终止树（exclusion ≠ dead branch）
- v13 = 50-rep 稳定性 runner 上线；首跑 r5 截断失败 → 根因是 early-stop 不是 max_tokens
- 凌晨连续补规则：P4 rule 6 口径分离（byte vs request hit rate 分开报）、P1 rule 8 子问题覆盖、
  P1 rule 9 定量承诺（每节点必须带数字/公式）、P4 rule 5 反 hedging（69% 的 p4-miss rep 明明有 verified 公式节点却说"无法给出定量"）
- 归因审计结论：**P1 > P4 > retrieval**（丢分大头在分解层不在检索层）

**11-09 早（v13/v14 判决）**：
- round-3 结果：**v13 gpu FAIL（depth mean 0.389 < 0.50）**；nat-v14 早期 0.605（+0.070 vs 之前）
- v14 = nat 101 reps 量产：mean cov 0.578，仍低于 S0 的 0.637
- rule 9b 两次变形：先是硬件 spec-table + TCO 公式强制（领域规则）→ 验证失败 → 换成通用参数敏感性分析
- soc rule 7 同构失败（point-0 命中率 54%→17%）

**11-09 上午（v15 + 转向决定）**：
- v15 = 阶段分离原则落地：P1 删敏感性规则（纯分解），P4 新增分析层（对 verified fact table 做敏感性/条件推断/分布估计）
- v15 smoke 6/6：mean cov 0.361，方差极大（0.0~0.667）
- **判决：prompt 层行为塑造有容量上限，继续加 rule 稀释基础覆盖，负收益**（v15 + soc rule 7 两个独立证据）
- goal v3 分解落盘（decomposition-goal-v3.md）：杠杆换方向——① 结构（状态机）② 激活（推理倾向）
- 同期 S0-gpu baseline 收口（n=10 cov=0.167）：gpu 题难是模型天花板，不是管线丢失

### Phase 3 · 状态机转向（11-09，v16→v16.3）

- v16：P1e 状态机臂——多轮回退分解 + confirmed-fact 注入 + S_α 边际停止
  （R1=全层饱和 / R2=预算阀 / R3=S_α 停滞 2 轮）
- v16.1：真无限回退（删固定轮数 cap）；v16.2：per-layer cap（6/round/layer，溢出顺延）
- v16.3：R2 降软约束（压缩信号而非停止）+ R4 防御硬帽（bug#5：R2 软化后 gpu R1 永不触发，单 rep 跑 >15min）
- smoke 结果：**nat 首次超过 S0（+0.03）**；gpu 被 R2 硬停杀死（cov 0.167，与 S0 持平）

### Phase 4 · v17 层级 INDEX 分解 + Goodhart 诊断（11-09~11）

- v17（11-09 14:41）：整题拆大树换成逐层 INDEX 分解——每个父节点是"文件夹"，
  子节点清单是该文件夹的 INDEX.md（只列条目+一句话说明），每层一次 LLM 调用只展开一个父节点，上下文永远小。无限预算。
- 11-09~11 之间跑了 prod 数据（S0-gpu r1-r10、S5-gpu-v13 r10-r28+、S5-soc r94-r99、v16.3 smoke）
- v17 真实分解量浮出（11-11 19:10）：**1930 节点 / 10 轮 / 有效维度仅 6-8**，指数膨胀尾巴 r7 +313 → r8 +412 → r9 +560，r10 崩（HTTP 502）
- 病根诊断三连（11-11 19:10→19:31）：
  1. 膨胀根因 = 无限预算 + 前 40 字符弱去重（同义节点判不出来）
  2. 判据与意图错位：可拆性判据 ≠ 正交性判据
  3. **本质定性（成璐质询后修正）：这是 Goodhart 刷分捷径，不是"模型没读懂"**——
     S_α 只奖规模不罚冗余，模型学会堆同义节点刷分。修法 = 冗余惩罚 + 边际信息增益停止判据
- 同一现象的学术侧调研外包 arena（T-PR-15：文字目标函数 Goodhart 雪球，COMPLETED，回执已落盘）

### Phase 5 · T53 目标函数驱动状态机（11-09~11，当前）

T53 = v17 的下一版（同一改进路线，非换名重启；版本号跟任务 ID 走，不另起 v18/v19/v20）。

设计：{IDLE, DECOMPOSE, VERIFY, REWORK, STOP}，J_necessary/J_verify/J_stop 机器裁决每个转移。
- 停止判据：necessary pass_rate < 30% × 2 连续轮（中文 n-gram Jaccard 不可靠，弃用 gain 阈值做停止）
- necessary-judge 批量化（单次 LLM 调用裁全部候选，~30× 提速）
- 防泄漏 v3：跳过英文/数字实体，拦 ≥8 字中文串；leak_check 每轮跑，命中即中止
- 顶层 try/except + checkpoint 落盘 + --resume 续跑（修 E6 静默死）

工程迭代（sm-modification-log r1-r6，详见该文件）：
- r2：核验全节点覆盖（AC3）+ parent_ids 索引 bug
- r3：checkpoint/resume/retries（E6 静默死修复）
- r4：--resume 参数解析修复 + skip_l1 防重拆 + 泄漏口径明确（给定实体白名单）+ E7 卡点定位（ClashX 挂掉→ego-browser 全盲）
- r5：5xx 指数退避 + 探针第三路
- r6：pass_rate 增量计算显式化（cumulative counter + hasattr 隐式默认值 bug）

smoke 轨迹：
- v5（11-11 白天）：**75 nodes / 2 rounds / natural stop / 0 leaks**（vs v17 的 1930/10/crash）
- r7（11-11 晚，L1 skeleton 加入后）：r1 +84（total 133），gain 0.893，ver 48/84，rework 42；
  r2 +0，dropped_redundant 236 → 自然停。**133 nodes / 2 rounds / 0 leaks**

下一步：开源 deepresearch 框架 baseline（criteria v2：本机 Qwen3-27B @8787 + 开源框架，同模型比策略）
→ 5 题泛化 bench 对比（AC4：≥5 题胜出才成立）。

## 2. 旁支（与主线正交，各自收口）

| 任务 | 内容 | 状态 |
|------|------|------|
| T51 | S(T)=Σn·ln(kₙ) 目标函数 prior-art 雪球调研 | done（11-08） |
| T52 | prompt 分解→推理深度碰撞调研 | done |
| T-PR-13 | persona 激活调研（paradigm-routing 仓） | RESOLVED：双重稀释假说 |
| T-PR-14 | reasoning-as-search 调研 | arena 在跑（session 01a1b467） |
| T-PR-15 | 文字目标函数 Goodhart 雪球调研 | COMPLETED（回执已落盘） |
| T53C | bench 派发 + SOTA 分数表 | 部分完成（12 系统表已 cherry-pick；baseline 框架 TBD） |
| 自判噪声实验 | H1/H2/H3 对照设计 | 设计完未跑 |

## 3. runs-* 目录 → 版本映射（stage-ablation/ 下，实测核实）

| 目录 | 对应版本/事件 | 实测数据 |
|------|--------------|----------|
| runs-s5-smoke | 早期 S5 管线冒烟（-v2 后缀 = 第二轮重跑） | — |
| runs-s5-gpu-v4 | 基础设施日后首个 gpu 单 rep | depth 0.228, cov 0.200, 23 nodes |
| runs-s5-gpu-v7 | P1 rule 6/7 时期 | depth 0.167, cov 0.267, 17 nodes |
| runs-s5-gpu-v10 | exclusion 修复后 | depth 0.249, cov 0.200, 37 nodes |
| runs-s5-gpu-v12 | 规则堆叠后期 | depth 0.377, cov 0.267, 40 nodes |
| runs-s5-gpu-v13 | v13 50-rep 稳定性 | 34 个 rep 文件，depth mean ≈ 0.395（FAIL < 0.50） |
| runs-s5-nat-v14 / runs-s5-soc-v14 | v14 量产 | nat 101 reps，mean cov 0.578 |
| runs-s5-prod | 早期 prod 数据（S0-gpu r1-r10 等） | — |
| runs-s5-v16.3-smoke / runs-s5-v17-hier-smoke | v16.3 / v17 冒烟 | v17 console log 含 r1-r9 全轨迹 |
| runs-s5-sm-gpu(-r3/-r4/-r7) | T53 状态机 smoke（sm = state-machine, gpu 域） | v5=75 nodes；r7=133 nodes |
| runs-t53 / runs-t53b | T53 早期 run（t53b = b 批次） | — |
| runs-s8b / runs-s8b-a3 / runs-s8b-a4 | S8B 四臂（a3/a4 = A3/A4 臂复测） | — |
| runs-d1-c1 / runs-d1-c1-scored / runs-d1score | D1 题 C1 臂 + 打分（d1score = 重复目录，待清） | — |
| runs-r293 | **11-06 r293 轮次的打分快照**（scores-final：S5 n=3/题，M1 judge 改进版 + Q4 gold 修正） | 不是 run 配置，是 scoring snapshot |
| runs-baseline / runs-prod / runs-prod-s3 / runs-prod-temp0 | S0 baseline / prod 各配置 | S0 nat 0.600±0.205, soc 0.957±0.075 |

注：v3-v12 各目录只有 1 个 rep（单 rep smoke 性质），不是量产数据；量产只有 v13（34 reps）和 v14（101 reps）。

## 4. "r" 的两个命名空间（易混点）

1. **run 内 rep/round**：`{ARM}-{Qn}-r{k}.json` 的 k = 第 k 个独立运行副本（rep）或管线内部第 k 轮
   （v17 层级分解的 r1-r10 = 逐层展开轮次）。scorer 硬编码此格式，**不改**。
2. **工程迭代轮**：`sm-modification-log.md` 的 r1-r6 = 跨 run 的代码修改批次。
   历史遗留：runs-r293 的 293 = 主仓全局迭代轮号（ralph-loop 时代，11-06），仅此一处。

## 5. 编号纪律（今后新增东西按这个来）

- 新实验臂 → 下一个 S 编号（S9 起），在 s8-report.md 同级加一行定义。
- S5 线代码大改 → 跟任务 ID 走（T53、T54…），不再发明 vN；需要版本锚点时在
  sm-modification-log.md 加一行 "vN = rX+rY merged release"。
- 新 run 目录 → `runs-{arm}-{domain}-{version}/`，version 用任务 ID 或版本号，禁止无后缀裸目录。
- 新任务 → tasks/ 全局递增 T 编号；stage-ablation/tasks/ 内的 T54+ 并入主序列前先查重。