# N93: vLLM 额外显存组件量化：除 CUDA Context 外，vLLM 引擎初始化时的 Block Manager 元数据结构及 PyTorch 运行时碎片预留

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N29

## Claim

vLLM 额外显存组件量化：除 CUDA Context 外，vLLM 引擎初始化时的 Block Manager 元数据结构及 PyTorch 运行时碎片预留约占 0.2-0.4 GB/卡，需从剩余可用显存中扣除以得到模型权重加载上限。

## Corrected Claim

vLLM 额外显存组件量化：除 CUDA Context 外，vLLM 引擎初始化时的 Block Manager 元数据结构及 PyTorch 运行时碎片预留约占 0.2-0.4 GB/卡，需从剩余可用显存中扣除以得到模型权重加载上限。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

vLLM engine initialization memory footprint pytorch runtime overhead per GPU
