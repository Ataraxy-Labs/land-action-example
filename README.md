# land action example

A tiny shop with three test files, wired to [land-action](https://github.com/Ataraxy-Labs/land-action).

Open a pull request that edits `shop/receipt.py` and only the receipt tests run. The pricing and catalog tests are carried from main, because land recorded every file they read and none of those files changed. The job summary says which tests ran, which were carried, and why.

See `.github/workflows/land.yml` for the whole setup.

