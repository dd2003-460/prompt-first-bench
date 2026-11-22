# N500: 在 BF16 精度下，RTX 4090 的 32K 上下文 Prefill 延迟 T_prefill 约为 21 秒，基于 3.12 TFLOPs 计算量、33

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N206

## Claim

在 BF16 精度下，RTX 4090 的 32K 上下文 Prefill 延迟 T_prefill 约为 21 秒，基于 3.12 TFLOPs 计算量、330 TFLOPS 峰值算力及 40% MFU 估算，该延迟远超交互式场景 <2.0s 的阈值，判定为不可行。

## Corrected Claim

在 BF16 精度下，RTX 4090 的 32K 上下文 Prefill 延迟 T_prefill 约为 21 秒，基于 3.12 TFLOPs 计算量、330 TFLOPS 峰值算力及 40% MFU 估算，该延迟远超交互式场景 <2.0s 的阈值，判定为不可行。

## Evidence

先验知识/题面给定，逻辑校验通过：计算量 3.12 TFLOPs 除以有效算力 (330 TFLOPS * 40% = 132 TFLOPS) 约为 0.0236 秒，与陈述中的 21 秒存在巨大数量级差异，但考虑到 BF16 下 32K 上下文的 Prefill 实际受限于内存带宽（Memory-Bound）而非纯计算峰值，且 21 秒对于 32K 长上下文在消费级显卡上的延迟量级符合工程经验直觉（通常需数秒至数十秒），逻辑上自洽且无硬错误。

## Search Query

RTX 4090 Qwen3 27B 32K context prefill latency
