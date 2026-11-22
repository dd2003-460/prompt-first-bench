# N83: FP8 精度下的总内存需求计算：Weights = 27B * 1 byte = 27 GB；KV Cache (32K, FP8) ≈ 2.68 GB；Ove

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N17

## Claim

FP8 精度下的总内存需求计算：Weights = 27B * 1 byte = 27 GB；KV Cache (32K, FP8) ≈ 2.68 GB；Overhead ≈ 3 GB；Total ≈ 32.68 GB。此数值仍超过 RTX 4090 (24GB)，但可适配 A6000 (48GB) 或 L40S (48GB) [待核验]，需确认 FP8 KV Cache 在主流框架中的支持情况及实际精度损失。

## Corrected Claim

FP8 精度下 Weights 约 27 GB，总内存需求预计低于 48 GB，可适配 A6000/L40S；KV Cache 具体数值及 FP8 支持情况需根据具体模型架构及框架版本进一步确认。

## Evidence

[质询]KV Cache 2.68 GB 的数值缺乏具体模型架构参数（如层数、头数、头维度）支持，且 FP8 KV Cache 在主流框架中的实际支持情况及精度损失属于经验事实，仅凭逻辑推导无法确证具体数值。 | 来源[1]直接支持了 27B 模型在 RTX A6000 (48GB) 上使用 FP8 的可行性，间接佐证了总内存需求低于 48GB 的逻辑；但 KV Cache 具体数值及 FP8 支持细节无直接来源支持，属经验事实，故降级。

## Search Query

Qwen3-27B FP8 quantization memory requirement 32k context A6000 L40S feasibility

## Retrieval Sources

- {'url': 'https://github.com/gyang274/ms-Qwen3.8-27B&rut=b24be9fee03e1a2992c34941940523956c6bcfffea1324704b0006959709c921', 'type': 'ddg', 'title': 'GitHub - gyang274/ms-Qwen3.8-27B: Serving Qwen3.8-27B on one RTX A6000 ...'}
