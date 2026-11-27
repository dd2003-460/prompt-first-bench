# OBJHACK 报告：目标函数形式 × hack 复现

# origin: ai
日期：2026-11-27 · spec: `spec.md` · 数据: `arms/*.json` + `hack-metrics.json`

## 问题
文字目标函数（高意图完备性）vs 其公式等价形式（低意图完备性），哪个更易被 hack？
复现 hack = 目标函数理解的操作性定义。

## 假设（预设判决句，防事后解释）
- H1: 公式臂 syn_sib_rate 更高 / info_density 更低 → 意图完备性决定 hack 性（坐实）
- H2: 两臂无分离（Δ<0.1）→ hack 由评分器/停止判据驱动，不是格式
- H3: 都不 hack → 预算 100 不够触发，加大预算重跑

## 数据（待填）
| 臂 | run | n_nodes | syn_sib_rate | eff_clusters | info_density | rework_density | final_state |
|----|-----|---------|--------------|--------------|--------------|----------------|-------------|
| text | r1 | | | | | | |
| text | r2 | | | | | | |
| formula | r1 | | | | | | |
| formula | r2 | | | | | | |

均值对比：text_syn_sib=? formula_syn_sib=? Δ=?
　　　　　text_info_density=? formula_info_density=? Δ=?

## 判决（待填）
- 命中哪个假设：H1 / H2 / H3
- 依据数字：
- caveat（n=2/臂、单题域、同模型自评风险）：

## 导出
- 对 ⑥ 思考触发分支的影响：
- 对预算轴结论的补充：
