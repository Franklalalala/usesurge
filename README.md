# usesurge

Use surge for molecule generation.

The original surge repository is [StructureGenerator/surge](https://github.com/StructureGenerator/surge). 

Some libraries are changed for the convenience of windows developers, details see [saltball/usenauty](https://github.com/saltball/usenauty).

### Compile from source code

```shell
git clone https://github.com/Franklalalala/usesurge
cd usesurge
mkdir build
cd build
cmake .. -G "Unix Makefiles"
make
```

The [CXX standard](https://en.wikipedia.org/wiki/C%2B%2B17) is set to be **17**, which means the gcc version needs to be 8 or higher, or a higher version of IDE, such as [Visual Studio 2017](https://en.wikipedia.org/wiki/Microsoft_Visual_Studio#2017).

The cmake version need to be **3.1** or higher.
