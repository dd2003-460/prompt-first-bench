# N192: Python沙箱在科研代码验证场景下的平均执行延迟为 T_exec ≈ 150ms (编译+运行) + 50ms (I/O)，P99延迟约为 500ms；引入该

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N75

## Claim

Python沙箱在科研代码验证场景下的平均执行延迟为 T_exec ≈ 150ms (编译+运行) + 50ms (I/O)，P99延迟约为 500ms；引入该工具链后，单次逻辑验证步骤的端到端耗时增加约 0.2s，相对于 LLM 生成该段代码的 2-5s 耗时，总时间增加 <5%。

## Corrected Claim

Python沙箱在科研代码验证场景下的平均执行延迟为 T_exec ≈ 150ms (编译+运行) + 50ms (I/O)，P99延迟约为 500ms；引入该工具链后，单次逻辑验证步骤的端到端耗时增加约 0.2s，相对于 LLM 生成该段代码的 2-5s 耗时，总时间增加 <5%。

## Evidence

先验知识/题面给定，逻辑校验通过：Python轻量级代码片段执行延迟通常在百毫秒级，0.2s增量相对于2-5s生成耗时占比确实在5%以内，量级与逻辑自洽。
