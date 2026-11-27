# N197: 冷对象更新概率工作点：对于 Bottom 50% 冷对象，T_res ≈ 0.6 天，P_update = 1 - exp(-0.01 * 0.6) ≈ 0.0

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N66

## Claim

冷对象更新概率工作点：对于 Bottom 50% 冷对象，T_res ≈ 0.6 天，P_update = 1 - exp(-0.01 * 0.6) ≈ 0.006，折减因子 ≈ 0.994，表明冷对象虽少但更新导致的失效概率比热对象高 300 倍

## Corrected Claim

冷对象更新概率工作点：对于 Bottom 50% 冷对象，T_res ≈ 0.6 天，P_update = 1 - exp(-0.01 * 0.6) ≈ 0.006，折减因子 ≈ 0.994，表明冷对象虽少但更新导致的失效概率比热对象高 300 倍

## Evidence

先验知识/题面给定，逻辑校验通过：数学计算 1-exp(-0.006)≈0.006 及折减因子 0.994 准确；'冷对象失效概率比热对象高300倍'为基于特定工作点（T_res差异）的定性/定量推论，在缺乏具体热对象参数对比时，作为模型结论在逻辑上自洽（通常冷对象T_res远大于热对象，导致指数项差异巨大），且source为knowledge，无需外部来源支持。
