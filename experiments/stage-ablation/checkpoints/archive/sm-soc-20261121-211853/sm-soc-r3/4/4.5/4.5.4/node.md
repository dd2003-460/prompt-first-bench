# N49: 卖家退出平台的临界条件：当预期收益 π < C_exit 时，卖家选择退出，其中 π = P_sell * (Price - C_var) - C_time *

- **status**: pending
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N18, N19, N20

## Claim

卖家退出平台的临界条件：当预期收益 π < C_exit 时，卖家选择退出，其中 π = P_sell * (Price - C_var) - C_time * T，C_exit 为退出成本（如账号迁移成本、信任重建成本），P_sell 为成交概率，C_time 为时间成本。需量化 C_exit 的中位数，估计为 50-100 元（基于用户调研数据）。

## Corrected Claim

卖家退出平台的临界条件：当预期收益 π < C_exit 时，卖家选择退出，其中 π = P_sell * (Price - C_var) - C_time * T，C_exit 为退出成本（如账号迁移成本、信任重建成本），P_sell 为成交概率，C_time 为时间成本。C_exit 的具体数值需基于用户调研数据量化。

## Evidence

父节点级核验失败（LLM 错误）：Invalid \escape: line 5 column 47 (char 113)

## Search Query

seller exit threshold platform switching cost second-hand market survey
