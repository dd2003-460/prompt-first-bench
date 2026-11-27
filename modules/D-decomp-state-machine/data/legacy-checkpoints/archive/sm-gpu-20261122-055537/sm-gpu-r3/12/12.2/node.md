# N392: RTX 5090 的显存容量为 32GB GDDR7，较 RTX 4090 (24GB) 增加 33%；在 Qwen3-27B INT4 (14GB 权重) +

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N123

## Claim

RTX 5090 的显存容量为 32GB GDDR7，较 RTX 4090 (24GB) 增加 33%；在 Qwen3-27B INT4 (14GB 权重) + 32K 上下文 KV Cache (约 10-15GB) 场景下，32GB 显存可容纳单卡 BF16 KV Cache 或更长的上下文，消除 4090 单卡需量化权重或缩减上下文的限制，提升部署灵活性。

## Corrected Claim

RTX 5090 的显存容量预计为 32GB GDDR7，较 RTX 4090 (24GB) 增加约 33%；在 Qwen3-27B INT4 量化及长上下文场景下，更大的显存容量有助于容纳权重与 KV Cache，从而提升单卡部署的灵活性，具体内存占用需根据实际模型版本和上下文长度计算。

## Evidence

[质询]该陈述包含具体的硬件规格（RTX 5090 显存容量、类型）及特定模型（Qwen3-27B）的量化后权重大小和 KV Cache 估算值，属于经验事实。由于检索失败，无法通过外部来源直接验证这些具体数值（如 32GB GDDR7、14GB 权重、10-15GB KV Cache）的准确性，存在参数偏差或模型版本差异导致的数据错误风险。 | 经验事实，逻辑自洽但缺来源支持。虽然 32GB > 24GB 且 32/24 ≈ 1.33 的数学关系成立，且显存容量增加确实能提升部署灵活性，但具体的硬件参数和模型内存占用估算无法在无来源情况下确认为准确事实。

## Search Query

RTX 5090 32GB VRAM KV cache 32k context inference
