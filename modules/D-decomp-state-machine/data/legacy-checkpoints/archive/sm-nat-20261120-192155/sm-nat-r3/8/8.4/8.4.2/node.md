# N135: 工作点2（更新间隔对比）：对象更新间隔 T_upd = 1/U = 100 days。对比 T_res_head ≈ 0.02 秒 与 T_upd = 100 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N50

## Claim

工作点2（更新间隔对比）：对象更新间隔 T_upd = 1/U = 100 days。对比 T_res_head ≈ 0.02 秒 与 T_upd = 100 days，比值 T_res/T_upd ≈ 2.3e-9。这表明在两次更新之间，头部对象会被访问约 10^8 次，因此头部对象的命中率折扣因子为 1 - T_res/T_upd ≈ 0.999999997，可视为 1.0。

## Corrected Claim

工作点2（更新间隔对比）：对象更新间隔 T_upd = 1/U = 100 days。对比 T_res_head ≈ 0.02 秒 与 T_upd = 100 days，比值 T_res/T_upd ≈ 2.3e-9。这表明在两次更新之间，头部对象会被访问约 10^8 次，因此头部对象的命中率折扣因子为 1 - T_res/T_upd ≈ 0.999999997，可视为 1.0。

## Evidence

先验知识/题面给定，逻辑校验通过：100天转换为秒约为8.64e6秒，与0.02秒的比值约为2.3e-9，其倒数约为4.3e7（即10^8量级），命中率折扣因子1-2.3e-9在数值上极接近1.0，推导自洽。
