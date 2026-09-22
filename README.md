# Local AI on Apple Silicon

Build and run a pure Python agent against a local model running on oMLX.

[Tech with Tim Tutorial](https://www.youtube.com/watch?v=c9AnqCeyxbI)


## Setup the Python Project

Initialize the project directory.

```sh
uv init --bare --name purpygent
```

```text
Initialized project `purpygent`
```

Install the lastest stable Python.


```sh
uv python install 3.14
```

```text
Installed Python 3.14.7 in 1.40s
 + cpython-3.14.7-macos-aarch64-none (python3.14)
```

Pin the latest version to the project.

```sh
uv python pin 3.14
```

```text
Pinned `.python-version` to `3.14`
```
