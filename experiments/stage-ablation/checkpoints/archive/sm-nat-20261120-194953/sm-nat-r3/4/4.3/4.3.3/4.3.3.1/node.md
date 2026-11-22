# N129: 修正后的热门对象字节命中率折损精确值：ΔH_hot = P_inval_hot * S_hot = 0.634 * 0.28 ≈ 0.1775，即 17.75 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N57

## Claim

修正后的热门对象字节命中率折损精确值：ΔH_hot = P_inval_hot * S_hot = 0.634 * 0.28 ≈ 0.1775，即 17.75 个百分点，而非 N57 原估计的 0.28 个百分点（修正自矛盾检测：N57 基于错误的 P_inval=0.01 计算）

## Corrected Claim

修正后的热门对象字节命中率折损精确值：ΔH_hot = P_inval_hot * S_hot = 0.634 * 0.28 ≈ 0.1775，即 17.75 个百分点，而非 N57 原估计的 0.28 个百分点（修正自矛盾检测：N57 基于错误的 P_inval=0.01 计算）

## Evidence

先验知识/题面给定，逻辑校验通过：0.634 * 0.28 = 0.17752，数值计算准确，量纲一致（概率*概率=概率/百分点），且明确指出了对N57错误假设（P_inval=0.01）的修正，逻辑自洽。
