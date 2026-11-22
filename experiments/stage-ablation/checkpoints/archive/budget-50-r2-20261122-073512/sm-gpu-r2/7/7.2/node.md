# N187: RTX 3090 在 BF16 精度下运行 Qwen3-27B 的可行性边界：单卡 24GB 显存无法容纳 54GB 权重，必须采用 INT8/FP8 量化；理

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N34

## Claim

RTX 3090 在 BF16 精度下运行 Qwen3-27B 的可行性边界：单卡 24GB 显存无法容纳 54GB 权重，必须采用 INT8/FP8 量化；理论吞吐上限修正为 936 / (27 + 1.5 + 2) ≈ 30.0 tokens/s；需验证 RTX 3090 对 FP8 内核的支持情况（Ampere 架构原生不支持 FP8，需软件模拟或仅用 INT8），若仅支持 INT8，则有效带宽利用率可能降低 5-10%。

## Corrected Claim

RTX 3090 在 BF16 精度下运行 Qwen3-27B 的可行性边界：单卡 24GB 显存无法容纳 54GB 权重，必须采用 INT8/FP8 量化；理论吞吐上限需根据具体硬件带宽和计算能力进一步验证；需验证 RTX 3090 对 FP8 内核的支持情况（Ampere 架构原生不支持 FP8，需软件模拟或仅用 INT8），若仅支持 INT8，则有效带宽利用率可能降低 5-10%。

## Evidence

[质询]RTX 3090 的显存容量为 24GB，而 Qwen3-27B 模型在 BF16 精度下的权重大小约为 54GB（27B * 2 bytes），单卡确实无法容纳。但陈述中提到的“理论吞吐上限修正为 936 / (27 + 1.5 + 2) ≈ 30.0 tokens/s”这一具体数值缺乏明确的推导依据或来源支持，且 936 这一分子来源不明（可能是某种带宽或算力指标，但未明确定义），属于经验性估算而非第一性原理可严格推导的数学事实。此外，RTX 3090 基于 Ampere 架构，确实原生不支持 FP8，需软件模拟或仅用 INT8，这部分逻辑自洽。 | 先验知识/题面给定，逻辑校验通过：RTX 3090 显存 24GB 无法容纳 54GB BF16 权重，需量化；Ampere 架构不支持 FP8 为已知事实。但吞吐上限的具体数值 30.0 tokens/s 缺乏来源支持，且推导过程不透明，属于经验事实，逻辑自洽但缺来源支持。

## Search Query

RTX 3090 FP8 support Qwen3-27B inference performance degradation
