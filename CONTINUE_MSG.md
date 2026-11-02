# CONTINUE_MSG — 2026-11-02 r217

## 本轮完成
**T7 v2 bench 数据修复收口**（decomp-bench 仓 @ main，r217/r217b 两 commit push）：
- **T7.4 gold v2 step span 修正**：r211 预拆分 G3→G3a/G3b、G6→G6a/G6b 时继承了父级相同 step span → mapping 启发式无法区分 V3/V5 归属（r213 R2=0.7 的 scorer-granularity artifact 未彻底消除）。本轮改各 split 成员独立区间（G3a=step-12→13 / G3b=step-13/14→15+ / G6a=step-27→28 / G6b=step-38→40），与 r213 报告分段一一对齐，无重叠 assert PASS。
- **T7.4 Lead 侧重打分**（executor 工件零改动）：receipt t74-blind-score-v2-r217.json — 映射全对齐 + V10 按 R2_precision_v2_rule 计 refinement 非 FP → R1 1.0 / R2 0.9（≥0.8 line）/ R3-R5 沿用 → **M8=1.0 PASS**；诚实注记 r213 原始口径 M8 0.925 亦 PASS，两口径结论一致。
- **T7.3 v2 重打分 receipt**（t73-blind-score-v2-r217.json）：R1-R5 方法锚点沿用 r208（M8 0.965 PASS，不依赖输入速率水平）；interval_hit 明确推迟到 v2 完整重跑——旧预测基于 v1 数据生成，拿它对 v2 gold 打分 = 让执行者为 Lead 的数据修复买单。
- T7 最终状态：4 域全 PASS + bench 构造缺陷清零。微信播报本轮 success:true。

## 当前状态
- decomp-bench @ main 9046610 pushed；pfb 侧 r211 后无新产出（G1b 仍 blocked-on-human 不变）
- C3 v3 描述层证据链闭合不变（G1a→G2→仲裁→独立复算五环齐）
- G1b family_check 仍 unknown，R5 PARTIAL-CLOSED，conf −0.1 不变

## 下一步
1. **G1b 升级（P1 唯一解锁项，卡成璐三选一）**：① 正常浏览器过一次 arena.ai 人机验证 → 我 CDP attach 跑 5 份 Direct 评分揭名；② 给任一非 Qwen API key（~5 调用按 r2 模板重打）；③ arena UI 能看到模型全名就直接登记
2. **T7 v2 完整重跑**（bench 闭环验证，~1h 本地降级通道）：执行侧用 v2 输入重跑 T7.3/T7.4，验收 interval_hit 恢复 + R2 新规则生效
3. **T8 C3 ablation 开跑**（产投比排序第一：P1 因果效应验证最强，方案已过 v3 对抗核验）——倾向此项
4. ACTIVE-candidates #4 ORF arXiv 手动上传 / #3 健康 strand 镜像源（均需人工或外部资源）