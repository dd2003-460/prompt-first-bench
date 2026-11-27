# N7: 消费级GPU显存容量下限为24GB，基于Qwen3-27B在FP8精度下权重占用约13.5GB，需预留KV Cache空间，低于24GB的显存（如RTX 406

- **status**: pending
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1

## Claim

消费级GPU显存容量下限为24GB，基于Qwen3-27B在FP8精度下权重占用约13.5GB，需预留KV Cache空间，低于24GB的显存（如RTX 4060/4070）在32K上下文下必然溢出，故排除显存<24GB的消费级显卡。

## Corrected Claim

消费级GPU显存容量下限为24GB，基于Qwen3-27B在FP8精度下权重占用约13.5GB，需预留KV Cache空间，低于24GB的显存（如RTX 4060/4070）在32K上下文下必然溢出，故排除显存<24GB的消费级显卡。

## Evidence

父节点级核验未通过：非正交, 有冗余（子节点3和4存在逻辑冗余（INT8与FP8在27B模型上均为1byte/param，计算结果完全一致，无需单独列出两个节点）；子节点6、7、8偏离了父节点‘显存容量下限与排除逻辑’的核心主题，转而讨论带宽和吞吐量，属于正交性破坏（引入了父节点未涉及的推理速度维度）。）
