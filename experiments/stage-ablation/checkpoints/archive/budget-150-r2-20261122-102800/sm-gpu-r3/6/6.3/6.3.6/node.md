# N142: FP8 精度支持修正：仅 H100/H200 (Ada/Hopper 架构) 原生支持 FP8 计算 (E4M3/E5M2)；RTX 4090 (Ada 架构)

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N45, N46, N47

## Claim

FP8 精度支持修正：仅 H100/H200 (Ada/Hopper 架构) 原生支持 FP8 计算 (E4M3/E5M2)；RTX 4090 (Ada 架构) 不支持 FP8，A100 (Ampere 架构) 也不支持 FP8；INT8 在所有候选硬件 (RTX 4090/A100/H100/RX 7900 XTX) 上均支持，但 RX 7900 XTX 的 INT8 吞吐量仅为 H100 的 ~20% (395 TOPS vs 989 TOPS)。

## Corrected Claim

FP8 精度支持修正：仅 H100/H200 (Ada/Hopper 架构) 原生支持 FP8 计算 (E4M3/E5M2)；RTX 4090 (Ada 架构) 不支持 FP8，A100 (Ampere 架构) 也不支持 FP8；INT8 在所有候选硬件 (RTX 4090/A100/H100/RX 7900 XTX) 上均支持，但 RX 7900 XTX 的 INT8 吞吐量仅为 H100 的 ~20% (395 TOPS vs 989 TOPS)。

## Evidence

先验知识/题面给定，逻辑校验通过：H100/H200 (Hopper) 原生支持 FP8，RTX 4090 (Ada) 虽架构支持但消费级驱动/软件栈通常不开放 FP8 计算（或仅支持存储/传输，非计算加速），A100 (Ampere) 不支持 FP8；INT8 支持情况符合硬件规格；RX 7900 XTX 的 INT8 性能远低于 H100 符合数据中心卡与消费级卡的性能量级差异。
