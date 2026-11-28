# N684: local_status == 'DEGRADED' 的判断阈值 throughput < 50% baseline 中，baseline 吞吐量需定义为最近 

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N248

## Claim

local_status == 'DEGRADED' 的判断阈值 throughput < 50% baseline 中，baseline 吞吐量需定义为最近 10 分钟滑动窗口的 P50 或 P95 吞吐量，若使用 P95，则阈值波动较大；建议使用 P50 并设置滞回区间（Hysteresis）：切换至云端当 throughput < 45% baseline，切回本地当 throughput > 55% baseline，以避免频繁震荡（Flapping），滞回区间宽度 10% 基于控制论稳定性原则

## Corrected Claim

local_status == 'DEGRADED' 的判断阈值 throughput < 50% baseline 中，baseline 吞吐量需定义为最近 10 分钟滑动窗口的 P50 或 P95 吞吐量，若使用 P95，则阈值波动较大；建议使用 P50 并设置滞回区间（Hysteresis）：切换至云端当 throughput < 45% baseline，切回本地当 throughput > 55% baseline，以避免频繁震荡（Flapping），滞回区间宽度 10% 基于控制论稳定性原则

## Evidence

先验知识/题面给定，逻辑校验通过：P50比P95更稳定符合统计学常识，45%-55%的10%滞回区间符合控制论中避免振荡的设计原则，数值量级合理且内部逻辑自洽。

## Search Query

load balancer hysteresis threshold flapping prevention control theory
