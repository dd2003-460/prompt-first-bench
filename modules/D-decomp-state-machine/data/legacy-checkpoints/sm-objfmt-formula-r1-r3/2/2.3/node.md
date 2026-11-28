# N12: 各候选硬件的有效可用显存系数（通常为总显存的80-90%，扣除CUDA Context、碎片化开销），用于将理论显存需求转换为实际最低显存门槛

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N2

## Claim

各候选硬件的有效可用显存系数（通常为总显存的80-90%，扣除CUDA Context、碎片化开销），用于将理论显存需求转换为实际最低显存门槛

## Corrected Claim

各候选硬件的有效可用显存系数（通常为总显存的80-90%，扣除CUDA Context、碎片化开销），用于将理论显存需求转换为实际最低显存门槛

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

GPU effective VRAM utilization overhead CUDA context fragmentation LLM inference
