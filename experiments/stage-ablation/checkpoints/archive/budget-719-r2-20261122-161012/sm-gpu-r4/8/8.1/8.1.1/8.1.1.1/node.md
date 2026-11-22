# N665: Apple M3 Ultra 实测有效带宽修正：在 LLM 推理负载下，由于内存控制器调度与 DRAM 访问模式，实际有效带宽约为标称值的 85-90%；取 8

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N275

## Claim

Apple M3 Ultra 实测有效带宽修正：在 LLM 推理负载下，由于内存控制器调度与 DRAM 访问模式，实际有效带宽约为标称值的 85-90%；取 800 GB/s * 0.875 ≈ 700 GB/s 作为 Decode 阶段的有效带宽上限，用于计算理论吞吐量。

## Corrected Claim

Apple M3 Ultra 在 LLM 推理负载下的实际有效带宽受内存控制器调度与 DRAM 访问模式影响，通常低于标称值；在缺乏具体实测数据的情况下，建议采用保守估计（如 70-80%）或明确标注为理论上限估算，而非固定为 85-90%。

## Evidence

[质询]85-90% 的有效带宽效率是一个经验性估算值，缺乏针对 Apple M3 Ultra 在 LLM 推理负载下的具体实测数据支持，且不同内存控制器和访问模式下的效率波动可能较大，该数值可能过于乐观或不符合特定场景。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

Apple M3 Ultra effective memory bandwidth LLM inference benchmark GB/s
