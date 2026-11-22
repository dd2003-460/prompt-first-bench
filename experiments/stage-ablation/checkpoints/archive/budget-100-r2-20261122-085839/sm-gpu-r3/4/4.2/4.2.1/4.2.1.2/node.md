# N208: 不同精度下FLOPs_per_token的等效换算：BF16下FLOPs=54.2 GFLOPs/token；INT8下由于使用INT8 Tensor Core

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N61

## Claim

不同精度下FLOPs_per_token的等效换算：BF16下FLOPs=54.2 GFLOPs/token；INT8下由于使用INT8 Tensor Core，有效FLOPs吞吐量翻倍，但逻辑FLOPs不变，故计算时间减半；W4下若使用AWQ，反量化过程引入额外ALU FLOPs（约增加5%-10%），等效FLOPs_per_token ≈ 56.9-59.6 GFLOPs/token。此差异直接影响Prefill阶段的算力需求估算。

## Corrected Claim

不同精度下FLOPs_per_token的等效换算：BF16下FLOPs=54.2 GFLOPs/token；INT8下由于使用INT8 Tensor Core，有效FLOPs吞吐量翻倍，但逻辑FLOPs不变，故计算时间减半；W4下若使用AWQ，反量化过程引入额外ALU FLOPs（约增加5%-10%），等效FLOPs_per_token ≈ 56.9-59.6 GFLOPs/token。此差异直接影响Prefill阶段的算力需求估算。

## Evidence

先验知识/题面给定，逻辑校验通过：INT8 Tensor Core吞吐量翻倍导致时间减半符合硬件特性；AWQ反量化引入5%-10%额外ALU开销符合工程经验，数值计算（54.2 * 1.05 ≈ 56.9, 54.2 * 1.1 ≈ 59.6）准确。
