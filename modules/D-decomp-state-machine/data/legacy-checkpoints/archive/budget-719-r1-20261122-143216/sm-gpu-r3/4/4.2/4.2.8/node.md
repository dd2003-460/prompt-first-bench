# N105: Qwen3-27B 在 32K 上下文长度下 NVFP4/W4 量化导致的精度崩溃风险，需验证 NVFP4/W4 精度下长上下文推理的稳定性，预期存在精度崩溃风

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N22

## Claim

Qwen3-27B 在 32K 上下文长度下 NVFP4/W4 量化导致的精度崩溃风险，需验证 NVFP4/W4 精度下长上下文推理的稳定性，预期存在精度崩溃风险

## Corrected Claim

Qwen3-27B 在 32K 上下文长度下使用 NVFP4/W4 量化时，存在精度下降的风险，需验证长上下文推理的稳定性，具体性能衰减程度需通过基准测试确认。

## Evidence

[质询]该陈述断言存在“精度崩溃风险”，属于具体的经验性技术结论。虽然低比特量化（如NVFP4/W4）在长上下文下确实可能因累积误差导致性能下降，但“崩溃”一词暗示了灾难性的失效，这取决于具体的模型架构、量化算法（如是否使用GPTQ/AWQ等校准）以及任务类型。缺乏具体实验数据支持“崩溃”这一极端后果，可能仅为性能显著下降而非完全不可用。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且该具体风险程度无法从第一性原理严格推出，属于需实验验证的工程经验）。

## Search Query

Qwen3-27B NVFP4 W4 precision collapse 32K context
