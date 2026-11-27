# N23: 推理延迟分解公式：Latency = T_prefill + T_decode；其中 T_prefill ≈ L * M * P / (2 * FLOPS * 

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N4, N5

## Claim

推理延迟分解公式：Latency = T_prefill + T_decode；其中 T_prefill ≈ L * M * P / (2 * FLOPS * MFU)，T_decode ≈ L * (M + KV_len) / (2 * FLOPS * MFU)，L=27B, M=32K, P=32K, KV_len=32K

## Corrected Claim

推理延迟分解公式：Latency = T_prefill + T_decode；其中 T_prefill ≈ L * M * P / (2 * FLOPS * MFU)，T_decode ≈ L * (M + KV_len) / (2 * FLOPS * MFU)，L=27B, M=32K, P=32K, KV_len=32K

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点逻辑清晰且正交：前两个节点分别修正 Prefill 和 Decode 阶段的理论公式错误（计算量 vs 内存带宽），后两个节点基于修正后的公式进行具体硬件（RTX 4090）下的数值量化。两者一为理论修正，一为实例计算，互不重叠且共同覆盖了父节点公式分解、修正及实例化的关键方面，无冗余。）

## Search Query

LLM inference latency prefill decode formula MFU
