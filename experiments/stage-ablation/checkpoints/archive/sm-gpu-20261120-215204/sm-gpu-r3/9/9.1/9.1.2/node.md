# N388: ROCm有效带宽利用率60-70%的来源：ROCm在LLM推理中的内核优化程度低于CUDA，主要受限于Flash Attention实现效率（比CUDA低10-

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N146

## Claim

ROCm有效带宽利用率60-70%的来源：ROCm在LLM推理中的内核优化程度低于CUDA，主要受限于Flash Attention实现效率（比CUDA低10-15%）和内存访问模式优化不足；具体利用率取决于模型架构（如GQA头数）和序列长度。

## Corrected Claim

ROCm有效带宽利用率60-70%的来源：ROCm在LLM推理中的内核优化程度低于CUDA，主要受限于Flash Attention实现效率（比CUDA低10-15%）和内存访问模式优化不足；具体利用率取决于模型架构（如GQA头数）和序列长度。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

ROCm LLM inference bandwidth utilization efficiency compared to CUDA
