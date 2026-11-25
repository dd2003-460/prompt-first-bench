# T-REPAIR-1 repair loop 实验设计（2026-11-24 22:40 · Lead 方向判断）

> origin: ai · 触发：给 D 的 pfb 上限判断中"repair loop 是唯一还开着的高杠杆"落成可执行设计。机制依据 = workshop-draft-metacog §5 implication-1（刚读，①类）。

## 背景（workshop §5，不重述）
- 节点级修复率 3.7%，85.3% 的 rework 节点落 degraded 终态
- 72.6% 的 Q6 rework 节点产出实质不同的 corrected_claim，但执行路径（angle）从不写回 claim
- 两个结构缺陷：(a) directed-fix 路径不可达（0/8,870 事件）(b) 单次尝试（rework_count 恒=1，pool 只含当前轮新节点）
- max_rework=2 参数从未被行使——上限是结构性的（pool 组成），不是参数

## 两个正交修复
- **Fix-A（directed 可达）**：让 directed-fix 分支可达。唯一 claim-writing 路径（L821）在 directed 分支里。修改点 = 使 directed 分支可达的路由条件。[具体条件待 subagent 读 SM 确认]
- **Fix-B（re-entry）**：让 reworked 节点跨轮重入 rework pool。修改点 = pool 构造（L1450，现从本轮 deduped 建）→ 并入上轮 rework 失败的节点。[具体 diff 待 subagent 确认]
- 正交性：A=路径可达性，B=尝试次数，各自独立可测

## 实验设计
- 析因 2×2：baseline / A / B / A+B（4 臂）
- budget=300（中段，cov 未饱和，修复效应才有空间显现）
- 域：Q6（rework 节点最多 621，对修复效应最敏感）
- 自变量：两修复。因变量：节点级修复率（rework 节点中 claim 被实质改写且过验证的比例）
- 控制：与 baseline 同 budget/域/seed

## 预测（可测，workshop §5 导出）
- **P-A**：Fix-A 后 value_mismatch 修复率 > blind-re-search 2.4% 基线；no_source rework（4.0%）不变
- **P-B**：Fix-B 后整体节点级修复率 > 单次 3.7% 基线
- **P-A+B**：若正交，A+B 臂 ≥ max(A,B)；若亚可加/超可加 = 新发现（说明两修复有交互）
- **判别**：若 A、B 都不升 → 瓶颈转移到 fixer 能力或 contradiction 证据，届时才考虑"停止 rework value_mismatch"

## 验收
- 统计门禁（非单 run）：修复率差 > within-run 噪声（judge 噪声 ~0.1）；n=3 suggestive，正式 claim 需 n≥5 + bootstrap CI
- 等效性：若声称"A 无效"需等效性检验（预设最小效应），不能用"不显著"代替"无效"

## 时序约束（关键）
- **必须在 T-PR-17 pilot 完成后（~09:00）**：pilot runner import s5_state_machine.py，现在改 SM 破坏单变量前提
- r3 队列也在跑（import SM），双重冻结
- 执行序：pilot 完 → 确认 SM 不再被 import → 应用 Fix-A/B（git commit 留回滚点）→ 跑 4 臂

## 与 T-PR-17 关系
- T-PR-17 = verify 阶段 4 臂 suffix 消融（canonical/verify-off/null-control/verify-late）
- T-REPAIR-1 = rework 阶段修复环改造
- 不同轴、不冲突，但都改 SM → 必须串行，T-PR-17 先（pilot 已在跑）

## 待办
- [x] pilot 后：subagent 读 SM directed/rework 代码，确认 Fix-A/B 具体修改点（路由条件 + pool 构造 diff）→ **2026-11-24 23:30 完成**，见 `repair-loop-diff-prep-20261124.md`（两缺陷证实 + 3 份 ready diff + 4 臂执行序列 + P-A 功效/口径注记）
- [ ] 应用修改（git commit）——**注意 4 臂序列**：baseline 臂必须跑未修改 SM（prep §4 的 5 步序列，勿先 apply 再跑臂）
- [ ] 跑 4 臂（budget=300, Q6, n=3）
- [ ] 分析：修复率矩阵（4 臂 × rework 类型）+ P-A/P-B/P-A+B 判别

