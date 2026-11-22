# land action example

A tiny shop with three test files, wired to [land-action](https://github.com/Ataraxy-Labs/land-action) with one test line split by file.

- [Pull request #3](https://github.com/Ataraxy-Labs/land-action-example/pull/3) edits `shop/receipt.py`, so only the receipt tests run and the other two are carried from main.
- [Pull request #4](https://github.com/Ataraxy-Labs/land-action-example/pull/4) breaks a tax rate, so the pricing tests run and fail.
- [Pull request #5](https://github.com/Ataraxy-Labs/land-action-example/pull/5) has three pushes. The first runs the receipt tests, the second only touches this README and runs nothing because the pull request remembers what its first push proved, and the third breaks the receipt and is caught.

Each run's job summary says which tests ran, which were carried, and why. See `.github/workflows/land.yml` for the whole setup.
