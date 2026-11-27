# N187: 若框架支持W4权重+INT8 KV Cache混合精度，总显存需求降至13.5GB + 5.35GB + 4GB = 22.85GB，该值低于RTX 4090的

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N57

## Claim

若框架支持W4权重+INT8 KV Cache混合精度，总显存需求降至13.5GB + 5.35GB + 4GB = 22.85GB，该值低于RTX 4090的24GB容量，理论上可实现单卡运行，但需验证该混合精度配置在vLLM或llama.cpp中的可用性及实际吞吐量损失（预计因KV Cache反量化开销增加10-15%延迟）。

## Corrected Claim

若框架支持W4权重+INT8 KV Cache混合精度，模型权重与KV Cache静态显存需求约为22.85GB，接近RTX 4090的24GB容量上限。考虑到CUDA上下文、内存碎片及框架运行时开销（通常1-2GB），实际单卡运行风险极高，可能因OOM失败，需严格验证实际占用及吞吐量损失。

## Evidence

[质询]数值计算存在内部矛盾：13.5 + 5.35 + 4 = 22.85，但 13.5 + 5.35 = 18.85，18.85 + 4 = 22.85 是正确的加法结果，然而通常 W4 权重显存估算需考虑对齐和开销，且 5.35GB KV Cache 与 4GB 其他开销的具体构成未明确，更关键的是，22.85GB 非常接近 24GB 上限，实际运行中 CUDA 上下文、碎片化及 vLLM/llama.cpp 的额外内存开销（通常 1-2GB）极可能导致 OOM，因此“理论上可实现”过于乐观，缺乏对运行时开销的考量。 | 先验知识/题面给定，逻辑校验发现数值虽算术正确但忽略了运行时显存开销（CUDA context, fragmentation, framework overhead），导致 22.85GB 在 24GB 卡上实际不可行或极不稳定，属于经验事实且缺乏来源支持，故降级。

## Search Query

W4 weights INT8 KV cache hybrid precision single GPU 4090 feasibility latency overhead
