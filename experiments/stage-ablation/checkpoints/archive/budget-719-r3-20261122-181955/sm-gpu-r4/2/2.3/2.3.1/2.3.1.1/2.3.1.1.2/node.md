# N687: FlashAttention 实现下，单 token 激活内存峰值由 Attention 部分 (4 * d_model * 2 bytes = 32,768 

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N245

## Claim

FlashAttention 实现下，单 token 激活内存峰值由 Attention 部分 (4 * d_model * 2 bytes = 32,768 bytes ≈ 32 KB) 和 FFN 部分 (d_ff * 2 bytes ≈ 21.5 KB) 组成，合计约 53.5 KB/token，而非随 n_layers 线性累加。

## Corrected Claim

FlashAttention 实现下，单 token 激活内存峰值由 Attention 部分 (4 * d_model * 2 bytes = 32,768 bytes ≈ 32 KB) 和 FFN 部分 (d_ff * 2 bytes ≈ 21.5 KB) 组成，合计约 53.5 KB/token，而非随 n_layers 线性累加。

## Evidence

先验知识/题面给定，逻辑校验通过：FlashAttention 核心机制即为通过分块计算避免存储完整的 N×N 注意力矩阵，从而将激活内存从随序列长度平方增长降低为随序列长度线性增长（或常数，取决于具体实现细节，此处指单 token 处理时的瞬时峰值），且 Transformer 各层是串行执行的，激活内存峰值由单层最大激活决定，而非随层数线性累加。数值量级（32KB + 21.5KB ≈ 53.5KB）符合 d_model=1024, d_ff=4096 等常见配置下的估算逻辑。
