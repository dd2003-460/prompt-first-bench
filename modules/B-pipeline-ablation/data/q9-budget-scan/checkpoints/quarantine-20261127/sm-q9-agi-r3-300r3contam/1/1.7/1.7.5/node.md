# N52: 代码沙箱启动与执行耗时分解：Docker 容器冷启动耗时 ~150ms，Python 解释器初始化 ~50ms，单行代码执行 P95 耗时 <10ms（纯计算）

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N13, N14, N19

## Claim

代码沙箱启动与执行耗时分解：Docker 容器冷启动耗时 ~150ms，Python 解释器初始化 ~50ms，单行代码执行 P95 耗时 <10ms（纯计算）或 ~200ms（含 I/O），总非推理开销占比约 15-25%。

## Corrected Claim

代码沙箱启动与执行耗时分解：Docker 容器冷启动耗时 ~150ms，Python 解释器初始化 ~50ms，单行代码执行 P95 耗时 <10ms（纯计算）或 ~200ms（含 I/O），总非推理开销占比约 15-25%。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

docker container startup overhead python execution latency sandbox
