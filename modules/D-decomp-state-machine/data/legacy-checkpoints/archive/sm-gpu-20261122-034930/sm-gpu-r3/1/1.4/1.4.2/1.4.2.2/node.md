# N183: A100 40GB在INT8权重+INT8 KV Cache配置下，总显存需求为36.35GB（权重27GB + KV 5.35GB + 框架4GB），剩余3.

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N56

## Claim

A100 40GB在INT8权重+INT8 KV Cache配置下，总显存需求为36.35GB（权重27GB + KV 5.35GB + 框架4GB），剩余3.65GB用于临时激活值和CUDA Context，该余量在Batch=1时安全，但在Batch=2时激活值峰值可能超过余量，导致OOM，因此Batch size上限为1。

## Corrected Claim

在A100 40GB上运行INT8权重大模型时，若总显存占用接近上限（如剩余余量仅约3-4GB），Batch=1通常安全，但Batch=2时激活值显存需求翻倍可能导致OOM，因此Batch size上限可能为1。具体数值需根据实际模型架构和框架开销确定。

## Evidence

[质询]该陈述包含具体的硬件显存占用数值（权重27GB、KV 5.35GB、框架4GB）及特定模型配置下的OOM阈值，属于经验事实。虽然逻辑上Batch=2导致激活值增加从而可能OOM是合理的，但具体的显存分配数值（如框架固定占4GB、KV Cache精确到5.35GB）缺乏通用性，高度依赖于具体的模型架构（如层数、头数、序列长度）和推理框架实现，无法仅凭'A100 40GB'和'INT8'这一通用条件严格推导得出。 | 经验事实，逻辑自洽但缺来源支持。数值量级在A100 40GB范围内合理，但具体分配比例和OOM临界点依赖于未指定的模型细节，无法从第一性原理严格推出，故降级。

## Search Query

A100 40GB INT8 weight INT8 KV cache memory budget batch size limit
