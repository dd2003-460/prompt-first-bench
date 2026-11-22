# N122: FP8 E4M3 推理吞吐量提升系数（FP8_TPS / BF16_TPS）在不同硬件（H100/H200 vs A100 vs 4090）上的具体数值，预期 

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N46

## Claim

FP8 E4M3 推理吞吐量提升系数（FP8_TPS / BF16_TPS）在不同硬件（H100/H200 vs A100 vs 4090）上的具体数值，预期 H100 上为 1.5-2x，A100 上可能仅 1.2-1.4x 或不支持原生 FP8 加速，需确认硬件兼容性。

## Corrected Claim

FP8 E4M3推理吞吐量提升系数因硬件而异：H100/H200支持原生FP8加速，预期提升约1.5-2x；A100不支持原生FP8，需软件模拟，提升有限（约1.2-1.4x）或不支持；4090不支持原生FP8。具体数值需实测确认。

## Evidence

[质询]参考来源仅讨论FP8量化原理与误差，未提供H100/A100/4090等具体硬件的吞吐量提升系数数值，无法验证具体倍数（1.5-2x vs 1.2-1.4x）及硬件兼容性细节。 | 来源[1]仅涉及FP8量化原理，与硬件吞吐量性能指标无关，属经验事实且缺直接来源支持，逻辑上H100支持原生FP8而A100不支持符合硬件架构常识，但具体数值无据。

## Search Query

Qwen3-27B FP8 inference throughput speedup H100 A100 4090

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/574825662&rut=c87a269dfa4d9955dab7d3ae40d9324695e60fe4431c8c6910afaaf110d7b824', 'type': 'ddg', 'title': 'Fp8 量化-原理、实现与误差分析 - 知乎'}
