# N142: RTX 3090 Ti 的 24GB 显存中，INT4 权重占 13.5GB，KV Cache (32K, BF16) 占 8.59GB，总占用 22.09GB

- **status**: pending
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N42, N43, N44

## Claim

RTX 3090 Ti 的 24GB 显存中，INT4 权重占 13.5GB，KV Cache (32K, BF16) 占 8.59GB，总占用 22.09GB，剩余仅 1.91GB 用于框架开销，存在 OOM 风险，需启用 PagedAttention 或降低 KV Cache 精度至 INT8 以释放约 4.3GB 空间。

## Corrected Claim

RTX 3090 Ti 的 24GB 显存中，INT4 权重占 13.5GB，KV Cache (32K, BF16) 占 8.59GB，总占用 22.09GB，剩余仅 1.91GB 用于框架开销，存在 OOM 风险，需启用 PagedAttention 或降低 KV Cache 精度至 INT8 以释放约 4.3GB 空间。

## Evidence

父节点级核验未通过：非正交（子节点1和子节点2存在逻辑耦合而非正交：子节点1计算的是显存容量（决定并发数），子节点2计算的是吞吐量（取决于单次推理的带宽/计算比）。虽然二者相关，但子节点2的吞吐量计算并未显式考虑子节点1得出的并发请求数（即未区分单请求独占带宽 vs 多请求共享带宽导致的吞吐下降），导致在“2个并发请求”场景下，子节点2给出的“40-46 tokens/s”可能是单请求峰值而非系统总吞吐或平均吞吐，存在隐含矛盾或歧义。此外，父节点提到的“PagedAttention”在子节点中未体现，子节点仅覆盖了“降低精度”和“CPU Offload”两种方案，遗漏了PagedAttention对碎片化显存管理和并发能力的具体影响分析。）

## Search Query

RTX 3090 Ti 24GB memory footprint Qwen3-27B INT4 KV cache 32k context
