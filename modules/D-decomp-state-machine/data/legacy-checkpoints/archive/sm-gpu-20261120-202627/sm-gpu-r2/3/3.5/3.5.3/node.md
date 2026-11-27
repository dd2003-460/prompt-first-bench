# N89: 2×RTX 3090 (FP8) 在 32K 输入/1K 输出条件下的预估吞吐量：基于显存带宽 936 GB/s 和计算瓶颈，预估约为 18-25 tokens

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N20

## Claim

2×RTX 3090 (FP8) 在 32K 输入/1K 输出条件下的预估吞吐量：基于显存带宽 936 GB/s 和计算瓶颈，预估约为 18-25 tokens/s [待核验：需实测验证]。

## Corrected Claim

2×RTX 3090 在 32K 输入/1K 输出条件下的预估吞吐量约为 18-25 tokens/s（基于显存带宽 936 GB/s 的估算，具体数值高度依赖模型架构及 FP8 实现效率，需实测验证）。

## Evidence

[质询]该吞吐量预估（18-25 tokens/s）属于经验事实，且未提供具体的模型规模（如参数量、层数）或计算细节，仅凭显存带宽和“计算瓶颈”这一模糊描述无法从第一性原理严格推导出该具体数值范围；此外，RTX 3090 原生不支持 FP8 硬件加速（需软件模拟或特定库支持，效率通常低于 FP16），直接假设 FP8 达到理论峰值带宽利用率存在技术合理性疑问。 | 参考来源 [1] 仅提及 GeForce 显卡在 AI 任务中通常以半速运行及 FP16/BF16 吞吐量提升，未提供 RTX 3090 在 32K/1K 场景下的具体 FP8 吞吐量数据，属于间接/无关支持；该事实为经验性性能预估，逻辑上量级合理（长上下文下受带宽限制，吞吐量下降），但缺乏直接来源支持，故降级。

## Search Query

Qwen3-27B RTX 3090 FP8 inference throughput 32k context tokens per second

## Retrieval Sources

- {'url': 'https://github.com/Zagitta/gpu-unlock&rut=521b78aaed49ed44834933dbc99693ecea533954e0e288b8fa34bb909bd03cfa', 'type': 'ddg', 'title': 'GitHub - Zagitta/gpu-unlock: Your GeForce runs AI at half speed. This ...'}
