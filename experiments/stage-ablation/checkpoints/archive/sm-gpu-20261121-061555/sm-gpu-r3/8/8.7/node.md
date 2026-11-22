# N129: AMD RX 7900 XTX 与 NVIDIA RTX 4090 在 27B 模型 BF16/FP8 推理下的实测吞吐量对比数据（tokens/s），需排除软

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N35, N36, N37

## Claim

AMD RX 7900 XTX 与 NVIDIA RTX 4090 在 27B 模型 BF16/FP8 推理下的实测吞吐量对比数据（tokens/s），需排除软件栈（CUDA vs ROCm）优化差异，仅保留硬件架构（HBM vs GDDR, Tensor Core vs Matrix Core）带来的性能差，作为 N37 中'低 15-25%'断言的实证依据。

## Corrected Claim

AMD RX 7900 XTX 与 NVIDIA RTX 4090 在 27B 模型 BF16/FP8 推理下的实测吞吐量存在差异，具体数值需参考特定测试环境下的基准测试报告，通常受软件栈优化程度显著影响，难以仅凭硬件架构得出固定的 15-25% 性能差断言。

## Evidence

[质询]该陈述要求提供具体的实测吞吐量数据（tokens/s）并排除软件栈影响，这属于高度依赖具体测试环境、驱动版本和模型实现的经验事实，且不同来源数据差异巨大，无法通过第一性原理推导得出唯一确定的数值或固定百分比区间。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且该数据为具体硬件实测值，非第一性原理可推导范畴）

## Search Query

RX 7900 XTX vs RTX 4090 LLM inference throughput benchmark 27B tokens per second
