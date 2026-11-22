# N391: RTX 4090 在 W4 精度下支持 4 并发 32K 上下文所需的总显存为 13.5GB (权重) + 5GB (框架) + 4 * 1.6GB (KV) 

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N134

## Claim

RTX 4090 在 W4 精度下支持 4 并发 32K 上下文所需的总显存为 13.5GB (权重) + 5GB (框架) + 4 * 1.6GB (KV) = 24.9GB，超出 24GB 显存 0.9GB，需通过减少上下文至 30K (KV 降至 1.5GB/req, 总 24.1GB) 或启用 PagedAttention 碎片优化勉强可行，但无冗余。

## Corrected Claim

RTX 4090 在 W4 精度下，若模型权重约 13.5GB 且框架开销约 5GB，则 4 并发 32K 上下文所需的 KV Cache 总显存需控制在 5.5GB 以内（即每请求约 1.375GB）才能勉强适配 24GB 显存；若按每请求 1.6GB KV Cache 估算，总需求 24.9GB 将超出显存，需减少上下文或启用 PagedAttention 优化。

## Evidence

[质询]KV Cache 的显存占用估算（1.6GB/req for 32K context）缺乏具体模型参数（如层数、头数、头维度）支持，不同模型架构下该数值差异巨大，属于经验估算而非固定事实；此外，'框架开销 5GB' 也高度依赖具体推理引擎（如 vLLM, TGI）及配置，非通用常数。 | source=knowledge，逻辑自洽（算术正确：13.5+5+6.4=24.9），但 KV Cache 和框架开销的具体数值为经验估算，缺乏特定模型/引擎上下文，无法从第一性原理严格推出，故降级。
