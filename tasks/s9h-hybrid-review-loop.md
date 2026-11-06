# S9H — 分阶段混合风格 + 真 review-loop 臂（设计）

> origin: ai · 2026-11-06 · 成璐指令"分解用引导、检查用机械，跑起来"
> 定位：新消融臂，测的是**多轮分阶段执行 + verdict 回退** vs S5 的**单 call 全流程 prompt**。
> 与 S8G 正交：S8G = 单 call + 尾部叠加规则；S9H = 多 call + 阶段间工件传递 + revise 回退。

## 1. 要回答的问题

S5 得 0.805 是"6 个阶段文件拼成一个 12K prompt 让模型一口气写完"的效果。流程文件里定义的
verdict/repair_stage 回退机制从未被执行过（harness 无 review loop）。问题：

**Q-A**：把流程真正拆成多次 LLM call、每阶段独立 review、允许 revise 回退，分数会升还是降？
**Q-B**：分解阶段用引导式（decomp 五步法 + 激发句）vs 机械式（01 主文件 checklist），哪个对最终事实质量贡献大？

## 2. Prompt 结构（每题 3 次 call）

### Phase 1 — 目标分解（引导式）

```
[系统] 你是一个严谨的研究分解者。
[注入] decomp-01.md 五步方法（根标量→正交切分→黑盒收口表→口径声明→瓶颈识别）
      + 01-goal-decomposition.md 的「判定原则」节（因素正交/覆盖目标/候选集冻结）
[激发句] 动笔之前先想 30 秒：这个问题域里最容易被忽略的维度是什么？
         如果你只列了 3 个因素，第 4 个可能是哪个？为什么它重要？
[任务] 输出分解工件：根标量定义 / 正交维度表(含独占参数) / 黑盒收口表(B1-Bn) / 口径声明 / 瓶颈识别
       末尾必须附「空缺清单」（无法闭式的项，编号与黑盒表一致）
```

### Phase 2 — 信息调研（机械式）

```
[系统] 你是资料搜集员。严格按 checklist 执行，不跳步。
[注入] 02-information-research.md 全文（不改）
[输入] Phase 1 的空缺清单
[要求] 每条关键主张必须记录：来源标题 / URL / 观察时间 / 具体观察 / 不确定性
       只围绕空缺清单搜集，不扩大范围。
[工具] harness 代跑 research_hook（增强版，见 §4），来源包注入本 phase prompt
[输出] 证据表（claim | source | url | observed_at | uncertainty）+ 未解决空缺
```

### Phase 3 — 核验 + verdict（机械式 + 回退）

```
[系统] 你是 Reviewer。你的职责是质检和路由，不是重新研究。
[注入] 02.5-cross-check.md 全文
       + 00-common-review.md 的 verdict 格式规范
[输入] Phase 1 分解工件 + Phase 2 证据表
[要求] 对每条关键主张输出核验行：
       claim | source_support (yes/partial/no) | verdict (keep/delete/revise)
       矛盾对必须显式列出并给解释或保留不确定性。
[verdict 路由]（最多回退 1 次）
       - 全部 keep/delete → verdict: pass，进入 Phase 4
       - 存在 revise 且原因是「分解遗漏维度」→ repair_stage: 01
         （harness 重跑 Phase 1，prompt 追加「上一轮 Reviewer 指出遗漏：<具体内容>，请补全后重新输出完整分解」）
       - 存在 revise 且原因是「证据不足/来源缺失」→ repair_stage: 02
         （harness 重跑 Phase 2，prompt 追加「需补充的证据：<具体内容>」）
       - 回退已用过 1 次仍 revise → 强制 pass，残余问题写入「未完成项」
[输出] 核验表 + verdict + (可选)repair_stage + 修正后的合并证据
```

### Phase 4 — 终审合成（机械式）

```
[系统] 你是最终复核者。从反方角度检查，不重新研究。
[注入] 04.5-final-review.md 全文
[输入] Phase 1 分解 + Phase 3 核验后的证据
[要求] 对照原始任务逐项打勾；结论不得超出证据支持范围；
       薄弱点/未完成项/残余风险显式列出；坏消息（限制陈述）放在前 1/3。
[输出] 最终答案（这就是评分对象）
```

## 3. Harness 改动（相对 ablation_harness.py）

