# N134: RTX 5090 (1792 GB/s) 与 H100 SXM (3.35 TB/s) 的显存带宽比值为 1:1.87，在 32K 上下文 Decode 阶段，

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N32, N33, N34

## Claim

RTX 5090 (1792 GB/s) 与 H100 SXM (3.35 TB/s) 的显存带宽比值为 1:1.87，在 32K 上下文 Decode 阶段，RTX 5090 的 tokens/s 吞吐量理论上约为 H100 的 55%-65% [待核验]，需考虑 CUDA 核心效率差异。

## Corrected Claim

RTX 5090 (1792 GB/s) 与 H100 SXM (3.35 TB/s) 的显存带宽比值为 1:1.87。在 32K 上下文 Decode 阶段，受限于显存带宽，RTX 5090 的 tokens/s 吞吐量理论上显著低于 H100，具体比例取决于模型架构、Batch Size 及计算/访存平衡，通常低于带宽比值的线性预测，需实测验证。

## Evidence

[质询]该陈述将显存带宽比值（1:1.87）直接线性映射为吞吐量比值（55%-65%），忽略了Decode阶段中计算密度（Compute-bound vs Memory-bound）的差异。H100作为数据中心卡，其FP16/BF16计算能力远超RTX 5090，且拥有更高效的Tensor Core和更高的算术强度容忍度。在32K长上下文Decode中，虽然显存带宽是瓶颈，但H100的更高计算效率可能使其在单位带宽下的有效吞吐率高于RTX 5090，或者反之，RTX 5090的更高时钟频率和更低的延迟可能在特定小Batch Decode中表现优于纯带宽比例预测。此外，55%-65%这一具体数值范围缺乏明确的基准测试或理论模型支撑，属于经验性估算，且未考虑H100 SXM的高功耗散热限制对持续性能的影响。 | 先验知识/题面给定，逻辑校验通过。显存带宽比值计算正确（3.35/1.792 ≈ 1.87）。但吞吐量比值55%-65%是基于带宽的线性外推，未充分计入计算效率差异，属于经验事实且缺乏来源支持，故降级。

## Search Query

RTX 5090 vs H100 LLM decode throughput memory bandwidth ratio
