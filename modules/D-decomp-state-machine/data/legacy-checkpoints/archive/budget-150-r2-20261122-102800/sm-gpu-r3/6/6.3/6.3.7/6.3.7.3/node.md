# N366: RX 7900 XTX 在 W4 量化下的性能瓶颈：由于 ROCm 对 4-bit 量化 kernel 的优化程度低于 CUDA，且 RDNA3 架构缺乏专用 

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N143

## Claim

RX 7900 XTX 在 W4 量化下的性能瓶颈：由于 ROCm 对 4-bit 量化 kernel 的优化程度低于 CUDA，且 RDNA3 架构缺乏专用 4-bit 硬件单元，其 W4 推理吞吐量通常仅为 NVIDIA 同级硬件的 15-25%，且质量损失可能与 NVIDIA 相当或略高，导致其在 W4 口径下的性价比极低。

## Corrected Claim

RX 7900 XTX 在 W4 量化下的性能瓶颈：由于 ROCm 对 4-bit 量化 kernel 的优化程度通常低于 CUDA，且 RDNA3 架构缺乏专用 4-bit 硬件单元，其 W4 推理吞吐量通常显著低于 NVIDIA 同级硬件，且质量损失可能与 NVIDIA 相当或略高，导致其在 W4 口径下的性价比相对较低。

## Evidence

[质询]具体数值区间（15-25%）缺乏公开基准测试支持，且‘质量损失略高’的断言过于绝对，不同模型和量化算法（如AWQ vs GPTQ）下表现差异巨大，该具体百分比可能源自特定小众测试或推测，而非普遍共识。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且具体性能比值为经验数据，无法从第一性原理严格推出）

## Search Query

RX 7900 XTX 4-bit quantization LLM performance ROCm
