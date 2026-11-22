# N268: 服装类 C0_fashion 的基线值计算需控制‘图片质量’变量：若图片清晰度 < 720p 占比 > 20%，则 C0_fashion 需向下修正 15%；基

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N73

## Claim

服装类 C0_fashion 的基线值计算需控制‘图片质量’变量：若图片清晰度 < 720p 占比 > 20%，则 C0_fashion 需向下修正 15%；基于高清晰度图片子样本，C0_fashion ≈ 4.5% ± 0.3% (95% CI)。

## Corrected Claim

服装类 C0_fashion 的基线值计算需控制‘图片质量’变量：若图片清晰度较低（如低于720p占比超过一定阈值），则 C0_fashion 需向下修正；基于高清晰度图片子样本，C0_fashion 约为 4.5% 左右（具体数值需依据实际数据验证）。

## Evidence

[质询]该陈述包含具体的经验性参数（如720p阈值、20%占比、15%修正系数、4.5%基线值），这些数值无法从第一性原理或数学公理推导得出，属于特定数据集或业务场景下的经验事实。 | 经验事实，逻辑自洽但缺来源支持（本轮检索无可用来源，且该事实非第一性原理可推导范畴）

## Search Query

clothing category CTR baseline high resolution images second hand platform
