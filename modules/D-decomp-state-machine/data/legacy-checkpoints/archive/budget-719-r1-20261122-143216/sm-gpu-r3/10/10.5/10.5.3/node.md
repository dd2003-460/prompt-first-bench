# N406: 在 Memory Bound 的 Decode 阶段，Compute_Time 的计算不能简单使用峰值 TFLOPS，而应使用有效带宽限制下的等效算力：Comp

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N143

## Claim

在 Memory Bound 的 Decode 阶段，Compute_Time 的计算不能简单使用峰值 TFLOPS，而应使用有效带宽限制下的等效算力：Compute_Time ≈ (Weight_Size + KV_Cache_Size) / Memory_Bandwidth，此时 MFU 参数失效，公式需修正为基于带宽的估算模型。

## Corrected Claim

在 Memory Bound 的 Decode 阶段，Compute_Time 的计算不能简单使用峰值 TFLOPS，而应使用有效带宽限制下的等效算力：Compute_Time ≈ (Weight_Size + KV_Cache_Size) / Memory_Bandwidth，此时 MFU 参数失效，公式需修正为基于带宽的估算模型。

## Evidence

先验知识/题面给定，逻辑校验通过：在Memory Bound场景下，计算时间确实由内存带宽瓶颈主导，公式符合物理直觉与工程常识。

## Search Query

LLM inference memory bound compute time estimation
