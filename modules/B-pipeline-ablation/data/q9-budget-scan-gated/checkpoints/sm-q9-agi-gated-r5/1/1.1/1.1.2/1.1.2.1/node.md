# N35: TP=4模式下，Decode阶段每token需从HBM读取的权重数据量为13.5GB/4=3.375GB。在900GB/s带宽下，单卡权重加载耗时为3.375/

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N19

## Claim

TP=4模式下，Decode阶段每token需从HBM读取的权重数据量为13.5GB/4=3.375GB。在900GB/s带宽下，单卡权重加载耗时为3.375/900=3.75ms，理论单卡decode吞吐上限为1/0.00375≈267 tok/s（非N19声称的67 tok/s）。

## Corrected Claim

TP=4模式下，Decode阶段每token需从HBM读取的权重数据量为13.5GB/4=3.375GB。在900GB/s带宽下，单卡权重加载耗时为3.375/900=3.75ms，理论单卡decode吞吐上限为1/0.00375≈267 tok/s（非N19声称的67 tok/s）。

## Evidence

先验知识/题面给定，逻辑校验通过：算术运算正确（13.5/4=3.375, 3.375/900=0.00375s, 1/0.00375≈266.7），符合内存带宽瓶颈下的理论吞吐计算逻辑。
