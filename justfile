set allow-duplicate-recipes
set allow-duplicate-variables
import? 'rocks.just'

lts_releases := '{"0.31": "2031-04-16"}'

[private]
@default:
  just --list
  echo ""
  echo "For help with a specific recipe, run: just --usage <recipe>"
