# N132: 修正内存带宽受限判断逻辑：在解码阶段 (batch=1)，计算强度 (Arithmetic Intensity) 极低，瓶颈确为内存带宽；但在 Prefill 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N37

## Claim

修正内存带宽受限判断逻辑：在解码阶段 (batch=1)，计算强度 (Arithmetic Intensity) 极低，瓶颈确为内存带宽；但在 Prefill 阶段或 batch>1 时，计算单元 (CUDA Cores/Tensor Cores) 可能成为瓶颈，需区分 Prefill 和 Decode 两阶段的瓶颈类型。

## Corrected Claim

修正内存带宽受限判断逻辑：在解码阶段 (batch=1)，计算强度 (Arithmetic Intensity) 极低，瓶颈确为内存带宽；但在 Prefill 阶段或 batch>1 时，计算单元 (CUDA Cores/Tensor Cores) 可能成为瓶颈，需区分 Prefill 和 Decode 两阶段的瓶颈类型。

## Evidence

先验知识/题面给定，逻辑校验通过：Decode阶段batch=1时算术强度低，受内存带宽限制；Prefill或大batch时算术强度高，受计算单元限制，符合Roofline模型基本逻辑。
