【执行前必读】
1. 本任务必须走 1-loop：先读 sop/arena-loop-pipeline.md + loop/prompt-first/00..04.5
2. 每阶段产出落盘 loop-artifacts/stages/<N>/
3. 完成后 commit + push
4. 通道故障 → 报告 Lead 降级，不得静默跳过

# T46: Add T17 LoCoMo Section to Paper §5.3

## 目标
在 paper-draft.md §5.3 (Arena Channel) 末尾新增 "Memory Benchmark Validation" 子节 (~200w)，引用 T45-final-report 数据。

## 执行步骤

1. 读 experiments/stage-ablation/paper-draft.md §5.3 当前内容 (316w, ends before §5.4)
2. 在 §5.3 末尾 (§5.4 之前) 插入新段落:
   - 开头: "Beyond open-ended technical Q&A, we validated the prompt-first approach on a memory benchmark..."
   - 数据: S0=71.3%, S1(entity-guard)=82.0%, ΔEG=+10.7pp (top_50, n=178, LoCoMo conv4)
   - 方法论关联: "entity-grounding constraint is load-bearing for memory tasks, paralleling how decomposition structure is load-bearing for research tasks"
   - Caveat: "preliminary single-conversation result; cross-conversation validation in progress"
   - 引用: (Mao et al., 2024) for LoCoMo benchmark
3. wc -w → 若 >7200 则 trim §2.2 或 §4.1 冗余句至 ≤7200
4. grep 验证所有 in-text citations 在 References 有对应 entry
5. git add + commit + push origin main

## 验收
- [ ] §5.3 含 "Memory Benchmark" 关键词, 子节 ≥150w
- [ ] wc -w ≤ 7200
- [ ] "Mao" 在 References 中
- [ ] 无 in-text citation 缺 ref
- [ ] push 成功
