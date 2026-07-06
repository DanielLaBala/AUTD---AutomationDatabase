$ruta = Split-Path -Parent $MyInvocation.MyCommand.Path
$path = [Environment]::GetEnvironmentVariable("Path", "User")

if ($path -notlike "*$ruta*") {
    [Environment]::SetEnvironmentVariable(
        "Path",
        "$path;$ruta",
        "User"
    )
    Write-Host "Added to PATH."
} else {
    Write-Host "Already in the PATH."
}