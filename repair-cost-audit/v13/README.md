# Three-policy cost-transfer audit v13

This fixed release adds the missing **charitable scalar-optimal diagnostic replay**, alongside native and setup-scope choices, and covers plans from **all three existing training profiles**.

Download the repository ZIP at this commit, then run:

```sh
python3 repair-cost-audit/v13/assemble.py
cd repair-cost-audit/v13/extracted
python3 tools/verify_replay_package_v13.py
```

Only standard-library Python is needed. The assembler checks and merges the unchanged v12 base (19 parts in the neighboring folder) and this v13 delta (3 parts). The verifier checks **202 base + 357 new file hashes**, reproducing **8 base + 5 new JSON/CSV outputs** byte for byte.

New timing: **112 successful sessions / 9950 passed test calls**, including two warmups and 110 group replays. Eleven distinct partitions, five repetitions each in two sequential isolated processes. Identical partitions across method/profile aliases share observations.

The charitable scalar reference uses additional setup information to favor scalar optima; it is a diagnostic reference, not a scalar-only deployment algorithm. Every policy uses the same execution path.

Complete-module setup/scalar maximum-phase median ratios across histories: **1.046, 0.951, 1.000** (last is an identical partition). Nested-family ratios: **0.818, 0.906, 0.913**. The nested family's process-wall sums do not improve. Profile-two module cut55 activates two broad setups per pair, while the other partitions activate four. These are descriptive observations, not parallel completion, stable effect estimates or net deployment speedups.

An analysis-only correction removed an inherited assertion that all partitions activate four setups. The failed analyzer and amendment are preserved; no timing data were rerun or replaced. One module plus its nested family, one new replay batch, no new independent project or training histories.

Delta ZIP: **1,240,410 bytes**  
SHA256: `1b13ddc93899dd16c12081fcc819a9cc144839d5b9771fdfb1de5730cf874000`

See extracted/READ_FIRST_V13.txt and the frozen protocol. Institutional full text and private scientific PDFs are excluded. Third-party components retain their original licenses; authored audit scripts use the v12 MIT license.
