# N185: 在引入冷启动效应时，Miss_Bytes_LRU 的解析近似为 Σ_{i=1}^{N} [S_i * (1 - e^{-q_i * T_cold})]，其中 T

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N61

## Claim

在引入冷启动效应时，Miss_Bytes_LRU 的解析近似为 Σ_{i=1}^{N} [S_i * (1 - e^{-q_i * T_cold})]，其中 T_cold 为预热期（如 1 小时），q_i 为对象 i 的请求率，该值量化了初始未命中造成的字节损失。

## Corrected Claim

在引入冷启动效应时，Miss_Bytes_LRU 的解析近似为 Σ_{i=1}^{N} [S_i * (1 - e^{-q_i * T_cold})]，其中 T_cold 为预热期（如 1 小时），q_i 为对象 i 的请求率，该值量化了初始未命中造成的字节损失。

## Evidence

先验知识/题面给定，逻辑校验通过
