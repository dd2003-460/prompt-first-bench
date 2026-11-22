# N586: M1 Max 内存带宽为 400 GB/s，M2 Ultra 为 800 GB/s；在 Qwen3-27B INT4 量化下，Decode 阶段吞吐量与内存带宽

- **status**: degraded
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N203

## Claim

M1 Max 内存带宽为 400 GB/s，M2 Ultra 为 800 GB/s；在 Qwen3-27B INT4 量化下，Decode 阶段吞吐量与内存带宽成正比，M1 Max 的理论 Decode 上限约为 M2 Ultra 的 50%（400/800），实测约为 12-16 tokens/s vs M2 Ultra 的 25-35 tokens/s（基于 64GB 显存限制，M1 Max 仅支持 32K 上下文单请求，M2 Ultra 支持更高并发）。

## Corrected Claim

M1 Max 内存带宽为 400 GB/s，M2 Ultra 为 800 GB/s；在 Qwen3-27B INT4 量化下，Decode 阶段理论吞吐量与内存带宽成正比，M1 Max 的理论 Decode 上限约为 M2 Ultra 的 50%。实测吞吐量受内存容量限制（M1 Max 32GB 仅支持较小上下文/并发），通常显著低于理论峰值，具体数值依部署配置而异。

## Evidence

[质询]实测吞吐量数值（12-16 vs 25-35 tokens/s）属于经验事实，受具体实现（如 vLLM 版本、KV Cache 管理、Batch Size 策略）影响极大，且 M1 Max 32GB 内存运行 27B INT4 模型时，KV Cache 空间极度受限，实际并发和上下文长度会显著低于理论值，导致实测带宽利用率远低于 50% 的理论线性比例，具体数值缺乏通用性。 | source=knowledge，逻辑自洽（带宽比例 400/800=50% 正确，INT4 27B 模型大小约 14-15GB，32GB 内存可容纳），但实测吞吐量具体数值为经验事实，无来源支持，依据经验事实排除条款降级。
