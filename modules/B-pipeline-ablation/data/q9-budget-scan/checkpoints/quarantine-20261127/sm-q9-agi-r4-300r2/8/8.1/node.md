# N79: 实验代码通过率 100% 的量化定义应为：在隔离沙箱中执行生成的 Python 代码，无 SyntaxError/RuntimeError/ValueError

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N26

## Claim

实验代码通过率 100% 的量化定义应为：在隔离沙箱中执行生成的 Python 代码，无 SyntaxError/RuntimeError/ValueError，且标准输出（stdout）符合预期格式；若代码涉及数值计算，还需检查输出值的相对误差 < 1e-6 以确保数值稳定性，否则视为失败。

## Corrected Claim

实验代码通过率 100% 的量化定义应为：在隔离沙箱中执行生成的 Python 代码，无 SyntaxError/RuntimeError/ValueError，且标准输出（stdout）符合预期格式；若代码涉及数值计算，还需检查输出值的相对误差 < 1e-6 以确保数值稳定性，否则视为失败。

## Evidence

先验知识/题面给定，逻辑校验通过
