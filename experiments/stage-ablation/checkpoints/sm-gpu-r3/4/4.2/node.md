# N21: 推理延迟由 Prefill 阶段（计算密集型，受 FLOPS 限制）和 Decode 阶段（访存密集型，受显存带宽限制）决定；Decode 单 token 生成

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N4, N5, N6

## Claim

推理延迟由 Prefill 阶段（计算密集型，受 FLOPS 限制）和 Decode 阶段（访存密集型，受显存带宽限制）决定；Decode 单 token 生成时间 T_decode ≈ (Weight_Size + KV_Cache_Size) / Memory_Bandwidth，其中 Weight_Size 随量化精度变化，KV_Cache_Size 随上下文长度线性增长。

## Corrected Claim

推理延迟由 Prefill 阶段（计算密集型，受 FLOPS 限制）和 Decode 阶段（访存密集型，受显存带宽限制）决定；Decode 单 token 生成时间 T_decode ≈ (Weight_Size + KV_Cache_Size) / Memory_Bandwidth，其中 Weight_Size 随量化精度变化，KV_Cache_Size 随上下文长度线性增长。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别覆盖了 Prefill 计算量、Decode 访存量、硬件吞吐推导三个不同维度，逻辑链条完整且互不重叠。数值计算（如 2*27e9*32768, 54GB 权重, 32KB KV 增量）与父节点定义的公式一致，未发现矛盾或冗余。）

## Search Query

LLM inference latency prefill decode memory bandwidth bound formula
