# N97: 降低TP度至TP=2对长上下文通信瓶颈的缓解效果量化：TP=2时，AllReduce通信量减半（因hidden_dim切分），但单卡权重读取量翻倍（3.375G

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N44

## Claim

降低TP度至TP=2对长上下文通信瓶颈的缓解效果量化：TP=2时，AllReduce通信量减半（因hidden_dim切分），但单卡权重读取量翻倍（3.375GB -> 6.75GB），需计算TP=2下的新decode步时间与通信延迟占比，判断是否优于TP=4

## Corrected Claim

降低TP度至TP=2对长上下文通信瓶颈的缓解效果量化：TP=2时，AllReduce通信量减半（因hidden_dim切分），但单卡权重读取量翻倍（3.375GB -> 6.75GB），需计算TP=2下的新decode步时间与通信延迟占比，判断是否优于TP=4

## Evidence

先验知识/题面给定，逻辑校验通过：TP=2相比TP=4，AllReduce通信量确实减半（数据量与TP成反比），单卡权重读取量翻倍（总权重不变，卡数减半），符合分布式推理基本原理。
