# N620: Alertmanager 通知发送延迟取决于通知通道（如 Slack/Webhook），典型 HTTP POST 往返时间在局域网内为 10-50ms，公网为 

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N220

## Claim

Alertmanager 通知发送延迟取决于通知通道（如 Slack/Webhook），典型 HTTP POST 往返时间在局域网内为 10-50ms，公网为 100-300ms；若使用重试机制，失败重试间隔默认 30s，需计入最坏情况延迟

## Corrected Claim

Alertmanager 通知发送延迟取决于通知通道（如 Slack/Webhook），典型 HTTP POST 往返时间在局域网内为 10-50ms，公网为 100-300ms；若使用重试机制，失败重试间隔默认 30s，需计入最坏情况延迟

## Evidence

先验知识/题面给定，逻辑校验通过：局域网HTTP往返10-50ms及公网100-300ms符合网络物理极限与常见RTT经验值；Alertmanager默认重试间隔30s符合其配置规范（repeat_interval默认值），逻辑自洽且数值量级合理。
