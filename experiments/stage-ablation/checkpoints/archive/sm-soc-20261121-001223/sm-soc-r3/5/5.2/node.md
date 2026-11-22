# N68: 初始曝光量差异的量化：计算高溢价组 (ΔP/P > 15%) 与基准组 (ΔP/P < 5%) 的 E_initial 均值差，使用 t 检验或 Mann-Wh

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N22

## Claim

初始曝光量差异的量化：计算高溢价组 (ΔP/P > 15%) 与基准组 (ΔP/P < 5%) 的 E_initial 均值差，使用 t 检验或 Mann-Whitney U 检验；若效应量 Hedges' g > 0.5 且 p < 0.01，则支持‘高溢价获得更高曝光’的 30-50% 提升假设。

## Corrected Claim

初始曝光量差异的量化：计算高溢价组 (ΔP/P > 15%) 与基准组 (ΔP/P < 5%) 的 E_initial 均值差，使用 t 检验或 Mann-Whitney U 检验；若效应量 Hedges' g > 0.5 且 p < 0.01，则支持‘高溢价获得更高曝光’的 30-50% 提升假设。

## Evidence

父节点级核验通过：正交+完备+无冗余（三个子节点分别针对数据预处理（归一化以消除混淆变量）、统计方法修正（小样本效应量偏差）和因果推断逻辑（内生性处理）进行分解，三者维度独立（数据清洗 vs 统计计算 vs 因果识别），无重叠或矛盾。父节点中的核心步骤（定义组、计算均值差、选择检验方法、判断效应量）均被覆盖，且子节点补充了父节点隐含的关键前提（如类别差异修正、小样本修正、因果假设的局限性），因此完备且无冗余。）

## Search Query

Effect size Hedges g initial exposure difference high premium listings
