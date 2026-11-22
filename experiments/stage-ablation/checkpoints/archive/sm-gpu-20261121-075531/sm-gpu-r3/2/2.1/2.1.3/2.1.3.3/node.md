# N173: Mac Studio M2 Ultra 运行 Qwen3-27B W4 量化模型的实际 TPS 折损系数估算：基于 Apple Silicon 统一内存架构的 

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N52

## Claim

Mac Studio M2 Ultra 运行 Qwen3-27B W4 量化模型的实际 TPS 折损系数估算：基于 Apple Silicon 统一内存架构的 CPU-GPU 数据搬运开销及 MLX 框架优化程度，实际 TPS 通常为理论峰值的 70%-85%，即 41.5-50.4 tokens/s，与 N52 中 40-50 TPS 区间吻合，需实测验证具体折损率。

## Corrected Claim

Mac Studio M2 Ultra 运行 Qwen3-27B W4 量化模型的实际 TPS 受统一内存架构及 MLX 框架优化影响，通常低于理论峰值，具体折损率及 TPS 数值需实测验证，预估区间约为 40-50 TPS。

## Evidence

[质询]该陈述包含具体的经验性数值（70%-85% 折损系数、41.5-50.4 TPS），属于硬件性能与软件框架优化的经验事实，无法从第一性原理严格推导，且缺乏实测数据支持，存在因模型版本、具体量化实现（如 MLX 版本）或系统负载不同而导致实际 TPS 显著偏离该区间的可能性。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源），无法排除其他可能性，故降级。

## Search Query

Mac Studio M2 Ultra Qwen3-27B W4 quantization actual TPS benchmark MLX
