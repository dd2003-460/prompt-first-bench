【执行前必读】
1. 本任务必须走 1-loop：先读 sop/arena-loop-pipeline.md + loop/prompt-first/00..04.5
2. 每阶段产出落盘 loop-artifacts/stages/<N>/
3. 完成后 commit + push
4. 通道故障 → 报告 Lead 降级，不得静默跳过

# PFB Gold-Gap 补全 — 任务卡 (v3)

## 目标
在**无答案泄漏**前提下（模型不得读取 gold/ 目录），通过"调研+实验+迭代优化"闭环，把 local-27b 全流程臂的分解树质量推到接近 gold（Total ≥ 0.80，且 M1/M4 均 ≥ S7V 基线）。不达标不结束，从失败的具体阶段回退调整 prompt 和工具。

## 背景（已确认事实，不用重查）
- v3 hardening 已完成: RESULTS-FINAL.md, S5=0.805 [0.762,0.841], S5-S0 Δ=+0.190 p=0.001** (stats-v3.json @ f876e1e)
- T23 诊断三层故障: ①检索层断供(bing跳转链假调研) ②judge M5 全零无区分度 ③gold 可达但需真实联网
- Q5 深挖发现 (2026-11-06): S8D-Q5 vs gold/Q5 差距在结构不在检索量——gold 有 L_comm 维度、C_FP/C_FN 空缺处理、SHARED 耦合识别、证据类型标注(S-a/b/c); 模型编造精度("MSE低10-30%")且 sources 只有 local-research 占位
- S8E pilot r2: M1≤S7V 但 M4>S7V (0.75 vs 0.52), 高方差 n=2
- research_hook v2 已有 arXiv API 双路查询; Q5 类方法论域召回差, 需补精准文献源

## 执行项（按阶段缺口入手，不从零）

### P1. Prompt patch (第三阶段缺口识别 + 叶子卡片)
- P1a: 分解 prompt 加"候选维度完备性检查"——对照决策论损失分解 (L_err/L_cost/L_comm/L_tail) 逐项核对, 缺哪个补哪个, 禁止自由发挥维度集
- P1b: 叶子卡片硬约束——场景未给定参数(如 C_FP/C_FN)必须进空缺清单, 禁止填默认值; 每个数值断言必须带真实 URL 或显式标"理论推导", 否则降级为定性描述
- P1c: 交叉验证要求两个独立口径(理论 vs 模拟/文献), 同源算一个

### P2. 调研层修复
- P2a: Q5 域补精准文献源 (Ioannidis 2005, p-hacking, 可重复性危机等经典文献), 写入 research_hook KNOWN_SITES 或专用 digest
- P2b: 验证 research_hook 对 Q5 的真实召回率 (跑一次 hook, 记录实际返回的 URL 列表)

### P3. 实验
- P3a: 新臂 S8G = S5 + P1 prompt patch + P2 调研源, 跑 Q1/Q4/Q5 × 2 rep
- P3b: 用 v3 judge 评分, 对比 S5/S7V/gold 三组

### P4. 迭代
- P4a: 若 Total < 0.80 或 M1/M4 < S7V, 定位失败阶段 (分解不到位? 缺口识别遗漏? 交叉验证没发现?), 回该阶段改 prompt/工具, 再跑一轮
- P4b: 最多 3 轮迭代; 每轮记录 delta 和归因

## 验收标准（量化）
- [ ] S8G 臂 Q5 Total ≥ 0.80 (bootstrap CI 下界 > 0.70)
- [ ] S8G 的 M1 ≥ S7V 基线 且 M4 ≥ S7V 基线
- [ ] 所有数值断言带真实 URL 或显式"理论推导"标签 (judge M5 重新启用后验证)
- [ ] 每轮迭代有归因记录 (loop-artifacts/stages/04/)
- [ ] commit + push

## 失败降级
- arena 不可用 → 本地 qwen3.8-27b 执行 (conf-0.2), 流程不降
- 某题域调研源确实缺失 → 该题标注 blocked-on-data, 用其余题域判定
- 3 轮迭代后仍 < 0.80 → 输出 gap-analysis 文档说明残余差距根因, 不强行宣称达标