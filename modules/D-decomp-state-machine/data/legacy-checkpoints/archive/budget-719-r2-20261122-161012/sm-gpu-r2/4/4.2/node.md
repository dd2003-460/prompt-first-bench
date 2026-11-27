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

父节点级核验通过：正交+完备+无冗余（子节点分别对应父节点中的Prefill计算逻辑、Decode访存数据量计算、以及最终吞吐/延迟推导，三者逻辑链条清晰且互不重叠，无矛盾。虽然子节点2和3都涉及Decode阶段，但2侧重于数据量（分子）的计算，3侧重于结合硬件带宽（分母）得出结果，属于因果递进关系而非重复。父节点提到的所有关键变量（FLOPS, MFU, Weight_Size, KV_Cache, Memory_Bandwidth, 量化/上下文影响）均被覆盖。）

## Search Query

LLM inference latency prefill decode memory bandwidth bound formula
