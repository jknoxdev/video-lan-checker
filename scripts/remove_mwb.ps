
# Check the installed applications
$malwareBytes = Get-WmiObject -Class Win32_Product | Where-Object { $_.Name -like "*MalwareBytes*" }

# Check the installation type and uninstall accordingly
if ($malwareBytes.InstallSource.StartsWith("msiexec")) {
    # Uninstall using Windows Installer
    $malwareBytes.Uninstall()
}
elseif ($malwareBytes.InstallSource.StartsWith("C:")) {
    # Uninstall using an executable or other method
    $installLocation = Split-Path -Path $malwareBytes.InstallSource -Parent
    $uninstallPath = Join-Path -Path $installLocation -ChildPath "unins000.exe"

    if (Test-Path $uninstallPath) {
        Start-Process -FilePath $uninstallPath -ArgumentList "/S" -Wait
    }
    else {
        Write-Host "Uninstall path not found."
    }
}
else {
    Write-Host "Unknown installation type."
}
