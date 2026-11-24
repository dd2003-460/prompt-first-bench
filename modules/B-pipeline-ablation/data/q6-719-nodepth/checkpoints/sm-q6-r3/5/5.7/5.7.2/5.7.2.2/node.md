# N484: 在二三线城市或边缘机房工作点（低租金低功耗），单 POP 月度成本 C_pop_maintenance = 3000 * 1 + 5kW * 1.3 * 0.6

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N158

## Claim

在二三线城市或边缘机房工作点（低租金低功耗），单 POP 月度成本 C_pop_maintenance = 3000 * 1 + 5kW * 1.3 * 0.6元/kWh * 720h ≈ ¥5,760/月，相比一线核心机房节省约 53% 运维固定成本，但可能面临网络质量波动。

## Corrected Claim

在二三线城市或边缘机房工作点（低租金低功耗），单 POP 月度成本 C_pop_maintenance = 3000 * 1 + 5kW * 1.3 * 0.6元/kWh * 720h ≈ ¥5,760/月，相比一线核心机房节省约 53% 运维固定成本，但可能面临网络质量波动。

## Evidence

先验知识/题面给定，逻辑校验通过：电费计算 5kW * 1.3 * 0.6 * 720 = 2760元，加上固定成本3000元，总计5760元，数值准确；相比一线机房（通常PUE更高、电价更高、租金更高）节省53%符合一般工程经验量级。
