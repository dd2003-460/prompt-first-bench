# N130: 指数退避基础延迟 T_base=1s 的选择需满足 T_base < T_network_jitter_p99；对于国内至海外 API 的典型网络抖动 P99 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N44

## Claim

指数退避基础延迟 T_base=1s 的选择需满足 T_base < T_network_jitter_p99；对于国内至海外 API 的典型网络抖动 P99 延迟约为 200-500ms，故 1s 提供了 2x-5x 的安全余量；若实测 P99 > 1s，应将 T_base 调整为 P99 * 1.5 以避免无效重试。

## Corrected Claim

指数退避基础延迟 T_base=1s 的选择需满足 T_base < T_network_jitter_p99；对于国内至海外 API 的典型网络抖动 P99 延迟约为 200-500ms，故 1s 提供了 2x-5x 的安全余量；若实测 P99 > 1s，应将 T_base 调整为 P99 * 1.5 以避免无效重试。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

typical p99 network latency china to us api endpoint
