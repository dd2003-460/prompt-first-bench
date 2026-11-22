# N102: Qwen3-27B在FP8精度下的权重占用为27GB（修正自矛盾检测：N13原称13.5GB有误，N19称27GB正确，因27B参数×1字节/参数=27GB），

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N13

## Claim

Qwen3-27B在FP8精度下的权重占用为27GB（修正自矛盾检测：N13原称13.5GB有误，N19称27GB正确，因27B参数×1字节/参数=27GB），因此RTX 5090 32GB显存无法容纳FP8权重的27GB+KV Cache 5.2GB+激活值2.5GB=34.7GB，该工作点不可行，需重新评估RTX 5090的可行精度组合。

## Corrected Claim

Qwen3-27B在FP8精度下的权重占用为27GB（修正自矛盾检测：N13原称13.5GB有误，N19称27GB正确，因27B参数×1字节/参数=27GB），因此RTX 5090 32GB显存无法容纳FP8权重的27GB+KV Cache 5.2GB+激活值2.5GB=34.7GB，该工作点不可行，需重新评估RTX 5090的可行精度组合。

## Evidence

先验知识/题面给定，逻辑校验通过：27B参数在FP8下确实占用约27GB显存，加上KV Cache和激活值后总需求超过32GB，结论符合硬件约束逻辑。
