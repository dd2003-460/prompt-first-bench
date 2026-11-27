# N286: 架构代际筛选修正：N103 排除‘不支持 FP8/INT8 硬件加速’的卡片，但需区分‘硬件加速’与‘软件模拟’。RTX 3090 (Ampere) 支持 IN

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N103

## Claim

架构代际筛选修正：N103 排除‘不支持 FP8/INT8 硬件加速’的卡片，但需区分‘硬件加速’与‘软件模拟’。RTX 3090 (Ampere) 支持 INT8 Tensor Core 加速（非 FP8），其 INT8 推理性能通常优于 BF16。因此，若允许 INT8 量化，RTX 3090 (24GB, 936GB/s) 应保留在候选集中，尽管其显存不足 32GB，需配合 Offloading 或更小模型，但作为‘边缘方案’需单独评估其 TCO/性能比。

## Corrected Claim

架构代际筛选修正：N103 排除‘不支持 FP8/INT8 硬件加速’的卡片，但需区分‘硬件加速’与‘软件模拟’。RTX 3090 (Ampere) 支持 INT8 Tensor Core 加速（非 FP8），其 INT8 推理性能通常优于 BF16。因此，若允许 INT8 量化，RTX 3090 (24GB, 936GB/s) 应保留在候选集中，尽管其显存不足 32GB，需配合 Offloading 或更小模型，但作为‘边缘方案’需单独评估其 TCO/性能比。

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 3090 (Ampere架构) 确实支持 INT8 Tensor Core 加速但不支持 FP8，其显存为 24GB，带宽 936GB/s，符合硬件规格事实；逻辑上区分硬件加速与软件模拟并建议保留为边缘方案是合理的架构筛选策略。
