# N52: FP8 (E4M3) 量化工作点（中性价比最优）：显存需求 ≈ 27GB (权重) + 6GB (KV, 若 KV 也 FP8) + 2GB ≈ 35GB。质量

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N12

## Claim

FP8 (E4M3) 量化工作点（中性价比最优）：显存需求 ≈ 27GB (权重) + 6GB (KV, 若 KV 也 FP8) + 2GB ≈ 35GB。质量损失预计 0.5-1.0% (MMLU)。可行硬件：1x RTX 4090 (24GB 不足，需 KV offload 或更激进量化) 或 1x L40S (48GB 充足) 或 2x RTX 4090 (48GB 充足)。

## Corrected Claim

FP8 (E4M3) 量化通常能显著降低显存需求（约为FP16的一半），具体数值取决于模型规模（例如7B模型权重约需4-5GB，而非27GB，除非是更大模型）。质量损失通常在可接受范围内（MMLU下降<1-2%）。硬件可行性方面，24GB显存（如RTX 4090）对于中等规模模型（如7B-13B）通常足够，而48GB显存（如L40S或双4090）可支持更大模型或更长上下文。

## Evidence

[质询]显存需求的具体数值（27GB权重、6GB KV、2GB其他）高度依赖于未指定的模型参数量（如7B/13B/70B）和序列长度，缺乏上下文导致数值无法验证；此外，FP8 E4M3在MMLU上的质量损失0.5-1.0%属于经验性估计，不同模型和量化策略下波动较大，缺乏通用性。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且具体数值依赖未给定的模型规模参数，无法从第一性原理严格推出）。

## Search Query

Qwen3 FP8 quantization accuracy loss MMLU benchmark
