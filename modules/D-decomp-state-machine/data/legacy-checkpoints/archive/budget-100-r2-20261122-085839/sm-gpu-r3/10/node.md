# N31: 最终推荐的条件性边界：若预算 < $3,000 且接受W4量化（质量损失可接受），推荐 2× RTX 3090/4090 (PCIe互联)，总显存48GB，满足

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

最终推荐的条件性边界：若预算 < $3,000 且接受W4量化（质量损失可接受），推荐 2× RTX 3090/4090 (PCIe互联)，总显存48GB，满足W4+32K KV Cache需求，性价比最高但延迟较高。若预算 $5,000-$8,000 且追求INT8精度（质量损失较小），推荐 1× A6000 Ada 48GB (单卡无互联瓶颈) 或 2× RTX 4090 (若框架支持高效PCIe TP)。若预算 > $10,000 且追求BF16原生精度或最高吞吐，推荐 1× A100/H100 80GB。任何排名必须在指定精度和并发数（Batch Size）下成立。

## Corrected Claim

最终推荐的条件性边界：若预算 < $3,000 且接受W4量化（质量损失可接受），推荐 2× RTX 3090/4090 (PCIe互联)，总显存48GB，满足W4+32K KV Cache需求，性价比最高但延迟较高。若预算 $5,000-$8,000 且追求INT8精度（质量损失较小），推荐 1× A6000 Ada 48GB (单卡无互联瓶颈) 或 2× RTX 4090 (若框架支持高效PCIe TP)。若预算 > $10,000 且追求BF16原生精度或最高吞吐，推荐 1× A100/H100 80GB。任何排名必须在指定精度和并发数（Batch Size）下成立。

## Evidence

检索失败: no sources from any channel (all 5 failed)
