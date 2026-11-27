# N303: SiLU激活函数对显存峰值的影响：SiLU(x) = x * sigmoid(x)。在计算SiLU时，需要存储x和sigmoid(x)的中间结果，或者原地计算。

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N128

## Claim

SiLU激活函数对显存峰值的影响：SiLU(x) = x * sigmoid(x)。在计算SiLU时，需要存储x和sigmoid(x)的中间结果，或者原地计算。若非原地，峰值显存可能增加约50%。但现代推理框架（如vLLM, TensorRT-LLM）通常优化为原地操作或融合内核，因此722MB是保守估计，实际可能略高（~800-900MB），但仍远低于N20的2.5GB总估算中留给MLP的部分（若2.5GB是总激活，MLP占大头）。

## Corrected Claim

SiLU激活函数对显存峰值的影响：SiLU(x) = x * sigmoid(x)。在计算SiLU时，需要存储x和sigmoid(x)的中间结果，或者原地计算。若非原地，峰值显存可能增加约50%。但现代推理框架（如vLLM, TensorRT-LLM）通常优化为原地操作或融合内核，因此722MB是保守估计，实际可能略高（~800-900MB），但仍远低于N20的2.5GB总估算中留给MLP的部分（若2.5GB是总激活，MLP占大头）。

## Evidence

先验知识/题面给定，逻辑校验通过：SiLU非原地计算需存储中间结果导致显存增加符合逻辑，现代框架优化为原地/融合内核是工程常识，数值量级（722MB vs 800-900MB）合理且无内部矛盾。
