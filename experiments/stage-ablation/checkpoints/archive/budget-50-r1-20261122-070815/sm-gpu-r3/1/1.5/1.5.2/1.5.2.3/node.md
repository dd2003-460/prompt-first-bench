# N194: Qwen3-27B 在 L40S 48GB 上运行 FP8 精度时的实际 Decode 速度约为 30-40 tokens/s (受限于 864 GB/s 带宽

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N49

## Claim

Qwen3-27B 在 L40S 48GB 上运行 FP8 精度时的实际 Decode 速度约为 30-40 tokens/s (受限于 864 GB/s 带宽)，Prefill 速度约为 1000-1500 tokens/s，其性能介于 RTX 4090 INT4 和 H100 FP8 之间，但价格仅为 H100 的 1/3，是平衡质量 (FP8) 与成本的中端选择

## Corrected Claim

Qwen3-27B 在 L40S 48GB 上运行 FP8 精度时，受限于 864 GB/s 带宽，Decode 速度通常在 30-40 tokens/s 量级，Prefill 速度在 1000-1500 tokens/s 量级。其性能定位介于 RTX 4090 INT4 和 H100 FP8 之间，成本显著低于 H100，是平衡质量与成本的中端选择。

## Evidence

[质询]该陈述包含具体的硬件性能指标（Decode/Prefill速度）和价格比例，属于经验事实。由于检索失败无外部来源支持，且不同驱动版本、量化实现（如AWQ/GPTQ vs FP8原生支持）及系统开销会导致实际速度波动较大，30-40 tokens/s 和 1000-1500 tokens/s 的具体数值缺乏权威基准测试的直接佐证，存在因特定配置偏差导致数值不准的风险。 | 经验事实，逻辑自洽但缺来源支持。L40S 864GB/s 带宽限制下，27B FP8 模型 Decode 速度受内存带宽瓶颈制约，30-40 tokens/s 在量级上合理（27B*1Byte/864GB/s ≈ 31 tokens/s 理论上限，实际略低或接近）；Prefill 受算力限制，1000-1500 tokens/s 亦符合 L40S 算力水平。价格约为 H100 1/3 符合市场常识。但因无来源直接支持具体数值，降级为定性/范围表述。

## Search Query

L40S 48GB Qwen3-27B FP8 inference benchmark throughput
