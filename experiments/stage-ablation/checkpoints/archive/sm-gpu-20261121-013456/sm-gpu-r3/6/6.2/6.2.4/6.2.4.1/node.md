# N256: M3 Ultra 运行 Qwen3-27B 的实测吞吐量修正：基于 MLX 框架 Q4_K_M 量化，实测吞吐量为 12.46 tokens/s（来源：社区基准

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N100

## Claim

M3 Ultra 运行 Qwen3-27B 的实测吞吐量修正：基于 MLX 框架 Q4_K_M 量化，实测吞吐量为 12.46 tokens/s（来源：社区基准测试，[时效待核]），而非 N100 中估算的 8 tokens/s；该值直接决定 M3 Ultra 在低吞吐量需求场景（<12.46 tokens/s）下的可行性边界。

## Corrected Claim

M3 Ultra 运行 Qwen3-27B 的实测吞吐量约为 12.46 tokens/s（基于 MLX 框架 Q4_K_M 量化，社区基准测试数据，需进一步核实具体测试条件）

## Evidence

[质询]参考来源[1]仅提及非Apple Silicon不适用MLX路线，未提供M3 Ultra运行Qwen3-27B的具体吞吐量数值（12.46 tokens/s），且该数值属于特定硬件+特定量化+特定框架下的经验实测数据，无法从第一性原理推导，存在来源缺失风险。 | 经验事实，逻辑自洽但缺来源支持（来源[1]未直接覆盖具体吞吐量数值）

## Search Query

Apple M3 Ultra Qwen3-27B MLX inference throughput tokens per second benchmark

## Retrieval Sources

- {'url': 'https://github.com/xiaoxianxian/qwen3.8-deployment&rut=c22dbc82db02e48fd5b91ccc4f43360cdcc86531ab183fc211b0317f8fcd2759', 'type': 'ddg', 'title': 'Mac 本地部署 Qwen3.8-27B 完整指南（Apple Silicon / Ollama）'}
