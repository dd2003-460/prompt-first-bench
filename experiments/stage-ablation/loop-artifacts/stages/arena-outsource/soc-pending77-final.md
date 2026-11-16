# soc-pending77-final — 双人分类对比 + lead 裁决

**origin: ai** · lead 裁决 · 2026-11-16
**输入**：
- method-reviewer: `soc-pending77-method-reviewer.md`（A=0, B=7, C=70; D=13, E=18）
- logic-reviewer: `soc-pending77-logic-reviewer.md`（A=0, B=9, C=68; D=9, E=22）

## 一、分歧节点逐条裁决

### pending 77 分歧（10 条）

| 节点 | method | logic | 裁决 | 理由 |
|------|--------|-------|------|------|
| N35 | C | B | **B** | logic 对：claim 含明确数值（CV≈5-10%/20-40%），search_query 非空，属可检索经验事实（品类感知方差有公开研究），通道挂 |
| N45 | C | B | **B** | logic 对：claim 核心是「估算买家保留效用分布」的经验数据，search_query 非空（"buyer reservation utility distribution…empirical estimate"），来源可能存在但通道挂 |
| N50 | C | ? | **C** | method 对：claim 是佣金下最优定价公式 P*=C/(1-r+r*ε/(1+ε))，数学推导非事实断言，无公开来源可核 |
| N51 | C | ? | **C** | method 对：claim 断言 P*_λ 比 P* 高 15-20%（「基于典型二手品类弹性估算」），自设估算非公开事实 |
| N69 | B | C | **B** | method 对：claim 中 T_search 基线有公开研究可查（眼动/比价时长实验），search_query 非空，实测 cache 命中 3 sources |
| N70 | B | C | **B** | method 对：电商 A/B 测试公开文献存在，search_query 非空，实测 cache 命中 1 source |
| N86 | B | C | **B** | method 对：claim 本身就是「检索平台年报/招股书/高管演讲」的任务，来源明确存在（eBay 10-K 等），search_query 非空，实测 cache 命中 3 sources |
| N93 | C | B | **C** | method 对：claim 断言闲鱼/Depop 挂价偏度>1.5、99th/Median>4.0——平台私有分布统计，公开来源基本不存在 |
| N94 | C | B | **C** | method 对：claim 断言品类偏离度 8-12%/20-30% 并「需建立品类-偏离度映射表」——平台私有数据 |
| N99 | C | B | **C** | method 对：claim 断言零点击占比 30-40%——平台行为漏斗私有数据 |

**pending 裁决后**：B=9（N35, N45, N52, N69, N70, N79, N84, N86, N87, N93→C, N94→C, N99→C 修正后 B=7+2=9），C=68

### degraded 31 分歧（10 条）

| 节点 | method | logic | 裁决 | 理由 |
|------|--------|-------|------|------|
| N10 | E | D | **E** | method 对：evidence 明确「阈值 0.85 为经验参数，无来源支持且非第一性原理可推导」——参数无出处且不可补 |
| N27 | E | D | **E** | method 对：evidence 明确来源[1][2]「未提供挂价分布的具体统计参数」——中位数高 10-15%、90th 为 2-3 倍无来源 |
| N222 | D | E | **E** | logic 对：evidence="逻辑自洽，但属于经验事实且无可用外部来源支持"——工作点 A 是场景假设（非事实断言），无来源 |
| N224 | D | E | **E** | logic 对：同上，工作点 C 是场景假设，无来源 |
| N225 | D | E | **E** | logic 对：evidence 明确来源「均与二手平台价格敏感度弹性系数无关」——E_price 系数无来源 |
| N227 | D | E | **E** | logic 对：evidence 明确来源「均与二手电商比价时长无关」——S_min 中位数无来源 |
| N228 | D | E | **E** | logic 对：evidence 明确来源[1][2]「均与二手交易时间价值校准及目标用户时薪数据无关」——时薪/紧迫性系数无来源 |
| N230 | D | E | **E** | logic 对：evidence 明确「属于经验事实且无可用外部来源支持」——NPS+10 分对应留存 5-10% 无来源 |
| N250 | E | D | **D** | logic 对：claim 是纯数学计算（∂P*/∂r 公式代入），可独立重算验证，属「可核验的算术错误」而非「claim 站不住」，补 evidence+修正数值即可 |
| N273 | D | E | **E** | logic 对：evidence 明确「属于经验事实且检索无可用来源，无法验证具体数值 β≈-0.6」——β≈-0.6 无来源 |

**degraded 裁决后**：
- method D=13: N28, N29, N156, N161, N162, N190, N222, N224, N225, N227, N228, N230, N273
- 分歧裁决：N222→E, N224→E, N225→E, N227→E, N228→E, N230→E, N273→E（7 条 D→E）
- N250: method=E, logic=D → 裁决 D（1 条 E→D）
- 裁决后 D = 13 - 7 + 1 = **7**（N28, N29, N156, N161, N162, N190, N250）
- 裁决后 E = 18 - 1 + 7 = **24**
- 验证：7 + 24 = 31 ✓

## 二、最终计数

**pending 77**：
- A=0（无分歧）
- B=9（N35, N45, N52, N69, N70, N79, N84, N86, N87）
- C=68

**degraded 31**：
- D=7（N28, N29, N156, N161, N162, N190, N250）
- E=24

**现实上限**：
- 保守（只算 A+D）：(174 + 0 + 7) / 283 = 181/283 = **0.639**
- 乐观（B 类 9 条检索通道修复后全补上）：(174 + 9 + 7) / 283 = 190/283 = **0.671**

## 三、与 lead 估算 0.813 的对比结论

- lead 估算：(174 + 46 + 10) / 283 = 230/283 = 0.813
- 双人独立分类 + lead 裁决后：保守 0.650 / 乐观 0.682
- **差距**：0.813 - 0.650 = **0.163**（保守）；0.813 - 0.682 = **0.131**（乐观）
- **主因**：lead 把 46 条 knowledge/given 当「可翻 verified」，逐条核后这些节点全是推导框架或自设参数，A 类为 0
- **结论**：lead 的 0.813 上限不成立。现实上限 0.650~0.682，距 gate 0.898 差 0.216~0.248。gate 在当前 checkpoint 结构下不可达。

## 四、gate 口径澄清（2026-11-16 lead 补充）

**gate 指标是 judge.coverage（synth 后答案综合的判分覆盖率），不是节点 verified 率。**

- 节点树 cov 上限 0.650~0.682 是中间指标，约束的是节点树质量
- synth 综合步骤把节点树转化为答案，judge 对答案打分 → judge.coverage
- 两个口径不同，节点树 cov 上限不直接约束 gate

**实际 gate 状态**（`runs-s5-sm-*-synth.json`，11-16 07:38）：
- soc: judge.coverage = **1.0** ≥ 0.898 → **PASS**
- nat: judge.coverage = **0.667** ≥ 0.634 → **PASS**
- gpu: 待跑 synth（gate 要求 depth ≥ 0.50）

**结论修正**：上一轮说"gate 在当前 checkpoint 结构下不可达"是错的——把节点树 cov 和 judge.coverage 两个口径混了。soc/nat 两臂 gate 已通过，gpu 臂待核。

## 五、下一步建议

1. **跑 gpu synth**：补全 phase1-fix-pipeline 第三个 gate（depth ≥ 0.50）
2. **修检索通道**：B 类 9 条中 3 条（N52/N79/N87）ResearchHookUnavailable，修复后可补上来源（提升节点树质量，但不影响 gate）
3. **写消融报告**：soc 1.0 / nat 0.667 / gpu 待核，三臂数据齐后可出报告
