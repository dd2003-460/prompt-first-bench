# N335: nvidia-smi 监控脚本的资源开销与精度：运行 nvidia-smi --query-gpu=temperature.gpu,utilization.gp

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N111

## Claim

nvidia-smi 监控脚本的资源开销与精度：运行 nvidia-smi --query-gpu=temperature.gpu,utilization.gpu --format=csv -l 1 脚本，CPU 占用率约为 0.5%，内存占用 10MB，日志文件大小约为 100KB/小时；该监控频率足以捕捉瞬时高温 (>90°C) 和高负载 (>95%) 事件，漏报率低于 5%。

## Corrected Claim

nvidia-smi 监控脚本资源开销极低（CPU 占用通常低于 1%，内存占用约 10MB 量级），日志增长缓慢；1 秒采样频率足以捕捉持续数秒以上的高温 (>90°C) 和高负载 (>95%) 事件，但对于毫秒级瞬时尖峰可能存在漏报。

## Evidence

[质询]具体数值（0.5% CPU, 10MB RAM, 100KB/h, <5% 漏报率）属于经验性测量数据，不同驱动版本、GPU 型号及系统负载下波动较大，且 1 秒采样间隔对于捕捉毫秒级瞬时高温/高负载事件存在理论上的漏报风险，断言漏报率低于 5% 缺乏普适性依据。 | 先验知识/题面给定，逻辑校验通过（量级合理，nvidia-smi 开销确实极低，1s 采样对分钟级监控足够，但对瞬时事件漏报率需视具体场景而定，故降级为定性表述）
