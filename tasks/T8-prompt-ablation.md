# T8: loop/prompt-first 消融研究——哪些 prompt 真有用，哪些是表演

**状态**: ready（T7.1 跑完后开跑；依赖 T7.1 基线工件）
**执行通道**: arena agent mode @ prompt-first-bench（任务书走仓库，prompt 只指路）
**动机**（成璐 r31 指令）：leader/subagent 中间轮次要能区分"真发现矛盾/漏洞" vs "装模作样演示"；需要把 7 个阶段 prompt 逐条研究清楚——提升在哪、什么提示有用、什么是无意义负载。

## Part A: 中间轮次真实性审计（对已有工件做，不新跑）

对象：prompt-first-bench 仓内全部历史 loop-artifacts（含 T6 run1、T7.1、bench/self-opt-tester/run2-arena）。

审计协议（每个核验/复核类工件逐条过）：
1. **具体性测试**：每条"矛盾/漏洞/质疑"必须指向具体来源+具体字段（如"S35 的 $19/spot 与 S36 的 $2.50/spot 冲突"）。只有形容词没有锚点 = 表演。
2. **可证伪测试**：该矛盾是否真的被后续动作消解或保留？只写出来但从不跟进 = 表演。
3. **反事实测试**：把这条质疑删掉，结论会变吗？不会变 = 装饰性内容。
4. 输出：每工件一张表（条目 | 类型:真矛盾/真漏洞/表演 | 证据），落 `loop-artifacts/audit/T8-intermediate-rounds-audit.md`。

## Part B: 七阶段 prompt 消融设计（先出方案，跑法由 verdict 定）

方法：paired runs，同域同题，A 组全量 prompt，B 组删减版。删减候选（按可疑度排序）：
- 02 §2 ralph web-llm 强制命令段（arena 环境无 ralph，疑似无效负载）
- 04.5「通用原则」三节 12 条（与操作流程高度重叠，疑似冗余）
- 各阶段 Reviewer 质检标准（删后看 reviewer 行为是否退化）
- 01 候选集冻结声明（T6 已验证生效 → 对照组保留，作阳性对照）

度量（复用 bench r4 指标 M1-M7 + 新增）：
- M8 核验真实性率 = 真矛盾数/(真矛盾+表演)（Part A 协议打分）
- M9 token 效率差（A vs B 的 input 总量）
- 判定：删减后 M8 不降且 M9 显著升 → 该段是无意义负载，从 prompt 移除；M8 降 → 该段有用，保留并记录作用机制。

样本：≥2 域 × 2 配置 = 4 runs 起步（n=1 不出结论，bench r4 教训）。

## 验收标准

1. Part A 审计表覆盖全部历史核验工件，每条有具体性/可证伪/反事实三测结果
2. Part B 消融方案经一轮对抗核验（r29 标准：找方案漏洞追问至瓶颈）后才开跑
3. 产出 `loop-artifacts/audit/T8-prompt-ablation-report.md`：每段 prompt 的 verdict（有用/无用/未决 + 证据）
4. 无用段落实际从 workspace loop/prompt-first/ 移除并 sync bench 仓（走 commit+push）

## 失败降级

- arena 跑 paired runs 成本过高 → 先只做 Part A（纯审计，零额外 run），Part B 标 pending
- 单 run 超时 → 重跑 1 次，仍死标 VOID 换下一域
