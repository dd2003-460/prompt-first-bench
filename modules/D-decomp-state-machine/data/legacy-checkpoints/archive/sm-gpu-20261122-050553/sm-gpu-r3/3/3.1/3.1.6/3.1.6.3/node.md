# N212: 未使用 SmoothQuant 的直接对称 INT8 量化在 Qwen3-27B 上的理论精度上限：由于激活值中的离群值 (outliers) 占据 scale

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N68

## Claim

未使用 SmoothQuant 的直接对称 INT8 量化在 Qwen3-27B 上的理论精度上限：由于激活值中的离群值 (outliers) 占据 scale 的主要范围，导致正常值量化步长过大，理论最大信噪比 SNR_max = 6.02 * effective_bits + 1.76 dB，若 effective_bits=6.5，则 SNR_max ≈ 41dB，对应 MSE 增加约 40% 相对于 BF16。

## Corrected Claim

未使用 SmoothQuant 的直接对称 INT8 量化在 Qwen3-27B 上，由于激活值离群值导致量化步长增大，有效量化位数降低（例如降至 6.5 位左右），导致量化噪声显著增加，使得模型精度相对于 BF16 出现明显下降（具体 MSE 增加比例取决于信号能量分布，通常表现为困惑度或下游任务指标恶化，而非简单的 40% MSE 增加）。

## Evidence

[质询]数值量级与因果归因存在严重偏差：1. 41dB 的 SNR 对应 MSE 增加约 40% 在数学上成立（10^(41/10)≈12590倍噪声功率，若原信号功率极小或此处指相对误差），但通常 41dB SNR 意味着极高的保真度（误差约 0.8%），这与“精度上限低”的定性描述矛盾，且 40% 的 MSE 增加通常对应约 4dB 的 SNR 损失（即 SNR 从 ~46dB 降至 ~42dB），而非 SNR 本身为 41dB 导致 40% 误差。2. 将“未使用 SmoothQuant”直接等同于“effective_bits=6.5”缺乏普适性，该比特数高度依赖于具体激活分布和量化策略，属于特定实验结果而非理论上限。 | 先验知识/题面给定，逻辑校验发现 SNR 与 MSE 增加的对应关系描述存在混淆（41dB SNR 本身代表高信噪比，而非导致 40% 误差的直接原因，40% 误差通常源于量化噪声功率相对于信号功率的比例，需结合具体信号能量计算，且 6.5 有效位是经验值而非理论推导出的固定上限），故降级。
