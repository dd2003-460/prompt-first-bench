# N35: Qwen3-27B 的架构参数量构成：总参数量 (27B) = Embedding层参数 + N_layers * (Attention参数 + FFN参数) 

- **status**: verified
- **level**: L3
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N7

## Claim

Qwen3-27B 的架构参数量构成：总参数量 (27B) = Embedding层参数 + N_layers * (Attention参数 + FFN参数) + Output Head参数，其中 Attention 参数 = 4 * hidden_dim^2 (Q/K/V/O 投影)，FFN 参数 = 2 * hidden_dim * intermediate_dim (GELU/GeGLU 结构)。

## Corrected Claim

Qwen3-27B 的架构参数量构成：总参数量 (27B) ≈ Embedding层参数 + N_layers * (Attention参数 + FFN参数) + Output Head参数。其中 Attention 参数 ≈ 4 * hidden_dim^2 (Q/K/V/O 投影)；FFN 参数取决于具体激活函数结构，若为标准两层线性层约为 2 * hidden_dim * intermediate_dim，若为GeGLU门控结构则约为 3 * hidden_dim * intermediate_dim。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别对应父节点公式中的 Attention、FFN、Embedding 和 Output Head 四个独立组成部分，彼此正交且无重复。内容覆盖了所有关键模块，且针对 GQA (num_kv_heads) 和 SwiGLU (3 matrices) 等 Qwen3 特有的架构细节进行了准确展开，无冗余。）

## Search Query

Qwen3-27B model config num_attention_heads num_key_value_heads hidden_size intermediate_size

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/2055287697623856945&rut=9eeddf0f14c1c269f39d9ab19c2f4848dd4aa0eac931137b38cbe095a39ec949', 'type': 'ddg', 'title': 'Qwen 3.6 27B深度评测：27B参数单挑397B，本地跑AI编程的时代来了'}
