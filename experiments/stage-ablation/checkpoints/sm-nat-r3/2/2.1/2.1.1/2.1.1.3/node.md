# N108: 工作点 C（尾部稀疏区）：若 x_min 假设错误（如 x_min=10KB），则 E[S]=110KB，Top 1% 对象平均大小 5KB，占用 5MB，剩余

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N38

## Claim

工作点 C（尾部稀疏区）：若 x_min 假设错误（如 x_min=10KB），则 E[S]=110KB，Top 1% 对象平均大小 5KB，占用 5MB，剩余容量可容纳 128GB/5KB ≈ 26,843,545 个对象，K_eff 仍 > N，需进一步调整 x_min 或 α 使 K_eff < N

## Corrected Claim

工作点 C（尾部稀疏区）：若 x_min 假设错误（如 x_min=10KB），则 E[S]=110KB，Top 1% 对象平均大小 5KB，占用 5MB，剩余容量可容纳 128GB/5KB ≈ 26,843,545 个对象，K_eff 仍 > N，需进一步调整 x_min 或 α 使 K_eff < N

## Evidence

先验知识/题面给定，逻辑校验通过
