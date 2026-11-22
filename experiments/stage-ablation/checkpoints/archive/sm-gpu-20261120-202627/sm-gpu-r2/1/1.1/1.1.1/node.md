# N35: Qwen3-27B 的架构参数量构成：总参数量 (27B) = Embedding层参数 + N_layers * (Attention参数 + FFN参数) 

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N7

## Claim

Qwen3-27B 的架构参数量构成：总参数量 (27B) = Embedding层参数 + N_layers * (Attention参数 + FFN参数) + Output Head参数，其中 Attention 参数 = 4 * hidden_dim^2 (Q/K/V/O 投影)，FFN 参数 = 2 * hidden_dim * intermediate_dim (GELU/GeGLU 结构)。

## Corrected Claim

Qwen3-27B 的架构参数量构成：总参数量 (27B) ≈ Embedding层参数 + N_layers * (Attention参数 + FFN参数) + Output Head参数。其中 Attention 参数 ≈ 4 * hidden_dim^2 (Q/K/V/O 投影)；FFN 参数取决于具体激活函数结构，若为标准两层线性层约为 2 * hidden_dim * intermediate_dim，若为GeGLU门控结构则约为 3 * hidden_dim * intermediate_dim。

## Evidence

[质询]FFN参数公式表述存在歧义且可能不准确：标准Transformer FFN通常包含两个线性层（W1和W2），参数量约为 2 * hidden_dim * intermediate_dim（若不计偏置）。若使用GeGLU等门控结构，通常涉及三个矩阵（W_gate, W_up, W_down），参数量约为 3 * hidden_dim * intermediate_dim。陈述中直接给出 '2 * hidden_dim * intermediate_dim' 并标注 '(GELU/GeGLU 结构)'，若指GeGLU则数值量级错误（少算1/3），若指标准GELU则标注误导。此外，Qwen3具体是否采用GeGLU需查证，但公式本身的通用性描述存在逻辑瑕疵。 | 来源[1]仅提及Qwen 3.6-27B为稠密设计，未提供具体的架构参数构成公式或FFN结构细节，无法直接支持或反驳具体的参数量计算公式。该陈述属于经验事实（具体模型架构参数），逻辑上基本自洽（总参数=各层参数之和），但FFN部分公式与结构标签的对应关系存在不确定性，且缺乏来源直接支持，故降级。

## Search Query

Qwen3-27B model config num_attention_heads num_key_value_heads hidden_size intermediate_size

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/2055287697623856945&rut=9eeddf0f14c1c269f39d9ab19c2f4848dd4aa0eac931137b38cbe095a39ec949', 'type': 'ddg', 'title': 'Qwen 3.6 27B深度评测：27B参数单挑397B，本地跑AI编程的时代来了'}
