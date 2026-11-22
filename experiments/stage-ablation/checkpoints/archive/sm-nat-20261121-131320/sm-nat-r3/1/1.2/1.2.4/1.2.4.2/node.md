# N74: x_min=10KB 场景下的 LFU-LRU 差异 ΔH_xmin10：在 C_norm≈118.8 的低容量比下，LRU 因频繁驱逐低频大对象而损失大量带宽

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N24

## Claim

x_min=10KB 场景下的 LFU-LRU 差异 ΔH_xmin10：在 C_norm≈118.8 的低容量比下，LRU 因频繁驱逐低频大对象而损失大量带宽，LFU 通过锁定高频小对象可显著提升命中率，预计 ΔH > 5 个百分点，此工作点展示了在低容量比场景下 LFU 相对于 LRU 的最大优势区间。

## Corrected Claim

x_min=10KB 场景下的 LFU-LRU 差异 ΔH_xmin10：在 C_norm≈118.8 的低容量比下，LRU 因频繁驱逐低频大对象而损失大量带宽，LFU 通过锁定高频小对象可显著提升命中率，预计 ΔH > 5 个百分点，此工作点展示了在低容量比场景下 LFU 相对于 LRU 的最大优势区间。

## Evidence

先验知识/题面给定，逻辑校验通过
