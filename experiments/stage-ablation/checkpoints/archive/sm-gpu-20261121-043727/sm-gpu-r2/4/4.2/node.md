# N23: 推理延迟分解公式：Latency = T_prefill + T_decode；其中 T_prefill ≈ L * M * P / (2 * FLOPS * 

- **status**: pending
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

父节点级核验未通过：不完备（子节点在修正公式（2个）和量化计算（2个）之间保持了良好的正交性，且没有明显的参数冗余。然而，完备性存在缺陷：父节点公式中明确引入了 'MFU' (Model FLOPs Utilization) 这一关键变量，但子节点中没有任何一个专门负责定义、估算或讨论该变量的取值依据（如为什么取40%，或不同负载下的变化），仅在子节点3中作为已知条件代入，导致对父节点关键参数的覆盖不全。）

## Search Query

LLM inference latency prefill decode formula MFU
