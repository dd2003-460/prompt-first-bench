# N128: 对象更新率 $u=1\%/day$ 下，LFU 计数器失效导致的命中率损失不仅来自失效概率 $P_{lfu\_invalidate}$，还来自失效后的重新学习成

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N57, N58, N59

## Claim

对象更新率 $u=1\%/day$ 下，LFU 计数器失效导致的命中率损失不仅来自失效概率 $P_{lfu\_invalidate}$，还来自失效后的重新学习成本：每次失效需 $N_{learn}$ 次请求才能重建频率计数，$N_{learn} \approx 1/\lambda_i$（对象 $i$ 的平均请求间隔）；对于热门对象（$\lambda_i$ 高），$N_{learn}$ 极小（<1 秒），损失可忽略；对于冷门对象（$\lambda_i$ 低），$N_{learn}$ 大，但字节占比低，需量化 $\Delta H_{relearn} = \sum_{i \in invalid} (N_{learn,i} \cdot S_i \cdot \lambda_i) / R_{byte}$，该值通常小于 $P_{lfu\_invalidate} \cdot (S_{hot}/S_{total})$ 的 10%。

## Corrected Claim

对象更新率 $u=1\%/day$ 下，LFU 计数器失效导致的命中率损失不仅来自失效概率 $P_{lfu\_invalidate}$，还来自失效后的重新学习成本：每次失效需 $N_{learn}$ 次请求才能重建频率计数，$N_{learn} \approx 1/\lambda_i$（对象 $i$ 的平均请求间隔）；对于热门对象（$\lambda_i$ 高），$N_{learn}$ 极小（<1 秒），损失可忽略；对于冷门对象（$\lambda_i$ 低），$N_{learn}$ 大，但字节占比低，需量化 $\Delta H_{relearn} = \sum_{i \in invalid} (N_{learn,i} \cdot S_i \cdot \lambda_i) / R_{byte}$，该值通常小于 $P_{lfu\_invalidate} \cdot (S_{hot}/S_{total})$ 的 10%。

## Evidence

先验知识/题面给定，逻辑校验通过
