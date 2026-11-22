# N33: 32K上下文KV Cache在BF16下的确切显存占用为 192MB (32,768 tokens * 2 bytes/token * 2 (K+V) * 1.

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N6

## Claim

32K上下文KV Cache在BF16下的确切显存占用为 192MB (32,768 tokens * 2 bytes/token * 2 (K+V) * 1.0 (Qwen3-27B标准KV头数/维度估算)，注：若考虑GQA/MQA或具体层数，需按 2 * layers * kv_heads * head_dim * 2 bytes 计算，Qwen3-27B具体层数与KV头数需查模型config.json [待核验]，但即使按保守估计，KV Cache仅占显存极小部分，主要瓶颈是权重)

## Corrected Claim

32K上下文KV Cache在BF16下的显存占用约为 8GB (估算值，具体取决于 Qwen3-27B 的层数和 KV 头数配置，公式为 2 * layers * kv_heads * head_dim * 32768 * 2 bytes)。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别提供了计算KV Cache所需的三个独立超参数（层数、KV头数、Head Dim）以及基于这些参数的最终计算结果。这四个子节点在逻辑上是正交的（前三个是输入参数，第四个是推导结论），没有重复或矛盾。它们共同覆盖了父节点中提到的‘需查config.json’的具体参数缺失问题，并纠正了父节点中192MB的错误估算，因此是完备的。不存在冗余，因为每个子节点代表不同的物理量或计算步骤。）

## Search Query

Qwen3-27B model config.json num_hidden_layers num_key_value_heads head_dim
