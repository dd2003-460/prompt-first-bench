# N282: INT8 工作点下 V100 的内存带宽瓶颈位置转移：虽然 Tensor Core 算力翻倍，但 KV Cache 若保持 FP16/FP8，Prefill 阶

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N112

## Claim

INT8 工作点下 V100 的内存带宽瓶颈位置转移：虽然 Tensor Core 算力翻倍，但 KV Cache 若保持 FP16/FP8，Prefill 阶段仍受 HBM2 带宽限制；若 KV Cache 也量化为 INT8，带宽需求减半，理论 Prefill 吞吐提升上限为 2x，但 Attention 计算精度损失需额外评估。

## Corrected Claim

INT8 工作点下 V100 的内存带宽瓶颈位置转移：虽然 Tensor Core 算力翻倍，但 KV Cache 若保持 FP16/FP8，Prefill 阶段仍受 HBM2 带宽限制；若 KV Cache 也量化为 INT8，带宽需求减半，理论 Prefill 吞吐提升上限为 2x，但 Attention 计算精度损失需额外评估。

## Evidence

先验知识/题面给定，逻辑校验通过：KV Cache 从 FP16 (16-bit) 量化至 INT8 (8-bit) 使数据体积减半，在带宽受限场景下理论吞吐上限提升 2x 符合物理直觉与算术逻辑。

## Search Query

INT8 KV cache bandwidth savings V100 inference throughput
