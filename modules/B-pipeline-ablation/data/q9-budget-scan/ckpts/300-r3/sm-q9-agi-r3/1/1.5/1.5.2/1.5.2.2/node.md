# N165: Qwen3.8-27B 在 FP16 精度下权重占用显存为 54GB，KV Cache (batch=1, len=4096) 额外占用约 4GB，总需求 58

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N48

## Claim

Qwen3.8-27B 在 FP16 精度下权重占用显存为 54GB，KV Cache (batch=1, len=4096) 额外占用约 4GB，总需求 58GB；M1 Max 最大统一内存配置为 64GB，扣除 macOS 系统预留 8-12GB 后可用内存上限为 52-56GB，故物理上无法加载完整 27B 模型进行推理

## Corrected Claim

Qwen3.8-27B 在 FP16 精度下权重占用显存为 54GB，KV Cache (batch=1, len=4096) 额外占用约 4GB，总需求 58GB；M1 Max 最大统一内存配置为 64GB，扣除 macOS 系统预留 8-12GB 后可用内存上限为 52-56GB，故物理上无法加载完整 27B 模型进行推理

## Evidence

先验知识/题面给定，逻辑校验通过：27B参数FP16权重约54GB，加上KV Cache后总需求58GB，超过M1 Max扣除系统预留后的可用内存上限（52-56GB），物理上无法加载。

## Search Query

Qwen 27B model memory footprint FP16 unified memory requirement MacBook Pro M1 Max 64GB
