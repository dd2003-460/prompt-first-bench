# N21: TP=1 配置下单卡剩余可用显存为 16GB - 6.94GB(权重) - 2.1GB(激活) = 6.96 GB，远高于 TP=4 配置下的单卡剩余 2.5 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N7

## Claim

TP=1 配置下单卡剩余可用显存为 16GB - 6.94GB(权重) - 2.1GB(激活) = 6.96 GB，远高于 TP=4 配置下的单卡剩余 2.5 GB，支持更长的上下文窗口而不触发 KV Cache 驱逐。

## Corrected Claim

TP=1 配置下单卡剩余可用显存为 16GB - 6.94GB(权重) - 2.1GB(激活) = 6.96 GB，远高于 TP=4 配置下的单卡剩余 2.5 GB，支持更长的上下文窗口而不触发 KV Cache 驱逐。

## Evidence

先验知识/题面给定，逻辑校验通过：算术运算正确（16-6.94-2.1=6.96），且TP=1相比TP=4通常能保留更多单卡显存用于KV Cache，符合大模型推理显存分配的基本逻辑。
