# N2: 精度选择与质量权衡：涵盖不同量化等级（BF16至W4）对推理质量的损耗评估、量化误差的可接受性论证，以及精度选择对显存占用和计算强度的耦合影响。

- **status**: verified
- **level**: L1
- **source**: given
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: (root)

## Claim

精度选择与质量权衡：涵盖不同量化等级（BF16至W4）对推理质量的损耗评估、量化误差的可接受性论证，以及精度选择对显存占用和计算强度的耦合影响。

## Evidence

父节点级核验通过：正交+完备+无冗余（三个子节点分别对应父节点定义的三个核心维度：1. 质量损耗（Perplexity/Hallucination），2. 显存占用（Memory Footprint），3. 计算效率/吞吐（Compute Intensity/Throughput）。三者视角独立，无逻辑重叠或矛盾，且完整覆盖了父节点中关于‘质量’、‘显存’、‘计算强度’的论述。）
