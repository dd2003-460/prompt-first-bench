# N219: BF16精度下消费级多卡可行性补充：N72指出2x RTX 4090 (48GB) 不足，但忽略了CPU Offload或INT8 KV Cache混合精度策略

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N72

## Claim

BF16精度下消费级多卡可行性补充：N72指出2x RTX 4090 (48GB) 不足，但忽略了CPU Offload或INT8 KV Cache混合精度策略。若允许KV Cache量化为INT8（5.35GB），BF16权重(54GB)+INT8 KV(5.35GB)+开销(4GB) = 63.35GB，仍超出48GB。但若进一步启用权重量化或更激进的Offload，2x 4090在BF16下仍不可行，除非降低模型精度至INT8，此时应归类至INT8可行性节点而非BF16节点。

## Corrected Claim

BF16精度下消费级多卡可行性补充：N72指出2x RTX 4090 (48GB) 不足，但忽略了CPU Offload或INT8 KV Cache混合精度策略。若允许KV Cache量化为INT8（5.35GB），BF16权重(54GB)+INT8 KV(5.35GB)+开销(4GB) = 63.35GB，仍超出48GB。但若进一步启用权重量化或更激进的Offload，2x 4090在BF16下仍不可行，除非降低模型精度至INT8，此时应归类至INT8可行性节点而非BF16节点。

## Evidence

先验知识/题面给定，逻辑校验通过：54GB权重+5.35GB KV+4GB开销=63.35GB，确实超出48GB显存，且结论符合硬件限制逻辑。

## Search Query

RTX 4090 dual BF16 27B offload feasibility
