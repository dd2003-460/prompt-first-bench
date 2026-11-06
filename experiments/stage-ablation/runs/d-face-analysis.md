# D 面盲测：pfb S5 跨域泛化 — Q6/Q7 vs Gold Tree

> 日期: 2026-11-07 | Pipeline: S5 (memory hook) | Model: qwen3.8-27b | Commit: pending

## 一句话结论

pfb S5 pipeline 在 AI/ML 域外（networking/storage）gold tree 覆盖率仅 0.446，
远低于 D3 门禁 0.70。**跨域泛化是当前最大短板**——pipeline 能打赢同域开源
（C 面 Δ+0.147 显著），但换到没见过的知识域就掉到不及格。

## 数据

### 逐 run 覆盖率

| Run | 域 | Coverage | Covered/Total | D3 Gate (≥0.70) |
|-----|------|----------|---------------|-----------------|
| Q6-r1 | networking | 0.424 | 14/33 | ❌ FAIL |
| Q6-r2 | networking | 0.333 | 11/33 | ❌ FAIL |
| Q7-r1 | storage | 0.553 | 21/38 | ❌ FAIL |
| Q7-r2 | storage | 0.474 | 18/38 | ❌ FAIL |
| **Overall** | | **0.446** | | **❌ FAIL** |

### 系统性遗漏模式

两题共同漏掉的节点类型：
1. **换算系数/归一化因子**（Q7 N-1.1~N-1.4: EC 冗余、元数据开销、预留水位、快照保留率）
   — pfb 输出直接拿硬件 $/TB 当答案，没做有效容量换算
2. **长尾/边缘场景**（Q6 N-7.1~N-7.3: 分流比、双跑最低消费、海外单价上浮）
   — pfb 只覆盖主流路径，不探索边界条件
3. **运维隐性成本**（Q6 N-5.3/N-5.4, Q7 N-6.3/N-6.4: 监控/DDoS/备件/巡检）
   — pfb 偏重直接采购价，忽略运营侧
4. **RTO/可用性代价**（Q7 N-7.3/N-7.4/N-7.5: 回灌时间、每小时业务代价、云取回等待）
   — pfb 纯成本视角，缺可用性维度

### 与 C 面对比

| 维度 | C 面（同域） | D 面（跨域） |
|------|-------------|-------------|
| 域 | AI/ML (Q1-Q5) | networking + storage (Q6-Q7) |
| 指标 | M1-M4 judge score | Gold tree leaf coverage |
| S5 分数 | 0.7907 | 0.446 coverage |
| 对手 | D1 (GPT Researcher) 0.644 | Gold tree (人工构建) |
| 结论 | S5 显著赢 D1 | S5 远不及 gold |

**解读**：C 面的"赢"是相对赢（比 GPT Researcher 好），D 面的"输"是绝对输
（离人工 gold 还差一半）。两个结论不矛盾——pfb 在同域内确实有优势，但这个
优势不随域迁移。

## 根因确认（v2 修正）

**v1 假设（搜索源不相关）→ 已修复但无效。** 给 Q6/Q7 加了 KNOWN_SITES（AWS CloudFront/Aliyun OSS 等真实定价页）后重跑，coverage 从 0.446 → 0.457，基本不变。

**真正根因：模型能力上限。** 即使 prompt 里注入了真实定价页内容（AWS CloudFront ¥/GB、阿里云 OSS 分层价格），27b 仍然：
1. 没有把 gold tree 里的换算系数（EC 冗余 1.375、元数据开销 1.05、预留水位 1.25）独立识别为叶子节点
2. 没有探索边缘场景（分流比、双跑最低消费、海外单价上浮）
3. 没有覆盖运维隐性成本（监控/DDoS/备件/巡检）和 RTO 维度

**结论：D 面 FAIL 是 27b 模型在跨域成本计算任务上的能力天花板，不是 pipeline 可修的 bug。** 要过 D3 gate (≥0.70)，需要更强模型（70B+）或针对成本计算类问题的专用 prompt variant（显式要求列出所有成本组件 + 换算系数）。