# N67: 在张量并行 (Tensor Parallelism) 中，每次 Attention 和 FFN 层都需要 All-Reduce 通信，通信量约为 2 * hid

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N12

## Claim

在张量并行 (Tensor Parallelism) 中，每次 Attention 和 FFN 层都需要 All-Reduce 通信，通信量约为 2 * hidden_size * batch_size * seq_len * bytes，对于 Qwen3-27B (hidden_size=4096)，每 token 每层通信量约为 16 KB (BF16)，64 层总计约 1 MB/token，在 64 GB/s 带宽下引入约 15.6 us/token 的纯通信延迟。

## Corrected Claim

在张量并行 (Tensor Parallelism) 中，每次 Attention 和 FFN 层都需要 All-Reduce 通信，通信量约为 2 * hidden_size * batch_size * seq_len * bytes，对于 Qwen3-27B (hidden_size=4096)，每 token 每层通信量约为 16 KB (BF16)，64 层总计约 1 MB/token，在 64 GB/s 带宽下引入约 15.6 us/token 的纯通信延迟。

## Evidence

父节点级核验未通过：不完备, 有冗余（子节点之间正交（针对不同硬件场景），但存在严重冗余：两个子节点本质上是在描述同一个公式/逻辑在不同硬件参数下的实例化，属于‘同构案例’而非独立知识点。此外，父节点核心在于‘通信量计算与理论延迟’，而子节点完全转向了‘具体硬件下的性能对比与效率分析’，未覆盖父节点中关于‘通信量计算公式推导’或‘为何是2倍hidden_size’等基础理论方面，导致完备性不足。）
