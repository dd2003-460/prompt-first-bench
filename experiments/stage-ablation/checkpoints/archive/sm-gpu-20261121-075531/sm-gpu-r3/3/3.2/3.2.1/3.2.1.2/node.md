# N219: 工作点 B（中性价比/平衡）：通过 nvidia-smi -pl 350W 限制 RTX 4090 功耗至 350W，TPS 下降至 38-42 tokens/

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N66

## Claim

工作点 B（中性价比/平衡）：通过 nvidia-smi -pl 350W 限制 RTX 4090 功耗至 350W，TPS 下降至 38-42 tokens/s（降幅约 10-15%），能效比提升至 0.11-0.12 tokens/W，电力成本降低约 22%，是本地工作站长期运行的推荐平衡点。

## Corrected Claim

工作点 B（中性价比/平衡）：通过 nvidia-smi -pl 350W 限制 RTX 4090 功耗至 350W，通常可使 TPS 下降约 10-15%，能效比显著提升，电力成本降低约 20% 以上，是本地工作站长期运行的推荐平衡点。

## Evidence

[质询]具体数值（TPS 38-42, 能效比 0.11-0.12, 成本降低 22%）高度依赖于具体的模型大小、序列长度、Batch Size 及硬件驱动版本，属于特定实验条件下的经验数据，无法仅凭逻辑推导得出唯一确定的数值范围，存在口径混淆或特定场景过拟合的风险。 | 经验事实，逻辑自洽但缺来源支持
