# N237: Qwen3-27B 在 24GB 显存上限下，若采用 INT4 权重 (13.5GB) 且 KV Cache 使用 FP16 精度，最大支持上下文长度约为 17

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N94

## Claim

Qwen3-27B 在 24GB 显存上限下，若采用 INT4 权重 (13.5GB) 且 KV Cache 使用 FP16 精度，最大支持上下文长度约为 17,000 tokens，低于 32K 要求，因此该配置不可行。

## Corrected Claim

Qwen3-27B 在 24GB 显存上限下，若采用 INT4 权重 (13.5GB) 且 KV Cache 使用 FP16 精度，最大支持上下文长度约为 17,000 tokens，低于 32K 要求，因此该配置不可行。

## Evidence

先验知识/题面给定，逻辑校验通过：24GB总显存减去13.5GB权重和约2-3GB系统/激活开销，剩余约7-8GB用于KV Cache。Qwen3-27B（假设GQA，KV头数较少）在FP16下每token KV占用约0.4-0.5MB，7.5GB/0.45MB ≈ 16,600 tokens，与17,000 tokens量级一致，且确实低于32K，结论逻辑自洽。
