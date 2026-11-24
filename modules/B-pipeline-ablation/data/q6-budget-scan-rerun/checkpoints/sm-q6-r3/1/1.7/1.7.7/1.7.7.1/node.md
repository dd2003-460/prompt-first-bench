# N187: 单台边缘服务器实际QPS处理能力：基于64核CPU及256GB内存，假设单请求CPU耗时为1ms（含缓存命中、压缩、加密），单核理论QPS为1000，考虑上下文

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N49

## Claim

单台边缘服务器实际QPS处理能力：基于64核CPU及256GB内存，假设单请求CPU耗时为1ms（含缓存命中、压缩、加密），单核理论QPS为1000，考虑上下文切换、I/O等待及网络栈开销，实际单核QPS约为200-300；64核服务器实际QPS约为12,800-19,200，而非N49原假设的100 QPS/台；原假设可能混淆了‘每核QPS’与‘每服务器QPS’，或考虑了极端重负载场景。

## Corrected Claim

单台边缘服务器实际QPS处理能力：基于64核CPU及256GB内存，假设单请求CPU耗时为1ms（含缓存命中、压缩、加密），单核理论QPS为1000，考虑上下文切换、I/O等待及网络栈开销，实际单核QPS约为200-300；64核服务器实际QPS约为12,800-19,200，而非N49原假设的100 QPS/台；原假设可能混淆了‘每核QPS’与‘每服务器QPS’，或考虑了极端重负载场景。

## Evidence

先验知识/题面给定，逻辑校验通过：单核1ms耗时理论上限1000 QPS，考虑系统开销后200-300 QPS符合工程常识，64核线性扩展至12,800-19,200 QPS量级合理，且明确指出了原假设中每核与每服务器QPS混淆的逻辑错误。

## Search Query

CDN edge server QPS per CPU core benchmark
