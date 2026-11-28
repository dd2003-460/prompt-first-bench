# N172: Qwen3.8-27B (NVFP4) 在 4x V100 (TP=4) 上运行 Prefill 阶段的实际理论峰值算力利用率 (MFU) 通常低于 40%，主

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N48

## Claim

Qwen3.8-27B (NVFP4) 在 4x V100 (TP=4) 上运行 Prefill 阶段的实际理论峰值算力利用率 (MFU) 通常低于 40%，主要受限于 Tensor Core 的 FP4 算子支持缺失（V100 无 FP4 Tensor Core，需 fallback 至 FP16/INT8 路径或软件模拟），导致实际 FLOPs 仅为标称 156 TFLOPS 的 30-50% [待核验]

## Corrected Claim

Qwen3.8-27B (NVFP4) 在 4x V100 (TP=4) 上运行时，由于 V100 缺乏原生 FP4 Tensor Core 支持，Prefill 阶段的实际算力利用率显著低于理论峰值，具体 MFU 数值需实测确认，但预计受限于 FP16/INT8 回退路径。

## Evidence

[质询]来源仅提供了 Decode 阶段的吞吐量数据（~66 tok/s），完全未涉及 Prefill 阶段、MFU 具体数值或 Tensor Core FP4 支持缺失导致的算力折损比例，无法直接支持‘MFU 低于 40%’及‘FLOPs 仅为标称 30-50%’的具体量化结论。 | 逻辑上 V100 确实缺乏原生 FP4 Tensor Core 支持，需回退至低精度或软件模拟，导致实际算力远低于标称值，符合硬件架构常识；但参考来源 [1] 仅证实了模型可在 V100 上运行及 Decode 速度，未提供 Prefill MFU 或算力利用率的具体数据，属于间接支持且缺乏关键量化证据。

## Search Query

V100 FP4 tensor core support performance loss Qwen3.8-27B inference MFU

## Retrieval Sources

- {'url': 'https://github.com/andreasknopke/V100-Qwen3.8-27b-NVFP4/blob/main/README.md&rut=718d966f11e67327dc084c3d085ff5493b630285fd6337c222f156956546c70b', 'type': 'ddg', 'title': 'V100-Qwen3.8-27b-NVFP4/README.md at main - GitHub'}
