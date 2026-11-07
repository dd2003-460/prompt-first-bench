# 先查后拆机制深聊 + M1 口径盲区（sub 讨论记录）

> origin: ai · 2026-11-07 · sub sa-c24c95f7（较真研究员 persona）× Lead 深度讨论
> 触发：随机轮询 hook + 成璐问"分解究竟轻松吗"

## 问题原文

1. 「先查后拆」减少幻觉的机制到底是什么？A(attention) / B(self-verification) / C(source grounding) / D(改变分布) 哪个？
2. M1 ±10% tolerance 能抓住 io.net 式"14x 口径混用"这种系统性方法论错误吗？

## Sub 核心判断

### 机制：C 主 + B 放大 + A 不成立 + D 部分成立

- **A 排除**：分步后 context 更长不是更短（R3 带着 R1+R2 全部产出）。S8E pilot 直接反驳（最短 context 变体 M1 反而最低）。RoPE 层面跟断言正确性无关。conf 0.9。
- **C 主机制**：withTools M2 增益来自"读了真 datasheet"（外部信息注入）；arXiv:2602.04853 标题即"Decomposed Prompting Does Not Fix Knowledge Gaps, But Helps Models Say I Don't Know"——分解不修知识缺口，只提高拒答率。
- **B 放大器**：R4 能 catch 的前提是 R3 已标来源。无 C 只有 B → 只能抓自相矛盾，抓不了参数化记忆的系统性错误。
- **D 部分成立**：noTools B 臂 6 run 中 4 个提到 14x，其中 2 个在自我纠错语境中（M1=0.700/0.545），2 个完全不提（M1=0.889/0.600）。方向支持"结构改变错误分布形态"。当前 M1 只判 final，分不清"真减少"vs"被拦截"。

### M1 口径盲区（已确认，非理论担心）

Sub 核对了 s10-scores-v2.json 全部 30 个 Q1 run judge 原文：
- A 臂 6/6 写了"NVLink 900 ÷ PCIe 64 ≈ 14x"，judge 全判 correct
- C/E 臂多次出现，同样放行
- 根因三层：① M1 逐断言判，错误在断言间关系中；② gold-Q1.md 把"14倍差距"当注脚而非陷阱；③ judge 自身也是 LLM，同源误差

### Rubric 修复方案（sub 提案，未验证）

1. 断言 schema 加 unit-dimension 四元组 (quantity, value, direction, scope)
2. 比值一致性检查（纯规则，不用 LLM）：A/B 得 X 时校验 A.direction==B.direction
3. gold 加口径锚点：数值对但口径不一致 = mismatch
4. judge 加 trap-aware 指令 + 已知陷阱清单

⚠️ 判分校准提醒：现有 90 run 的 M1 在新口径下会整体重算，跨版本比较前必须全量重评。

## 可证伪实验（按区分力排序）

| 编号 | 设计 | 区分什么 | 成本 |
|------|------|----------|------|
| E1 | Sham-decomposition：S5 结构但 R2/R3 给假来源 | C vs A/B | 中（需构造 sham 来源） |
| E2 | 消融 R4：S5 去掉终审 | 隔离 B | 低（改 prompt） |
| E3 | 双轨评分：final-only vs 全程断言 | D（真减少 vs 被拦截） | **最低**（score.py 加参数） |
| E4 | Rubric 敏感性探针：合成口径错误输出跑 M1 | 量化 false-negative 率 | 低 |

**我的判断**：E3 优先做——改动最小、回答的问题最核心（"+0.235 里多少是真减少"）、且直接暴露 rubric 的结构性盲区。E1 最有学术价值（回应 PhantomFill 反方）但构造 sham 来源有难度。

## 对后续工作的影响

1. **Rubric v2 → v2.1**：加 M1b "measurement condition consistency" 维度（或 M1 内加 ratio-consistency check）。现有分数需重算。
2. **E3 实验**：排入下一个 goal（pfb-rubric-v21 或并入 c1c3-paired-test 的补充分析）。
3. **Gold tree 修订**：Q1 gold 的"常见误读"节从注脚升级为判据（trap list）。
4. **论文 related work**：arXiv:2602.04853 + PhantomFill + CoT Obscures 三篇构成"为什么分步走有效/无效"的文献三角，值得在 discussion 节展开。

## 不确定点

- E1-E4 都是设计提案，没跑过
- arXiv:2602.04853 只确认了标题存在性，摘要没读全文（conf 降半）
- "sham 引用会不会反而降低 M1"没有先验把握（PhantomFill 说 required fields 诱发编造，但 sham 是自填字段，可能触发 self-consistency 优势）