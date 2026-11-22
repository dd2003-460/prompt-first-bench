# N105: 修正矛盾：Qwen3-27B 在 FP8 (E4M3) 精度下的静态权重显存占用为 27 GB (27B × 1 byte)，N27-N31 中引用的 '13.

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N24

## Claim

修正矛盾：Qwen3-27B 在 FP8 (E4M3) 精度下的静态权重显存占用为 27 GB (27B × 1 byte)，N27-N31 中引用的 '13.5 GB' 为 INT4 数值误植，FP8 下无法在 24GB 显存卡上运行 32K 上下文。

## Corrected Claim

修正矛盾：Qwen3-27B 在 FP8 (E4M3) 精度下的静态权重显存占用为 27 GB (27B × 1 byte)，N27-N31 中引用的 '13.5 GB' 为 INT4 数值误植，FP8 下无法在 24GB 显存卡上运行 32K 上下文。

## Evidence

先验知识/题面给定，逻辑校验通过：27B参数在FP8(1字节/参数)下权重占用确为27GB，超过24GB显存限制，且27GB与13.5GB（INT4）的数值关系符合精度减半的规律，逻辑自洽。
