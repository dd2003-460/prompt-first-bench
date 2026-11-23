# N199: 骨干网交换机处理延迟T_switch_origin的P99分布：T_switch_origin_P99 = T_forwarding + T_queue_wai

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N60

## Claim

骨干网交换机处理延迟T_switch_origin的P99分布：T_switch_origin_P99 = T_forwarding + T_queue_wait，其中T_forwarding为硬件转发延迟（典型1-3μs，可忽略），T_queue_wait为队列排队延迟，在低负载（<50%）时T_queue_wait≈0-1ms，在高负载（>80%）时T_queue_wait可达5-20ms，P99值通常取高负载场景，故T_switch_origin_P99≈5-20ms，需根据骨干网实际负载率校准

## Corrected Claim

骨干网交换机处理延迟T_switch_origin的P99分布：T_switch_origin_P99 = T_forwarding + T_queue_wait，其中T_forwarding为硬件转发延迟（典型1-3μs，可忽略），T_queue_wait为队列排队延迟，在低负载（<50%）时T_queue_wait≈0-1ms，在高负载（>80%）时T_queue_wait可达5-20ms，P99值通常取高负载场景，故T_switch_origin_P99≈5-20ms，需根据骨干网实际负载率校准

## Evidence

先验知识/题面给定，逻辑校验通过：骨干网交换机硬件转发延迟确为微秒级，队列延迟随负载率非线性增长，高负载下毫秒级排队延迟符合排队论直觉，数值量级合理。
