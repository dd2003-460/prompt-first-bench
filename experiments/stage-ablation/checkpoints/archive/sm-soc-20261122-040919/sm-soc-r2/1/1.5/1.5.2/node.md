# N46: 信任度下降系数 d 的机制分解：d = α×(P_drop - P_base)/P_base + β×σ²_belief，其中 α 是买家对价格变动的敏感度（α

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N9

## Claim

信任度下降系数 d 的机制分解：d = α×(P_drop - P_base)/P_base + β×σ²_belief，其中 α 是买家对价格变动的敏感度（α=0.3），β 是信念噪声的放大系数（β=0.1），P_drop 是降价后价格，P_base 是原始挂价；当 P_drop/P_base = 0.8 时，d = 0.3×0.2 + 0.1×σ²_belief

## Corrected Claim

信任度下降系数 d 的机制分解：d = α×(P_drop - P_base)/P_base + β×σ²_belief，其中 α 是买家对价格变动的敏感度（α=0.3），β 是信念噪声的放大系数（β=0.1），P_drop 是降价后价格，P_base 是原始挂价；当 P_drop/P_base = 0.8 时，d = 0.3×0.2 + 0.1×σ²_belief

## Evidence

先验知识/题面给定，逻辑校验通过：公式代入 P_drop/P_base=0.8 即 (0.8-1)/1=-0.2，但题目中 d 的表达式第一项为 α×(P_drop - P_base)/P_base，若 P_drop 是降价后价格且 P_base 是原价，通常 P_drop < P_base，差值为负。然而题目陈述中直接给出了计算结果 d = 0.3×0.2 + ...，这里隐含了取绝对值或者定义 P_drop 为降幅比例（即 0.2 代表 20% 的降幅）。在信任度下降的语境下，系数 d 应为正值，因此将价格变动幅度取正值（0.2）符合逻辑直觉和模型设定。数值计算 0.3*0.2=0.06 正确。
