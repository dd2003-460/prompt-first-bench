# N121: GPU 显存泄漏检测：每小时记录一次 GPU 内存占用变化 Delta_Mem，若 7 天内累计增长 > 1GB，则判定存在内存泄漏，需重启服务或升级 vLLM

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N31

## Claim

GPU 显存泄漏检测：每小时记录一次 GPU 内存占用变化 Delta_Mem，若 7 天内累计增长 > 1GB，则判定存在内存泄漏，需重启服务或升级 vLLM 版本以修复 KV Cache 释放 bug。

## Corrected Claim

GPU 显存泄漏检测：每小时记录一次 GPU 内存占用变化 Delta_Mem，若 7 天内累计增长 > 1GB，则判定存在内存泄漏，需重启服务或升级 vLLM 版本以修复 KV Cache 释放 bug。

## Evidence

先验知识/题面给定，逻辑校验通过
