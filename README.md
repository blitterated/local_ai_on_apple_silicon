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


## Install the OpenAI API lib

```sh
uv add openai
```

```text
Using CPython 3.14.7
Creating virtual environment at: .venv
Resolved 16 packages in 75ms
      Built purpygent @ file:///Users/pete/Development/blitterated/local_ai_on_apple_silicon/src                                                       Prepared 15 packages in 154ms                                                                                                                          Installed 15 packages in 15ms                                                                                                                           + annotated-types==0.8.0                                                                                                                               + anyio==4.15.1                                                                                                                                        + h11==0.16.0                                                                                                                                          + httpcore2==2.13.0                                                                                                                                    + httpx2==2.13.0                                                                                                                                       + idna==3.20                                                                                                                                           + jiter==0.17.0                                                                                                                                        + openai==3.18.0                                                                                                                                       + purpygent==0.1.0 (from file:///Users/pete/Development/blitterated/local_ai_on_apple_silicon/src)                                                     + pydantic==2.13.5
 + pydantic-core==2.46.5
 + sniffio==1.3.1
 + truststore==0.10.4
 + typing-extensions==4.16.0
 + typing-inspection==0.4.4
 ```



