# N650: 公有云 CDN 自动扩缩容触发阈值 CPU_threshold 为 60%，基于阿里云/Cloudflare 的默认策略，当 CPU 利用率超过 60% 时触发

- **status**: degraded
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N214

## Claim

公有云 CDN 自动扩缩容触发阈值 CPU_threshold 为 60%，基于阿里云/Cloudflare 的默认策略，当 CPU 利用率超过 60% 时触发扩容，确保稳态下 CPU 利用率 < 60%，故 ΔT_load_steady = 0ms

## Corrected Claim

在采用阿里云/Cloudflare 默认策略且 CPU 阈值设为 60% 的场景下，若系统成功在 CPU 超过 60% 前完成扩容，则稳态 CPU 利用率可维持在 60% 以下，理论上可避免由 CPU 饱和导致的额外延迟（ΔT_load_steady ≈ 0ms），但这依赖于具体的扩容速度和负载模型。

## Evidence

[质询]将特定厂商（阿里云/Cloudflare）的默认策略或最佳实践直接等同于通用的'公有云 CDN 自动扩缩容触发阈值'，且断言该阈值必然导致稳态延迟增量为 0ms，忽略了不同厂商、不同配置及负载波动下的实际差异，属于以偏概全的经验性断言。 | 经验事实，逻辑自洽但缺来源支持；虽然 60% 是常见的 CPU 扩容阈值，但将其作为通用标准并推导 ΔT=0ms 缺乏普适性依据，且无外部来源验证。
