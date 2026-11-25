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
- **2026-11-25 13:58 r2 完成 + baseline 复现间方差（新事实，影响功效解读）**：r2 DONE 91min（r1 54min），300 节点，reworks=121（angle=77），**repair_rate=3/77=0.039**（r1 3/50=0.06），status verified 192/pending 48/degraded 60（r1 218/35/47），leaks=0。**同代码两次 rep：angle rework 50→77（+54%）、repair_rate 0.06→0.039、degraded 47→60** → baseline 自身噪声不小，明早析因必须用 3-rep 池化均值（分析脚本已是此口径），且单臂 diff 的置信区间要计入 rep 间方差，实际功效低于单点估计（0.10 效应可能更偏 suggestive）。**减速原因定量**（推翻 13:45"卡住"误判）：LLM 中位耗时 r2 2.9s ≈ r1 2.8s，慢在尾部——p90 20.4s vs 9.6s、max prompt 193k vs 106k（树长到后期 verify 批变大）；r2 调用量 755 已超 r1 全程 686，不是卡住是每 rep 自然变长。**ETA 修正**：每 rep ~90min（非 54min），剩 10 reps ≈ 15h → 11-26 凌晨~清晨完成（checklist 的"凌晨~上午"窗口仍成立）。
- **2026-11-25 13:15 Fix-B 效应机制先验（43 个改写失败节点的质询理由分类）**：对 43 个 angle-rework→degraded 节点的质询驳回理由做正则分类：**A 经验常数缺普适性 37（86%）/ D 逻辑·量纲·公式真错误 3 / E 未分类 3**。决定性证据：**14 个 corrected_claim 已去数字改纯对冲（"具体取决于带宽/供应商而异"）仍被驳** → 墙不在数字本身，在 verify 标准（第一性原理普适性）与 L4 经验常数内容的结构性不兼容，改写（含对冲化）无法突破。**Fix-B（第二次机会）机制预测：救回上限 = D/E 类可修真错误 ≈ 3-6 节点 → 节点级修复率 ≈ 0.12-0.18**（baseline 0.06 之上 +0.06~0.12），恰在功效临界区（power=0.8 需 0.16）→ 明早结果大概率 suggestive 不 conclusive，TOST margin 0.10 成为关键读法：diff CI 落 [-0.1,0.1] 内 = 与 baseline 等效（Fix-B 无效，瓶颈=verify 标准而非尝试次数，下一步应改 verify 对 L4 经验常数的判据而非加 rework）；落外 = 部分有效。**正面对照（3 个修复成功节点）**：N38/N41 的改写都把经验常数剥成可推导结构关系（"70%→50% 阈值"→"当自建单位成本>公有云变动成本时"）→ 过验证；N271 为 rework 后逻辑推导成立（来源未直接覆盖仍放行）。→ **Fix-B 二次改写的有效路径 = "常数→结构关系"剥离，不是换个角度重搜**；救回上限预测维持 3-6 节点（86% A 类里只有少数能剥出结构关系）。
- **2026-11-25 13:05 统计功效核算 + TOST margin 修正（预防明早结论死区）**：①功效（节点池化 n=150/臂, p0=0.06）：power=0.8 需 p1≈0.16（救回 ~15 节点/臂）；真 diff=0.05 时 power≈0.15、diff=0.10 时 ≈0.46、diff=0.14 时 ≈0.74 → **若 Fix-B 真实效应 <0.10，明早"不显著"不能下"无效"结论，须看 TOST**；②发现 TOST margin=0.05 不可行：n=150/臂时差值 CI 宽≈0.107 > 2×0.05=0.10 → margin=0.05 下"等效"永不触发，"无效"与"功效不足"无法区分（bootstrap 校准单臂半宽 0.037，与解析 0.038 一致）。**已修**：`t-repair1-analysis.py` MIN_EFFECT 0.05→0.10（恢复 T-PR-17 先例值），dry-run 验证 gate 正常 + TOST 双向行为正确（CI⊂[-0.1,0.1]→等效；越界→不等效）。明早读法：P-B 差值 CI 落在 [-0.1,0.1] 内才可判"等效/无效"；落在外且不显著 = 功效不足，不下结论。
- **2026-11-25 12:45 判别逻辑鉴别力测试（构造数据，4 分支全过）**：①rate/bootstrap_ci/tost 单元行为正确（3/50→CI(0,0.14)；0/50 边界退化 CI=(0,0) 但双向 TOST 结论均不翻转：fixB=0 vs baseline=3 → 判不等效✓；双臂都 0 → 判等效✓）；②交互分类 4 分支（orthogonal×2/superadditive/subadditive）构造值全命中；③parse_rep_rc 对真实 executor log 解析正确（baseline-r1 rc=0）；④load_arm_runs 文件名模式与实际产物 `baseline-r1-<ts>.json` 匹配，rep_rc 门禁生效。**遗留 caveat（不修，现实风险≈0）**：load_arm_runs 注释"glob 按文件名排序取最新"不严谨（glob.glob 不保证排序），仅当同一 rep 存在两个文件（手动重跑）时才有歧义；今晚全自动链每 rep 单文件 + 无重试 + checkpoint 在子目录不被递归 → 不触发。
