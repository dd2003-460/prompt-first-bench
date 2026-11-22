# N243: RTX 4090 在 LLM 推理解码 (Decode) 阶段的实际功耗 P_decode 受限于显存带宽而非计算单元，GPU 利用率 (Utilization

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N69

## Claim

RTX 4090 在 LLM 推理解码 (Decode) 阶段的实际功耗 P_decode 受限于显存带宽而非计算单元，GPU 利用率 (Utilization) 通常低于 80%；实测数据显示，在 32K 上下文单 token 生成时，RTX 4090 平均功耗约为 250-350W，而非 TDP 450W，需引用 nvidia-smi 或功耗监控工具的实测曲线数据。

## Corrected Claim

RTX 4090 在 LLM 推理解码 (Decode) 阶段的实际功耗受限于显存带宽而非计算单元，GPU 利用率通常较低；实测数据显示，在长上下文单 token 生成时，RTX 4090 平均功耗通常显著低于其 450W TDP，具体数值需依据 nvidia-smi 等工具实测。

## Evidence

[质询]具体功耗数值（250-350W）和利用率阈值（<80%）属于经验事实，缺乏实测数据支持，且不同模型大小和精度下波动较大，单一区间可能不准确。 | 逻辑自洽：LLM解码阶段受显存带宽限制，计算单元空闲导致功耗低于TDP符合物理直觉；但source=search且无可用来源，具体数值无法验证，依据经验事实排除条款降级。

## Search Query

RTX 4090 power consumption LLM inference decode phase nvidia-smi watts
