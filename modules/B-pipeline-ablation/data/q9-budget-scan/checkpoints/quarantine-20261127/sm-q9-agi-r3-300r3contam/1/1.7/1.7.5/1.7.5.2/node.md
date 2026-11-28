# N149: Python 解释器初始化耗时中，标准库导入（import sys, json, os 等）占 60-70%，剩余为 GIL 初始化与内存分配，可通过 `pyt

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N52

## Claim

Python 解释器初始化耗时中，标准库导入（import sys, json, os 等）占 60-70%，剩余为 GIL 初始化与内存分配，可通过 `python -X importtime -c 'pass'` 量化各模块导入耗时，若使用 venv 隔离环境，额外增加 5-10ms 的路径查找开销。

## Corrected Claim

Python 解释器初始化耗时中，标准库导入通常占据主要比例，剩余为 GIL 初始化与内存分配，可通过 `python -X importtime -c 'pass'` 量化各模块导入耗时，若使用 venv 隔离环境，通常会因路径查找增加少量毫秒级开销。

## Evidence

[质询]标准库导入占比60-70%及venv增加5-10ms开销属于高度依赖具体Python版本、操作系统及硬件环境的经验数据，缺乏普适性，且不同环境下波动较大，直接断言固定区间存在以偏概全的风险。 | 先验知识/题面给定，逻辑校验通过，但具体数值为经验事实，缺乏通用性保证，故降级为定性表述。
