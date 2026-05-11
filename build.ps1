
function Install-MissingTool ($command, $installCommand) {
    try {
        &$command --version
    } catch {
        Invoke-Expression $installCommand
    }
}

Install-IfMissing "npam" "winget install NodeJS.NodeJS"
Install-IfMissing "Python" "winget install Python.Python.3.12 --source winget; python -m pip install --upgrade setuptools"
Install-IfMissing "vcpkg" "git clone https://github.com/microsoft/vcpkg.git; & '.\vcpkg\bootstrap-vcpkg.bat'; vcpkg integrate install; vcpkg install"

if (-NOT (Get-Module -ListAvailable PSMSI)) {
    Install-Module -Name PSMSI -Scope CurrentUser -Force
}

python gyp_library.py x64

msbuild /m main.sln /p:VcpkgEnableManifest=true

$makeappx = "C:\Program Files (x86)\Windows Kits\10\App Certification Kit\makeappx.exe"
        
python3 .\scripts\generate_pkg.py stable x64 .\template\AppxManifest.xml

Set-Location out

& "$makeappx" pack /d "stable_explorer_pkg_x64" /p "Code Modern Explorer Menu x64.appx" /nv

Set-Location out

Copy-Item -LiteralPath "Default\Code Modern Explorer Menu.dll" -Destination "..\out"

$Version = 1.0.0

run: .\build-msi.ps1 -ProductName "Code Modern Explorer Menu" -Variant stable -Platform x64 -Version $Version
