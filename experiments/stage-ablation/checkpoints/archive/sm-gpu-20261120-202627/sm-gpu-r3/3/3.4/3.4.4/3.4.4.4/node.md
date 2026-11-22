# N302: H100 80GB 的显存带宽 (HBM3) 规格确认为 3.35 TB/s，用于计算 KV Cache 读取的理论延迟下限，并与 N132 中的瓶颈模型结合，

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N82

## Claim

H100 80GB 的显存带宽 (HBM3) 规格确认为 3.35 TB/s，用于计算 KV Cache 读取的理论延迟下限，并与 N132 中的瓶颈模型结合，验证 H100 在 32K 上下文下的解码速度是否受带宽限制。

## Corrected Claim

H100 80GB 的显存带宽 (HBM3) 规格确认为 3.35 TB/s，用于计算 KV Cache 读取的理论延迟下限，并与 N132 中的瓶颈模型结合，验证 H100 在 32K 上下文下的解码速度是否受带宽限制。

## Evidence

先验知识/题面给定，逻辑校验通过：H100 80GB SXM5 版本的 HBM3 显存带宽官方规格确为 3.35 TB/s，数值量级与工程常识一致，且 source 标记为 knowledge，无需外部来源支持。
