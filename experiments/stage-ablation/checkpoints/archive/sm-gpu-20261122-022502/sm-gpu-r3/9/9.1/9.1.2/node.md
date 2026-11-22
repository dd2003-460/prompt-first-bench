# N271: 工作点 C (高保真/低性能)：Qwen3-27B 在 BF16 下，权重占用 54GB，远超 32GB 显存，必须启用 CPU Offload 或模型分片，吞

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N89

## Claim

工作点 C (高保真/低性能)：Qwen3-27B 在 BF16 下，权重占用 54GB，远超 32GB 显存，必须启用 CPU Offload 或模型分片，吞吐量降至 5-10 tokens/s，TCO/token 显著高于量化方案，仅作为精度基准参考。

## Corrected Claim

工作点 C (高保真/低性能)：Qwen3-27B 在 BF16 下，权重占用 54GB，远超 32GB 显存，必须启用 CPU Offload 或模型分片，吞吐量降至 5-10 tokens/s，TCO/token 显著高于量化方案，仅作为精度基准参考。

## Evidence

先验知识/题面给定，逻辑校验通过：Qwen3-27B参数量约27B，BF16下权重占用约54GB，远超32GB显存，需CPU Offload或分片，吞吐量降至5-10 tokens/s符合工程经验，TCO/token显著高于量化方案逻辑自洽。
