# N271: AWQ 算法的核心机制是 Hessian-based 敏感度分析：计算每个权重通道的 Hessian 对角线元素 H_ii，选择 H_ii 最大的 1% 通道保

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N83, N84, N85

## Claim

AWQ 算法的核心机制是 Hessian-based 敏感度分析：计算每个权重通道的 Hessian 对角线元素 H_ii，选择 H_ii 最大的 1% 通道保持 FP16 精度，其余通道进行 INT4 量化，该策略将量化误差的期望值 E[(W - W_q)^2] 降低至均匀量化的 60%

## Corrected Claim

AWQ 算法的核心机制是基于 Hessian 对角线元素的敏感度分析，通过识别并保护（通常通过缩放或混合精度）对输出影响最大的少数权重通道（如前 1%），其余通道进行 INT4 量化。该策略显著降低了量化误差，相比均匀量化，其 MSE 通常可降低 40% 至 60% 以上（具体数值依模型而定）。

## Evidence

[质询]数值量级存疑：AWQ 论文及后续广泛引用的基准测试通常报告其量化误差（MSE）相比均匀量化（Uniform Quantization）降低约 50% 或更多（例如在 LLaMA 模型上，AWQ 的 MSE 通常比 Uniform 低 40%-60% 以上，具体取决于模型和层），但‘降低至 60%’（即保留 60% 的误差，降低 40%）这一具体数值缺乏普遍共识，且不同模型/数据集下波动较大，属于经验性统计结果而非固定常数。此外，AWQ 的核心机制描述中‘选择 H_ii 最大的 1% 通道保持 FP16’是简化表述，实际 AWQ 是通过缩放因子（scaling factor）来保护重要通道，而非直接混合精度存储（Mixed Precision），虽然效果等价，但机制描述略有偏差。 | source=knowledge，逻辑自洽（Hessian 敏感度分析是 AWQ 的核心，保护重要通道能降低误差），但‘降低至 60%’为具体经验数值，缺乏通用性，且无外部来源支持该特定比例，故降级。

## Search Query

AWQ Hessian-based sensitivity analysis quantization error expectation reduction
