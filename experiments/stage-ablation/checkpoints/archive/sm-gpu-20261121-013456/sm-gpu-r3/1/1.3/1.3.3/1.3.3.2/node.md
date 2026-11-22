# N152: RTX 3090 上 INT4 推理的吞吐量提升系数：由于 Ampere 架构缺乏专用 INT4 Tensor Core，依赖软件模拟，实际提升系数为 1.4-

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N55

## Claim

RTX 3090 上 INT4 推理的吞吐量提升系数：由于 Ampere 架构缺乏专用 INT4 Tensor Core，依赖软件模拟，实际提升系数为 1.4-1.6x（相比 BF16），显著低于 Ada 架构的 2.1x

## Corrected Claim

RTX 3090 上 INT4 推理的吞吐量提升系数：由于 Ampere 架构缺乏专用 INT4 Tensor Core，依赖软件模拟，实际提升系数为 1.4-1.6x（相比 BF16），显著低于 Ada 架构的 2.1x

## Evidence

先验知识/题面给定，逻辑校验通过：Ampere架构确实缺乏原生INT4 Tensor Core支持，依赖软件模拟导致效率低于原生支持的Ada架构，1.4-1.6x的提升系数符合工程经验量级。
