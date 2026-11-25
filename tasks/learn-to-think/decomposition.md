# learn-to-think 分解树

# origin: ai · 2026-11-25 04:30 · D 微信 00:21 指令「让 qqbot 加个这样的目标，如果能思考得很好，离 AGI 就几乎更近了」

## 目标
让本地 27b + prompt/hook（不改权重）学会 D 式思考：第一性原理 → 机制层 → 可检验预言，
压缩-解压往返无损，带预言质量约束。D 的 taste 判据：general（=简洁压缩）+ 符合实际 + 有预言力。

## 分解树

```
learn-to-think
├── 01-mechanism  D 思考机制的第一性原理描述（无损）
│   ├── 假设已提出：残差驱动 + 压缩-解压往返无损 + 预言质量约束
│   ├── D 7 点修正已吸收（00:33 微信：tier 系统思考=对随机的适配，微扰下找精细差别）
│   └── [待核验] 无损性判据的可操作化（"唯一完整复现整个链路"如何度量）
├── 02-trigger    触发层：何时启动这套思考（think-trigger T1-T5）
│   ├── T1 stop_hook 反思注入 ✓（5 场景 pass）
│   ├── T2 接着考虑实验 ✓（域偏移 0/6 D机制域命中 → 触发词需域锚点）
│   ├── T3 judge 整合 ✓（formalism flip/shift 拆，align=flip×form）
│   ├── T4 spin 检测 ✓（12 session 0 误报）
│   └── T5 流程索引层 ✓（咒语=调度器，路由表初稿）
├── 03-experiment 核心实验：27b 能否接住 D 思考链往下推
│   ├── 输入：D 原话前半段（claude 会话 L320-399 调试大型工程排查思路）
│   ├── gold：D 后半段（只作判据，绝不泄露给 27b）
│   ├── 判据：爬到机制层 + 推出 ≥1 个 D 原文没有的可检验预言
│   └── [协议已锁 2026-11-25] 臂C 预注册 @ exp03-armc-prereg-20261125.md (5e6294aba): 域锚点+因果层指令, H1=flip 0→1 可证伪, 复用 T2 A/B 只新跑 C 3 次; 等 pilot 释放 8787
├── 04-eval       评测：如何判定"思考得像 D"
│   ├── formalism 维度（form 5.67/6 但 flip=0 → "形似神未到"）
│   ├── align 维度（flip×form，T3 新增）
│   └── [待核验] 预言质量的客观度量（D 01:06：等价于无损解压/可复现）
└── 05-generalize 泛化：从单题到跨域
    ├── 域锚点按问题域调整（T2 结论）
    └── [待核验] 跨域迁移条件（选域=校验公理成立范围）
```

## 正交性自检
- 01(机制是什么) ⊥ 02(何时触发) ⊥ 03(能否执行) ⊥ 04(如何评判) ⊥ 05(能否迁移)
- 完备性：机制→触发→执行→评判→迁移，覆盖"学会思考"全链，无遗漏子项

## 缺口清单
1. ~~[待核验] 无损性判据可操作化~~ → **已闭合**（lossless-criterion-operationalization.md：三元组 压缩比/ε_rep/ε_pred，结构对齐非逐字，03 协议已落）
2. [待核验] 27b 在 D 机制域的正面表现（T2 只有负信号 0/6）
3. ~~[待核验] 预言质量度量~~ → **已闭合**（= ε_pred，同上文件；04-eval 三维改为 压缩比/ε_rep[=align]/ε_pred）
4. [待核验] 跨域迁移条件——选域判据已有，但迁移后公理是否仍成立未验证

## 当前状态
- 01-mechanism：部分完成（假设 + D 修正已落盘 d-thinking-mechanism-first-principles-20261124.md）
- 02-trigger：完成（T1-T5 全落地，commits a34e187d7/e0cdbcf6d/7d2584ac6/9d37b2fa3/35d498b8a）
- 03-experiment：协议已锁（臂C 预注册 5e6294aba，runner 44350b270 dry-run 过；已入 post-pilot 队列 STEP4，等 pilot 释放 8787 后自动执行）
- 04-eval：设计完成（form/align 已有 + 预言质量=ε_pred 由 lossless-criterion-operationalization.md 闭合：04-eval 三维=(压缩比, ε_rep[=align], ε_pred)；待 Arm C 产出后跑评分）
- 05-generalize：待启动（前置=03 出结果）
- stage-gate 同步：00-decomp→05-accept 全推进（11-25 09:40-10:00，门禁逐项物理核验过）。**当前停在 05-accept，blocked 等 Arm C 数据**（队列 STEP4 自动跑 3 次调用→四维打分→verify.md 数据层回填→验收终判）。验收标准=爬到机制层∧ε_pred≥1/N，数据回填后执行。
