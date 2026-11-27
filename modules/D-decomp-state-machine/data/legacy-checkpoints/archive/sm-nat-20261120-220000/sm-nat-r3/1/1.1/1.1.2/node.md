# N20: 在 α=1.1 且 S_min=1KB 的假设下，若 S_max 未给出，S_total 无法计算有限值；若假设 S_max=1GB (典型大对象)，则 S_t

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N5

## Claim

在 α=1.1 且 S_min=1KB 的假设下，若 S_max 未给出，S_total 无法计算有限值；若假设 S_max=1GB (典型大对象)，则 S_total ≈ 100,000 * 1KB * (1 - (1000)^{-0.1})/0.1 ≈ 100,000 * 1KB * 8.5 ≈ 850 MB，远小于 128GB 缓存，验证了 N6 中 C >> S_total 的结论。

## Corrected Claim

在 α=1.1 且 S_min=1KB 的假设下，若 S_max 未给出，S_total 无法计算有限值；若假设 S_max=1GB (典型大对象)，则 S_total ≈ 100,000 * 1KB * (1 - (1000)^{-0.1})/0.1 ≈ 100,000 * 1KB * 8.5 ≈ 850 MB，远小于 128GB 缓存，验证了 N6 中 C >> S_total 的结论。

## Evidence

父节点级核验未通过：非正交, 有冗余（子节点1和子节点3存在严重冗余和逻辑重叠。两者都在重复进行相同的数值计算（验证 S_total 是否为 499MB 而非 850MB），并得出相同的结论（原计算有误）。子节点1侧重于'假设合理性'，但核心内容却是数值纠错；子节点3直接就是'数值纠错'。这两个节点本质上是同一件事的两个表述，缺乏正交性。）
