# N292: QoS调度器引入的额外处理延迟开销 ΔP99_overhead 约为 2-5ms，基于Linux tc HTB或硬件交换机的优先级队列实现，需从视频请求的P99

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N94

## Claim

QoS调度器引入的额外处理延迟开销 ΔP99_overhead 约为 2-5ms，基于Linux tc HTB或硬件交换机的优先级队列实现，需从视频请求的P99收益中扣除以得到净收益

## Corrected Claim

QoS调度器引入的额外处理延迟开销 ΔP99_overhead 约为 2-5ms，基于Linux tc HTB或硬件交换机的优先级队列实现，需从视频请求的P99收益中扣除以得到净收益

## Evidence

先验知识/题面给定，逻辑校验通过：Linux tc HTB或硬件交换机优先级队列的调度开销通常在微秒至毫秒级，2-5ms作为P99尾延迟的保守估计符合工程直觉，且无来源矛盾。
