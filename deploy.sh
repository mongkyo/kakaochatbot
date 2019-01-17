#!/usr/bin/env bash
git add -f .secrets/
eb deploy --profile kakaoeb --staged
git reset HEAD .secrets/
