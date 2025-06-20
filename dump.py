"""
----------------------------------------------
StormworksAddonLuaDocumentation: An up-to-date Lua LSP meta file for Stormworks Addon Lua.
https://github.com/Cuh4/StormworksAddonLuaDocumentation
----------------------------------------------

Copyright (C) 2025 Cuh4

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

# rushed and hardcoded, but works
# tested on python 3.13, may work on earlier versions

# // Main
with open("docs/intellisense.lua") as f:
    lines = f.readlines()
    
funcs: list[str] = []
callbacks: list[str] = []

for line in lines:
    if line.startswith("server."):
        func_name = line.split(" =")[0]
        funcs.append(func_name)
    
    if line.startswith("function") and not line.startswith("function on") and not line.startswith("function httpReply"):
        func_name = line.split()[1].split("(")[0]
        funcs.append(func_name)
        
    if line.startswith("function on") or line.startswith("function httpReply"):
        func_name = line.split()[1].split("(")[0]
        callbacks.append(func_name)

with open("dump_functions.txt", "w") as f:
    f.write("\n".join(funcs))
    
with open("dump_callbacks.txt", "w") as f:
    f.write("\n".join(callbacks))