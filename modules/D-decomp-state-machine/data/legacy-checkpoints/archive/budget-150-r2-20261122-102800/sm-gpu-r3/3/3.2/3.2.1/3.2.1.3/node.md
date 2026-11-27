# N249: L40S (Ada Lovelace) 在 INT8 量化下的实测 Token 生成吞吐量（Decode 阶段，batch_size=1, seq_len=32

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N91, N92, N93

## Claim

L40S (Ada Lovelace) 在 INT8 量化下的实测 Token 生成吞吐量（Decode 阶段，batch_size=1, seq_len=32K）约为 18-22 tokens/s，受限于其 864 GB/s 的显存带宽（低于 A6000 的 960 GB/s）及类似的 Ada 架构 Attention 计算效率，尽管其 FP8/INT8 Tensor Core 规格较高，但在内存受限的 Decode 阶段优势不明显。

## Corrected Claim

L40S (Ada Lovelace) 在 INT8 量化下的 Decode 阶段吞吐量受限于其 864 GB/s 的显存带宽（低于 A6000 的 960 GB/s），尽管其 Tensor Core 规格较高，但在内存受限的 Decode 阶段优势不明显。具体吞吐量取决于模型架构和序列长度，通常低于同代高端卡。

## Evidence

[质询]该陈述包含具体的实测性能数值（18-22 tokens/s）和硬件规格对比，属于经验事实。在缺乏任何参考来源支持的情况下，无法验证该具体吞吐量数值是否准确，且不同模型架构（如LLaMA vs Mistral）在相同硬件上的Decode速度差异巨大，仅凭硬件带宽推导具体Token/s存在较大不确定性。 | 经验事实，逻辑自洽但缺来源支持。虽然864 GB/s带宽低于A6000的960 GB/s符合硬件常识，且Decode阶段受内存带宽限制符合LLM推理原理，但具体的18-22 tokens/s吞吐量属于特定模型和配置下的经验数据，无来源佐证，故降级。

## Search Query

NVIDIA L40S INT8 inference throughput tokens/s benchmark LLM decode
