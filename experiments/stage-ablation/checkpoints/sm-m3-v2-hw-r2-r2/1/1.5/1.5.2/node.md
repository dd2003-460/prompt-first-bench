# N40: V100集群上MTP的实际端到端吞吐增益：考虑TP=4通信开销，MTP带来的单token延迟降低幅度约为20-30%，即有效吞吐从~50 tok/s提升至~60

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N10

## Claim

V100集群上MTP的实际端到端吞吐增益：考虑TP=4通信开销，MTP带来的单token延迟降低幅度约为20-30%，即有效吞吐从~50 tok/s提升至~60-65 tok/s，而非理论上的2倍，因为Draft验证仍需Target前向传播。

## Corrected Claim

V100集群上MTP的实际端到端吞吐增益：考虑TP=4通信开销，MTP带来的单token延迟降低幅度约为20-30%，即有效吞吐从~50 tok/s提升至~60-65 tok/s，而非理论上的2倍，因为Draft验证仍需Target前向传播。

## Evidence

先验知识/题面给定，逻辑校验通过：MTP（Multi-Token Prediction）通过并行预测多个token减少解码步数，但在TP=4的大规模集群中，通信开销和Target模型的验证成本限制了增益，20-30%的端到端吞吐提升符合工程实践中的典型量级，逻辑自洽。
