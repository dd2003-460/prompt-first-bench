# N104: RX 7900 XTX 的 FP16 峰值算力为 60.6 TFLOPS，计算方式为 96 CUs * 2 FMA * 2 (FP16) * 2.4 GHz *

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N24, N25, N35

## Claim

RX 7900 XTX 的 FP16 峰值算力为 60.6 TFLOPS，计算方式为 96 CUs * 2 FMA * 2 (FP16) * 2.4 GHz * 1e12，基于 RDNA 3 架构规格。

## Corrected Claim

RX 7900 XTX 的 FP16 峰值算力为 60.6 TFLOPS，计算方式为 96 CUs * 2 FMA * 2 (FP16) * 2.4 GHz * 1e12，基于 RDNA 3 架构规格。

## Evidence

父节点级核验未通过：不完备（子节点1解释了理论峰值的计算参数（静态规格），子节点2描述了实际负载下的频率衰减（动态行为），两者视角不同（理论 vs 实际），正交性良好。但是，父节点仅陈述了“理论峰值算力为60.6 TFLOPS”这一事实及其计算依据，并未提及“实际负载下的性能衰减”。子节点2引入了父节点未包含的“实际算力”和“频率下降”信息，超出了父节点的知识边界，导致分解不完备（或者说子节点2不是父节点的直接分解，而是父节点的延伸或补充）。严格来说，分解应聚焦于解释父节点中的“60.6 TFLOPS”是如何得出的，而不应引入父节点未提及的“实际性能”概念。）

## Search Query

RX 7900 XTX FP16 TFLOPS calculation RDNA 3
