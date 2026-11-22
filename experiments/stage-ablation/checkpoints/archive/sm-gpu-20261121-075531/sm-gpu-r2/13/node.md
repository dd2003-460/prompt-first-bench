# N128: 条件性决策框架中的关键变量“软件栈成熟度”：若用户主要使用 vLLM 且依赖 FP8 量化加速，则排除 AMD RX 7900 XTX（ROCm FP8 支持滞

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

条件性决策框架中的关键变量“软件栈成熟度”：若用户主要使用 vLLM 且依赖 FP8 量化加速，则排除 AMD RX 7900 XTX（ROCm FP8 支持滞后）；若用户主要使用 llama.cpp 且接受 W4/INT8 精度，则 AMD 方案因低 TDP 和高性价比可能进入候选前列。此条件直接改变硬件排序。

## Corrected Claim

条件性决策框架中的关键变量“软件栈成熟度”：若用户主要使用 vLLM 且依赖 FP8 量化加速，则排除 AMD RX 7900 XTX（ROCm FP8 支持滞后）；若用户主要使用 llama.cpp 且接受 W4/INT8 精度，则 AMD 方案因低 TDP 和高性价比可能进入候选前列。此条件直接改变硬件排序。

## Evidence

检索失败: no sources from any channel (all 5 failed)
