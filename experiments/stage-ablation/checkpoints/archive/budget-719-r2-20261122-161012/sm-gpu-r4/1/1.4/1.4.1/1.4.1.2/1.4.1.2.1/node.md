# N384: 2x RTX 4090 平台在 Qwen3-27B BF16 推理满载时的 GPU 总功耗为 900W (2 * 450W TGP)，此为计算墙插功耗的基准负载

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N160, N161, N162

## Claim

2x RTX 4090 平台在 Qwen3-27B BF16 推理满载时的 GPU 总功耗为 900W (2 * 450W TGP)，此为计算墙插功耗的基准负载值。

## Corrected Claim

2x RTX 4090 平台在 Qwen3-27B BF16 推理满载时的 GPU 总功耗为 900W (2 * 450W TGP)，此为计算墙插功耗的基准负载值。

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 4090 的 TGP 为 450W，2 张卡满载总功耗 900W 符合硬件规格，且作为基准负载值逻辑自洽。

## Search Query

RTX 4090 TGP power consumption watts
