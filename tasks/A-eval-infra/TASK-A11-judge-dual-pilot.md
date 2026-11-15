# TASK: pilot 矩阵 judge 双判（judge1 + judge2）

> 状态：待派发 | 目标会话：01a195cb（taskSpace: pfb-rejudge-g1b-20261101，pfb 唯一活跃会话）
> 前置：main @ 2e8f737 已含 judge-packet-judge1.json + judge-packet-judge2.json（O3 claim 清单已内嵌，无需读仓库其他文件）

## 背景（一句话）
pilot 试测 9 份答卷（3 个 prompt 变体 × 3 独立 run）已全部落 main。现在要两个独立评分员各打一遍分，用来算"两个裁判去掉瞎蒙成分后的真实一致程度"（κ），验证这套评分标准本身靠不靠谱。

## 任务书要求

### Step 1: 切换分支并拉取最新
```bash
git fetch origin && git checkout -B arena/4a614e63-prompt-first-bench origin/main
```
（工作分支切到与 main 同内容的本地分支名，产出 push 回此分支；不要动 main）

### Step 2: judge1 评分（先做这个）
读取 `bench/rubric-v3/ablation/pilot-matrix/judge-packet-judge1.json`，严格按其中 instructions 对 5 个 run（A-r1, A-r2, A-r3, B-r1, B-r2）逐一按 rubric_items 打二值分（0/1 或 NA），输出 JSON 数组（每 run 一个对象，结构见 packet 内 output_schema）。
把结果写入 `bench/rubric-v3/ablation/pilot-matrix/judge-results/judge1.json`（目录不存在则创建）。

### Step 3: judge2 评分（再做这个，独立重判）
读取 `bench/rubric-v3/ablation/pilot-matrix/judge-packet-judge2.json`，同样规则对 4 个 run（B-r3, C-r1, C-r2, C-r3）打分。
**独立性要求**：judge2 必须重新独立判定，不许直接照抄 judge1 对重叠维度（如 O1 低先验候选集合）的结论——虽然两包 run 不重叠，但 O1 需要对照"全批次候选集交集"，请基于本包可见信息独立推断，无法确定就标 NA 并在 notes 说明。
结果写入 `bench/rubric-v3/ablation/pilot-matrix/judge-results/judge2.json`。

### Step 4: commit + push
```bash
git add bench/rubric-v3/ablation/pilot-matrix/judge-results/
git commit -m "feat(pilot): judge 双判完成 — judge1(5 run) + judge2(4 run)，二值分 + 片段定位证据"
git push origin arena/4a614e63-prompt-first-bench
```

## 硬约束
1. 只输出 JSON 内容进文件，不加 markdown 围栏外的解释文字。
2. E5 全部标 NA（无外部核对通道）；P1-E1/E2、P2-E1/E2/E3、P3-E3 全部标 NA（只有终态产出无过程工件）——这些已在 instructions 里写明，照做即可。
3. 每个非 NA 条目必须在 evidence 里给片段定位（行号或段落关键词）。
4. 单批 ≤15 cell 防截断：judge1 有 5 run × ~8 条目 = 40 判定，若单次输出过长可分两次写文件（先 A-r1..A-r3，再 B-r1..B-r2 追加合并为合法 JSON 数组）。
5. 完成后回执格式：`JUDGE-DONE judge1=<n>runs judge2=<n>runs sha=<commit hash>`。

## 验收（Lead 侧）
- 两文件存在且 JSON 合法
- 9 个 run_id 全覆盖、无重复
- 非 NA 条目均有 evidence 定位
- 本地复算 sha256_16 与远端一致
