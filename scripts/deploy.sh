#!/bin/bash

# cog push
cd realistic-voice-cloning
bash python3 src/download_models.py
cog push r8.im/platform-kit/rvc-inference