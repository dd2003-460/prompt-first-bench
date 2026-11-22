# N295: 修正N20的激活值精度依赖性：在推理阶段，中间激活值（Attention/MLP）的存储精度由计算框架决定（通常与权重精度解耦，如BF16计算/FP8存储），而

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N126

## Claim

修正N20的激活值精度依赖性：在推理阶段，中间激活值（Attention/MLP）的存储精度由计算框架决定（通常与权重精度解耦，如BF16计算/FP8存储），而KV Cache的精度由推理引擎配置决定（如vLLM的--kv-cache-dtype）。因此，'激活值与权重精度无关'仅在特定框架默认配置下成立，并非绝对物理定律。

## Corrected Claim

修正N20的激活值精度依赖性：在推理阶段，中间激活值（Attention/MLP）的存储精度由计算框架决定（通常与权重精度解耦，如BF16计算/FP8存储），而KV Cache的精度由推理引擎配置决定（如vLLM的--kv-cache-dtype）。因此，'激活值与权重精度无关'仅在特定框架默认配置下成立，并非绝对物理定律。

## Evidence

先验知识/题面给定，逻辑校验通过：现代推理框架（如vLLM）确实允许独立配置计算精度（如BF16）与KV Cache存储精度（如FP8/INT8），且中间激活值通常随计算精度或框架默认设置，与权重存储精度解耦，陈述符合工程事实。
