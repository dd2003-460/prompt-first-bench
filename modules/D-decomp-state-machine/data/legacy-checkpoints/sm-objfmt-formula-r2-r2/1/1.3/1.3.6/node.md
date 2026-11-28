# N45: SGLang 推理框架的固定运行时开销与 vLLM 类似，约为 1-2GB，但其 RadixAttention 前缀缓存机制可能增加额外的 KV Cache 管

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N8

## Claim

SGLang 推理框架的固定运行时开销与 vLLM 类似，约为 1-2GB，但其 RadixAttention 前缀缓存机制可能增加额外的 KV Cache 管理开销，具体数值需根据实际部署场景实测确定。

## Corrected Claim

SGLang 推理框架的固定运行时开销与 vLLM 类似，约为 1-2GB，但其 RadixAttention 前缀缓存机制可能增加额外的 KV Cache 管理开销，具体数值需根据实际部署场景实测确定。

## Evidence

先验知识/题面给定，逻辑校验通过
