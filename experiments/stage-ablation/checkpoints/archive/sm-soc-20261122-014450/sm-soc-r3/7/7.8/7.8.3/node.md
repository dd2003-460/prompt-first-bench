# N382: GMV 时间窗口效应：短期 GMV 下降 (-5%) 可能随时间逆转。需计算 GMV 恢复至基线的时间 T_GMV_recover。基于需求曲线右移，若价格下降

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N122

## Claim

GMV 时间窗口效应：短期 GMV 下降 (-5%) 可能随时间逆转。需计算 GMV 恢复至基线的时间 T_GMV_recover。基于需求曲线右移，若价格下降持续 30 天，需估算累计 GMV 变化 ΔGMV_cumulative = ∫(GMV_t - GMV_base)dt，判断 30 天内是否实现盈亏平衡。

## Corrected Claim

GMV 时间窗口效应：短期 GMV 下降 (-5%) 可能随时间逆转。需计算 GMV 恢复至基线的时间 T_GMV_recover。基于需求曲线右移，若价格下降持续 30 天，需估算累计 GMV 变化 ΔGMV_cumulative = ∫(GMV_t - GMV_base)dt，判断 30 天内是否实现盈亏平衡。

## Evidence

先验知识/题面给定，逻辑校验通过：GMV恢复时间定义及累计GMV积分公式符合经济学基本逻辑，量纲与计算框架自洽。
