# 1.生成依赖文件 requirements.txt
pipreqs.exe ./  --encoding utf-8
pipreqs.exe ./  --encoding utf-8  --force  # 如果已经存在则覆盖

# 2.把依赖包下载到packages中
pip3.exe download -r requirements.txt -d packages\

# 3. 安装
python setup.py bdist_egg

# 4. 项目启动时先从指定目录安装依赖包
pip3 install --no-index --find-links=./packages -r requirements.txt

# 5. 运行程序
python main.pyc

# 查看 setup.py 支持的命令
python setup.py  --help-commands
### 输出如下
(python_operation) λ python setup.py --help-commands
Standard commands:
  build             build everything needed to install
  build_py          "build" pure Python modules (copy to build directory)
  build_ext         build C/C++ extensions (compile/link to build directory)
  build_clib        build C/C++ libraries used by Python extensions
  build_scripts     "build" scripts (copy and fixup #! line)
  clean             clean up temporary files from 'build' command
  install           install everything from build directory
  install_lib       install all Python modules (extensions and pure Python)
  install_headers   install C/C++ header files
  install_scripts   install scripts (Python or otherwise)
  install_data      install data files
  sdist             create a source distribution (tarball, zip file, etc.)
  register          register the distribution with the Python package index
  bdist             create a built (binary) distribution
  bdist_dumb        create a "dumb" built distribution
  bdist_rpm         create an RPM distribution
  bdist_wininst     create an executable installer for MS Windows
  check             perform some checks on the package
  upload            upload binary package to PyPI

Extra commands:
  bdist_wheel       create a wheel distribution
  alias             define a shortcut to invoke one or more commands
  bdist_egg         create an "egg" distribution
  develop           install package in 'development mode'
  dist_info         create a .dist-info directory
  easy_install      Find/get/install Python packages
  egg_info          create a distribution's .egg-info directory
  install_egg_info  Install an .egg-info directory for the package
  rotate            delete older distributions, keeping N newest files
  saveopts          save supplied options to setup.cfg or other config file
  setopt            set an option in setup.cfg or another config file
  test              run unit tests after in-place build (deprecated)
  upload_docs       Upload documentation to PyPI

usage: setup.py [global_opts] cmd1 [cmd1_opts] [cmd2 [cmd2_opts] ...]
   or: setup.py --help [cmd1 cmd2 ...]
   or: setup.py --help-commands
   or: setup.py cmd --help