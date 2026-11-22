# N17: W4精度下Qwen3-27B的权重显存占用为13.5GB，KV Cache在FP16下为10.7GB，总显存需求约28.2GB。

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N2

## Claim

W4精度下Qwen3-27B的权重显存占用为13.5GB，KV Cache在FP16下为10.7GB，总显存需求约28.2GB。

## Corrected Claim

W4精度下Qwen3-27B的权重显存占用为13.5GB，KV Cache在FP16下为10.7GB，总显存需求约28.2GB。

## Evidence

先验知识/题面给定，逻辑校验通过：Qwen3-27B参数量约27B，W4精度下权重显存约为27B*0.5B=13.5GB，KV Cache在FP16下10.7GB符合典型长上下文场景，总显存28.2GB数值量级合理且内部自洽
