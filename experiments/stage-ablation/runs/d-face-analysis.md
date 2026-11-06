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

## 根因假设（待验证）

1. **Research hook 搜索词偏 AI/ML**：ego-browser 搜索 prompt 是通用模板，
   对 CDN 定价/存储 TCO 这类非 AI 话题搜出来的源质量可能不够
2. **Memory hook 无跨域记忆**：S5 的 memory 积累全在 AI/ML 域，
   networking/storage 域没有历史经验可调用
3. **Prompt 模板假设 AI/ML 结构**：decomp-01 v3 的分解逻辑
   （先查后拆→找矛盾→按证据拆）可能对成本计算类问题不够适配

## 下一步

- [ ] 检查 research hook 实际搜到的 5 个源是什么（是否相关）
- [ ] 对比 Q6/Q7 的 pfb 输出 vs gold tree 的具体内容差异（定性分析）
- [ ] 如果搜索源质量是瓶颈 → 改进 search_query 或增加搜索轮次
- [ ] 如果 prompt 模板是瓶颈 → 为成本计算类问题设计专用 prompt variant
- [ ] 扩 n（每 rep 从 2→5）确认 0.446 不是小样本噪声