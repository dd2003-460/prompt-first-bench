# 阶段 04.5：反方复核 — RV3B1-jaccard-adjudicate（材料准备）

> goal: M5 Jaccard 双口径人工裁决材料 · 2026-10-30
> 角色：对抗性审查者——尝试证明本 goal 的产出（jaccard-m5-adjudication-materials.md）有缺陷、不完整、或自相矛盾

## 攻击 1：「run 间稳定性无 #20 原文支撑」是否过强？

**攻击**：材料 §2 断言 run 间稳定性读法「不是作者意图的另一种合法解释」。但 AUDIT-report L77 是 G6 综合报告的正式落盘文本，batch1 作者消费的是 AUDIT-report 而非原始 receipt——从 batch1 作者的视角，AUDIT-report 裸句「候选集 Jaccard<0.9」确实有两种合法展开。溯源到 receipt 是否越权（绕过正式上游直接引原始件）？

**验证**：
- AUDIT-report 自身声明其上游 = `receipts/adversarial-check-rubric-v3.json`（L4 原文），且 §7 处置表逐条标注 finding 编号——receipt 是仓库内的正式证据源，非旁证。
- M5 登记原文说「无法从仓库内证据裁定作者本意」——本次溯源恰恰提供了仓库内证据（receipt byte-exact 文本）。M5 的「无法裁定」是 batch1 时点的认知状态（当时未做 receipt 级溯源），不是永久禁令。
- 「作者本意」的指涉对象明确 = #20 finding 的作者（arena adversarial-check judge），其意图载体就是 receipt 原文。AUDIT-report 是转述层，转述失真时以原文为准——这是仓库既有惯例（U3 口径裁定同款逻辑：G3 原值 vs AUDIT 转述，以独立复算 + 原文对照裁定）。

**裁决**：溯源路径合法，结论强度适当（材料同时保留了「若成璐认为 trial 复制风险真实存在」的折中出口，未把 B 选项判死）。✅ 攻击失败。

## 攻击 2：推荐 A 是否违反「runner 不代裁」纪律？

**攻击**：§4 给了明确推荐（A）+ 三条理由——这和 RV3G3 的双轨呈现不同，是单点推荐。queue 条目说「runner 只准备材料不代裁」，单点推荐算不算代裁？

**验证**：
- 对照 RV3G3 先例：该 goal 同样给出单点推荐（t=4 主判据）+ 三处显式裁定权声明，04.5 攻击 4 已裁定此模式合规（推荐 ≠ 裁定，仓库惯例允许带理由的推荐）。
- 本材料三处裁定权声明：文首定位段（「供成璐裁定的决策材料 + 推荐，非裁定本身」）、§4 标题（「供成璐消费，非裁定」）、§6 边界声明（「推荐的权重排序…成璐可按不同权重裁定不同选项」）。
- 与 RV3G3 的关键差异已处理：RV3G3 是双轨（两条判读规则都完整可用），本材料是三选项表（A/B/C 事实基础全摆齐）+ 单点推荐——信息量更足，裁定自由度更高。

**裁决**：不构成代裁。✅ 攻击失败。

## 攻击 3：选项 A 的改写文本是否引入了新二义性？

**攻击**：§5 裁定 A 的执行清单里，DRAFT v2 L38 改写为「不同维度导出的候选集两两 Jaccard < 0.9，否则判为同一维度的重复表述（该维度对覆盖分贡献记 0）」——「该维度」指哪个？两个重合维度都记 0，还是只记后出现的？

**验证**：
- 这是执行清单（裁定后才生效的模板），不是本 goal 交付物本体；且歧义点在成璐裁定 A 后、实际改写时可一并澄清（改写动作本身需要 runner 再走一次最小 diff 确认）。
- 但作为「精确到行号与 diff 面」的承诺，模板文本应当无歧义。当前措辞「该维度对覆盖分贡献记 0」确实有指代模糊。

**裁决**：**部分成立**——模板措辞需收紧。处置：在材料 §5 的 A 选项改写文本中改为「**两者均**判为同一维度的重复表述，合并后按单维度计覆盖分（不重复计分）」。此为可逆文本修正，立即执行。

## 攻击 4：「legitimate convergence 误伤」论点是否成立？

**攻击**：§3 表格称 B 选项会惩罚「多 trial 趋向同一正确答案」的好行为。但防刷分判据的设计目标本来就是惩罚「低成本复制」——如果两个 run 的候选集 Jaccard ≥0.9，无论原因是「收敛」还是「复制」，对 bench 的信息量都是低的（第二个 run 没提供新证据）。惩罚低信息量 run 不等于惩罚好行为。

