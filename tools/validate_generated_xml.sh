#!/usr/bin/env bash
set -euo pipefail

xmllint --noout mods/HarranVirusEvolved/generated/*.xml
echo "XML validation passed."
