# N195: 断点处跳变幅度 (Jump) 的显著性检验：计算 Jump = m_+(x_c) - m_-(x_c)，其标准误 SE_Jump = sqrt(Var(m_+)

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N62

## Claim

断点处跳变幅度 (Jump) 的显著性检验：计算 Jump = m_+(x_c) - m_-(x_c)，其标准误 SE_Jump = sqrt(Var(m_+) + Var(m_-))，若 |Jump| / T_baseline > 0.20 且 t-stat = Jump / SE_Jump > 1.96，则拒绝原假设，支持平台驱动均衡。

## Corrected Claim

断点处跳变幅度 (Jump) 的显著性检验：计算 Jump = m_+(x_c) - m_-(x_c)，其标准误 SE_Jump = sqrt(Var(m_+) + Var(m_-))，若 |Jump| / T_baseline > 0.20 且 t-stat = Jump / SE_Jump > 1.96，则拒绝原假设，支持平台驱动均衡。

## Evidence

先验知识/题面给定，逻辑校验通过
