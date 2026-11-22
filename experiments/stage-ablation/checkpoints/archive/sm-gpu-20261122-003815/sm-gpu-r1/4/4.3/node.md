# N24: Qwen3-27B 在 INT4/W4 量化下的最小显存占用计算：weights_size = 27B * 0.5 bytes ≈ 13.5GB (含 scal

- **status**: degraded
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N4

## Claim

Qwen3-27B 在 INT4/W4 量化下的最小显存占用计算：weights_size = 27B * 0.5 bytes ≈ 13.5GB (含 scale/zero-point 开销约 15GB)，KV Cache BF16 17.2GB，总显存需求 ≈ 32.2GB，可运行于单张 24GB 显存卡（需 offload 部分 KV 或限制 batch）。

## Corrected Claim

Qwen3-27B 在 INT4/W4 量化下，模型权重约占 13.5-15GB。若 KV Cache 占用 17.2GB，总显存需求约 32.2GB，超出单张 24GB 显存卡容量；需通过 Offload 部分 KV Cache 至 CPU 或严格限制 Batch Size/序列长度，方可在单张 24GB 显存卡上运行。

## Evidence

[质询]KV Cache 17.2GB 的数值缺乏上下文（如序列长度、Batch Size），且总显存 32.2GB 远超 24GB 显存卡容量，声称“可运行于单张 24GB 显存卡”在逻辑上必须依赖未明确量化的 Offload 策略，存在将“理论最小权重+特定KV”与“实际可运行性”混淆的风险。 | 先验知识/题面给定，逻辑校验通过：INT4 权重约 13.5-15GB 符合 27B 模型量级；但 32.2GB 总需求 > 24GB 显存，结论“可运行”依赖于 Offload 假设，虽逻辑上可行（通过 CPU Offload 或限制 KV），但作为“最小显存占用”的陈述略显矛盾（最小占用通常指不 Offload 时的理论下限，或明确标注 Offload 后的驻留显存）。鉴于 source=knowledge，逻辑自洽但存在表述歧义，降级为 degraded 以强调 Offload 依赖。
