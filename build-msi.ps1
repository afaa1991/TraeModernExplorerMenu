param($ProductName = 'Trae Modern Explorer Menu', $Variant = 'stable', $Platform = 'x64', $Version = '1.0.0')

Import-Module PSMSI

$ScriptRoot = if ( $PSScriptRoot ) { $PSScriptRoot} else { ($(try { $script:psEditor.GetEditorContext().CurrentFile.Path } catch {}), $script:MyInvocation.MyCommand.Path, $script:PSCommandPath, $(try { $script:psISE.CurrentFile.Fullpath.ToString() } catch {}) | % { if ($_ ) { $_.ToLower() } } | Split-Path -EA 0 | Get-Unique ) | Get-Unique }

$OutputDirectory = "$ScriptRoot\output"

if (Test-Path $OutputDirectory) {
    Get-ChildItem -Path $OutputDirectory | ForEach-Object { Remove-Item -Path $_ -Force -Recurse  }
}

$ProductId = 'F36C31D8-B5D4-492B-B766-CDB73D3C68D4'
$UpgradeCode = 'D59C3F6E-2468-46FD-9044-36A3731223B2'

if ($Variant -eq 'insiders') {
    $ProductName = 'Trae Insiders Modern Explorer Menu'
    $ProductId = '0DCF9DDB-F0D7-42B2-ACCB-92407353C706'
    $UpgradeCode = 'F62062DB-AD16-4344-BB3C-779A49166025'
}

$CustomAction = @(
    New-InstallerCustomAction -FileId 'RunOnInstall' -RunOnInstall
    New-InstallerCustomAction -FileId 'RunOnUninstall' -RunOnUninstall
)

$InstallerFile = {
    New-InstallerFile -Source "$ScriptRoot\[Content_Types].xml"
    New-InstallerFile -Source "$ScriptRoot\AppxBlockMap.xml"
    New-InstallerFile -Source "$ScriptRoot\out\$($Variant)_explorer_pkg_$($Platform)\AppxManifest.xml"
    New-InstallerFile -Source "$ScriptRoot\out\$ProductName $Platform.appx"
    New-InstallerFile -Source "$ScriptRoot\out\$ProductName.dll"
    New-InstallerFile -Source "$ScriptRoot\msi\RunOnInstall.ps1" -Id 'RunOnInstall'
    New-InstallerFile -Source "$ScriptRoot\msi\RunOnUninstall.ps1" -Id 'RunOnUninstall'
}

New-Installer -ProductName $ProductName -ProductId $ProductId -UpgradeCode $UpgradeCode -Platform $Platform -Version $Version -Content {
    New-InstallerDirectory -PredefinedDirectory "LocalAppDataFolder" -Content {
        New-InstallerDirectory -DirectoryName "Programs" -Content {
            New-InstallerDirectory -DirectoryName $ProductName -Content $InstallerFile
        }
    }
} -CustomAction $CustomAction -OutputDirectory $OutputDirectory #-RequiresElevation
