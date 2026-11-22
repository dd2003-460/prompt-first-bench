# N85: Batch Size 对 Decode 吞吐的影响：由于权重加载是共享的，Batch Size 增加时，每 token 的权重读取成本被分摊，吞吐近似线性增加直

- **status**: degraded
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

[质询]公式中的数值参数（如1.6GB、54GB*0）缺乏具体模型上下文，且'54GB*0'表述冗余或暗示特定模型（如7B/13B量化版）但未明确，导致公式无法直接验证其普适性或具体数值准确性；此外，'近似线性增加'在接近显存瓶颈时通常会出现非线性下降，表述略显绝对。 | 先验知识/题面给定，逻辑校验通过：Batch Size增加分摊权重读取成本是LLM推理的基本原理，显存计算公式结构合理（总显存-权重-激活-Overhead），但具体数值依赖未指定的模型配置，故降级为定性表述。

## Search Query

LLM batch size impact decode throughput memory bandwidth
