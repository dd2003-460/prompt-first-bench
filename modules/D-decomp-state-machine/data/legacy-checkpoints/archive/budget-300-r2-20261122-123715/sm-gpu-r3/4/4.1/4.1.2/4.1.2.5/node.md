# N296: 工作点 B (中等保真/性价比最优)：FP8 精度下，VRAM_Required ≈ 47.5GB (权重27GB + KV 18GB + 激活2.5GB)，需

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N85, N86, N87

## Claim

工作点 B (中等保真/性价比最优)：FP8 精度下，VRAM_Required ≈ 47.5GB (权重27GB + KV 18GB + 激活2.5GB)，需选择显存 ≥48GB 的硬件（如 1x L40S 48GB 或 1x RTX 4090 24GB+CPU Offload 不可行，故排除 24GB 单卡），此工作点在质量损失可接受范围内平衡了硬件成本。

## Corrected Claim

工作点 B (中等保真/性价比最优)：在特定模型配置下，FP8 精度所需 VRAM 约为 47.5GB，需选择显存 ≥48GB 的硬件（如 1x L40S 48GB），24GB 单卡因显存不足被排除。

## Evidence

[质询]VRAM 数值（47.5GB）为特定模型配置下的经验估算值，缺乏通用性；且‘性价比最优’属于主观经济判断，无法仅凭逻辑推导得出，属于经验事实。 | 经验事实，逻辑自洽但缺来源支持
