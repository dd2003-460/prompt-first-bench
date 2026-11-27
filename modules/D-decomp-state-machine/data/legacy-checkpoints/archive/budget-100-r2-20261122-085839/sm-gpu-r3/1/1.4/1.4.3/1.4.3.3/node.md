# N151: llama.cpp 在 RTX 3090 上支持 Q8_0 KV Cache，无需 FP8 Tensor Core，但 Q8_0 KV 的计算吞吐量比 BF16

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N42

## Claim

llama.cpp 在 RTX 3090 上支持 Q8_0 KV Cache，无需 FP8 Tensor Core，但 Q8_0 KV 的计算吞吐量比 BF16 KV 低约 15%-25% [待核验: 实测数据]，因量化/反量化开销及内存带宽效率降低。

## Corrected Claim

llama.cpp 在 RTX 3090 上支持 Q8_0 KV Cache，无需 FP16/FP8 Tensor Core 加速，但 Q8_0 KV 的计算吞吐量通常低于 BF16 KV，具体性能差异取决于序列长度和实现优化，一般存在一定程度的开销。

## Evidence

[质询]具体数值区间（15%-25%）缺乏公开基准测试支持，且吞吐量差异受序列长度、Batch Size及具体llama.cpp版本优化程度影响极大，该固定区间可能不准确或仅适用于特定极端场景。 | 逻辑自洽：Q8_0 KV Cache确实无需FP8 Tensor Core支持（RTX 3090不支持FP8），且量化/反量化开销及内存带宽效率变化会导致性能波动；但作为经验事实，具体百分比缺乏来源直接支持，故降级。

## Search Query

llama.cpp Q8_0 KV cache performance overhead RTX 3090
