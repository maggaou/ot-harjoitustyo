from sys import platform
from invoke import task
from subprocess import call

@task
def reset_database(ctx):
    ctx.run("python src/initialize_database.py", pty=True)

@task
def show_users(ctx):
    ctx.run('sqlite3 data/database.sqlite "SELECT * FROM Users;"', pty=True)

@task
def build(ctx):
    ctx.run("python src/build.py")

@task
def start(ctx):
    ctx.run("python3 src/index.py", pty=True)

@task
def test(ctx):
    ctx.run("pytest src", pty=True)

@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest src", pty=True)

@task(coverage)
def coverage_report(ctx):
    ctx.run("coverage html", pty=True)
    file = "htmlcov/index.html"
    if platform == "darwin":
        ctx.run("open " + file, pty=True)
    if platform == "linux":
        call(("xdg-open", file))

@task
def repo_github(ctx):
    if platform == "darwin":
        ctx.run("open 'https://github.com/maggaou/ot-harjoitustyo/'", pty=True)
    if platform == "linux":
        call(("xdg-open", 'https://github.com/maggaou/ot-harjoitustyo/'))

@task
def format_with_autopep8(ctx):
    ctx.run("autopep8 --in-place --recursive src", pty=True)

@task
def clear_moves(ctx):
    ctx.run("rm -f data/my-moves/*", pty=True)

@task
def lint(ctx):
    ctx.run("pylint src", pty=True)