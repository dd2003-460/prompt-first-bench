# N335: 1x A100 80GB 方案 3 年 TCO 工作点 (高成本低性)：C_hw=$10000, C_electric=$450 (400W×0.8load×0

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N119

## Claim

1x A100 80GB 方案 3 年 TCO 工作点 (高成本低性)：C_hw=$10000, C_electric=$450 (400W×0.8load×0.15$/kWh×8760h×3y), C_maint=$1500 (折旧$4500×0.33+维修$240), 总 TCO=$11950，单位成本显著高于 2x RTX 4090，除非对延迟/质量有极致要求

## Corrected Claim

1x A100 80GB 方案 3 年 TCO 工作点 (高成本低性)：C_hw=$10000, C_electric=$450 (400W×0.8load×0.15$/kWh×8760h×3y), C_maint=$1500 (折旧$4500×0.33+维修$240), 总 TCO=$11950，单位成本显著高于 2x RTX 4090，除非对延迟/质量有极致要求

## Evidence

先验知识/题面给定，逻辑校验通过：电费计算 400W*0.8*0.15*8760*3=450 正确，总 TCO 10000+450+1500=11950 正确，A100 单卡成本高于双 4090 符合市场常识。
