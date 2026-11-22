# N192: Qwen3-27B 架构参数修正：hidden_size 应为 4096（非 1024），num_attention_heads=32，num_key_valu

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N63

## Claim

Qwen3-27B 架构参数修正：hidden_size 应为 4096（非 1024），num_attention_heads=32，num_key_value_heads=8（GQA 4:1），head_dim=128，num_hidden_layers=64；该参数集是计算 KV Cache 大小和通信量的基础，若 hidden_size 误判为 1024 会导致后续所有带宽/显存计算缩小 4 倍。

## Corrected Claim

Qwen3-27B 架构参数需进一步核实：若 hidden_size 确为 4096（而非 1024），则 KV Cache 大小和通信量计算需基于此修正，原误判会导致结果缩小 4 倍。

## Evidence

[质询]该陈述包含具体的模型架构参数（hidden_size, num_layers等），属于经验事实。虽然逻辑上指出hidden_size从1024修正为4096会导致计算量/显存占用变化4倍（4096/1024=4）在数学上自洽，但缺乏外部来源直接证实Qwen3-27B的具体架构参数是否为hidden_size=4096且num_hidden_layers=64。若实际参数不同（例如hidden_size为其他值或层数不同），则结论错误。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源）

## Search Query

Qwen3-27B model architecture parameters hidden_size num_key_value_heads config.json
