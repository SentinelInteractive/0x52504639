# Refresh the snapshot from a prepared working copy.
#
# Copies sanitized docs and data into this repository, runs the validator,
# and prints the git commands. It does not commit, push or deploy.

[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)]
    [string]$Source,

    [string]$RepoRoot = (Split-Path -Parent $PSScriptRoot),

    [switch]$NoWrite
)

$ErrorActionPreference = "Stop"

$sourceRoot = (Resolve-Path -LiteralPath $Source).Path
$repo = (Resolve-Path -LiteralPath $RepoRoot).Path

if (-not (Test-Path -LiteralPath (Join-Path $sourceRoot "docs"))) {
    throw "Source has no docs directory: $sourceRoot"
}
if (-not (Test-Path -LiteralPath (Join-Path $sourceRoot "data"))) {
    throw "Source has no data directory: $sourceRoot"
}

Write-Host "Copying docs from $sourceRoot"
New-Item -ItemType Directory -Force -Path (Join-Path $repo "docs") | Out-Null
New-Item -ItemType Directory -Force -Path (Join-Path $repo "data") | Out-Null
Copy-Item -Path (Join-Path $sourceRoot "docs\*.md") -Destination (Join-Path $repo "docs") -Force
Copy-Item -Path (Join-Path $sourceRoot "data\*.md") -Destination (Join-Path $repo "data") -Force
Copy-Item -Path (Join-Path $sourceRoot "data\*.json") -Destination (Join-Path $repo "data") -Force

$validator = Join-Path $repo "scripts\validate_snapshot.py"
if (-not (Test-Path -LiteralPath $validator)) {
    throw "Validator not found: $validator"
}

$validatorArgs = @($validator, "--repo-root", $repo)
if ($NoWrite) { $validatorArgs += "--no-write" }

Write-Host "Running validator"
& python @validatorArgs
if ($LASTEXITCODE -ne 0) {
    throw "Validator failed with exit code $LASTEXITCODE. Nothing was committed."
}

$today = (Get-Date).ToUniversalTime().ToString("yyyy-MM-dd")

Write-Host ""
Write-Host "Review the diff, then run:"
Write-Host ""
Write-Host "  git -C `"$repo`" add -A"
Write-Host "  git -C `"$repo`" commit -m `"docs: refresh snapshot $today`""
Write-Host "  git -C `"$repo`" push"
Write-Host ""
Write-Host "This script does not commit, push or deploy."
