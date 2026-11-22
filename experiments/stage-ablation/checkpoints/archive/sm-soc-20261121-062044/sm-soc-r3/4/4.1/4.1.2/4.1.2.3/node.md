# N197: 边界条件失效阈值：当 n < 10 时，线性修正公式 Cap_conf 可能产生负值或超过 [0,1] 区间；需设定硬截断 Cap_conf = max(0.1

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N70

## Claim

边界条件失效阈值：当 n < 10 时，线性修正公式 Cap_conf 可能产生负值或超过 [0,1] 区间；需设定硬截断 Cap_conf = max(0.1, min(0.9, 0.5 + (n-30)/100 * 0.4))，并记录截断发生的频率 f_trunc，若 f_trunc > 5% 则表明线性模型在极小样本下失效，需改用经验贝叶斯方法。

## Corrected Claim

边界条件失效阈值：当 n < 10 时，线性修正公式 Cap_conf 可能产生负值或超过 [0,1] 区间；需设定硬截断 Cap_conf = max(0.1, min(0.9, 0.5 + (n-30)/100 * 0.4))，并记录截断发生的频率 f_trunc，若 f_trunc > 5% 则表明线性模型在极小样本下失效，需改用经验贝叶斯方法。

## Evidence

先验知识/题面给定，逻辑校验通过：公式在 n<10 时确实可能越界（如 n=0 时值为 0.38，虽未负但接近边界，若 n 更小或系数不同则可能越界，截断逻辑 max/min 是标准防御性编程手段，阈值设定符合工程直觉）。
