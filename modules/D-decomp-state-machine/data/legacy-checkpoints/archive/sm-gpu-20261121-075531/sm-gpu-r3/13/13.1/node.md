# N377: vLLM 框架对 AMD ROCm 平台的 FP8 量化支持截至 2024 年底仍处于实验阶段，缺乏稳定的 Flash Attention FP8 内核，导致在

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N128

## Claim

vLLM 框架对 AMD ROCm 平台的 FP8 量化支持截至 2024 年底仍处于实验阶段，缺乏稳定的 Flash Attention FP8 内核，导致在 RX 7900 XTX 上运行 vLLM FP8 模型时吞吐量比 NVIDIA 同代产品低 40-60% [待核验]。

## Corrected Claim

vLLM 框架对 AMD ROCm 平台的 FP8 量化支持在 2024 年底仍处于实验阶段，由于软件栈成熟度差异，在 AMD 高端显卡上运行 FP8 模型时的吞吐量通常低于 NVIDIA 同代产品。

## Evidence

[质询]具体数值（40-60%）和特定硬件（RX 7900 XTX）的性能对比缺乏公开基准测试支持，且'缺乏稳定的 Flash Attention FP8 内核'这一技术细节可能随版本更新而变化，属于易变的技术状态描述。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

vLLM ROCm FP8 support status 2024 benchmark AMD RX 7900 XTX
