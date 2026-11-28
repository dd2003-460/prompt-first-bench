# N77: V100 FP16 Tensor Core 峰值算力基准：单卡 V100-SXM2-16GB 的 FP16 Tensor Core 峰值算力为 15.7 TFL

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N29

## Claim

V100 FP16 Tensor Core 峰值算力基准：单卡 V100-SXM2-16GB 的 FP16 Tensor Core 峰值算力为 15.7 TFLOPS，4 卡 TP=4 理论聚合峰值为 62.8 TFLOPS，此为反量化后计算的理论上限参考值。

## Corrected Claim

V100 FP16 Tensor Core 峰值算力基准：单卡 V100-SXM2-16GB 的 FP16 Tensor Core 峰值算力为 15.7 TFLOPS，4 卡 TP=4 理论聚合峰值为 62.8 TFLOPS，此为反量化后计算的理论上限参考值。

## Evidence

先验知识/题面给定，逻辑校验通过：V100-SXM2-16GB FP16 Tensor Core 峰值算力确为 15.7 TFLOPS，4 卡聚合 62.8 TFLOPS 符合线性叠加逻辑。

## Search Query

Tesla V100 SXM2 FP16 Tensor Core peak FLOPS specifications
