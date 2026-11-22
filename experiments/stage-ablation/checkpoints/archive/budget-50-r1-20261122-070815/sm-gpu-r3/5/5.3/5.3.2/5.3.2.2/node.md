# N355: Qwen3-27B 在 RTX 4090 (Ada) 上运行 INT4 (AWQ/GPTQ) 精度时，Batch Size=1 的实测单 token 生成吞吐量

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N126

## Claim

Qwen3-27B 在 RTX 4090 (Ada) 上运行 INT4 (AWQ/GPTQ) 精度时，Batch Size=1 的实测单 token 生成吞吐量（tokens/s）及 TTFT (ms) 具体数值，需对比 BF16 基线以量化量化带来的速度增益（通常 1.5-2x）。

## Corrected Claim

Qwen3-27B 在 RTX 4090 上运行 INT4 (AWQ/GPTQ) 精度时，Batch Size=1 的单 token 生成吞吐量通常显著高于 BF16 基线，速度增益一般在 1.5-2x 范围内，具体 tokens/s 及 TTFT 数值需依据特定软件栈实测确定。

## Evidence

[质询]该陈述要求提供具体的实测数值（tokens/s 及 TTFT ms），但参考来源为空，无法验证具体数值；且不同硬件驱动、CUDA版本及具体量化实现（AWQ vs GPTQ）会导致数值波动，缺乏具体上下文下的唯一确定值。 | 经验事实，逻辑自洽但缺来源支持。INT4量化通常带来1.5-2x的速度增益符合硬件带宽瓶颈下的理论预期，但具体实测数值无来源佐证。

## Search Query

Qwen3-27B INT4 AWQ benchmark RTX 4090 batch size 1 throughput
