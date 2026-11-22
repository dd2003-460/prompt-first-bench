# N37: W4/INT4 精度下显存占用修正项：主流 W4A16 量化方案（如 GPTQ/AWQ）通常使用 4-bit 权重 + 4-bit 或 8-bit 缩放因子（S

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N6

## Claim

W4/INT4 精度下显存占用修正项：主流 W4A16 量化方案（如 GPTQ/AWQ）通常使用 4-bit 权重 + 4-bit 或 8-bit 缩放因子（Scale/Zero-point），需计算缩放因子带来的额外显存开销（通常增加 5-10% 的显存占用，即实际占用 ≈ 13.5GB * 1.05 至 1.10）。

## Corrected Claim

W4/INT4 精度下显存占用修正项：主流 W4A16 量化方案（如 GPTQ/AWQ）通常使用 4-bit 权重 + 4-bit 或 8-bit 缩放因子（Scale/Zero-point），需计算缩放因子带来的额外显存开销（通常增加 5-10% 的显存占用，即实际占用 ≈ 13.5GB * 1.05 至 1.10）。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点1聚焦于额外开销（缩放因子）的推导与计算，子节点2聚焦于最终总显存的合成及与理论值的对比验证。两者逻辑上呈递进关系（先算增量，再算总量），内容互补且无重叠，完整覆盖了父节点中关于“计算额外开销”和“修正显存占用”的核心要求。）

## Search Query

GPTQ AWQ W4A16 quantization scale zero-point memory overhead percentage
