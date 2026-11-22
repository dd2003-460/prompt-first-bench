# N247: A6000 (Ada Lovelace) 在 INT8 量化下的实测 Token 生成吞吐量（Decode 阶段，batch_size=1, seq_len=3

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N91, N92, N93

## Claim

A6000 (Ada Lovelace) 在 INT8 量化下的实测 Token 生成吞吐量（Decode 阶段，batch_size=1, seq_len=32K）约为 12-15 tokens/s，显著低于基于纯显存带宽计算的 26.3 tokens/s 理论上限，主要受限于 Ada 架构在长序列 Attention 计算上的 Tensor Core 利用率瓶颈。

## Corrected Claim

A6000 (Ada Lovelace) 在 INT8 量化下的实测 Token 生成吞吐量（Decode 阶段，batch_size=1, seq_len=32K）通常低于基于纯显存带宽计算的 26.3 tokens/s 理论上限，具体数值受 Attention 计算效率及 Tensor Core 利用率影响，需实测确认。

## Evidence

[质询]该陈述包含具体的实测性能数值（12-15 tokens/s）和特定的硬件瓶颈归因（Tensor Core利用率），属于经验事实。在缺乏任何参考来源支持的情况下，无法验证具体数值的准确性，且'显著低于'的幅度及具体瓶颈原因可能因驱动版本、具体模型架构（如是否使用FlashAttention）及量化实现细节而异，存在口径混淆或特定环境偏差的风险。 | 经验事实，逻辑自洽但缺来源支持（本轮检索无可用来源）。

## Search Query

NVIDIA A6000 INT8 inference throughput tokens/s benchmark Qwen 27B
