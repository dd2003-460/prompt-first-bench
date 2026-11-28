# N18: 数据流采用事件驱动架构，每个科研步骤产生结构化事件（如HypothesisGenerated, ExperimentCompleted），事件队列持久化到SQL

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N2

## Claim

数据流采用事件驱动架构，每个科研步骤产生结构化事件（如HypothesisGenerated, ExperimentCompleted），事件队列持久化到SQLite，支持断点续传和并行分支探索，单个事件的处理时间为1-10ms，队列吞吐量>100 events/sec。

## Corrected Claim

数据流采用事件驱动架构，每个科研步骤产生结构化事件（如HypothesisGenerated, ExperimentCompleted），事件队列持久化到SQLite，支持断点续传和并行分支探索，单个事件的处理时间为1-10ms，队列吞吐量>100 events/sec。

## Evidence

先验知识/题面给定，逻辑校验通过
