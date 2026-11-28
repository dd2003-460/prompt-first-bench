# 任务卡 J3a：层级因素树 + 三性质按层级检查

# origin: ai
# 派发: 2026-11-26 · Lead 规划 · sub 纯执行
# 上游: decomposition.md J3 行（D 11-25 修正方向）+ J3b 已完成（j3b_generalization.py, commit 8ad7dea37）

## 目标
把 gold 树的"顶层 4 因素 = 3 性能 + 1 成本"结构形式化成**层级因素树**，并对每一层做三性质检查：
**正交**（同层因素不重叠）/ **最小**（去掉任一层就不能压缩下层）/ **完备**（层合起来覆盖全部贡献因子）。
这是开放论证：证不出来的性质标 `[开放]` + 说明缺什么，不硬证、不编。

## 只读这些输入文件（不读其他，不联网）
1. `bench/rubric-v3/ablation/gold-tree.md` — gold 树结构（层级+因素+SHARE/BOUND 标注）
2. `bench/rubric-v3/tasks/T0-local-27b/reference/calc.py` — c_pass 公式（顶层估计器，看它实际消费哪些叶子）
3. `modules/G-think-mechanism/think-trigger/exp-results/j3b_generalization.py` — J3b 结果（作用域边界 4 判据，你的"作用域"节要引用它）
4. `modules/G-think-mechanism/think-trigger/decomposition.md` — J3 行的"共同方向"段（你的论证方向锚）

## 产出
`modules/G-think-mechanism/think-trigger/exp-results/j3a-hierarchy.md`，结构：
- §1 层级因素树（顶层 4 因素 → 各层叶子，用 gold-tree.md 的实际结构，不发明新因素）
- §2 正交检查（逐层：同层两因素的 SHARE 乘积/交集是否为空；gold 树的 SHARE 标注就是判据）
- §3 最小检查（逐层：删掉该层后下层是否失去压缩——用 calc.py 的公式结构论证，如删掉带宽层 t_decode 项失去解释）
- §4 完备检查（逐层：叶子并集是否覆盖 c_pass 公式的全部输入参数；列公式参数清单逐一映射）
- §5 作用域（引用 J3b 的 4 判据：候选集依赖 / tf_peak 作用域 / 价格口径 / 芯片命名）

## 硬约束
- **不做质量提升 claim**（D 方向锚：c_pass=顶层估计器有作用域，不声称它比异族同意更好）
- 证不出 = 标 `[开放]` + 缺什么，不硬凑
- **每节写完立即 commit**（每节 <40 行，增量落盘，防截断丢工作）
- 最终汇报 ≤15 行：文件路径 + 三性质各几个层通过/开放 + commit 链

## 验收（Lead 对照核）
- [ ] 文件存在，5 节齐全，每节 <40 行
- [ ] 三性质检查覆盖 gold 树每一层（层数与 gold-tree.md 一致）
- [ ] 无质量提升 claim（grep "更好/优于/提升" 类措辞，出现即 fail）
- [ ] 开放项有 [开放] 标记 + 缺口说明
- [ ] commit 链 ≥5（每节一个）
