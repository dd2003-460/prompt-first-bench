# N292: 单元测试生成模块需基于AST生成至少3个边界测试用例（包括正常值、边界值、异常值），生成耗时需<1s，且生成的测试代码在GVisor沙箱中的执行通过率需>95%

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N92, N93, N94

## Claim

单元测试生成模块需基于AST生成至少3个边界测试用例（包括正常值、边界值、异常值），生成耗时需<1s，且生成的测试代码在GVisor沙箱中的执行通过率需>95%，否则视为无效测试并回退到纯stderr反馈

## Corrected Claim

单元测试生成模块需基于AST生成至少3个边界测试用例（包括正常值、边界值、异常值），生成耗时需<1s，且生成的测试代码在GVisor沙箱中的执行通过率需>95%，否则视为无效测试并回退到纯stderr反馈

## Evidence

先验知识/题面给定，逻辑校验通过
