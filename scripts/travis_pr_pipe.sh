#!/bin/bash

# Run Python Pipeline
#python ./scripts/travis_pr_pipe.py

# Post a comment on the PR with pipeline output images
curl -H "Authorization: token ${GITHUB_TOKEN}" -X POST \
-d "{\"body\": \"Here is a plot: \n ![PAPER_noise_sim](./scripts/paper_noise_sim.png)\"}" \
"https://api.github.com/repos/${TRAVIS_REPO_SLUG}/issues/${TRAVIS_PULL_REQUEST}/comments"

