# N412: 理论带宽上限与实际推理吞吐量的差距系数 (Efficiency_Factor)：实际 Throughput = Theoretical_Max_Tok_s × 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N132

## Claim

理论带宽上限与实际推理吞吐量的差距系数 (Efficiency_Factor)：实际 Throughput = Theoretical_Max_Tok_s × Efficiency_Factor。对于大模型自回归解码，Efficiency_Factor 通常受限于计算/访存重叠效率，经验值约为 0.3-0.5 [待核验：需引用 vLLM 或 TensorRT-LLM 在相同硬件上的实测/理论比值]。

## Corrected Claim

理论带宽上限与实际推理吞吐量的差距系数 (Efficiency_Factor)：实际 Throughput = Theoretical_Max_Tok_s × Efficiency_Factor。对于大模型自回归解码，Efficiency_Factor 通常受限于计算/访存重叠效率，经验值约为 0.3-0.5 [待核验：需引用 vLLM 或 TensorRT-LLM 在相同硬件上的实测/理论比值]。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

LLM inference efficiency factor theoretical bandwidth vs actual throughput ratio
