name: SAST Scan Project 3

permissions:
  contents: read
  security-events: write

on:
  push:
    branches: [ main ]

jobs:
  sast:
    name: SAST Scan
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v3

      - name: Initialize CodeQL
        uses: github/codeql-action/init@v3
        with:
          languages: python

      - name: Run CodeQL Analysis
        uses: github/codeql-action/analyze@v3