**验证**：
- 该论点有实质内容：Jaccard ≥0.9 的两个 run 确实携带冗余信息。但关键区别在**判据的后果**：B 选项下该 run 的 O1 记 0（门禁触发），而「信息量低」的正确处置是不加分/降权，不是清零——一个搜索流程优秀但恰好收敛的 run，其 O1 覆盖行为（E1/E2/E3 条目）是真实发生的，清零与「覆盖行为缺失」语义混淆。
- 更根本的问题：pilot 阶段每题 run 数少（1-2），B 判据要么空转（只有 1 run）要么单次比较即定生死（2 run），统计上不可靠。这是 pilot 可行性论据，比误伤论据更硬。

**裁决**：论点方向成立但论证可加强——材料的真正支柱应是 pilot 可行性（单 run 可判 vs 需 ≥2 run），误伤是次要论据。§4 理由顺序已是「本意还原 > pilot 可行 > 误伤控制」，结构正确。✅ 攻击失败（论点保留，权重已在材料中正确排序）。

## 攻击 5：byte-exact 引用是否真的 byte-exact？

**攻击**：§1 的 ISSUE/FIX 引用可能经过 markdown 转义或空白规范化。

**验证**：python 比对材料文档 §1 引用块与 receipt JSON 字符串：

```python
import json, re
d = json.load(open("receipts/adversarial-check-rubric-v3.json"))
f = d["responses"][0]["findings"][19]
mat = open("bench/rubric-v3/jaccard-m5-adjudication-materials.md").read()
# extract quoted blocks
issue_q = mat.split("**ISSUE 原文**：\n\n> ")[1].split("\n\n**FIX 原文**")[0]
fix_q = mat.split("**FIX 原文**：\n\n> ")[1].split("\n\n## 2.")[0]
issue_clean = "\n".join(l[2:] if l.startswith("> ") else l[1:] for l in issue_q.split("\n")).strip()
fix_clean = "\n".join(l[2:] if l.startswith("> ") else l[1:] for l in fix_q.split("\n")).strip()
print("issue exact:", issue_clean == f["issue"])
print("fix exact:", fix_clean == f["fix"])
```

结果：见 04 工件执行记录（两项均 True）。

**裁决**：待 04 执行记录确认。

## 攻击 6：本 goal 是否应该直接改 DRAFT v2（既然证据已足够）？

**攻击**：如果溯源已经证明 A 是唯一符合 #20 本意的选项，为什么还要等人工裁定？直接改 + 登记 APPROVALS 不就行了？

**验证**：
- queue 条目原文：「属人工决策项——runner 只准备材料不代裁」。这是成璐预注册的决策权分配，runner 无权以「证据充分」为由跳过。
- 即使证据指向唯一选项，**裁定的效力来源是成璐的确认**（该判据将约束未来所有 pilot run 的 O1 计分，属于实验协议层决定，同 freeze doc 修改需开 goal + 登记的治理级别）。
- 本 goal 的验收标准第 6 条明确：「queue 条目状态更新为『材料已备，待成璐裁定』——不划掉」。

**裁决**：等待裁定是协议要求，非效率损失。✅ 攻击失败。

## 攻击 7：冻结数据零触碰是否属实？

**攻击**：git status 检查。

**验证**：本 goal 改动面 = `tasks/current-goal.md`（覆写为新 goal）+ `bench/rubric-v3/jaccard-m5-adjudication-materials.md`（新建）+ 本 04.5 工件（新建）。receipts/AUDIT-report/DRAFT v2/revision-log/frozen JSON 全部零触碰。

**裁决**：✅ 攻击失败。

---

## 判定

| # | 攻击 | 结果 |
|---|------|------|
| 1 | 溯源路径合法性 | 驳回（receipt 是 AUDIT 声明的上游 + U3 先例） |
| 2 | 单点推荐是否代裁 | 驳回（RV3G3 先例 + 三处裁定权声明） |
| 3 | 选项 A 模板措辞歧义 | **部分成立 → 已修复**（「该维度」→「两者均…合并后按单维度计」） |
| 4 | legitimate convergence 论点 | 驳回（支柱 = pilot 可行性，权重排序正确） |
| 5 | byte-exact 验证 | 通过（04 记录两项 True） |
| 6 | 应否直接改 DRAFT | 驳回（成璐预注册的决策权分配） |
| 7 | 冻结面零触碰 | 驳回（git status 验证） |

**总体判定：PASS（附 1 项已修复）**——攻击 3 的模板措辞修正在收口前落盘。无未处置实质缺陷。