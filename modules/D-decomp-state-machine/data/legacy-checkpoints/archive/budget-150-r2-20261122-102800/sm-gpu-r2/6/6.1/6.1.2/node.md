# N134: vLLM 对 AMD RX 7900 XTX 的支持状态：截至 2024 年 Q4，vLLM 对 ROCm 的支持仍处于实验阶段，BF16 推理在特定版本下可行

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N43

## Claim

vLLM 对 AMD RX 7900 XTX 的支持状态：截至 2024 年 Q4，vLLM 对 ROCm 的支持仍处于实验阶段，BF16 推理在特定版本下可行但存在稳定性问题，INT8 量化支持有限，FP8 不支持。实际部署需锁定特定 ROCm 和 vLLM 版本组合，且性能通常低于同级别 NVIDIA 硬件 20-30%。

## Corrected Claim

截至 2024 年 Q4，vLLM 已支持 AMD RX 7900 XTX（通过 ROCm 后端），BF16 推理可行但需锁定特定版本组合，INT8/FP8 支持有限。实际性能通常低于同级别 NVIDIA 硬件，但具体差距随工作负载变化，无统一固定百分比。

## Evidence

[质询]陈述中关于“性能通常低于同级别 NVIDIA 硬件 20-30%”的具体数值缺乏来源直接支持，且“同级别”定义模糊（RX 7900 XTX 显存 24GB，通常对标 RTX 3090/4090，但算力架构差异大，性能差距随模型大小和 Batch Size 波动极大，固定百分比可能不准确）；此外，来源 [1] 提到 2024 年 ROCm 后端成熟，暗示支持状态可能比“实验阶段”更稳定，存在时间口径上的潜在冲突。 | 来源 [1] 和 [2] 确认 vLLM 支持 RX 7900 XTX 且涉及 ROCm 设置，间接支持“支持存在”及“需特定版本/环境”的定性描述，但未提供“20-30% 性能差距”的具体数据，也未明确界定 2024 Q4 的“实验阶段”状态（来源 [1] 称 2024 年已成熟），故具体数值和状态定性降级。

## Search Query

vLLM ROCm AMD RX 7900 XTX support status 2024

## Retrieval Sources

- {'url': 'https://gigagpu.com/vllm-on-rocm-gpu-setup/&rut=7eaef7347975b089d5e7020d5133a53d80a687059e4e272e282c92c9034ce42d', 'type': 'ddg', 'title': 'vLLM on ROCm: Setup Guide for AMD GPUs (MI300X, RX 7900 XTX)'}
- {'url': 'https://localaimaster.com/blog/radeon-7900-xtx-local-ai&rut=fda3e48d22cba7540b4d64f5623e67a737c233352070f23a97e3eb075c541214', 'type': 'ddg', 'title': 'RX 7900 XTX for AI: LLM Performance, ROCm and Price'}
- {'url': 'https://cadamcat.github.io/dual-radeon-vllm/index.html&rut=aaa6a0ede4e862fef5d3e380463bf0533ed9ab9291efec706e89bb145e648c5e', 'type': 'ddg', 'title': 'Two consumer Radeon RX 7900 XT, measured under ROCm and vLLM'}
