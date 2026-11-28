# N280: 对背景文献部分应用 3x 压缩后，Prompt 总长度减少 60%，使得 KV Cache 显存占用降低，从而允许 Batch Size 从 4 提升至 8，吞

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N96

## Claim

对背景文献部分应用 3x 压缩后，Prompt 总长度减少 60%，使得 KV Cache 显存占用降低，从而允许 Batch Size 从 4 提升至 8，吞吐量提升约 1.5x，抵消了压缩带来的潜在精度损失。

## Corrected Claim

对背景文献部分应用 3x 压缩后，Prompt 总长度显著减少，KV Cache 显存占用降低，允许 Batch Size 从 4 提升至 8，预期吞吐量提升，以权衡压缩带来的潜在精度损失。

## Evidence

[质询]吞吐量提升1.5x与Batch Size翻倍（2x）及KV Cache显存释放的逻辑关联过于简化，忽略了计算密集度变化及硬件瓶颈，且'抵消精度损失'属于主观价值判断而非客观事实。 | 先验知识/题面给定，逻辑校验通过，但具体数值（1.5x）缺乏通用性保证，属经验性推断。
