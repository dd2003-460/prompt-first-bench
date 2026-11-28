# N15: 代码执行沙箱隔离度：实验执行阶段的代码需在Docker沙箱中运行，其资源限制（CPU<4核，内存<16GB，网络禁用）确保主服务不受影响，预期沙箱启动开销<2s

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N2

## Claim

代码执行沙箱隔离度：实验执行阶段的代码需在Docker沙箱中运行，其资源限制（CPU<4核，内存<16GB，网络禁用）确保主服务不受影响，预期沙箱启动开销<2s

## Corrected Claim

代码执行沙箱隔离度：实验执行阶段的代码需在Docker沙箱中运行，其资源限制（CPU<4核，内存<16GB，网络禁用）确保主服务不受影响，预期沙箱启动开销<2s

## Evidence

先验知识/题面给定，逻辑校验通过
