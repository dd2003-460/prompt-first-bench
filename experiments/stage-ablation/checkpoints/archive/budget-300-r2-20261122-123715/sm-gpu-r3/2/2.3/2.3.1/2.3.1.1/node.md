# N215: RTX 4090 的 FP8 Tensor Core 吞吐量 330 TOPS 是基于稀疏性 (Sparsity) 关闭状态下的理论峰值；在 vLLM 实际推理

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N60

## Claim

RTX 4090 的 FP8 Tensor Core 吞吐量 330 TOPS 是基于稀疏性 (Sparsity) 关闭状态下的理论峰值；在 vLLM 实际推理中，由于 Attention 算子无法完全利用 Tensor Core 的 FP8 路径，有效 FP8 吞吐量通常仅为理论值的 60-70%，即 ~200-230 TOPS [待核验]。

## Corrected Claim

RTX 4090 的 FP8 Tensor Core 理论峰值吞吐量为 330 TOPS（稀疏关闭）。在 vLLM 实际推理中，受限于内存带宽、Kernel 启动开销及算子融合效率等因素，有效 FP8 计算吞吐量通常显著低于理论峰值，具体效率取决于模型架构、序列长度及 Batch Size，一般经验值在 50%-80% 之间波动，而非固定由 Attention 算子决定。

## Evidence

[质询]将‘Attention算子无法完全利用FP8路径’作为导致整体吞吐量仅60-70%的主要原因存在逻辑归因偏差。在vLLM等现代推理框架中，Attention通常由FlashAttention等高度优化的CUDA内核处理，其瓶颈往往在于内存带宽而非Tensor Core计算能力；且FP8加速主要作用于GEMM（矩阵乘法）部分，Attention部分的计算占比及具体瓶颈机制因模型架构和序列长度而异，不能简单断言Attention是限制FP8有效吞吐至60-70%的核心原因。此外，60-70%的效率范围缺乏统一的基准测试支持，实际效率受batch size、序列长度、硬件配置等多重因素影响，波动范围可能更大。 | 先验知识/题面给定，逻辑校验通过。虽然数值量级（60-70%效率）在工程实践中属于合理范围（GPU实际利用率通常低于理论峰值），但归因于‘Attention算子’不够严谨，且缺乏具体来源支持该特定百分比区间。根据source=knowledge规则，逻辑自洽本可判verified，但因第一步反方质询指出了归因逻辑的潜在缺陷（将整体效率下降主要归因于Attention的FP8路径限制，而忽略了内存带宽、kernel launch overhead等其他更主要因素），该攻击点成立且无法完全排除，故降档为degraded。

## Search Query

RTX 4090 FP8 effective throughput vLLM tensor core utilization
