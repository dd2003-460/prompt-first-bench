# N51: 多卡推理的并行策略分类：Tensor Parallelism (TP) 涉及每层激活值和中间结果的跨卡同步，通信量 = 2 × seq_len × hidden

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N8, N9, N10

## Claim

多卡推理的并行策略分类：Tensor Parallelism (TP) 涉及每层激活值和中间结果的跨卡同步，通信量 = 2 × seq_len × hidden_size × batch_size × dtype_bytes；Pipeline Parallelism (PP) 仅涉及层间激活值传递，通信量较小但存在流水线气泡。

## Corrected Claim

多卡推理的并行策略分类：Tensor Parallelism (TP) 涉及每层激活值和中间结果的跨卡同步，通信量 = 2 × seq_len × hidden_size × batch_size × dtype_bytes；Pipeline Parallelism (PP) 仅涉及层间激活值传递，通信量较小但存在流水线气泡。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

Tensor Parallelism vs Pipeline Parallelism communication overhead LLM inference
