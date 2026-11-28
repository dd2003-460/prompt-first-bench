# N18: 将科研循环分解为5个原子操作节点：HypothesisGen -> ExperimentDesign -> Execution(Compute/Retrieve

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N4

## Claim

将科研循环分解为5个原子操作节点：HypothesisGen -> ExperimentDesign -> Execution(Compute/Retrieve) -> Analysis -> ConclusionUpdate，其中Execution节点必须调用外部工具链（Python/SQL/API）而非仅靠LLM生成代码文本

## Corrected Claim

将科研循环分解为5个原子操作节点：HypothesisGen -> ExperimentDesign -> Execution(Compute/Retrieve) -> Analysis -> ConclusionUpdate，其中Execution节点必须调用外部工具链（Python/SQL/API）而非仅靠LLM生成代码文本

## Evidence

先验知识/题面给定，逻辑校验通过
