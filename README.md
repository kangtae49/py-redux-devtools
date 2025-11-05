```shell
mkdir py-redux-devtools

cd py-redux-devtools

uv init src-py
Initialized project `src-py` at `C:\sources\py-redux-devtools\src-py`

pnpm create vite src-react
.../19a538d2ac3-ce0                      |   +1 +
.../19a538d2ac3-ce0                      | Progress: resolved 1, reused 0, downloaded 1, added 1, done
|
o  Select a framework:
|  React
|
o  Select a variant:
|  TypeScript + React Compiler
|
o  Use rolldown-vite (Experimental)?:
|  No
|
o  Install with pnpm and start now?
|  No
|
o  Scaffolding project in C:\sources\py-redux-devtools\src-react...
|
—  Done. Now run:

  cd src-react
  pnpm install
  pnpm dev
```

```shell
github.com/new
Repository name: py-redux-devtools
Create repository
```

```shell
cmd> rmdir /s /q "src-py/.git"

git init
git config --global core.autocrlf true
git add .
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/kangtae49/py-redux-devtools.git
git push -u origin main
```

