# origin: ai — 2026-11-07 下午 sub 讨论：先查后拆的机制 + M1 口径盲区

> 参与者：Lead (Qwen3.8-27B) + Sub "较真研究员" (同模型，独立 context)
> 触发：随机轮询 hook（第 2 次命中）+ Lead 主动 steer
> 状态：结论已出，可证伪实验待执行

## 问题

「先查后拆」（S5: R1分解→R2查矛盾→R3逐节点填→R4终审）比 S0（直接答）高 +0.235 分。减少幻觉的机制到底是什么？

四个候选：A=attention allocation / B=self-verification loop / C=source grounding / D=改变幻觉分布而非总量

## Sub 的判断（conf 标注为 sub 自评）

**主机制 = C（source grounding），B 是放大器，A 基本不成立，D 部分成立。**

### 排除 A 的理由（conf 0.9）

1. 分步执行后每轮 context 其实**更长**不是更短——R3 要带着 R1+R2 的全部产出干活
2. 我们自己的 S8E pilot 数据直接反驳：S8E 把验证指令内联进单条 prompt（context 最短最聚焦的变体），M1 反而 ≤ S7V（两遍调用）。如果"短 context → 低 token-level 幻觉率"成立，S8E 应该赢
3. RoPE/位置编码影响的是相对位置建模，跟断言对不对没关系

### C 是主机制的证据链

1. withTools pilot：M2 从 0.236→1.0 的增益来自"去读了 NVIDIA datasheet"——外部信息注入，不是认知改善
2. noTools 时 B 臂 M3（无源断言率）= 0.028（几乎全部有源标注）但 M1 只有 0.875——说明"标了来源"不等于"来源是对的"，但"强制标来源"这个行为本身减少了编造
3. PhantomFill (arXiv:2607.20492) 的反面印证：required **fields** → fabrication（因为模型被迫填空）；required **sources** → 减少 fabrication（因为模型被迫承认"我没查到"）

### B 是放大器

R4 终审提供了纠错机会，但没有 R4 时 C 的效果打折（错误不会被 catch）。证据：S5-full vs S5-noR4 的差异（待跑）。

### D 部分成立

在 M1（数字命中率）维度上，分步确实改变了幻觉分布——让错误集中在"没查到来源的节点"而非均匀散布。但在 M3（无源断言率）维度上，分步确实减少了总幻觉量。所以 D 是否成立取决于你测哪个维度。

## 第二问：M1 ±10% 能抓住系统性口径错误吗？

**不能。** Sub 翻了全部 30 个 Q1 run 的 judge 记录：
- "14x 带宽比"（900/64≈14倍）在 A 臂 6/6 次出现、C/E 臂多次出现
- Judge 几乎全判 correct（因为 900 GB/s 和 64 GB/s 各自都对 gold）
- 问题在于比值的方法论：NVLink 900 GB/s 是双向，PCIe 64 GB/s 是单向，直接除是口径混用
- ±10% tolerance 只检查单个数字是否在 gold 值附近，不检查"这个数字是怎么算出来的"

### 修复方向（M1b）

加一个 "单位/口径一致性" 子检查：judge 不仅判"数字对不对"，还判"这个数字的测量条件/单位/方向是否跟 gold 一致"。具体实现：gold tree 的每个叶子节点标注 measurement_condition（bidirectional/unidirectional/dense/sparse 等），judge 对比时检查 condition match。

## 我的判断（Lead）

- **认同 C 是主机制**。Sub 用 S8E pilot 数据反驳 A 的那一步很关键——这是用自己项目的内部证据做交叉验证，不是空谈。
- **认同 M1 抓不住口径错误**。这解释了为什么 A 臂 M1=0.856（v2 评分）但异族 judge 说它 fabrication 最多——A 臂的数字"对"但方法论错，M1 看到了"对"就给了分。
- **不确定 B 的贡献度**。需要跑 S5-noR4 消融才能定量。这个实验成本不高（改 prompt 去掉 R4 指令，跑 5 runs），可以加到 T51 的 step 列表里。
- **论文价值重新评估**：原来以为"先查后拆 = attention engineering"最有论文潜力，现在看真正的新贡献是 **"required sources vs required fields 的不对称效应"**——结构化 prompt 减少幻觉不是因为 attention 重分配，而是因为行为约束改变了模型的"承认不知道"阈值。这跟 PhantomFill 形成互补（他们测了 fields 方向，我们测 sources 方向）。

## 可证伪实验（下一步）

| # | 实验 | 区分什么 | 成本 |
|---|------|---------|------|
| E1 | S5-noR4（去掉终审）× 5 runs | B 的贡献度 | 低（改 prompt + 5 runs） |
| E2 | S5-noSource（R3 不要求标来源）× 5 runs | C 的贡献度 | 低 |
| E3 | M1b 口径一致性 judge × 现有 90 runs | M1 盲区量化 | 中（改 scorer + 重跑 M1） |
| E4 | Required-fields 对照臂（PhantomFill 复现）× 5 runs | 不对称效应的另一侧 | 中（新 arm + gold） |

E1+E2 合起来就能分解 C 和 B 各自的贡献。E3 直接量化 M1 盲区有多大。E4 是把我们的发现跟 PhantomFill 对接——如果 required-fields 臂确实 fabrication 更高而 required-sources 臂更低，不对称效应就确认了。

## 对 rubric v2 的影响

- M1 需要加 M1b（口径一致性），否则系统性方法论错误会持续漏过
- M3 的定义可能需要微调：当前 regex 对表格内"✓ 来源支持"的识别不够好（withTools run 实际 M3 应该更高）
- 新增 M7 候选："承认不知道的质量"——不是"说了我不知道"（M4 已覆盖），而是"在应该知道的地方承认不知道，在不该承认的地方没有过度弃权"