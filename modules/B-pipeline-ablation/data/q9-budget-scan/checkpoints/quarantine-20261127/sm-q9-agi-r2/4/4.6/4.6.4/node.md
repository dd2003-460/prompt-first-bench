# N82: 双重验证的时序约束：Self-Consistency 采样 (5x 推理) 耗时约 5-10 分钟，外部检索+相似度计算耗时约 2-5 秒；总验证开销约为原始生

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N26

## Claim

双重验证的时序约束：Self-Consistency 采样 (5x 推理) 耗时约 5-10 分钟，外部检索+相似度计算耗时约 2-5 秒；总验证开销约为原始生成时间的 3-5 倍，需在 Agent 工作流中异步执行，避免阻塞主推理链路。

## Corrected Claim

双重验证的时序约束：Self-Consistency 采样通常耗时显著高于单次生成（取决于模型与硬件），外部检索耗时较短；总验证开销通常为原始生成时间的数倍，建议在 Agent 工作流中异步执行以优化响应延迟。

## Evidence

[质询]数值量级缺乏普适性：Self-Consistency 的耗时高度依赖模型规模、硬件加速及并发能力，'5-10分钟'并非固定常数，且'总开销为原始生成3-5倍'这一比例关系在不同场景下波动极大，属于特定实验条件下的经验数据而非通用工程常量。 | source=knowledge，逻辑自洽（异步执行避免阻塞符合系统设计原则），但具体耗时数值和倍数关系属于经验事实，缺乏通用来源支持，故降级。

## Search Query

asynchronous validation pipeline latency overhead LLM agent workflow
