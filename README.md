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
## .gitattributes
```
* text=auto

*.bat text eol=crlf
*.cmd text eol=crlf

*.sh text eol=lf
```
```shell
git config --global core.autocrlf true
```

```shell
cmd> rmdir /s /q "src-py/.git"

git init
git add .
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/kangtae49/py-redux-devtools.git
git push -u origin main
```

# src-py
## .pyproject.toml
```toml
[project]
name = "src-py"
version = "0.1.0"
description = "Add your description here"
readme = "README.md"
requires-python = ">=3.13"
dependencies = [
    "pywebview==6.1",
    "pyinstaller",
    "setuptools",
]
```

```shell
cd src-py
uv init
```
## rustrover python interpreter uv setting

## py-redux-devtools.iml
- `<sourceFolder url="file://$MODULE_DIR$/src-py" isTestSource="false" />`
```iml
<?xml version="1.0" encoding="UTF-8"?>
<module type="EMPTY_MODULE" version="4">
  <component name="FacetManager">
    <facet type="Python" name="Python facet">
      <configuration sdkName="uv (src-py) (3)" />
    </facet>
  </component>
  <component name="NewModuleRootManager">
    <content url="file://$MODULE_DIR$">
      <excludeFolder url="file://$MODULE_DIR$/src-py/.venv" />
      <sourceFolder url="file://$MODULE_DIR$/src-py" isTestSource="false" />
    </content>
    <orderEntry type="inheritedJdk" />
    <orderEntry type="sourceFolder" forTests="false" />
    <orderEntry type="library" name="uv (src-py) (3) interpreter library" level="application" />
  </component>
</module>
```

```
uv run main.py
or
uv run main.py --verbose
```


# src-react
```
cd src-react
pnpm install
```
## .vite.config.ts
- base: './'
```ts
export default defineConfig({
  plugins: [
    react({
      babel: {
        plugins: [['babel-plugin-react-compiler']],
      },
    }),
  ],
  base: './'
})
```

```shell
pnpm add @redux-devtools/app
```

## development
```
cd src-py && uv run main.py
cd src-react && pnpm dev
```

