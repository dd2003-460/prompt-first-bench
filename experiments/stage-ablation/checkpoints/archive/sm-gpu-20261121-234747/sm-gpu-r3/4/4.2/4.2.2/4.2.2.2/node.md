# N297: 软件/驱动参数（如CUDA版本, vLLM版本）的'重大更新'量化阈值定义为：若版本号发生次级（Minor）以上变更（如12.4 -> 12.5或13.0），或

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N106

## Claim

软件/驱动参数（如CUDA版本, vLLM版本）的'重大更新'量化阈值定义为：若版本号发生次级（Minor）以上变更（如12.4 -> 12.5或13.0），或Changelog中标记为'Breaking Change'或'New Feature: FP8 Support'，则视为架构级变更，置信度强制降为'低'。

## Corrected Claim

软件/驱动参数（如CUDA版本, vLLM版本）的'重大更新'量化阈值定义为：若版本号发生次级（Minor）以上变更（如12.4 -> 12.5或13.0），或Changelog中标记为'Breaking Change'或'New Feature: FP8 Support'，则视为架构级变更，置信度强制降为'低'。

## Evidence

先验知识/题面给定，逻辑校验通过
