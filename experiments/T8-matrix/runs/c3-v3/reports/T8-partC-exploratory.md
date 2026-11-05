# T8 Part C 可解释性加速：top-k 嫌疑段归因的探索性证据

**状态**: exploratory-closed（r245s · 2026-11-02）
**origin**: ai（依据成璐 m01140 自主收口；纯文档产出，可回滚）
**数据面**: pfb `experiments/T8-matrix/runs/c3-v3/`（R6 36 run + R5 D3 18 run，J1/J2 双判 qwen3.8-27b）
**定位**: 方向性发现。非确认性结论，不可用于功效声明或跨域泛化断言。

---

## 一、主发现（只报方向，不报效应量）

### F1 · freeze 段的主效应三域一致为负
删掉 freeze 段（B-nofreeze）相对完整配置（A-full），truth 均分下降：
- R6 (D1+D2)：Δtruth = A-full − B-nofreeze = **+0.8175**（4 pair 全同向）
- R4 (J1v11 口径)：+0.35
- R5 (D3)：+0.779

三轮独立执行方向全部指向"删 freeze 显著降 truth"。幅度跨轮波动大（0.35→0.82/0.78），故**只报方向**。这是 Part C 的核心价值主张：freeze 是 7 段 prompt 中可优先保留的高价值段，消融预算可以集中到其余段。

### F2 · sham-freeze 段近乎无害
sham 组（内容无关填充的 freeze 段）J1 均分 0.875，与 A-full 的 0.929 接近；而 B-none（全删）J1 均分 0.0（4/4 run 全 fail）。说明评分差异主要来自 evidence/freeze 的**功能性内容**，而非 token 长度——单纯占位不贡献价值。

### F3 · cover 门槛在 D1/D2 激活
低 cover 集中在 B-nofreeze (0.742) / B-2del-fo (0.62)，未覆盖项全是交付物类核验点（推荐方案/淘汰理由/成本明细）。即删 freeze 漏的是"报告结构件"而非约束条件——与 R5 D3 的发现（freeze 管数值阈值覆盖）互补：**freeze 同时管住结构完整性与规格覆盖**。

### F4 · C2 行为代理操纵检查通过
B-nofreeze 的冻结声明率 0.0，其他所有 config 均值 1.0——删除在行为层确实生效，排除了"模型换种方式补偿冻结"作为 M8 下降的唯一解释。

### F5 · B-2del-fo 被行为污染，只作下界
3/4 run 输出 <400 字符（模型跟随残留 web-llm 指令只发命令不产报告），其分数代表"未完成报告"，该 config 的消融结论不作正向引用。

## 二、核心警示：高 cover ≠ 真核验

独立宽松复算（receipt-r7-cover-recompute）显示：
- B-none：truth = **0.0417** 但 cover_loose = **0.913**
- 全矩阵 truth×cover 相关：Pearson r = 0.634, Spearman ρ = 0.683（n=9 configs）

两个指标未按同一机会集绑定，所以覆盖率数字**只能作描述性统计**，不能用于跨 config 排序的最终判定。任何基于 M8-cover 单独得出的"通过"结论都需联合 truth 读数。

## 三、诚实边界（五条硬限制）

1. **非确认性**：n=6/cell（R6 4 + R5 2），功效不足，所有 Δ 只报方向。
2. **指标口径未冻结**：cover 与 truth 分母不一致（见上节警示），两版 cover 命中规则不同导致跨轮不可比。
3. **同族评审**：J1/J2 均为 qwen3.8-27b（仅 prompt 面不同），一致性指标只反映同族内部稳定度。rubric v2 重放实测一致率 0.661 < 0.85 门槛（pfb @ cea07e9），J2 对 A-full/B-2del-eo 恒打 1.0 分不开好坏配置——异源 judge 到位前，双判交叉验证能力有限。
4. **无真正 hold-out 域**：D1/D2/D3 均参与 top-k 选择，跨域泛化声明降级为"既定三域内"。
5. **阳性对照不完整**：X5 mutated 工件存在内部矛盾（对抗核验 partial 3），敏感度验证未闭环。

## 四、失败模式清单（两轮对抗核验原样附录）

来源：`calibration/receipt-c3v3-adversarial-r243.md`（v2 · arena @ ba84c0b）

| # | 判定 | conf | 要点 | 修复方向 |
|---|------|------|------|---------|
| 1 | FAIL | 0.97 | 分母漏洞：truth 按模型自产条目打分，遗漏不进分母 → 高 cover 可规避 | 独立标注员预建冻结机会表；M8-fixed = Σ[机会被实际核验且结论正确]/\|冻结集\|，逐机会联合判定 |
| 2 | FAIL | 0.97 | cover 口径 gap：r6 五组 1.0 vs r7 复算 0.90-0.975 不可比；seeda/seedb 分母 9 vs 10 项 | seedc 前冻结归一化；每项 2-3 个人工确认等价 pattern；盲双判复核；旧结果标探索性 |
| 3 | partial | — | C1 地板吞吐 24-64 min/题，探针量现实性存疑 | Lead 定：硬门禁 vs 降级为 top-k 抽验 |
| 4 | partial | — | 预注册 n=9 power 缺 δ/方差/独立任务数；实际 8 run 非 9 | 补 preregistration 三要素 + hash |
| 5 | partial | — | 阳性对照 X5 有实质风险但内部矛盾 | 原件 diff + 下游影响证明 |
| 6 | partial | — | holdout 域：D1/D2/D3 均参与选择 | 新 D4 或放弃跨域声明 |

横向门禁（第二轮新增）：J1/J2 同族，family_check BLOCKED——异源评审硬门槛未过。

## 五、下一步：确认性实验的解锁条件

seedc 功效 run（9 configs × D1/D2 各加 seedc = 18 run + 双判 36 调用）**四条全满足才启动**：

1. 异源判官到位（≥1 个非 Qwen 家族 API key）→ 过横向门禁
2. M8-fixed 逐机会标注完成（独立标注员 + 双盲复核）→ 堵 FAIL 1
3. cover 口径冻结（每项 2-3 个等价命中 pattern，机判 assert）→ 堵 FAIL 2
4. APPROVALS #2 预算放行

缺任何一条，维持本文档的探索性表述，不升级结论。

## 六、来源回执

- `runs-r6/receipt-r6-mainanalysis.json`（主分析，F1-F5）
- `receipt-r7-cover-recompute.json`（独立 cover 复算，第二节警示）
- `receipt-r7-c2-behavior-proxy.json`（C2 操纵检查，F4）
- `calibration/receipt-c3v3-adversarial-r243.md`（两轮对抗核验，第四节）
- pfb `calibration/receipt-r7-rubric-v2-replay.json` + `RUBRIC-V2-REPLAY-ANALYSIS.md`（rubric v2 重放，第三节 3）