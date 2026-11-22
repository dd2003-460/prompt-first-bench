# N85: Batch Size 对 Decode 吞吐的影响：由于权重加载是共享的，Batch Size 增加时，每 token 的权重读取成本被分摊，吞吐近似线性增加直

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N17

## Claim

Batch Size 对 Decode 吞吐的影响：由于权重加载是共享的，Batch Size 增加时，每 token 的权重读取成本被分摊，吞吐近似线性增加直到 KV Cache 显存或带宽成为瓶颈；RTX 4090 在 32K 上下文下，最大 Batch Size 约为 (24GB - 54GB*0 - 1.6GB*Batch - 10% overhead) / (1.6GB + weights_per_batch)，需计算具体上限

## Corrected Claim

Batch Size 对 Decode 吞吐的影响：由于权重加载是共享的，Batch Size 增加时，每 token 的权重读取成本被分摊，吞吐通常随 Batch Size 增加而提升，直到 KV Cache 显存或带宽成为瓶颈；RTX 4090 在 32K 上下文下，最大 Batch Size 受限于可用显存（总显存减去模型权重、KV Cache 及系统开销），具体上限需根据实际模型大小和精度计算。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点逻辑链条清晰且正交：节点1修正了KV Cache计算基础（关键前提），节点2和3分别针对BF16和W4精度进行了显存预算与Batch Size上限的独立推导（互斥场景，无矛盾），节点4基于节点3的结论（BS=1上限）分析了吞吐特性。虽然节点2和3结构相似，但分别对应不同的量化方案（BF16不可行 vs W4可行），属于必要的情景分析而非简单冗余。父节点中提到的'线性增加'在子节点4中被正确修正为'受限于BS=1故无线性空间'，覆盖了所有关键方面。）

## Search Query

LLM batch size impact decode throughput memory bandwidth
