# 貢獻 Contributing

## 設置 Setup

1 Clone 你所 fork 的專案 Clone your fork of the repository

```sh
git clone https://github.com/YOUR_USERNAME/PetMonitoringSystemBackend
```

2 Install pip dependencies

```sh
pipenv install
```

3 Run unit test

```sh
pipenv run python manage.py test
```

## 指南 Guidelines

- 請參考在 Push 前包含多個 Commit. Please try to [combine multiple commits before pushing](http://stackoverflow.com/questions/6934752/combining-multiple-commits-before-pushing-in-git)

- 當在修復 Bug 的時候請使用 `TDD`.這代表你應該去寫單元測試錯誤代表他重製了 Issue 然後修復 Issue 最後執行測試確保 Issue 被解決.避免此 Issue 在未來重複發生.  Please use `TDD` when fixing bugs. This means that you should write a unit test that fails because it reproduces the issue, then fix the issue and finally run the test to ensure that the issue has been resolved. This helps us prevent fixed bugs from happening again in the future

- 請將測試覆蓋率保持在 100%. 寫額外的單元測試是必要的. Please keep the test coverage at 100%. Write additional unit tests if necessary

- 請放輕鬆去求助於其他 PetMonitoringSystem 團隊透過 Discord  或者 GitHub Issues. Feel free to ask for help from other members of the PetMonitoringSystem team via the Discord or Github issues.
