# N56: H_static 的具体数值依赖：D_eff 的绝对影响取决于 H_static。若 H_static = 0.8（N28 假设），则 H_effective 

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N15

## Claim

H_static 的具体数值依赖：D_eff 的绝对影响取决于 H_static。若 H_static = 0.8（N28 假设），则 H_effective = 0.8 * 0.995 = 0.796，绝对下降 0.004。若 H_static = 0.9，则 H_effective = 0.8955，绝对下降 0.0045。

## Corrected Claim

H_static 的具体数值依赖：D_eff 的绝对影响取决于 H_static。若 H_static = 0.8（N28 假设），则 H_effective = 0.8 * 0.995 = 0.796，绝对下降 0.004。若 H_static = 0.9，则 H_effective = 0.8955，绝对下降 0.0045。

## Evidence

父节点级核验未通过：有冗余（子节点通过选取不同的 H_static 取值（0.95, 0.80, 0.50）来展示同一公式在不同参数下的结果，这属于同一维度的参数扫描，而非正交的独立概念分解。此外，子节点中 D_eff 的取值不一致（前两个用 0.9512，第三个用 0.995），导致对比基准不统一，削弱了纯粹展示 H_static 影响的逻辑连贯性。）
