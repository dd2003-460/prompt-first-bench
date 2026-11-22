# N6: 消费级GPU候选集筛选：基于显存容量≥24GB且支持FP8/INT8推理的当前主流型号（RTX 4090 24GB, RTX 4080 Super 16GB, 

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1

## Claim

消费级GPU候选集筛选：基于显存容量≥24GB且支持FP8/INT8推理的当前主流型号（RTX 4090 24GB, RTX 4080 Super 16GB, RTX 3090 24GB），需标注各型号FP16/BF16/FP8/INT8下的理论显存占用与吞吐基准

## Corrected Claim

消费级GPU候选集筛选：基于显存容量≥24GB且支持FP8/INT8推理的当前主流型号（RTX 4090 24GB, RTX 3090 24GB），需标注各型号FP16/BF16/FP8/INT8下的理论显存占用与吞吐基准

## Evidence

[质询]RTX 4080 Super 显存为 16GB，不满足陈述中设定的 '显存容量≥24GB' 筛选条件，存在内部逻辑矛盾。 | 先验知识/题面给定，逻辑校验发现内部矛盾：RTX 4080 Super 显存为 16GB，不符合 ≥24GB 的筛选标准。

## Search Query

RTX 4090 4080 Super 3090 FP8 INT8 inference benchmark 2024
