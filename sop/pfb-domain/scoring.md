# 评分流程

> origin: ai · 2026-11-07 · pfb 领域 SOP
> 为什么需要这份文件：评分是 pfb 的"测量仪器"。仪器校准不对，所有读数都没意义。这份文件定义怎么跑 scorer、怎么读分数、哪些数字能信哪些不能。

## 两个 Scorer

| 脚本 | 适用臂 | 读取字段 | 输出 |
|------|--------|---------|------|
| `score.py` | S0, S1, S5, D1-C1 | `output_text` | `scores.json` |
| `score_s10.py` | S10-A ~ S10-E | `final` | `s10-runs/s10-scores.json` |

**为什么不合并**：S10 的 run 格式（`final` 字段 + `rejections`/`soothed` 元数据）和主实验不同。强行统一会让两边都变复杂。等 v4 重构时再考虑。

## 运行方式

```bash
# 主实验（S0/S1/S5）
cd experiments/stage-ablation
python3 score.py --runs runs/ --gold bench/rubric-v3/ablation/ --out scores.json

# S10 tone 实验
python3 score_s10.py --resume > s10-scoring.log 2>&1 &

# 快速测试（前 2 个 run）
python3 score_s10.py --limit 2
```

## M1-M6 各维度怎么算

| 维度 | 计算方式 | Judge 参与？ |
|------|---------|-------------|
| M1 事实准确率 | LLM judge 对照 gold tree 叶子节点逐条判对错 | ✅ judge_m1() |
| M2 结构完整性 | LLM judge 评估子方面覆盖 | ✅ judge_m4()（共用） |
| M3 不确定性标注 | 正则检测 hedge 词 + LLM 判断是否合理 | 部分（LLM_CONF_CAP=0.7） |
| M4 缺口覆盖 | Jaccard(输出关键词, gold 叶子值) | ❌ 纯计算 |
| M5 诚实度 | URL spot-check + 数字验证 | ✅ check_urls() |
| M6 URL 存活 | HTTP HEAD 请求每个引用 URL | ❌ 纯网络 |

**为什么 M4 是纯计算不用 judge**：Jaccard 覆盖率是确定性的——gold 里有 41 个叶子值，模型输出命中了 20 个，覆盖率就是 20/41。不需要 LLM 判断"这个值算不算覆盖了那个概念"。用 judge 反而引入噪音。

## Gold Tree 对齐

评分前必须确认 gold tree 版本跟 run 版本匹配：
- Q1-Q5 → `bench/rubric-v3/ablation/gold-Q1.md` ~ `gold-Q5.md`
- Q6/Q7 → `bench/rubric-v3/ablation/gold-Q6.md` / `gold-Q7.md`（D-face 专用）
- Q8-Q10 → [待建]（B1 任务卡）

**Gold tree 格式**：markdown，含节点树 + 叶子值（具体数值/事实）。`detect_gold_type()` 自动识别类型。改 gold 后必须重跑评分——旧分数对新 gold 无效。

## Conf Cap

- 本地 27b judge：所有 LLM 给出的分数 cap 在 0.7
- 为什么：27b 的"我确信这是对的"不等于真的对。cap 是保守估计。
- 异族 judge 复评后可以去掉 cap（多源交叉验证提高了可信度）

## 出对比表

标准格式（写入 `runs/<name>-results.md`）：

1. **一句话结论**（大白话，带最大 Δ 和方向）
2. **总分对比表**（arm × M1-M6 × Total × vs baseline）
3. **维度解读**（哪个维度贡献了主要差距，为什么）
4. **与已有 finding 的一致性检查**
5. **下一步**（什么条件下这个数字可以对外说）

## 常见陷阱

1. **n 不够就报显著性**：n=5 时 p=0.03 可能是运气。n≥30 才可信。
2. **自判数字写进论文**：conf cap 0.7 的数字只能当"初步信号"，不是结论。
3. **跨 prompt 版本比分数**：v2 的 0.79 和 v3 的 0.82 不能直接比（结构不同）。
4. **忽略 M3 的反直觉**：M3 最高的是最差臂（A），因为短输出+大量hedge。单看 M3 会得出错误结论。
5. **M5/M6=0 当 bug 修**：模型不引用 URL 时这两个维度就是 0，是真实测量不是故障。
## 实验发现 → 生产路径（2026-11-07 成璐指令）

**为什么需要这条**：pfb 实验验证出的 prompt 优化如果只留在实验臂里，等于白做——生产路径（`loop/prompt-first/` 各阶段文件 + `ablation_harness.py` 引导式臂）才是真正跑日常任务的地方。但两边之间没有自动同步机制，全靠人记得去搬。今天（2026-11-07）第一次手动搬运了三个已验证优化（来源标签三分 → 02、量纲口径检查 → 02.5、终审来源一致性 → 04.5），commit `0e6fb77f`。以后每次 goal 验收时都要过一遍这个 checklist。

### 验收时必查：有没有可落地的生产更新？

goal 进入 05-accept 时，除了对照验收标准逐项检查，额外问一个问题：**"这次实验验证出的东西，有没有哪条该写进 `loop/prompt-first/` 或 harness 引导式臂？"**

判断标准（不是所有发现都能落地）：
- ✅ 能落地：经过异族 judge 验证的机制结论（如 S10 tone finding、C-face 来源接地主效应），且改动是"加一句话讲道理"级别的
- ❌ 不落地：单 rep 观察、未过 κ 门禁的数字、纯 scorer 侧改进（那是评分仪器的事，不是 prompt 的事）

### 落地动作

1. 改对应 `loop/prompt-first/*.md` 阶段文件（引导式写法，讲原因，不打勾清单）
2. 同步改 `ablation_harness.py` 里对应的引导式臂（S6/S7T/S7F/S7V 等），保持实验和生产一致
3. commit message 注明 "vN 补丁: <来源实验> + <改了哪些文件>"
4. 在 `sop/pfb-domain/INDEX.md` 核心原则区追加一条（如果该发现够格成为共享原则）

### 已落地记录

| 日期 | 来源实验 | 落了什么 | commit |
|------|---------|---------|--------|
| 2026-11-07 | S10 "14x" 案例 + 来源三角验证讨论 | 02 来源标签三分 + 02.5 量纲口径检查 + 04.5 终审来源一致性 + S6/S7 臂同步 | `0e6fb77f` |
