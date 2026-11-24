# N524: 混合策略带宽成本的加权公式 C_bw_mix = P_core * C_bw_self + P_tail * C_bw_public，其中C_bw_self和C

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N173

## Claim

混合策略带宽成本的加权公式 C_bw_mix = P_core * C_bw_self + P_tail * C_bw_public，其中C_bw_self和C_bw_public需分别计算自建和公有云的每千请求带宽成本，不能简单用平均值代替。

## Corrected Claim

混合策略带宽成本的加权公式 C_bw_mix = P_core * C_bw_self + P_tail * C_bw_public，其中C_bw_self和C_bw_public需分别计算自建和公有云的每千请求带宽成本，不能简单用平均值代替。

## Evidence

先验知识/题面给定，逻辑校验通过：加权平均公式符合概率期望定义，且强调需分别计算不同场景成本以避免辛普森悖论或口径混淆，逻辑自洽。
