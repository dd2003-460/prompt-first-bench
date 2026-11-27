# N259: SmoothQuant 算法中平滑因子 s 的最优值需通过最小化激活值离群程度与权重分布平滑度的加权损失确定，对于 Qwen3-27B，实证最优 s 值通常在 

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N81

## Claim

SmoothQuant 算法中平滑因子 s 的最优值需通过最小化激活值离群程度与权重分布平滑度的加权损失确定，对于 Qwen3-27B，实证最优 s 值通常在 0.5-1.5 区间，s=1.0 时 WikiText-103 PPL 增量最小（约 0.12），s 偏离最优值每 0.1 单位，PPL 增量增加约 0.03（二次函数关系）。

## Corrected Claim

SmoothQuant 算法中平滑因子 s 的最优值需通过平衡激活值离群程度与权重分布平滑度确定。对于大语言模型（如 Qwen 系列），实证最优 s 值通常位于 0.5-1.5 区间，s=1.0 常为较优选择，但具体 PPL 增量及敏感度需根据特定模型和数据集实测确定。

## Evidence

[质询]该陈述包含极其具体的经验参数（Qwen3-27B 的特定 PPL 增量数值 0.12、0.03 及二次函数关系），属于典型的经验事实。在缺乏任何检索来源支持的情况下，这些具体数值无法通过第一性原理推导，且不同模型、不同数据集下的平滑因子最优值及敏感度差异巨大，直接断言具体数值存在极高的幻觉风险。 | 经验事实，逻辑自洽但缺来源支持（检索失败，无外部证据验证具体数值）

## Search Query

SmoothQuant Qwen3-27B optimal smoothing factor s PPL sensitivity
