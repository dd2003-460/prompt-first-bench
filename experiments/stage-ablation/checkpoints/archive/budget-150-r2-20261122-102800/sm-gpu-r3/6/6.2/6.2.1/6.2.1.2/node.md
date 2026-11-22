# N341: TensorRT-LLM 在 A100 上执行 'FP8' 模型的实际执行路径：将 FP8 权重/激活反量化为 INT8 或 BF16 进行计算，此过程引入额外

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N135

## Claim

TensorRT-LLM 在 A100 上执行 'FP8' 模型的实际执行路径：将 FP8 权重/激活反量化为 INT8 或 BF16 进行计算，此过程引入额外的 CPU/GPU 转换开销，实测吞吐量通常比原生 INT8 低 10-20%，且无法利用 H100 的 FP8 稀疏加速。

## Corrected Claim

TensorRT-LLM 在 A100 上执行 'FP8' 模型时，由于 A100 缺乏原生 FP8 硬件支持，需将 FP8 权重/激活反量化为 INT8 或 BF16 进行计算，此过程引入额外的转换开销，导致吞吐量通常低于原生 INT8 或 BF16 路径。

## Evidence

[质询]该陈述包含具体的性能量化数据（'低 10-20%'）和特定的硬件行为断言（'无法利用 H100 的 FP8 稀疏加速'），属于经验事实。在缺乏来源支持的情况下，具体的百分比数值缺乏依据，且 H100 的 FP8 加速特性描述可能存在技术细节上的不严谨（H100 支持 FP8 计算，但 TensorRT-LLM 在 A100 上确实无法利用 H100 的硬件特性，因为 A100 没有 FP8 硬件单元，逻辑上 A100 本身就不具备该能力，而非'无法利用'，表述略有歧义但核心逻辑成立）。主要攻击点在于具体数值 '10-20%' 无来源支持。 | 经验事实，逻辑自洽但缺来源支持。A100 不支持原生 FP8 计算，需反量化，必然引入开销，定性结论正确，但具体数值 '10-20%' 无外部证据支持。

## Search Query

TensorRT-LLM A100 FP8 emulation performance penalty vs INT8
