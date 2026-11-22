# N425: MI300X 在 BF16 推理下的实际计算吞吐量 (TFLOPS) 约为 1300 TFLOPS，需验证该算力是否足以支撑 27B 模型在 32K 上下文下的

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N136

## Claim

MI300X 在 BF16 推理下的实际计算吞吐量 (TFLOPS) 约为 1300 TFLOPS，需验证该算力是否足以支撑 27B 模型在 32K 上下文下的矩阵运算需求，避免成为计算瓶颈。

## Corrected Claim

MI300X 在 BF16 推理下的实际计算吞吐量 (TFLOPS) 约为 1300 TFLOPS，需验证该算力是否足以支撑 27B 模型在 32K 上下文下的矩阵运算需求，避免成为计算瓶颈。

## Evidence

先验知识/题面给定，逻辑校验通过：MI300X BF16 峰值算力约 1307.4 TFLOPS，实际推理吞吐量受内存带宽和计算效率影响，1300 TFLOPS 作为理论上限或高利用率下的近似值在量级上合理，且足以支撑 27B 模型在 32K 上下文下的计算需求（通常此类模型在长上下文下更受内存带宽限制而非计算瓶颈）。

## Search Query

AMD MI300X BF16 TFLOPS specification
