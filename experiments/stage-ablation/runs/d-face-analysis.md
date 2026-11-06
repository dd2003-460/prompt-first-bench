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

## 根因确认（已验证）

**Research hook 搜索源全部不相关。** Q6 的 5 个源全是 arXiv 论文（量子行走/DNN 推理/K8s/语言栈/网络优化），没有一个实际 CDN 定价页。Q7 类似（纠删码/tokenizer/后量子/视觉/因果存储），没有阿里云 OSS 或 S3 价目表。

pfb 在不相关的源上硬生成 12K chars 结构化输出（29-38 sections），但具体数字全来自模型权重而非真实数据。Gold tree 里的 ¥0.21/GB、$28/TB、PUE 1.2 等值不可能从这些源提取。

**这是 D 面 FAIL 的直接原因，不是 prompt 模板问题。**

### 待修

- [ ] Research hook 搜索策略：当前 ego-browser 搜索偏学术源，需要加商业定价站权重
- [ ] 搜索 query 质量：QUESTIONS dict 里的 search_query 可能不够精确
- [ ] 修复后重跑 D 面（同 Q6/Q7，n=2→5）