@echo off
rem Rebuilds the Reliant website from tools\ and publishes it to Cloudflare Pages (the live site).
cd /d "%~dp0"
set PY=python
where python >nul 2>nul || set PY=py
echo === 1 of 4: Building pages ===
%PY% tools\build.py || goto :fail
echo === 2 of 4: Checking pages ===
%PY% tools\check.py || goto :fail
echo === 3 of 4: Saving a version in git ===
git add tools
git add site
git add docs
git add PROJECT-STATUS.md "Publish Reliant site.bat"
git commit -m "Site update %date% %time%"
git push
echo === 4 of 4: Publishing to the live site ===
call npx --yes wrangler pages deploy site --project-name reliant-site --branch main --commit-dirty=true || goto :fail
echo.
echo PUBLISH-OK > publish-result.txt
echo DONE. The live site is updated.
goto :end
:fail
echo PUBLISH-FAILED > publish-result.txt
echo.
echo SOMETHING WENT WRONG. Nothing else was changed. Leave this window open and tell Claude.
:end
pause
