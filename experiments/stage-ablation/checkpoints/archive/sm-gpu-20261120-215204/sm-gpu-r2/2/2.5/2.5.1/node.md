# N79: RTX 4090 (Ada Lovelace) 运行 Qwen3-27B 时，INT8 精度下的实际推理吞吐量（Tokens/s）与 BF16 精度的比值，需考

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N17

## Claim

RTX 4090 (Ada Lovelace) 运行 Qwen3-27B 时，INT8 精度下的实际推理吞吐量（Tokens/s）与 BF16 精度的比值，需考虑 Tensor Core INT8 加速比及显存带宽瓶颈，预期比值为 1.5-1.8 倍，需检索具体 benchmark 数据。

## Corrected Claim

RTX 4090 (Ada Lovelace) 运行 Qwen3-27B 时，INT8 精度下的实际推理吞吐量（Tokens/s）与 BF16 精度的比值预期在 1.5-1.8 倍之间，但具体数值需依赖实际 benchmark 数据验证。

## Evidence

[质询]来源[1]仅提及在RTX 4090上运行Qwen3.8-27B（注意模型版本为3.8而非3，且未明确提及INT8与BF16的对比数据），未提供具体的吞吐量比值或benchmark数据，无法直接支持1.5-1.8倍这一具体数值范围。 | 逻辑上INT8通常比BF16快，但具体比值受显存带宽和计算瓶颈影响，1.5-1.8倍在合理范围内；来源[1]相关但仅间接支持可行性，未提供具体数值支持。

## Search Query

RTX 4090 Qwen3-27B INT8 vs BF16 inference throughput tokens per second

## Retrieval Sources

- {'url': 'https://github.com/sergiuszm/ninfer-4090&rut=904eb85b03313bc909d07c24710c0df700c8f141e34dfbaac7ed9f2629d57a5c', 'type': 'ddg', 'title': 'GitHub - sergiuszm/ninfer-4090: Qwen3.8-27B on one RTX 4090: full ...'}
