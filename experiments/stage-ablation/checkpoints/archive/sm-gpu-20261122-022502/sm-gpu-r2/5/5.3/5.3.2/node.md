# N79: 1×RTX 4090 采用 INT8 量化时，显存占用 ~27GB+KV Cache，吞吐量 35-40 tokens/s，TCO/Throughput 为 $

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N27

## Claim

1×RTX 4090 采用 INT8 量化时，显存占用 ~27GB+KV Cache，吞吐量 35-40 tokens/s，TCO/Throughput 为 $0.009-$0.011/token，MMLU 准确率下降 ~1.0-1.5%，在 2% 阈值内，是量化方案中精度与性能的最优平衡点，适用于预算极低但需保持通用推理能力的场景。

## Corrected Claim

1×RTX 4090 采用 INT8 量化时，通常能显著降低显存占用并提升吞吐量（具体数值依模型规模与配置而异，常见场景下吞吐量可达数十 tokens/s），TCO 具有竞争力，MMLU 准确率下降通常在 1-2% 左右，是精度与性能的良好平衡点，适用于预算受限且需保持通用推理能力的场景。

## Evidence

[质询]该陈述包含大量具体的经验性数值（显存占用、吞吐量、TCO、MMLU下降幅度），这些参数高度依赖于具体的模型大小（如7B/13B/70B）、上下文长度、硬件驱动版本及量化算法（如GPTQ/AWQ），且不同来源的数据波动较大，无法仅凭逻辑推导得出唯一确定的数值区间，存在将特定测试环境数据泛化为通用事实的风险。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且具体性能指标与成本数据属于经验参数，无法从第一性原理严格推出，故降级）

## Search Query

Qwen3 27B INT8 quantization MMLU accuracy RTX 4090 throughput