## 运行中核验记录
- **2026-11-25 12:35 分析链动态对账（baseline-r1 真实数据）**：执行器 [stat] `rework=97 mode={unknown:47, angle:50} repair_rate=0.06` 与 `t-repair1-analysis.py` 直接计算完全一致——47 个"unknown"= parent-review 事件（`{parent_id, issues, suggestions}` 结构，无 mode 键，非解析失败），`event_modes()` 第 85-86 行 `if not mode: continue` 正确排除；节点级 n_rework_nodes=50 / n_fixed=3 / n_corrected=50，3/50=0.06 与执行器 repair_rate 吻合。→ 4 臂 mode 比较不被 parent-review 污染，明早 postcheck 自动析因的数据链在真实数据上验证通过（比静态预验证强一档：动态数字对账）。
- **2026-11-25 12:40 baseline-r1 效度+画像**：leak_hits=0（无 gold 泄露，效度 OK）；status 分布 verified 218 / pending 35 / degraded 47。~~degraded 47 全部来自 SM 第 761 行（rework_count≥max_rework 放弃）~~【12:55 修正，见下条】；43/50 angle rework 节点最终 degraded。→ **baseline 缺陷画像闭合：不是"没 rework"（rework=50、corrected=50 全改写），是"改写后过不了验证"（3/50 verified，43 改写失败判死）**。Fix-A/B 预期效应方向=降低 degraded 计数（修复环路由/pool 让改写更对路）。
- **2026-11-25 12:55 degraded 路径精修（推翻 12:40 的"全来自 761"）**：逐节点对账 rework_count + rework_events 成员资格 + SM 源码（616/761/785/1231/1777 五个 degraded 赋值点），degraded 47 实际分三路：**① 43 个 rework_count=1**（在 rework_events，angle 模式）= 质询失败→进 pool→改写一次→仍不过验证→**SM 785 行**（`if not ok and status!=verified: degraded`，尝试失败判死）；**② 4 个 rework_count=0**（N49/N65/N68/N89，全 L3，**不在 rework_events**）= verify_node 判 degraded（s5_pipeline L246-247，质询驳回具体经验常数）后**所在轮次批次 verified 率 ≥ 0.85 → `_should_rework`(L728,verify_threshold=0.85) 返回 False → L1451 整批跳过 `_rework` → 这几个节点从未进 pool**（代码铁证：rework_count=0 + 不在 rework_events ⟹ 其批次 `_rework` 未被调用 ⟹ 批次 rate≥0.85）。**数据级坐实（rounds_log）**：R2=N31-N118（n_new=88），4 节点 N49/65/68/89 全落 R2 区间，且 R2 `reworked=0`（verified 80/88=0.91≥0.85 门禁跳过）；对照 R1（23/30=0.77）reworked=7、R3（135/177=0.76）reworked=43 均触发 → 机制从代码推理升级为轮次日志实证。**50 个 angle-rework 节点完整终态分解**：43 degraded + 4 pending（改写一次后停在 pending，strict 口径不计入修复分子，安全）+ 3 verified（=repair_rate 0.06 的分子）。**③ 0 个走 761**（rework 预算耗尽需 count≥max_rework=2，因 pool 只含当轮新节点〔结构性缺陷 b〕，节点改写失败后下轮不在 pool，第二次机会永不发生，count 封顶=1）。→ **Fix-B（跨轮重入）的主杠杆=救那 43 个"改写一次没过却没机会再试"的节点；4 个批次门禁漏掉的 Fix-B 也救不了（需另路：`_should_rework` 批次级门禁不应整批跳过 degraded 节点——批次 rate≥0.85 时个别 degraded 仍应进 pool，或 degraded 节点无条件入池）**。degraded 高度集中 L4（42/47，L4 退化率 24% vs L3 5%），claim 全是具体经验常数（计费档位/校准系数/成本公式），evidence 全 `[质询]`："具体经验参数缺乏普适性/缺来源"→corrected_claim 改成对冲表述（"需根据实际负载测算"）→对冲版仍不过验证。
- **2026-11-25 14:12 复现方差性质定量（树结构级分叉，节点 ID 跨 rep 不稳定）**：r1/r2 rework 节点 ID 集合 **Jaccard=0.09**（交集 11，r1 独有 39，r2 独有 66）；"交集" ID 的 claim 相似度仅 0.08-0.13 → **节点 ID 按创建顺序分配，树早期分叉后 ID 错位，同 ID ≠ 同节点**，节点级跨 rep 比较无效（~14:12 初稿误把 1 个 ID 碰撞的 degraded→verified 当"跨 rep 修复成功案例"，撤回）。**正确读法**：复现方差是树结构级分叉——temp=0.0 确定性下，早期检索差异（Bing 实时漂移 + 缓存不对称）→ claim 不同 → verify/rework 路由不同 → 下游级联，两个 rep 是**不同轨迹**而非同轨迹的判定噪声。**对功效的实质影响**：节点级 bootstrap CI 把 rep 内节点当独立样本，但 rep 间是不同轨迹，CI 系统性偏窄；真实不确定性在 rep 级（r1 0.06 / r2 0.039，spread 0.021）。**明早读法强化**：TOST/显著性以 rep_spread caveat 为闸门（已内置：spread>0.5×CI 宽→自动降权）；rep 级方向一致性（3 rep 中 ≥2 同向）比节点级 p 值更可信。level 分布（仅 rep 内有效）：r2 rework 偏均匀（L2 13/L3 23/L4 30），r1 集中 L4（33）+L2（6）。
- **2026-11-25 14:05 rep 独立性审计（缓存共享问题，已知限制不中断 run）**：执行器**未设 Q6_REP** → research_hook 缓存 key（qid+question，7 天 TTL）不含 rep 标识 → r2 有 17 次 CACHE-HIT 直接复用 r1 的检索快照（r1=0 冷启动）。**影响评估**：①LLM temperature=0.0（SM L180/237 确定性），缓存命中内容=r1 冻结的 web 快照，不引入 LLM 采样偏差；②r1↔r2 观测到的复现方差（rework 50→77）主要来自**实时 web 检索的非确定性**（Bing 结果集随时间漂移），缓存反而部分抑制它（17 次命中冻结了早期查询）；③对 4 臂比较：早期树确定性相同→问题串相同→缓存命中在各臂间**对称**（非差异化混淆），分歧从首次 rework 后才开始，耦合面 ≈ 早期 8%（17/~200 查询）；④方向不明、幅度小 → 定性为**已知限制**，不中断 run（已跑 9h+，重启代价 ≫ 影响；且运行中改执行器=改运行中程序，红线）。**若重跑**：执行器 rep 循环加一行 `export Q6_REP=$rep`（11-23 既有修复机制，T-REPAIR-1 执行器漏接）。分析脚本的 rep_spread caveat 是运行时兜底（spread 超阈值自动降权读法）。
- **2026-11-25 13:58 r2 完成 + baseline 复现间方差（新事实，影响功效解读）**：r2 DONE 91min（r1 54min），300 节点，reworks=121（angle=77），**repair_rate=3/77=0.039**（r1 3/50=0.06），status verified 192/pending 48/degraded 60（r1 218/35/47），leaks=0。**同代码两次 rep：angle rework 50→77（+54%）、repair_rate 0.06→0.039、degraded 47→60** → baseline 自身噪声不小，明早析因必须用 3-rep 池化均值（分析脚本已是此口径），且单臂 diff 的置信区间要计入 rep 间方差，实际功效低于单点估计（0.10 效应可能更偏 suggestive）。**减速原因定量**（推翻 13:45"卡住"误判）：LLM 中位耗时 r2 2.9s ≈ r1 2.8s，慢在尾部——p90 20.4s vs 9.6s、max prompt 193k vs 106k（树长到后期 verify 批变大）；r2 调用量 755 已超 r1 全程 686，不是卡住是每 rep 自然变长。**ETA 修正**：每 rep ~90min（非 54min），剩 10 reps ≈ 15h → 11-26 凌晨~清晨完成（checklist 的"凌晨~上午"窗口仍成立）。
- **2026-11-25 13:15 Fix-B 效应机制先验（43 个改写失败节点的质询理由分类）**：对 43 个 angle-rework→degraded 节点的质询驳回理由做正则分类：**A 经验常数缺普适性 37（86%）/ D 逻辑·量纲·公式真错误 3 / E 未分类 3**。决定性证据：**14 个 corrected_claim 已去数字改纯对冲（"具体取决于带宽/供应商而异"）仍被驳** → 墙不在数字本身，在 verify 标准（第一性原理普适性）与 L4 经验常数内容的结构性不兼容，改写（含对冲化）无法突破。**Fix-B（第二次机会）机制预测：救回上限 = D/E 类可修真错误 ≈ 3-6 节点 → 节点级修复率 ≈ 0.12-0.18**（baseline 0.06 之上 +0.06~0.12），恰在功效临界区（power=0.8 需 0.16）→ 明早结果大概率 suggestive 不 conclusive，TOST margin 0.10 成为关键读法：diff CI 落 [-0.1,0.1] 内 = 与 baseline 等效（Fix-B 无效，瓶颈=verify 标准而非尝试次数，下一步应改 verify 对 L4 经验常数的判据而非加 rework）；落外 = 部分有效。**正面对照（3 个修复成功节点）**：N38/N41 的改写都把经验常数剥成可推导结构关系（"70%→50% 阈值"→"当自建单位成本>公有云变动成本时"）→ 过验证；N271 为 rework 后逻辑推导成立（来源未直接覆盖仍放行）。→ **Fix-B 二次改写的有效路径 = "常数→结构关系"剥离，不是换个角度重搜**；救回上限预测维持 3-6 节点（86% A 类里只有少数能剥出结构关系）。
- **2026-11-25 13:05 统计功效核算 + TOST margin 修正（预防明早结论死区）**：①功效（节点池化 n=150/臂, p0=0.06）：power=0.8 需 p1≈0.16（救回 ~15 节点/臂）；真 diff=0.05 时 power≈0.15、diff=0.10 时 ≈0.46、diff=0.14 时 ≈0.74 → **若 Fix-B 真实效应 <0.10，明早"不显著"不能下"无效"结论，须看 TOST**；②发现 TOST margin=0.05 不可行：n=150/臂时差值 CI 宽≈0.107 > 2×0.05=0.10 → margin=0.05 下"等效"永不触发，"无效"与"功效不足"无法区分（bootstrap 校准单臂半宽 0.037，与解析 0.038 一致）。**已修**：`t-repair1-analysis.py` MIN_EFFECT 0.05→0.10（恢复 T-PR-17 先例值），dry-run 验证 gate 正常 + TOST 双向行为正确（CI⊂[-0.1,0.1]→等效；越界→不等效）。明早读法：P-B 差值 CI 落在 [-0.1,0.1] 内才可判"等效/无效"；落在外且不显著 = 功效不足，不下结论。
- **2026-11-25 12:45 判别逻辑鉴别力测试（构造数据，4 分支全过）**：①rate/bootstrap_ci/tost 单元行为正确（3/50→CI(0,0.14)；0/50 边界退化 CI=(0,0) 但双向 TOST 结论均不翻转：fixB=0 vs baseline=3 → 判不等效✓；双臂都 0 → 判等效✓）；②交互分类 4 分支（orthogonal×2/superadditive/subadditive）构造值全命中；③parse_rep_rc 对真实 executor log 解析正确（baseline-r1 rc=0）；④load_arm_runs 文件名模式与实际产物 `baseline-r1-<ts>.json` 匹配，rep_rc 门禁生效。**遗留 caveat（不修，现实风险≈0）**：load_arm_runs 注释"glob 按文件名排序取最新"不严谨（glob.glob 不保证排序），仅当同一 rep 存在两个文件（手动重跑）时才有歧义；今晚全自动链每 rep 单文件 + 无重试 + checkpoint 在子目录不被递归 → 不触发。
- **2026-11-25 19:08 r1 机械指纹闭合（两 Fix 均按设计工作, 效果方向待 3 rep 定论）**：rework_events mode 分布——baseline: angle 50 + directed **0**（directed 不可达=设计文档所述缺陷, 铁证）；fixA: angle 80 + directed **4**（Fix-A 让 directed 可达 ✓）；fixAB: angle 98 + directed 6 + multi-rework **25**（Fix-B 跨轮重入 ✓）。**25 个 multi-rework 节点终态 25/25 全 degraded, 救回 0**——二次机会被消耗但无一过验证, 与 13:15 悲观支预测一致（墙在 verify 标准 × L4 经验常数结构性不兼容, 非尝试次数）。fixAB 单次 rework 54 节点终态: degraded 45 / pending 8 / verified 1。⚠️ r1-only 不定论; 若 r2/r3 同向（multi 全 degraded + 修复率 ≤ baseline）, 则 TOST 等效判定的概率上升, 下一步方向=改 verify 对 L4 经验常数的判据（"常数→结构关系"剥离路径, 见 13:15 正面对照 N38/N41）, 而非再加 rework 机会。
- **2026-11-25 19:11 r1+r2 同向确认（19:18 预测兑现一半）**：fixAB 二次机会节点累计 40 个（r1 25 + r2 15）**全 degraded、救回 0**；修复率 r1 0.013 / r2 0.021，均 ≤ baseline（0.060/0.039）。fixA 同样不高于 baseline（0.048/0.012）。→ 19:18 预测"r2/r3 同向（multi 全 degraded + 修复率 ≤ baseline）→ TOST 等效概率高"已兑现 r2 一半，剩 r3 确认。机械指纹跨 2 rep 稳定（fixA directed=4/5，fixAB multi=25/15）→ 两 Fix 确实在工作，效应量不涨。**当前方向判断（r3 前, conf 0.7）**：Fix-B 的"二次机会"机制成立但无效（墙在 verify 标准），明早大概率 TOST 等效（CI⊂[-0.1,0.1]）→ 下一步改 verify 判据而非加机会。
- **2026-11-25 19:18 二次机会机制诊断升级（fixAB-r1 25 multi 节点逐事件对账）**：排除"同策略重复"假设——25 节点第二次 rework 全部生成了**新改写**（corrected_claim 非空且≠原 claim，15/25 为对冲表述"取决于/而异/需根据"），但新改写 25/25 仍不过验证 → 墙在 verify 标准 × L4 经验常数结构性不兼容（非尝试次数、非改写策略）。与 13:15 正面对照一致：唯一有效路径="常数→结构关系"剥离（N38/N41），二次机会给的是"换说法重试"，给不出"剥结构"。**若 r2/r3 同向（multi 全 degraded + 修复率 ≤ baseline），TOST 等效判定概率高，下一步方向=改 verify 对 L4 经验常数的判据（或给 rework 注入"剥结构"指令），而非再加 rework 机会。**（事件 issues/suggestions 字段为空=驳回理由未落盘，属记录缺口不影响本结论：结论基于 corrected_claim 变化 + 终态。）
- **2026-11-25 19:15 4 臂机械指纹预注册表（明早读法, 确定性判读不靠 LLM 自评）**：
  | 臂 | 预期指纹 | 已观测(r1) | 失效判据(指纹不符=执行异常, 该臂作废重跑) |
  |---|---|---|---|
  | baseline | directed=0, multi=0 | directed=0 ✓ multi=0 ✓ | directed>0 或 multi>0 = SM 泄漏了 Fix |
  | fixA | directed>0, multi=0 | directed=4 ✓ multi=0 ✓ | directed=0 = Fix-A 未生效 |
  | fixAB | directed>0, multi>0 | directed=6 ✓ multi=25 ✓ | multi=0 = Fix-B 未生效 |
  | fixB | directed=0, multi>0 | (未跑) | directed>0 = reverse Fix-A 失败(脚本有 marker 门禁, 应 FATAL 中止) |
  效应量判读（3 rep 池化 + bootstrap CI, 口径=节点级 strict）: ①P-A: fixA 的 value_mismatch 修复率 vs baseline（Q6 域 VM 分母=0 → 只能看 directed 事件数间接信号）; ②P-B: fixB/fixAB 修复率 vs baseline, TOST margin 0.10; ③交互: fixAB-(fixA+fixB-baseline) 正/负 = superadditive/subadditive。
- **2026-11-25 19:05 r1 三臂节点级早期信号（fixAB-r1 落盘即算, 非等 4 臂全完）**：baseline 50 rework/3 fixed/0.060/multi=0；fixA 84/4/0.048/multi=0；fixAB 79/1/0.013/**multi=25**。①**Fix-B 机械指纹确认**：fixAB 独有 25 节点 rework≥2（baseline/fixA 因 pool 只含当轮新节点 count 封顶=1, multi 必 0）→ 跨轮重入确实在发生, Fix-B 按设计工作。②**但方向偏悲观分支**：第二次机会没换来修复（fixAB 修复率 0.013 < baseline 0.060, 非预测的 0.12-0.18）→ 与 13:15 机制先验的悲观支吻合（墙在 verify 标准与 L4 经验常数内容的结构性不兼容, 非尝试次数）。③**fixA 稀释效应**：Fix-A 让 directed 分支可达 → rework 节点 50→84（更多节点进改写）但 fixed 只 3→4 → 分母涨分子不涨, 修复率反降。⚠️**r1-only（n=1 rep）, 全 3 rep 池化 + bootstrap CI 才定论**; 此条仅供明早读法预置, 不作结论。
