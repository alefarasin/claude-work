#!/usr/bin/env bash
# larql POC demo — knowledge graph queries on Gemma 3 4B
# Requires: larql binary built, vindex cached at VPATH

LARQL="/home/claude/workspace/claude-work/larql/target/release/larql"
VPATH="/home/claude/.cache/huggingface/hub/models--chrishayuk--gemma-3-4b-it-vindex/snapshots/4806e9a8ebc2325da43dcd837f2d969ecdf0e403"
VINDEX_INFERENCE="/home/claude/workspace/claude-work/larql/models/gemma3-4b.vindex"

echo "=== larql POC Demo ==="
echo ""

echo "--- 1. List cached vindexes ---"
$LARQL list
echo ""

echo "--- 2. Show vindex metadata ---"
$LARQL show chrishayuk/gemma-3-4b-it-vindex
echo ""

echo "--- 3. DESCRIBE France (knowledge graph from model weights) ---"
$LARQL lql "USE \"$VPATH\"; DESCRIBE \"France\";"
echo ""

echo "--- 4. WALK France in output layers (what features activate for 'France'?) ---"
$LARQL lql "USE \"$VPATH\"; WALK \"France\" TOP 3 LAYERS 24-33;"
echo ""

echo "--- 5. SHOW RELATIONS (all relation types extracted from model) ---"
$LARQL lql "USE \"$VPATH\"; SHOW RELATIONS;"
echo ""

echo "--- 6. SELECT capitals from model knowledge ---"
$LARQL lql "USE \"$VPATH\"; SELECT entity, relation, target FROM EDGES WHERE relation = \"capital\" ORDER BY confidence DESC LIMIT 5;"
echo ""

echo "--- 7. SELECT nationality relations ---"
$LARQL lql "USE \"$VPATH\"; SELECT entity, relation, target FROM EDGES WHERE relation = \"nationality\" ORDER BY confidence DESC LIMIT 5;"
echo ""

echo "--- 8. DESCRIBE Rome ---"
$LARQL lql "USE \"$VPATH\"; DESCRIBE \"Rome\" KNOWLEDGE;"
echo ""

# Inference (requires converted vindex from GGUF)
if [ -d "$VINDEX_INFERENCE" ]; then
  echo "--- 9. INFER (full autoregressive inference) ---"
  $LARQL run "$VINDEX_INFERENCE" "The capital of France is"
  echo ""

  echo "--- 10. INFER via LQL INFER statement ---"
  $LARQL lql "USE \"$VINDEX_INFERENCE\"; INFER \"Einstein was born in\" TOP 5;"
  echo ""
else
  echo "--- 9. Inference vindex not ready yet ---"
  echo "    Convert with: larql convert gguf-to-vindex models/gemma-3-4b-it-Q4_K_M.gguf -o models/gemma3-4b.vindex --level inference"
fi
