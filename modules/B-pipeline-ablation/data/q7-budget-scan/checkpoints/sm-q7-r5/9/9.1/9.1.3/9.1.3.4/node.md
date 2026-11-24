# N667: 共享基础设施总功耗 P_Shared_Infra_Final：P_Shared_Infra = P_Controller (40W) + P_Backplane

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N276

## Claim

共享基础设施总功耗 P_Shared_Infra_Final：P_Shared_Infra = P_Controller (40W) + P_Backplane_Loss (30W) + P_Fan (10W, 取中值) = 80W。此值略低于 N276 原估的 85-100W 下限，主要因风扇功耗修正。在 TCO 计算中，此项应固定为 80W 用于后续电力成本折算。

## Corrected Claim

共享基础设施总功耗 P_Shared_Infra_Final：P_Shared_Infra = P_Controller (40W) + P_Backplane_Loss (30W) + P_Fan (10W, 取中值) = 80W。此值略低于 N276 原估的 85-100W 下限，主要因风扇功耗修正。在 TCO 计算中，此项应固定为 80W 用于后续电力成本折算。

## Evidence

先验知识/题面给定，逻辑校验通过：各项功耗数值（40W+30W+10W=80W）算术正确，量级符合小型服务器/交换机共享基础设施的工程常识，且内部逻辑自洽（解释了与旧估值差异的原因）。
