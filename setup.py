import cx_Freeze
executables =[cx_Freeze.Executable("test.py")]

cx_Freeze.setup(
     name="Alladin",
     options={"build_exe":{"packages":["pygame"],"include_files":["ald.png","sky.png","eagle.png","lamp.png"]}},
description="alladin game",
executables=executables
)
