# N13: 多卡方案中，张量并行（Tensor Parallelism）的通信开销约为每层2 * hidden_size * dtype_size，Qwen3-27B的hi

- **status**: degraded
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N1, N2, N3

## Claim

多卡方案中，张量并行（Tensor Parallelism）的通信开销约为每层2 * hidden_size * dtype_size，Qwen3-27B的hidden_size为4096，BF16下每层通信量为16 KB，48层总通信量为768 KB，需除以互联带宽得到延迟

## Corrected Claim

多卡方案中，张量并行（Tensor Parallelism）的通信开销约为每层2 * hidden_size * dtype_size，Qwen3-27B的hidden_size为4096，BF16下每层通信量为8 KB，48层总通信量为384 KB，需除以互联带宽得到延迟

## Evidence

[质询]数值量级错误：BF16下每层通信量计算错误，4096 * 2 bytes = 8 KB，而非16 KB；且张量并行通信量通常涉及激活值（batch_size * seq_len * hidden_size）而非仅hidden_size，此处简化过度导致量级偏差。 | 逻辑校验发现数值计算错误：4096 * 2 = 8192 bytes = 8 KB，而非16 KB；48层总通信量应为384 KB而非768 KB。

## Search Query

Tensor Parallelism communication overhead formula
