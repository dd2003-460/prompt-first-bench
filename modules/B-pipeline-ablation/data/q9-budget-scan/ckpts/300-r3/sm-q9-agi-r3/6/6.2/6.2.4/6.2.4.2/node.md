# N306: 当草稿 token 数从 4 增加到 8 时，C_verify 线性增长至 100ms，但 AR 仅从 40% 提升至 45%（边际收益递减），导致 Speed

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N109

## Claim

当草稿 token 数从 4 增加到 8 时，C_verify 线性增长至 100ms，但 AR 仅从 40% 提升至 45%（边际收益递减），导致 Speedup 曲线在 batch_size=4 处达到峰值，超过此点后验证开销抵消生成加速，最优工作点锁定在 batch_size=4。

## Corrected Claim

当草稿 token 数增加时，验证开销线性增长，而接受率的边际收益递减，导致 Speedup 曲线存在一个最优工作点（如 batch_size=4），超过此点后验证开销将抵消生成加速。

## Evidence

[质询]该陈述包含具体的经验数值（C_verify=100ms, AR 40%->45%, 峰值在 batch_size=4），这些并非第一性原理可推导的数学或物理常数，而是依赖于特定硬件、模型规模及负载分布的经验观测值。作为 knowledge 节点，虽然逻辑框架自洽，但缺乏通用性，具体数值可能因环境不同而显著变化，存在将特定实验结果泛化为普遍规律的风险。 | 先验知识/题面给定，逻辑校验通过：验证开销随草稿长度线性增加，接受率边际递减，导致加速比存在峰值，符合推测解码（Speculative Decoding）的基本经济学逻辑；但具体数值为经验事实，非普适真理。
