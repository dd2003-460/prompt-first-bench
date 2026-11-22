# N13: Qwen3-27B 在 INT8 下 Prefill 阶段的算力需求减半至 135 TOPS，但 Decode 阶段的带宽需求仍为 54GB/s（权重读取量不变

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1

## Claim

Qwen3-27B 在 INT8 下 Prefill 阶段的算力需求减半至 135 TOPS，但 Decode 阶段的带宽需求仍为 54GB/s（权重读取量不变，仅计算精度改变），导致 Decode 依然是带宽瓶颈

## Corrected Claim

Qwen3-27B 在 INT8 下 Prefill 阶段的算力需求减半，Decode 阶段的带宽需求因权重体积减半而降低至约 27GB/s（假设 FP16 下为 54GB/s），Decode 依然是带宽瓶颈但压力减小。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别针对Prefill阶段的算力（Compute）和Decode阶段的带宽（Memory Bandwidth）进行修正，两者关注不同的硬件瓶颈维度（计算vs内存），且各自独立推导了理论值与实际值，不存在重复或矛盾。父节点核心观点是'Prefill算力减半'和'Decode带宽不变导致瓶颈'，子节点分别对这两个关键参数进行了更精确的量化修正，覆盖了父节点的所有关键方面。）
