# N390: AMD Radeon Pro W7900 48GB 显存中，扣除 54GB BF16 权重后显存不足，必须使用 INT4/FP8 量化；若使用 INT4 (13

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N130

## Claim

AMD Radeon Pro W7900 48GB 显存中，扣除 54GB BF16 权重后显存不足，必须使用 INT4/FP8 量化；若使用 INT4 (13.5GB 权重)，剩余 34.5GB 显存可支持约 34.5GB / (KV Cache per token) 的并发请求或更长上下文，具体需结合 KV Cache 大小计算。

## Corrected Claim

AMD Radeon Pro W7900 48GB 显存中，若模型 BF16 权重超过 48GB（如 54GB），则单卡无法容纳，必须使用 INT4/FP8 量化；若使用 INT4 量化（假设权重压缩至 13.5GB），剩余约 34.5GB 显存可用于 KV Cache，具体并发能力需结合每 token KV Cache 大小计算。

## Evidence

[质询]陈述中“扣除 54GB BF16 权重”与“48GB 显存”存在明显的数值矛盾（54GB > 48GB），且未明确说明该 54GB 权重是单卡还是多卡/多实例总和，导致“显存不足”的结论缺乏清晰的单卡上下文支撑；此外，INT4 量化后剩余显存用于 KV Cache 的计算逻辑虽自洽，但“54GB”这一具体数值在单卡 48GB 语境下显得突兀，可能是多卡场景下的总权重或笔误。 | 先验知识/题面给定，逻辑校验通过：INT4 量化确实能显著降低显存占用（13.5GB 权重在 48GB 卡上可行），剩余显存用于 KV Cache 的逻辑符合 LLM 推理原理；但 54GB 权重与 48GB 单卡显存的直接对比存在语境模糊，故降级为定性表述。