| 项 | 现状 | S9H |
|----|------|-----|
| LLM calls/run | 1（S7V 为 2） | 3-4（含 1 次回退时 4） |
| prompt 构造 | build_prompt() 全文拼接 | build_phase_prompt(phase, artifacts) 分阶段 |
| 阶段间传递 | 无 | artifacts dict：phase1→{tree, gaps}，phase2→{evidence}，phase3→{verified} |
| review loop | 无 | phase3 verdict 解析（正则 `verdict:\s*(pass\|revise)` + `repair_stage:\s*(01\|02)`），回退重跑对应 phase |
| temperature | 0 | Phase 1 用 0.3（激发需要多样性），Phase 2/3/4 用 0 |
| max_tokens/call | 8000（单次） | 4000×4（每次只需一个阶段的产出） |
| 预计 tokens/run | ~18K | ~30K（贵 1.7x） |
| 预计 wall/run | ~60-300s | ~4-8 min（串行 4 calls） |

实现方式：新建 `s9h_runner.py`（~200 行），复用 ablation_harness 的 call_llm/research_hook/inject_sources，不动主 harness。输出 schema 与现有 run 文件一致（output_text = Phase 4 最终答案，sources = Phase 2 证据表来源，新增字段 `phases`: 各阶段原文 + `verdicts`: 各 phase3 verdict 历史）。

## 4. Research hook 修复（前置依赖，P0）

当前 hook 是负资产（S7F mean 0.586 < S5 0.805），根因两个：

1. **`_fetch_page()` 只抓前 300 字符**——NVIDIA/ThunderCompute 页面导航栏占满前 300 字符，规格表在更深处。
   → 改为抓 full body innerText（上限 20K 字符），或至少 5000。
2. **arXiv 查询词偏学术**（"inference throughput benchmark"）——返回论文摘要，不含 datasheet 级规格。
   → Q1 类查表题优先走 KNOWN_SITES 直抓（datasheet/blog 规格页），arXiv 只做辅助。

这个修复对 S7F/S7V/S8G 都生效，建议先修再跑 S9H（否则 S9H 的 Phase 2 拿到的还是垃圾来源，测不出流程价值）。

## 5. 实验预算

| 项 | 数量 | 成本 |
|----|------|------|
| 题目 | Q1, Q4（与 s8g 同两题，可直接对比 S8G/S5） | — |
| reps | 3/题（与 s8g 对齐，n=3 出方向性结论） | 6 runs × 4 calls = 24 LLM calls |
| 对照 | 不需要重跑 S5/S8G（已有分数） | — |
| 判分 | v3 judge 不变 | 6 score calls |

**跳过论证（为什么不跑全 5 题 × n=5）**：S9H 的核心假设是"多轮+回退 > 单轮"，Q1/Q4 已有 S5/S8G/S7V 三组对照分数，n=3 足够出方向；若 Q1/Q4 上 S9H ≤ S5，则假设被否，直接停，不烧后续 3 题。若显著为正，再扩到 Q2/Q3/Q5（+15 runs）。这是 sequential testing 的最小化版本：先用最便宜的检验砍掉最可能的失败分支。

## 6. 验收标准

- S9H-Q1 mean ≥ S5-Q1 mean（0.805 基线，n=15）− 0.05（容差）
- S9H-Q4 mean ≥ S8G-Q4 mean（0.738）
- 至少 1 个 run 实际触发了 revise 回退（否则该机制没被测到，实验无效需加 rep）
- 回退 run 的最终分 ≥ 未回退 run 的均分（回退有效性的直接检验）

## 7. 风险

1. **Phase 3 的 verdict 解析可能不稳**：27b 不一定严格输出 `verdict: revise` 格式 → 缓解：prompt 里给 few-shot 示例 + 正则宽松匹配 + 解析失败默认 pass（记 note）。
2. **回退重跑 Phase 1 时上下文膨胀**：第二轮 prompt = 原 Phase 1 + 第一轮工件 + reviewer 意见 ≈ 8K tokens → 在 4000 max_tokens 输出内可控。
3. **wall time**：6 runs × 8 min ≈ 50 min 串行；可接受。
4. **judge 局限继承**：v3 judge 对 methodology gold 不注入 gold 文本（R-06 同族），M1 可能偏高——但所有臂共享同一 judge，臂间比较不受影响。