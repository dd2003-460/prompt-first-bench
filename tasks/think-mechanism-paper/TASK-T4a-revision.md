# TASK-T4a — think-mechanism-paper 文本修订（按 arena review 报告）

> origin: ai · 2026-11-26 · 触发：arena review 判决"需修改后投"（conf 0.7）。报告：`tasks/think-mechanism-paper/arena-review-report-raw-20261126.md`（先完整读它）
> 性质：【按报告修订】，不是自由发挥。所有修改点都来自 arena 报告，你不发明新内容、不加新 claim。pilot 结果节（arena 修改#3 后半）由后续任务 T4c 填入，你留占位符。

## [输入]
- 论文：`tasks/think-mechanism-paper/draft/paper.tex`（476 行，8pp，xelatex 编译 0 err，6 条已验证引用）
- arena 报告：`tasks/think-mechanism-paper/arena-review-report-raw-20261126.md`
- 数字溯源：`tasks/think-mechanism-paper/draft/number-trace.md`（改动涉及数字时同步更新）

## [修改清单（按优先级，全部来自 arena 报告）]

### M1（top-3 #1，硬伤）：Definition 1 非平凡性约束 + 全文 ≈id 统一
- arena Q2(a)：D∘C=id 在 C=D=id 时平凡满足（"理解"=定义空转）；tolerance 下实为 ≈id，与 Definition 的 =id 漂移
- 改法：Definition 1 加非平凡性条款——压缩必须产生可测量的节省（用显式 cost 条款表述，如 C 的输出表示尺寸严格小于输入表征尺寸减 slack；Kolmogorov 复杂度形式 K(C(x)) < K(x) − slack 可作为 remark 提及但注明 uncomputable、仅作直觉）；tolerance 带内把 =id 统一为 ≈id（全文 grep 一遍，包括 §3 facet 2 已出现的 ≈id 要与定义一致）
- 同步：Abstract/Intro 里引用该定义的措辞跟着改；Limitations 加一条"非平凡性约束是操作性定义，非认知主张"

### M2（top-3 #2）：两个 derivation 降级
- arena Q2(c)：自指有限性论证——Gödel 适用条件（算术表达力）被误述为"退化系统"；"iteration converging" 无收敛条件 → 结论可救、论证是断言
- arena Q2(d)：两阶段不可逆——直觉合理但无反例构造、无测度、无定理陈述，"derivation/structural result" 措辞过强
- 改法：两处 "derivation" 措辞降级为 "heuristic argument"（或 structural sketch）；自指有限性节：修正 Gödel 适用条件的表述（说清楚我们在说的是表达力不足的系统，不是 Gödel 定理的直接推论），收敛声明降级为"在无收敛条件保证下，本文把收敛当作经验观察而非定理"；两阶段节：补一个最小反例构造（错域精化有害的具体小例子，可以从源文件 `projects/AI-计算科学/D1-persona-align/memory/d-thinking-mechanism-first-principles-20261124.md` 里已有的例子取材，不发明）

### M3（Q3c）：两处越界表述降级
- facet 4 "explains why a model that misses its leading term fails"（因果语气）→ 改为描述性（"is consistent with" / "offers a reading of"）
- facet 3 "Progress is gradient descent"（隐喻作事实陈述）→ 明确标为 metaphor（"as a metaphor, ..."）

### M4（Q1）：Chaitin 2006 必引 + 相关近邻补引
- arena Q1 线(a)：Chaitin《Epistemology as Information Theory: From Leibniz to Ω》是 "Understanding is compression!" 口号原始出处，窗口外必引
- **已验证引文条目（Lead 实查 arXiv API，直接用，不许改 ID）**：
  ```
  \bibitem{chaitin_epistemology_2006}
  G.~J. Chaitin. ``Epistemology as Information Theory: From Leibniz to $\Omega$.'' 2006. arXiv preprint math/0506552 (submitted 2005-06-27).
  ```
- Related Work 加一句切割：Chaitin 是一向的压缩-解释观（epistemology as information theory），没有 round-trip 恒等/无损往返结构；我们是把压缩-解压往返本身作为理解的操作性定义
- 可选补引（Lead 已验证存在，arXiv 2026-09）：Queloz & Beckmann, "Why We Care About Understanding: Competence through Predictive Compression"（认知科学侧，理解=预测压缩）——加进 Related Work 一句话切割（他们讨论 competence 的哲学基础，不做 agent 协议）。如果你觉得 Related Work 已经够长，这条可省，但 Chaitin 不可省

### M5（Q5b）：LLM 套壳观感降低
- "Our difference:" ×4 同构句式 → 改成四种不同句式（有的用 "In contrast, we..."，有的用 "Whereas X focuses on Y, our focus is Z"，有的直接陈述区别不带引导短语）
- 7/7 表保留内容不动（核心证据），但表前引导句加一句说明这是内部一致性检查而非质量证明（如果已有类似句就不重复）
- 不做大规模改写，只破同构

### M6（Q2b）："无损=唯一+可复现"条款修正
- arena：D 是函数则可复现自动成立——该条款在 round-trip 之外零增量；tolerance 下与信息论 lossless（双射）术语冲突
- 改法：把"可复现"条款从无损定义里挪出来（或改成 tolerance 下的操作判据：同输入两次压缩输出差异在 tolerance 带内），避免与信息论 lossless 术语冲突（必要时在定义处加一句 "we use 'lossless' in an operational sense distinct from information-theoretic invertibility"）

### M7（占位）：pilot 结果节
- 在 Protocol 节末尾（或新增一小节 "A Minimal Pilot (preliminary)"）放占位注释 `% PILOT_RESULTS_PLACEHOLDER: T4c 填入`，不写内容

## [红线（违反即返工）]
1. 红线词仍 0：first/unprecedented/no one has/the only/nobody（时间序用法除外）——改完全文 grep 自查
2. 7/7 的 internal consistency / self-referential 限定词不许丢（abstract/§5/Limitations/附录四处）
3. 不发明新内容、不加新 claim、不加新实验声明（pilot 占位除外）
4. 6 条现有引用不许动（已验证）；新增引用只用上面给的已验证条目
5. 编译 0 error，页数 8-15
6. 数字改动同步 number-trace.md

## [交付]
1. `draft/paper.tex` 修订版（原地改）
2. `draft/paper.pdf` 重编译（xelatex 两遍）
3. `draft/revision-log.md` — 修改对照表：M1-M7 每项 → 改了哪里（行号/节）→ 改前/改后措辞（各 ≤2 句）→ 对应 arena 报告哪条
4. `draft/number-trace.md` 如有数字变动则同步

## [防截断协议（27b 输出上限教训）]
- 用 patch 增量改，每完成一个 M 项立即落盘，不攒着
- 每改完 2 个 M 项跑一次 xelatex 确认没改坏
- 推理从简：这是按单执行，不是研究

## [回执]
完成后回执：M1-M7 各项落地状态（done/skipped+理由）+ 编译结果（err 数/页数）+ 红线词 grep 结果 + revision-log 路径。
