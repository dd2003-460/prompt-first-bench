# N644: RTX 4090 在 INT4 量化 + INT8 KV Cache 配置下的有效 $/GB(KV) 指标修正：权重 13.5GB，框架 2GB，剩余 8.5G

- **status**: degraded
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N228

## Claim

RTX 4090 在 INT4 量化 + INT8 KV Cache 配置下的有效 $/GB(KV) 指标修正：权重 13.5GB，框架 2GB，剩余 8.5GB 显存；INT8 KV Cache 单 token 占用 128KB，可支持 68,152 tokens KV Cache；若限制为 32K 上下文单请求，剩余 4.5GB 可支持额外 35,840 tokens 或 1 个额外并发请求；修正后 $/GB(可用 KV) = $3,300 / 8.5GB ≈ $388/GB，但考虑到其仅支持 1-2 并发，单位并发成本 $1,650-$3,300，远高于 A100 的 $5,258/并发，表明其在高并发场景下性价比劣势明显。

## Corrected Claim

RTX 4090 在 INT4 量化 + INT8 KV Cache 配置下，若限制为 32K 上下文单请求，剩余显存可支持额外并发。修正后 $/GB(可用 KV) ≈ $388/GB。其单位并发成本估算为 $1,650-$3,300，低于 A100 的 $5,258/并发，但在高并发场景下受限于显存容量，总吞吐量成本效益需结合具体负载评估，不能仅凭单并发成本断定劣势。

## Evidence

[质询]结论存在逻辑矛盾：陈述称单位并发成本（$1,650-$3,300）'远高于' A100 的 $5,258/并发，但数值上 $3,300 明显低于 $5,258，'远高于'的定性描述与给出的具体数值直接冲突。 | 先验知识/题面给定，逻辑校验发现内部数值与定性结论矛盾（$3,300 < $5,258，非'远高于'），且缺乏外部来源支持具体硬件价格与显存分配细节。

## Search Query

RTX 4090 INT4 quantization KV cache memory usage Qwen 27B
