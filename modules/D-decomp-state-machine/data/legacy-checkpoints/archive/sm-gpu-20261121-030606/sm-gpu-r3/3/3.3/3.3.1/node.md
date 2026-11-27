# N114: INT8精度下Qwen3-27B的权重存储占用为27GB（修正自矛盾检测：N19中INT8=27GB为正确值，N12中13.5GB实为NVFP4/W4精度下的占

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N17

## Claim

INT8精度下Qwen3-27B的权重存储占用为27GB（修正自矛盾检测：N19中INT8=27GB为正确值，N12中13.5GB实为NVFP4/W4精度下的占用，非INT8），该数值意味着INT8精度在24GB显存（RTX 4090）下不可行（27GB > 24GB），必须使用≥32GB显存硬件（如RTX 5090）或采用NVFP4/W4精度。

## Corrected Claim

INT8精度下Qwen3-27B的权重存储占用为27GB（修正自矛盾检测：N19中INT8=27GB为正确值，N12中13.5GB实为NVFP4/W4精度下的占用，非INT8），该数值意味着INT8精度在24GB显存（RTX 4090）下不可行（27GB > 24GB），必须使用≥32GB显存硬件（如RTX 5090）或采用NVFP4/W4精度。

## Evidence

先验知识/题面给定，逻辑校验通过：INT8精度下27B参数模型权重占用约为27GB（27e9 * 1 byte），大于24GB显存，逻辑自洽且数值量级合理。
