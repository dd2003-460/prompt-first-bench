# N384: RTX A5000 24GB 在 32K 上下文、BF16 精度下，理论 Prefill 吞吐量上限为 (31.2 TFLOPS * 1e12) / (2 * 

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N129

## Claim

RTX A5000 24GB 在 32K 上下文、BF16 精度下，理论 Prefill 吞吐量上限为 (31.2 TFLOPS * 1e12) / (2 * 27e9 * 32768) ≈ 17.7 tokens/s (假设 31.2 TFLOPS 为 BF16 稠密算力，需核验)。

## Corrected Claim

RTX A5000 24GB 在 32K 上下文、BF16 精度下，若假设 31.2 TFLOPS 为 BF16 稠密算力且模型参数量为 27B，理论 Prefill 吞吐量上限约为 17.7 tokens/s（需核验硬件参数和模型规模）。

## Evidence

[质询]该陈述依赖于RTX A5000的具体硬件参数（31.2 TFLOPS BF16算力、27B模型参数量），属于经验事实。虽然数学计算逻辑正确，但缺乏外部来源直接支持这些具体数值，且RTX A5000的BF16峰值算力通常标称为31.2 TFLOPS（稠密），但实际Prefill吞吐量受内存带宽、架构效率等影响，理论上限计算需明确假设条件。 | 经验事实，逻辑自洽但缺来源支持。数学推导：(31.2e12) / (2 * 27e9 * 32768) ≈ 17.7 tokens/s，计算无误，但硬件参数和模型规模需外部验证。

## Search Query

RTX A5000 BF16 tensor FLOPS performance
