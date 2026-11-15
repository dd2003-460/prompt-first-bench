# pfb-paper-add-t17-section — Decomp

> origin: ai · 2026-11-06 · goal: pfb-paper-add-t17-section

## 分解树

```
pfb-paper-add-t17-section
├── A. 内容写入
│   ├── A1. §5.3 新增 "Memory Benchmark Validation (LoCoMo)" 子节 (~200w)
│   │       原子: 写 T17 数据 (S0=71.3%, S1=82.0%, ΔEG=+10.7pp, OD=25%)
│   │       + 方法论关联 (prompt constraint as first-order lever)
│   │       完成判据: 子节存在且 ≥150w
│   └── A2. References 新增 LoCoMo paper (arXiv:2402.17753)
│           原子: 检查是否已在 refs → 不在则添加
│           完成判据: grep "Mao" OR "LoCoMo" references/ 有结果
├── B. 字数控制
│   ├── B1. 插入后 wc -w → 若 >7200 则 trim
│   │       原子: 优先压缩 §2.2/§2.4 冗余句 (已有先例: 7728→7197)
│   │       完成判据: wc -w ≤ 7200
│   └── B2. in-text ↔ References 一致性检查
│           原子: grep 所有 (Author, Year) 引用 → 逐条确认 refs 有对应 entry
│           完成判据: 零缺失
└── C. 交付
    ├── C1. git commit + push origin main
    │       完成判据: push 成功
    └── C2. loop-state.json 更新
            完成判据: iteration+1, notes 含 T17 section added
```

## 缺口清单

| # | 子项 | 缺什么 | 来源 |
|---|------|--------|------|
| G1 | A2 | LoCoMo paper (Mao et al., 2024, arXiv:2402.17753) 是否已在 42 refs 中? | grep paper-draft.md |
| G2 | A1 | §5.3 当前结构 (标题/段落边界) 确定精确插入点 | read §5.3 |
| G3 | B1 | 插入后实际字数增量 (预估 +200-300w, 需 trim ~200-300w) | wc -w after insert |
| G4 | A1 | [待核验] T17 数据是否需要 cross-conversation 支撑才能写入论文 (当前只有 conv4) | 判断: 单 conv 结果作为 "evidence" 还是 "preliminary"? |

## 正交性自检

- A(内容) ⊥ B(字数): A 加内容, B 控总量 ✓
- A1(子节) ⊥ A2(引用): 正文 vs. 参考文献 ✓
- B1(trim) ⊥ B2(一致性): 量 vs. 质 ✓
- C(交付) ⊥ A+B: 执行 vs. 提交 ✓
- 完备性: 从"写什么"到"怎么提交"全覆盖 ✓
