# N239: ONNX Runtime + NPU 方案中，适配工时上限 20 人天源于 NPU 不支持动态 Shape 导致的静态图编译失败，需额外 10 人天进行 Sha

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N91

## Claim

ONNX Runtime + NPU 方案中，适配工时上限 20 人天源于 NPU 不支持动态 Shape 导致的静态图编译失败，需额外 10 人天进行 Shape 固定化改造及内存布局优化（如从 NCHW 转为 NHWC）。

## Corrected Claim

ONNX Runtime + NPU 方案中，若 NPU 不支持动态 Shape，通常需进行静态图编译适配（如 Shape 固定化、内存布局优化），具体工时取决于模型复杂度与 NPU 架构，一般需额外投入数人天至十余人天不等。

## Evidence

[质询]具体数值（20人天、10人天）属于特定项目或团队的经验估算，缺乏通用性，且不同NPU架构（如华为昇腾、高通、苹果ANE）对动态Shape的支持程度及优化难度差异巨大，无法一概而论。 | 经验事实，逻辑自洽但缺来源支持
