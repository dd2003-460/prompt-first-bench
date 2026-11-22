# N148: Qwen3-27B 的 Head Dimension (d_head) 确认为 128，结合 num_kv_heads=8，单层单 token 的 K+V 总元

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N39

## Claim

Qwen3-27B 的 Head Dimension (d_head) 确认为 128，结合 num_kv_heads=8，单层单 token 的 K+V 总元素数为 2 * 8 * 128 = 2048 个，在 BF16 (2 bytes/element) 下为 4096 bytes，该数值是单卡显存预算计算的原子单位 [search]

## Corrected Claim

Qwen3-27B 的 Head Dimension (d_head) 和 num_kv_heads 需依据官方配置确认；若确认为 d_head=128 且 num_kv_heads=8，则单层单 token 的 K+V 总元素数为 2048 个，BF16 下为 4096 bytes。

## Evidence

[质询]参考来源[1]描述的是Qwen3.5-27B（含DeltaNet混合架构），来源[2]是Qwen3.8-27B（多模态），均非Qwen3-27B（纯Transformer架构）。Qwen3-27B的具体配置（如num_kv_heads=8, d_head=128）未在提供的来源中直接证实，且不同版本/架构的KV头数可能不同，存在口径混淆风险。 | 数学计算逻辑自洽（2*8*128*2=4096），但参考来源与Qwen3-27B具体参数不匹配，无法提供直接支持，属于经验事实缺来源支持。

## Search Query

Qwen3-27B head_dim 128 architecture details

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/2010079474104963160&rut=336d25a4988526b6be857ced6e5fc040a0f025afaa4a16b40b3bafb074499abe', 'type': 'ddg', 'title': 'Qwen/Qwen3.5-27B模型结构（dense）分析 - 知乎'}
- {'url': 'https://huggingface.co/Qwen/Qwen3.8-27B&rut=f4a8505e184453f0072dff61003e506186593cb27e55fa60c3183db1cee66710', 'type': 'ddg', 'title': 'Qwen/Qwen3.8-27B · Hugging Face'}
