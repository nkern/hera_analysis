#!/bin/bash

# Run Python Pipeline
#python ./scripts/travis_pr_pipe.py

# Post a comment on the PR with pipeline output images
curl -H "Authorization: token ${GITHUB_TOKEN}" -X POST \
-d "{\"body\": \"Hello world\"}" \
"https://api.github.com/repos/${TRAVIS_REPO_SLUG}/issues/${TRAVIS_PULL_REQUEST}/comments"

