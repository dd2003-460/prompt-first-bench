# N13: 多卡方案中，张量并行（Tensor Parallelism）的通信开销约为每层2 * hidden_size * dtype_size，Qwen3-27B的hi

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N1, N2, N3

## Claim

多卡方案中，张量并行（Tensor Parallelism）的通信开销约为每层2 * hidden_size * dtype_size，Qwen3-27B的hidden_size为4096，BF16下每层通信量为16 KB，48层总通信量为768 KB，需除以互联带宽得到延迟

## Corrected Claim

多卡方案中，张量并行（Tensor Parallelism）的通信开销约为每层2 * hidden_size * dtype_size，Qwen3-27B的hidden_size为4096，BF16下每层通信量为8 KB，48层总通信量为384 KB，需除以互联带宽得到延迟

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别覆盖了带宽参数基础、通信延迟计算公式、以及实际吞吐率模型，三者维度不同（硬件参数、算法公式、系统性能模型），无重叠或矛盾，且共同构成了从理论通信量到实际延迟再到吞吐影响的完整逻辑链，覆盖了父节点中关于通信开销、具体数值代入及延迟/性能影响的关键方面。）

## Search Query

Tensor Parallelism communication overhead formula
