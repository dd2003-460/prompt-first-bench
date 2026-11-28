# N506: 工作点1 下 4×V100 TP=4 的有效吞吐量 Tokens/s 理论上限：基于 V100 FP16 峰值算力 125 TFLOPS 和模型 FLOPs p

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N181

## Claim

工作点1 下 4×V100 TP=4 的有效吞吐量 Tokens/s 理论上限：基于 V100 FP16 峰值算力 125 TFLOPS 和模型 FLOPs per token (≈2×Params)，Throughput ≈ (4 × 125e12 × Efficiency) / (2 × 27e9) tokens/s，Efficiency 取 0.4-0.6

## Corrected Claim

工作点1 下 4×V100 TP=4 的有效吞吐量 Tokens/s 理论上限：基于 V100 FP16 峰值算力 125 TFLOPS 和模型 FLOPs per token (≈2×Params)，Throughput ≈ (4 × 125e12 × Efficiency) / (2 × 27e9) tokens/s，Efficiency 取 0.4-0.6

## Evidence

先验知识/题面给定，逻辑校验通过：V100 FP16峰值算力125 TFLOPS及LLM推理FLOPs≈2×Params均为标准工程常识，计算公式量纲正确，效率系数取值范围符合实际硬件表现。
