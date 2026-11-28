# N258: UECC 错误对推理任务的具体影响分类：区分‘静默数据损坏’（Silent Data Corruption, 输出错误但不报错）与‘显存访问异常’（抛出 CUD

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N80

## Claim

UECC 错误对推理任务的具体影响分类：区分‘静默数据损坏’（Silent Data Corruption, 输出错误但不报错）与‘显存访问异常’（抛出 CUDA Error 导致进程崩溃），需量化两类错误在科研循环中的后果差异，前者导致结论不可信（需重跑），后者导致中断（需 MTTR 恢复），直接影响‘可靠达到 AGI’的定义。

## Corrected Claim

UECC 错误对推理任务的具体影响分类：区分‘静默数据损坏’（Silent Data Corruption, 输出错误但不报错）与‘显存访问异常’（抛出 CUDA Error 导致进程崩溃），需量化两类错误在科研循环中的后果差异，前者导致结论不可信（需重跑），后者导致中断（需 MTTR 恢复），直接影响‘可靠达到 AGI’的定义。

## Evidence

先验知识/题面给定，逻辑校验通过：UECC（Uncorrectable ECC）错误在硬件层面确实会导致数据位翻转（静默损坏）或触发总线错误/页错误（显存访问异常/CUDA Error），其后果分别对应数据完整性失效和进程中断，符合计算机体系结构与GPU故障处理的基本原理。
