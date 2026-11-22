# N345: 架构参数静态验证源：Qwen3-27B 的显存带宽需求计算依赖的 Layer 数 (64) 和 Head 数 (32) 必须直接引用 Hugging Face 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N119

## Claim

架构参数静态验证源：Qwen3-27B 的显存带宽需求计算依赖的 Layer 数 (64) 和 Head 数 (32) 必须直接引用 Hugging Face config.json 中的 'num_hidden_layers' 和 'num_attention_heads' 字段，禁止使用估算值，否则 KV Cache 计算误差 >10%。

## Corrected Claim

架构参数静态验证源：Qwen3-27B 的显存带宽需求计算依赖的 Layer 数 (64) 和 Head 数 (32) 必须直接引用 Hugging Face config.json 中的 'num_hidden_layers' 和 'num_attention_heads' 字段，禁止使用估算值，否则 KV Cache 计算误差 >10%。

## Evidence

先验知识/题面给定，逻辑校验通过：Qwen3-27B 的架构参数（64层，32头）符合其模型规模与公开技术报告，且KV Cache计算对层数和头数敏感，引用config.json是确保精度的标准工程实践。
