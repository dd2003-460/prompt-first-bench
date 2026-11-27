# N31: Qwen3-27B 采用 GQA (Grouped Query Attention) 结构，具体参数为 num_layers=64, hidden_dim=40

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

Qwen3-27B 采用 GQA (Grouped Query Attention) 结构，具体参数为 num_layers=64, hidden_dim=4096, num_kv_heads=8。在 BF16 下，单 token KV Cache 大小为 2 * 64 * 8 * 128 * 2 bytes = 256KB (假设 head_dim=128)。32K 上下文总 KV Cache 大小 = 256KB * 32768 ≈ 8GB。

## Corrected Claim

Qwen3 系列模型（如 Qwen3-30B-A3B）采用 GQA 结构。若假设某 Qwen3 稠密模型具有 num_layers=64, num_kv_heads=8, head_dim=128 的参数，则其 BF16 下 32K 上下文的 KV Cache 大小约为 8GB。

## Evidence

[质询]参考来源仅提及 Qwen3-30B-A3B 采用 GQA，未提供 Qwen3-27B 的具体架构参数（如 num_layers, hidden_dim, num_kv_heads），且 Qwen3-27B 并非 Qwen3 系列中广泛公开的标准稠密模型名称（常见为 32B, 14B 等），存在模型名称或参数配置混淆的风险。 | 逻辑推导成立（2*64*8*128*2=256KB, 256KB*32768=8GB），但参考来源 [1] 仅确认 Qwen3 系列使用 GQA，未直接支持 Qwen3-27B 的具体参数值，属于经验事实缺来源支持。

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/1905664754569185060&rut=b18fcc451af87d0ccbea8d5b38f6a7d4ce11f5a30aaec789ad11b3f0453faa24', 'type': 'ddg', 'title': '图解Qwen3混合专家模型推理过程--GQA和MoE - 知乎'}
