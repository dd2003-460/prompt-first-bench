# N385: 当 Batch Size 增加到 8 时，Qwen3-27B 的算术强度提升至约 16 FLOPs/Byte（假设计算线性增加，访存重叠优化后），此时对于 RT

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N135

## Claim

当 Batch Size 增加到 8 时，Qwen3-27B 的算术强度提升至约 16 FLOPs/Byte（假设计算线性增加，访存重叠优化后），此时对于 RTX 5090（平衡点 58），仍处于带宽受限区但系数 η 下降至 0.85；对于 H100（平衡点 295），仍深度带宽受限，系数 η 保持 0.95。需通过实测 vLLM 日志中的 MFU (Model FLOPs Utilization) 校正此系数。

## Corrected Claim

当 Batch Size 增加到 8 时，Qwen3-27B 的算术强度提升至约 16 FLOPs/Byte。此时对于 RTX 5090（平衡点 58）和 H100（平衡点 295），均处于带宽受限区。具体效率系数 η 需通过实测 vLLM 日志中的 MFU 进行校正，理论估算值仅供参考（如 RTX 5090 约 0.85，H100 约 0.95）。

## Evidence

[质询]系数 η 的具体数值（0.85 和 0.95）属于经验性估算，缺乏通用理论支持，且不同硬件架构和软件栈下的实际 MFU 波动较大，直接断言具体数值存在过度精确的风险。 | 先验知识/题面给定，逻辑校验通过：算术强度计算逻辑自洽（16 < 58 < 295），带宽受限判断正确；但具体 η 值为经验估计，无来源直接支持，故降级。

## Search Query

vLLM MFU model flops utilization batch size impact decode speed
