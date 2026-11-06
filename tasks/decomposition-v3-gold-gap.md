# Decomp: PFB Gold-Gap 补全 (v3)

> origin: ai · 2026-11-06 · goal: pfb-v3-gold-gap · 任务卡: tasks/v3-gold-gap.md @3ce999e
> 约束: 无答案泄漏 (模型不得读 gold/); 调研+实验+迭代闭环; 不达标不结束

## 分解树

```
gold-gap 补全 (Q5 Total>=0.80, M1/M4>=S7V, 无泄漏)
├── A. Prompt patch (第三阶段缺口识别 + 叶子卡片)     [正交: 改的是 prompt 文本]
│   ├── A1 维度完备性检查 (L_err/L_cost/L_comm/L_tail 逐项核对)
│   ├── A2 空缺强制 (未给定参数进空缺清单, 禁默认值)
│   └── A3 来源真实性门禁 (数值断言带真实 URL 或标"理论推导")
├── B. 调研层修复 (research_hook)                     [正交: 改的是工具/数据源]
│   ├── B1 Q5 域精准文献源 (Ioannidis 等经典文献)
│   └── B2 hook 召回率验证 (跑一次记录实际 URL)
├── C. 实验 (S8G 臂)                                  [正交: 消费 A+B 的产出]
│   ├── C1 S8G = S5 + A-patch + B-sources, 跑 Q1/Q4/Q5 × 2rep
│   └── C2 v3 judge 评分, 对比 S5/S7V/gold
└── D. 迭代 (<=3轮)                                   [正交: 消费 C 的结果]
    ├── D1 失败归因 (定位到 A/B/C 哪个子项)
    └── D2 回该子项修改, 再跑一轮
```

正交性自检: A(改prompt)⊥B(改工具)⊥C(跑实验)⊥D(迭代决策) —— 任意两项可独立变更而不影响另一项的实现。完备性: 从"当前臂输出"到"gold 质量"的因果链上, 只有 prompt 表达力(A)、信息供给(B)、测量(C)、反馈修正(D) 四个环节, 无遗漏。

## 缺口清单

| # | 子项 | 缺什么 | 状态 |
|---|------|--------|------|
| G1 | A1 | L_comm 维度的具体 checklist 措辞 (如何要求模型检查"沟通误读损失"而不泄漏 gold 结构) | [待核验] —— 需设计 prompt 使模型自主发现 L_comm, 不能直接写"加 L_comm"(那等于泄漏) |
| G2 | A3 | "真实 URL" 的判定标准 (judge 侧): 哪些域名算不可定位 (bing.com/ck/a 类)? 需要更新 gates.py/score.py 的 M5 逻辑 | [待核验] —— T23 已诊断 M5 bug, 但修复方案未实现 |
| G3 | B1 | Q5 域 (统计方法论/可重复性危机) 的高价值文献清单: 具体哪几篇? arXiv 还是普通期刊? research_hook 当前只查 arXiv API, 普通期刊 (Nature/Science/PNAS) 覆盖不了 | [待核验] |
| G4 | C1 | S8G 的完整 prompt 文本: A1+A2+A3 patch 后的最终 prompt 还没写 | [待核验] —— 依赖 A 完成 |
| G5 | C2 | gold 分数口径: RESULTS-FINAL 里 gold=1.0 是 self-score, S8G 与 gold 对比时用同一 judge 重评 gold 还是用存档分? | [待核验] —— 建议同 judge 重评保证可比 |
| G6 | D1 | 归因判据: Total 差多少算 A 的问题 vs B 的问题? 需要预设阈值规则 | [待核验] |

## 关键风险

- R1: A1 若直接写"检查 L_comm" = 泄漏 gold 结构 → 必须用通用原则表述 (如"对照决策论标准损失分解检查维度完备性") 让模型自己推出 L_comm
- R2: B1 若把 gold 引用的文献名写进 prompt = 变相泄漏 → 只能给领域关键词, 不给具体论文
- R3: n=2/题 方差大 (S8E pilot 已见 0.33→0.875 波动) → 验收看 CI 不看单点