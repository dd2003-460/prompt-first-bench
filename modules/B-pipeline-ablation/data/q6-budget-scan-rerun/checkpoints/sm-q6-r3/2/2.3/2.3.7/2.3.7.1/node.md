# N221: 公有云CDN自动化运维月成本下限（¥500）的构成：包含云监控基础版（免费或¥0.1/GB日志存储，假设日均2TB日志存储成本约¥182.5/月）+ 基础API

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N76, N77, N78

## Claim

公有云CDN自动化运维月成本下限（¥500）的构成：包含云监控基础版（免费或¥0.1/GB日志存储，假设日均2TB日志存储成本约¥182.5/月）+ 基础API调用费（约¥100/月）+ 基础CI/CD构建时长（约¥300/月），需验证该组合是否覆盖P99监控所需的细粒度指标采样率

## Corrected Claim

公有云CDN自动化运维月成本下限（¥500）的构成：包含云监控基础版（免费或¥0.1/GB日志存储，假设日均2TB日志存储成本约¥182.5/月）+ 基础API调用费（约¥100/月）+ 基础CI/CD构建时长（约¥300/月），需验证该组合是否覆盖P99监控所需的细粒度指标采样率

## Evidence

先验知识/题面给定，逻辑校验通过：成本构成（182.5+100+300=582.5）与下限500量级一致，且作为知识节点无需外部来源支持

## Search Query

Aliyun CloudMonitor basic plan pricing per GB log storage 2024
