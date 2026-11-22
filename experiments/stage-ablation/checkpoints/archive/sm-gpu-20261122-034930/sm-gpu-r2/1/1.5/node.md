# N11: 消费级GPU候选集：RTX 4090 (24GB), RTX 3090 (24GB), RTX 4080 (16GB), RTX 3060 (12GB)。其中仅

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N1

## Claim

消费级GPU候选集：RTX 4090 (24GB), RTX 3090 (24GB), RTX 4080 (16GB), RTX 3060 (12GB)。其中仅4090/3090在W4精度下可能满足单卡需求，但24GB<28.2GB，需验证W4实际占用或需双卡。

## Corrected Claim

消费级GPU候选集包括RTX 4090 (24GB)和RTX 3090 (24GB)等。由于24GB显存可能小于模型在W4精度下的理论或估算占用（如28.2GB），需进一步验证实际内存占用或考虑双卡方案。

## Evidence

[质询]该陈述包含具体的硬件规格（显存大小）和特定量化精度下的内存占用估算（28.2GB），属于经验事实。由于检索失败，无法验证28.2GB这一具体数值是否准确对应特定模型在W4精度下的实际占用，存在数值偏差或口径混淆的风险。 | 经验事实，逻辑自洽但缺来源支持。硬件规格（如RTX 4090/3090为24GB）符合常识，但28.2GB的具体估算值无法通过第一性原理严格推导，且无外部来源佐证，故降级。

## Search Query

NVIDIA RTX 4090 24GB VRAM price 2024
