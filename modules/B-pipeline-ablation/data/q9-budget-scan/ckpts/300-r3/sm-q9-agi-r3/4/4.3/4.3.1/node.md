# N83: 科研循环单次调用的Token消耗量分解：Input_Tokens = System_Prompt(约1500) + RAG_Context(平均5000, 受限

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N22, N23, N24

## Claim

科研循环单次调用的Token消耗量分解：Input_Tokens = System_Prompt(约1500) + RAG_Context(平均5000, 受限于N15检索权重) + History_Turns(线性增长，假设平均5轮对话约3000)，Output_Tokens = Reasoning_Trace(约800) + Final_Answer(约500)，总Tokens ≈ 10800/循环

## Corrected Claim

科研循环单次调用的Token消耗量分解：Input_Tokens = System_Prompt(约1500) + RAG_Context(平均5000, 受限于N15检索权重) + History_Turns(线性增长，假设平均5轮对话约3000)，Output_Tokens = Reasoning_Trace(约800) + Final_Answer(约500)，总Tokens ≈ 10800/循环

## Evidence

父节点级核验未通过：不完备, 有冗余（子节点实质上是同一公式在不同输入规模下的两个实例（短上下文 vs 长上下文），属于连续变量的离散采样而非正交维度分解；同时，父节点明确指出的‘平均5轮对话’基准场景未被单独覆盖，导致对‘标准/基准’工作点的描述缺失。）

## Search Query

vLLM typical token usage per turn scientific reasoning benchmark
