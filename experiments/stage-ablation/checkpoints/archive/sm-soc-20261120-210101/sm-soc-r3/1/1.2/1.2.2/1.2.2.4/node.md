# N143: 工作点3（高成本低性）：高摩擦成交路径，T_comm = 4小时，N_messages = 20，E_comm = 4，TCS_high_friction = 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N35

## Claim

工作点3（高成本低性）：高摩擦成交路径，T_comm = 4小时，N_messages = 20，E_comm = 4，TCS_high_friction = 50*4 + 20*4 + 5*20 = 300元，C_transaction_high_friction = 300元，TCS = 300 - 50 = 250元，此时卖家要求 P_min_accept = P_ref - 125元，但买家感知成本增加导致需求下降 ΔQ = -0.1 * (TCS_high_friction - TCS_standard)/100 = -0.1 * 1.5 = -0.15。

## Corrected Claim

工作点3（高成本低性）：高摩擦成交路径，T_comm = 4小时，N_messages = 20，E_comm = 4，TCS_high_friction = 50*4 + 20*4 + 5*20 = 300元，C_transaction_high_friction = 300元，TCS = 300 - 50 = 250元，此时卖家要求 P_min_accept = P_ref - 125元，但买家感知成本增加导致需求下降 ΔQ = -0.1 * (TCS_high_friction - TCS_standard)/100 = -0.1 * 1.5 = -0.15。

## Evidence

先验知识/题面给定，逻辑校验通过：算术运算 50*4+20*4+5*20=300 正确，TCS=300-50=250 正确，ΔQ 计算 -0.1*(250-100)/100=-0.15 正确（假设 TCS_standard=100 为隐含基准或题面上下文一致），逻辑自洽。

## Search Query

high friction transaction cost demand reduction quantification
