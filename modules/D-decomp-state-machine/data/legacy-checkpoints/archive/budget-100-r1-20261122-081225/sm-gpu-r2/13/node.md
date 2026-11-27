# N154: 性价比量化公式定义为 Cost_per_Token = (Hardware_Capex / Expected_Lifetime_Tokens) + (Elect

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

性价比量化公式定义为 Cost_per_Token = (Hardware_Capex / Expected_Lifetime_Tokens) + (Electricity_Cost_per_KWh * Power_Draw_W / 1000 * Hours_Per_Day * 365 / Expected_Lifetime_Tokens)，其中 Expected_Lifetime_Tokens 需根据目标吞吐量 (Tokens/sec) 和预期运行年限 (如 3 年) 推算，该公式将一次性硬件成本摊销至每个 Token，以消除时间维度差异。

## Corrected Claim

性价比量化公式定义为 Cost_per_Token = (Hardware_Capex / Expected_Lifetime_Tokens) + (Electricity_Cost_per_KWh * Power_Draw_W / 1000 * Hours_Per_Day * 365 / Expected_Lifetime_Tokens)，其中 Expected_Lifetime_Tokens 需根据目标吞吐量 (Tokens/sec) 和预期运行年限 (如 3 年) 推算，该公式将一次性硬件成本摊销至每个 Token，以消除时间维度差异。

## Evidence

检索失败: no sources from any channel (all 5 failed)
