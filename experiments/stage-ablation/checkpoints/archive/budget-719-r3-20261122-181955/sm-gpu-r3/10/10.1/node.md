# N123: 2x RTX 4090 通过 PCIe 4.0 x16 互联时的实际带宽为 64 GB/s (双向)，而 NVLink 4.0 带宽为 900 GB/s；在 T

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N37

## Claim

2x RTX 4090 通过 PCIe 4.0 x16 互联时的实际带宽为 64 GB/s (双向)，而 NVLink 4.0 带宽为 900 GB/s；在 TP=2 推理中，All-Reduce 通信量与模型层数成正比，通信开销占比 = (通信时间 / 总推理时间)，需具体计算在 32K 上下文下，每层 All-Reduce 的数据量（如 2 * n_kv_heads * head_dim * seq_len * dtype_size）及对应的 PCIe 传输时间。

## Corrected Claim

2x RTX 4090 通过 PCIe 4.0 x16 互联时的实际带宽为 64 GB/s (双向)，而 NVLink 4.0 带宽为 900 GB/s；在 TP=2 推理中，All-Reduce 通信量与模型层数成正比，通信开销占比 = (通信时间 / 总推理时间)，需具体计算在 32K 上下文下，每层 All-Reduce 的数据量（如 2 * n_kv_heads * head_dim * seq_len * dtype_size）及对应的 PCIe 传输时间。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点正交且完备地覆盖了父节点要求的三个核心维度：1. All-Reduce 数据量计算（针对 Prefill 场景）；2. PCIe 传输时间计算及瓶颈分析；3. 实际性能影响（Prefill 与 Decode 阶段的对比）。虽然子节点1和2紧密关联（数据量决定时间），但它们分别对应‘计算通信量’和‘计算传输延迟’两个不同的物理步骤，且子节点4补充了 Decode 阶段的对比，确保了逻辑的完整性。没有发现明显的重复或矛盾。）
