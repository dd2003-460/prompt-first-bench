# N304: RTX 4090 运行 Qwen3-27B INT4 时的实测吞吐量 tokens/s 需结合 N131 的理论值（~65 tok/s）与社区实测偏差（通常 0

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N105

## Claim

RTX 4090 运行 Qwen3-27B INT4 时的实测吞吐量 tokens/s 需结合 N131 的理论值（~65 tok/s）与社区实测偏差（通常 0.7-0.9 倍）估算，以计算单位 token 能耗 (W/token) = P_avg / Throughput

## Corrected Claim

RTX 4090 运行 Qwen3-27B INT4 时的实测吞吐量需结合理论估算值与社区实测偏差估算，以计算单位 token 能耗 (W/token) = P_avg / Throughput

## Evidence

[质询]该陈述包含具体的经验性数值（理论值~65 tok/s、偏差系数0.7-0.9），属于硬件性能与模型推理效率的经验事实，无法从第一性原理严格推导，且缺乏来源支持。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源）

## Search Query

RTX 4090 Qwen 27B INT4 inference throughput tokens per second benchmark
