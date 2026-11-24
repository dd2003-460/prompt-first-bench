# N105: 公有云CDN自动扩容的响应延迟 T_scaling 通常为 10-30 秒（基于云厂商内部监控触发阈值与资源调度链路），在此期间超出预置容量的请求将经历队列等待

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N27, N28, N29

## Claim

公有云CDN自动扩容的响应延迟 T_scaling 通常为 10-30 秒（基于云厂商内部监控触发阈值与资源调度链路），在此期间超出预置容量的请求将经历队列等待或回源，导致 P99 延迟上升幅度 ΔP99_scaling ≈ T_scaling × Queue_Rate

## Corrected Claim

公有云CDN自动扩容存在响应延迟（通常为数秒至数十秒量级），在此期间超出预置容量的请求可能经历队列等待或回源，导致P99延迟上升。

## Evidence

[质询]该陈述包含具体的经验参数（10-30秒）和特定的工程模型公式（ΔP99 ≈ T × Rate），属于经验事实而非第一性原理可推导内容。参考来源仅涉及腾讯云CDN的价格和基础问答，未提供关于自动扩容响应延迟的具体数值或内部调度机制的技术细节，无法直接支持该具体数值范围及公式的准确性。 | 逻辑上自洽（扩容存在延迟导致排队符合排队论直觉），但参考来源[1]与具体扩容延迟数值及公式无关，且该事实为经验参数，缺乏直接来源支持，依据经验事实排除条款降级。

## Search Query

cloud CDN autoscaling response time latency impact P99

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/2048430333788528788&rut=3ec305190329235aed0770fcda50f0a57294dd1d14f94f8c32d5c93d21144baa', 'type': 'ddg', 'title': '腾讯云cdn加速10个高频问题：2026年最新解答 - 知乎'}
